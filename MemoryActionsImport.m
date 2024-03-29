function MemoryActionsImport(filename, long)
% only filename without a path
% e.g. MemoryActionsImport('js211006_MemoryActions_2021_Oct_06_1557.csv', 0)
% if long=0, in output saves the general data with RT, corr/missed etc. in xls file
% if long=1 saves .mat file with a structure with all data incl. coordinates of joystick for every frame

cd 'd:\eeg\motol\PsychoPydata\MemoryActions\' % set directory where to find the files

if ~exist('long', 'var') || isempty(long)
    long = 1;
end

% first read table
dataTable = readtable(filename, 'Delimiter', ',', 'ReadVariableNames', true);

% for file as09102020 and others in which 15 buttons of joystick (to remove last 6 buttons)
dataTable(end,:) = [];
dataTable = removevars(dataTable, {'joystick_ImmedResp_button_10','joystick_ImmedResp_button_11','joystick_ImmedResp_button_12','joystick_ImmedResp_button_13','joystick_ImmedResp_button_14','joystick_ImmedResp_button_15'});
dataTable = removevars(dataTable, {'joystick_DelResp_button_10','joystick_DelResp_button_11','joystick_DelResp_button_12','joystick_DelResp_button_13','joystick_DelResp_button_14','joystick_DelResp_button_15'});

% then convert to cell array
dataCell = table2cell(dataTable);
dataCell = [dataTable.Properties.VariableNames;dataCell]; % with names of columns

% choose only important columns with the nessesary info
if long == 0
%     data = dataCell(:,[2 9 10 68:72 116:119 106:107 102:103 121 142 143]); % only for patient ma201211 (the very first one, for him - the csv file format was a bit different)
    data = dataCell(:,[2 9 10 68:72 123:126 113:114 109:110 128 103 104]); % for new patients, from new version Psychopy 01.02.2021, columns: 
 % 'condition','feedback','block','joystick_resp_corr_immed','joystick_RT_corr_immed','joystick_RT_start_immed','missed_immed','ITI_immed',
 % 'joystick_resp_corr_del','joystick_RT_corr_del','joystick_RT_start_del','missed_del','text_cross_delay_started','text_cross_delay_stopped',
 % 'image_del_started','image_del_stopped', 'ITI_del',
 % 'answer_button_corr', 'answer_button.rt'

else
%     data = dataCell(:,[2 9 10 68:72 116:119 106:107 102:103 121 142 143 66:67 73:75 114:115 122:124 3:6 8]); % only for patient ma201211   
    data = dataCell(:,[2 9 10 68:72 123:126 113:114 109:110 128 103 104 66:67 73:75 121:122 129:131 3:6 8]); % from new version Psychopy 01.02.2021, % with x,y coordinates and time of joystick moves
end

% save names of columns separately and delete from data
VarNames = data(1,:);
data(1,:) = [];

% calculate true delay (column 14,delay stopped - column 13,delay started)
data(:,13) = cellfun(@minus,data(:,14),data(:,13),'UniformOutput',false);
VarNames{13} = 'delay';

% 04.04.2022 calculate true duration of encoding phase in delayed trials (column 16,image_del_stopped - column 15,image_del_started)
data(:,14) = cellfun(@minus,data(:,16),data(:,15),'UniformOutput',false);
VarNames{14} = 't_encod_del';
data(:,15:16) = [];
VarNames(15:16) = [];

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
        data{ri,20} = str2num(data{ri,20})-data{ri,18}; % x_immed - x1_immed (substract the displacement of joystick before the trial)
        data{ri,21} = str2num(data{ri,21})-data{ri,19}; % y_immed - y1_immed
        data{ri,22} = str2num(data{ri,22})-data{ri,8} + 0.02; % time points in immed - ITI_immed + 0.02 sec (joystick starts 2 ms before updating cursor)
        data{ri,25} = str2num(data{ri,25})-data{ri,23}; % x_del - x1_del
        data{ri,26} = str2num(data{ri,26})-data{ri,24}; % y_del - y1_del
        data{ri,27} = str2num(data{ri,27})-data{ri,13}-data{ri,14}-data{ri,15} + 0.02; % time points in del - delay - ITI_del - t_encod_del(image encoding) + 0.02 sec
    end
    
    % replace names of correct object by number: 3 - triangle, 4 - square
    tri = strcmpi(data(:,32),'triangle');
    data(tri,32) = {3};
    sqi = strcmpi(data(:,32),'square');
    data(sqi,32) = {4};
    
    coord_data = [data(:,20:22) data(:,25:32)]; % all coordinates together with correct ones
    coord_names = [VarNames(20:22) VarNames(25:32)]; % names of columns {'joystick_ImmedResp_x' 'joystick_ImmedResp_y' 'joystick_ImmedResp_time' 'joystick_DelResp_x' 'joystick_DelResp_y' 'joystick_DelResp_time' 'x_square' 'y_square' 'x_triangle' 'y_triangle' 'correct_object'}
    data = data(:,1:17); % general data {'condition' 'feedback' 'block' 'joystick_resp_corr_immed' 'joystick_RT_corr_immed' 'joystick_RT_start_immed' 'missed_immed' 'ITI_immed' 'joystick_resp_corr_del' 'joystick_RT_corr_del' 'joystick_RT_start_del' 'missed_del' 'delay' 't_encod_del' 'ITI_del' 'answer_button_corr'}
