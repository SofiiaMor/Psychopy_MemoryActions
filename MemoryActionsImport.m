function MemoryActionsImport(filename, long)
% only filename without a path
% if long=0, in output saves the general data with RT, corr/missed etc. in xls file
% if long=1 saves .mat file with a structure with all data incl. coordinates of joystick for every frame

cd 'd:\psychopy\MemoryActions\data\' % set directory where to find the files

if ~exist('long', 'var') || isempty(long)
    long = 1;
end

% first read table
dataTable = readtable(filename);

% then convert to cell array
dataCell = table2cell(dataTable);
dataCell = [dataTable.Properties.VariableNames;dataCell]; % with names of columns

% choose only important columns with the nessesary info
if long == 0
    data = [dataCell(:,2) dataCell(:,9) dataCell(:,10) dataCell(:,68) dataCell(:,69) dataCell(:,70) dataCell(:,71)...
        dataCell(:,72) dataCell(:,116) dataCell(:,117) dataCell(:,118) dataCell(:,119) dataCell(:,120) dataCell(:,121) dataCell(:,142)]; 
else
    data = [dataCell(:,2) dataCell(:,9) dataCell(:,10) dataCell(:,68) dataCell(:,69) dataCell(:,70) dataCell(:,71)...
        dataCell(:,72) dataCell(:,116) dataCell(:,117) dataCell(:,118) dataCell(:,119) dataCell(:,120) dataCell(:,121) dataCell(:,142)...
        dataCell(:,66) dataCell(:,67) dataCell(:,73) dataCell(:,74) dataCell(:,75) dataCell(:,114) dataCell(:,115)...
        dataCell(:,122) dataCell(:,123) dataCell(:,124) dataCell(:,3) dataCell(:,4) dataCell(:,5) dataCell(:,6) dataCell(:,8)]; % with x,y coordinates and time of joystick moves
end

% save names of columns separately and delete from data
VarNames = data(1,:);
data(1,:) = [];

% replace names of conditions by number: 0 - immed_s, 1 - immed_d, 2 - del_s, 3 - del_d
immed_samei = strcmpi(data(:,1),'immed_s');
data(immed_samei,1) = {0};
immed_diffi = strcmpi(data(:,1),'immed_d');
data(immed_diffi,1) = {1};
del_samei = strcmpi(data(:,1),'del_s');
data(del_samei,1) = {2};
del_diffi = strcmpi(data(:,1),'del_d');
data(del_diffi,1) = {3};

% for some reason column 6 and 11 (joystick_RT_start_del and immed) in some files represents values as chars and not as numbers,
% cycles for the conversion:
if ischar(data{1,6})
    for ri = 1:size(data,1)
        data{ri,6} = str2double(data{ri,6});
    end
end
if ischar(data{1,11})
    for ri = 1:size(data,1)
        data{ri,11} = str2double(data{ri,11});
    end
end

if long == 1    % convert coordinates-chars into numbers
    for ri = 1:size(data,1)
        data{ri,18} = str2num(data{ri,18})-data{ri,16}; % x_immed - x1_immed (substract the displacement of joystick before the trial)
        data{ri,19} = str2num(data{ri,19})-data{ri,17}; % y_immed - y1_immed
        data{ri,20} = str2num(data{ri,20})-data{ri,8} + 0.02; % time points in immed - ITI_immed + 0.02 sec (joystick starts 2 ms before updating cursor)
        data{ri,23} = str2num(data{ri,23})-data{ri,21}; % x_del - x1_del
        data{ri,24} = str2num(data{ri,24})-data{ri,22}; % y_del - y1_del
        data{ri,25} = str2num(data{ri,25})-data{ri,13}-data{ri,14}-2.0 + 0.02; % time points in del - delay - ITI_del - 2 sec(image encoding) + 0.02 sec
    end
    
    % replace names of correct object by number: 3 - triangle, 4 - square
    tri = strcmpi(data(:,30),'triangle');
    data(tri,30) = {3};
    sqi = strcmpi(data(:,30),'square');
    data(sqi,30) = {4};
    
    coord_data = [data(:,18:20) data(:,23:30)]; % all coordinates together with correct ones
    coord_names = [VarNames(18:20) VarNames(23:30)]; % names of columns {'joystick_ImmedResp_x' 'joystick_ImmedResp_y' 'joystick_ImmedResp_time' 'joystick_DelResp_x' 'joystick_DelResp_y' 'joystick_DelResp_time' 'x_square' 'y_square' 'x_triangle' 'y_triangle' 'correct_object'}
    data = data(:,1:15); % general data {'condition' 'feedback' 'block' 'joystick_resp_corr_immed' 'joystick_RT_corr_immed' 'joystick_RT_start_immed' 'missed_immed' 'ITI_immed' 'joystick_resp_corr_del' 'joystick_RT_corr_del' 'joystick_RT_start_del' 'missed_del' 'delay' 'ITI_del' 'answer_button_corr'}