end

% transform into matrix for easier manipulations
dataMat = cell2mat(data);

% take only rows with meaningful values (without NaN)
ivalid = false(size(data,1),2);
ivalid(:,1) = ~isnan(dataMat(:,4));  % for immediate trials
ivalid(:,2) = ~isnan(dataMat(:,9));  % for delayed trials
ivalidAll = any(ivalid,2); % join indexes of both types of trials

% join RT, correct and missed responses for immed and delayed trials in one column
dataMat(ivalid(:,2),4:7) = dataMat(ivalid(:,2),9:12); % correct;RT of correct;RT of start of movement;missed trials

if long == 1   % join x,y coordinates and time points for immed and delayed trials in one column
    coord_data(ivalid(:,2),1:3) = coord_data(ivalid(:,2),4:6); % x; y; time points
    
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
AnswButIm = dataMat(~isnan(dataMat(:,16))& dataMat(:,1)==1,16); % for immed_diff
AnswButDel = dataMat(~isnan(dataMat(:,16))& dataMat(:,1)==3,16); % for del_diff 

% for column answer_button.rt: take only rows without NaN - different indexes than in ivalid
AnswButImRT = dataMat(~isnan(dataMat(:,16))& dataMat(:,1)==1,17); % for immed_diff
AnswButDelRT = dataMat(~isnan(dataMat(:,16))& dataMat(:,1)==3,17); % for del_diff 

% take all valid values for the entire matrix
dataMat = dataMat(ivalidAll,:); 

% replace last two columns - answer_button.corr and answer_button.rt by correct values for immed_diff and del_diff trials
dataMat(dataMat(:,1)==1,16)=AnswButIm; % immed_diff
dataMat(dataMat(:,1)==3,16)=AnswButDel; % del_diff
dataMat(dataMat(:,1)==1,17)=AnswButImRT; % immed_diff rt
dataMat(dataMat(:,1)==3,17)=AnswButDelRT; % del_diff rt

% May 2023: not nesessary anymore: missed trials should be stored separately to be comparable with iEEG package
% % join missed and correct in one column (missed - 0, correct - 1, incorrect - -1)
% imissed = logical(dataMat(:,7)); % find indexes of missed trials
% dataMat(imissed,4) = 0;  % in corr column replace missed by 0

% join ITI_immed and ITI_del in one column
iITI_im = ~isnan(dataMat(:,8));  % ITI for immediate trials
dataMat(iITI_im,15) = dataMat(iITI_im,8); % put them in column with del ITI

% now colums with delayed and missed trials can be deleted
dataMat(:, 8:12) = [];

% new names of variables
newVarNames = [VarNames(1:7) VarNames(13:17)];
tempCell =  regexp(newVarNames(4:6), '_', 'split');

% to get rid of word 'immed' and 'delayed' in names
for j = 1:length(tempCell)
    name = join(tempCell{j}(2:3), '_');
    newVarNames{3+j} = name{1};
end
name7 = regexp(newVarNames(7), '_', 'split');
newVarNames{7} = name7{1}{1};
name10 = regexp(newVarNames(10), '_', 'split');
newVarNames{10} = name10{1}{1};

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
    resp_corr = cell(2,2);
    resp_corr(1,:)={'incorrect' -1};
    %resp_corr(2,:)={'missed' 0};
    resp_corr(2,:)={'correct' 1};
    
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