end

% transform into matrix for easier manipulations
dataMat = cell2mat(data);

% take only rows with meaningful values (without NaN)
ivalid = false(size(data,1),2);
ivalid(:,1) = ~isnan(dataMat(:,4));  % for immediate trials
ivalid(:,2) = ~isnan(dataMat(:,9));  % for delayed trials
ivalidAll = any(ivalid,2); % join indexes of both types of trials

% join RT, correct and missed responses for immed and delayed trials in one column
dataMat(ivalid(:,2),4) = dataMat(ivalid(:,2),9); % correct
dataMat(ivalid(:,2),5) = dataMat(ivalid(:,2),10); % RT of correct
dataMat(ivalid(:,2),6) = dataMat(ivalid(:,2),11); % RT of start of movement
dataMat(ivalid(:,2),7) = dataMat(ivalid(:,2),12); % missed trials

if long == 1   % join x,y coordinates and time points for immed and delayed trials in one column
    coord_data(ivalid(:,2),1) = coord_data(ivalid(:,2),4); % x
    coord_data(ivalid(:,2),2) = coord_data(ivalid(:,2),5); % y
    coord_data(ivalid(:,2),3) = coord_data(ivalid(:,2),6); % time points
    
    % take only valid values for the entire cell array (without NaN rows)
    coord_data = coord_data(ivalidAll,:);
    
    % get rid of unused columns of delayed trials
    coord_data(:,4:6) = [];
    coord_names = [coord_names(1:3) coord_names(7:11)]; %{'joystick_x' 'joystick_y' 'joystick_time' 'x_square' 'y_square' 'x_triangle' 'y_triangle' 'correct_object'}
    
    % convert cell array with x,y coordinates and time into matrix
    maxElem = max(cellfun(@numel,coord_data));  % find max of points (frames)
    equal_coord = (cellfun(@(x)cat(2,x,NaN(1,maxElem(1)-numel(x))),coord_data(:, 1:3),'UniformOutput',false)); % populate missing frames by NaN
    equal_coord2 = (cellfun(@(x)x',equal_coord,'UniformOutput',false)); % transpose cells from 1 x N frames to N frames x 1 
    
    coordMat = zeros(maxElem(1),3,size(coord_data,1)); % initialize 3D matrix: N frames x 3 (x,y,time) x trials
    for triali=1:size(coord_data,1)
        coordMat(:,:,triali)=cell2mat(equal_coord2(triali,1:3)); % join x,y,t of one trial and convert to matrix
    end
    
    % put coordinates of correct object in separate matrix
    coord_corr = cell2mat(coord_data(:,4:8)); % {'x_square' 'y_square' 'x_triangle' 'y_triangle' 'correct_object'}
    coord_corr_names = coord_names(4:8);
end

% for column answer_button.corr: take only rows without NaN - different indexes than in ivalid
AnswButIm = dataMat(~isnan(dataMat(:,15))& dataMat(:,1)==1,15); % for immed_diff
AnswButDel = dataMat(~isnan(dataMat(:,15))& dataMat(:,1)==3,15); % for del_diff 

% take all valid values for the entire matrix
dataMat = dataMat(ivalidAll,:); 

% replace last column-answer_button.corr by correct values for immed_diff and del_diff trials
dataMat(dataMat(:,1)==1,15)=AnswButIm; % immed_diff
dataMat(dataMat(:,1)==3,15)=AnswButDel; % del_diff

% join missed and correct in one column (missed - 0, correct - 1, incorrect - -1)
imissed = logical(dataMat(:,7)); % find indexes of missed trials
dataMat(imissed,4) = 0;  % in corr column replace missed by 0

% join ITI_immed and ITI_del in one column
iITI_im = ~isnan(dataMat(:,8));  % ITI for immediate trials
dataMat(iITI_im,14) = dataMat(iITI_im,8); % put them in column with del ITI

% now colums with delayed and missed trials can be deleted
dataMat(:, 7:12) = [];

% new names of variables
newVarNames = [VarNames(1:6) VarNames(13:15)];
tempCell =  regexp(newVarNames(4:6), '_', 'split');

% to get rid of word 'immed' in names
for j = 1:3
    name = join(tempCell{j}(2:3), '_');
    newVarNames{3+j} = name{1};
end
name8 = regexp(newVarNames(8), '_', 'split');
newVarNames{8} = name8{1}{1};

% save data 
shortName = regexp(filename,'_', 'split'); 
shortName = join(shortName(1:2), '_'); % name of test and patient
dir = 'D:\eeg\motol\PsychoPydata\MemoryActions\'; % path where to save data
if long == 0 % for short format, export to xls 
    xlsfilename = fullfile(dir, [shortName{1} '.xls']);
    xlswrite(xlsfilename ,vertcat(newVarNames,num2cell(dataMat))); % write to xls file
else  % for long format save structure in .mat file
    
    % create one structure for all data (dataMat, coordMat, coord_corr) and their headers
    namesGdata = {};  % structure with headers for general data with RT, corr/missed etc.-dataMat
    for n=1:numel(newVarNames)
        namesGdata.(newVarNames{n}) = n;
    end
    
    % codes for conditions
    condition = cell(4,2);
    condition(1,:)={'immed_same' 0};
    condition(2,:)={'immed_diff' 1};
    condition(3,:)={'del_same' 2};
    condition(4,:)={'del_diff' 3};
    
    % column - correctness
    resp_corr = cell(3,2);
    resp_corr(1,:)={'incorrect' -1};
    resp_corr(2,:)={'missed' 0};
    resp_corr(3,:)={'correct' 1};
    
    % structure with headers for 3D matrix of x,y coordinates and time points - coordMat (N frames x 3 (x,y,time) x trials)
    namesCoordData = {};
    namesCoordData.x = 1;
    namesCoordData.y = 2;
    namesCoordData.t = 3;
    
    % structure with headers for matrix with correct coordinates and correct object - coord_corr
    namesCoordCorr = {};
    for n=1:numel(coord_corr_names)
        namesCoordCorr.(coord_corr_names{n}) = n;
    end
    
    % column - correct object
    correct_object = cell(2,2);
    correct_object(1,:) = {'triangle' 3};
    correct_object(2,:) = {'square' 4};
    
    % join all data and structures together
    MemoryActions = struct('Gdata',dataMat,'namesGdata',namesGdata,'CoordData',coordMat,'namesCoordData',namesCoordData,...
        'Coord_correct', coord_corr, 'namesCoord_Corr',namesCoordCorr);
    MemoryActions.strings.condition = condition;
    MemoryActions.strings.resp_corr = resp_corr;
    MemoryActions.strings.correct_object = correct_object;
    
    % save
    matfilename = fullfile(dir, [shortName{1} '.mat']);
    save(matfilename, 'MemoryActions');
end
end
