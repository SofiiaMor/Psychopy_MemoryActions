function PlotJoyTrajectory(matFilename)
%%%% function for ploting joystick trajectory of one subject in the test MemoryActions
%%%% per each block separately (without training blocks)
%%%%
%%%%     matFilename - the name of mat file with behavioral data,
%%%%     obtained after calling function MemoryActionsImport (without path)

% the folder where behav data were saved
dir = 'D:\eeg\motol\PsychoPydata\MemoryActions\';
% dir = 'E:\работа\MemoryActions\data\';
fullfilename = fullfile(dir, matFilename);
% load .mat file with behavioural data
load(fullfilename)

% new folder where to save output images
newFolder = split(matFilename,'.');
newFolder = newFolder{1}; % name of test and patient
eval(['!mkdir D:\eeg\motol\PsychoPydata\MemoryActions\' newFolder]); % create folder
% eval(['!mkdir E:\работа\MemoryActions\data\' newFolder]); % create folder
path = [dir newFolder]; % path for saving images

% get the general behavioral data (matrix separately)
general_data = MemoryActions.Gdata;
% get coordinates data
joy_coordinates = MemoryActions.CoordData; % frames x (x,y,t) x trials
corr_coordinates =  MemoryActions.Coord_correct;

% from 1 to the last block without training session
for blocki = 1:general_data(end,3)
    blockiTrials = find(general_data(:,3) == blocki); % find the indexes (trials) of this block
    Ntrials = numel(blockiTrials); % the number of trials for subplot
    
    % initialize for ploting
    subploti = 0;
    fig=figure('Name', ['block ' num2str(blocki)]); hold on
    fig.WindowState = 'maximized';
    
    % for trials of this block
    for triali = blockiTrials(1): blockiTrials(end)
        
        % get joystick's coordinates for one trial
        x = squeeze(joy_coordinates(:,1,triali)); % x
        y = squeeze(joy_coordinates(:,2,triali)); % y
        
        % get coordinates of correct object and another object
        if corr_coordinates(triali,5)==3 % if correct object - triangle
            x_corr = corr_coordinates(triali,3); % take triangle's coordinates
            y_corr = corr_coordinates(triali,4);
            x_uncorr_obj = corr_coordinates(triali,1); % take coordinates of another object
            y_uncorr_obj = corr_coordinates(triali,2);
            corr_Obj = '^'; % for ploting triangle
            uncorr_Obj = 's'; % for ploting square
        else % if correct object - square
            x_corr = corr_coordinates(triali,1); % take squares's coordinates
            y_corr = corr_coordinates(triali,2);
            x_uncorr_obj = corr_coordinates(triali,3); % take coordinates of another object
            y_uncorr_obj = corr_coordinates(triali,4);
            corr_Obj = 's';
            uncorr_Obj = '^';
        end
        
        % define the type of objects in the trial
        if general_data(triali,1) == 0 || general_data(triali,1) == 2 % immed_same or delayed_same
            obj1 = 'o';  % plot circles
            obj2 = obj1;
        else
            obj1 = corr_Obj;   % plot triangle and square
            obj2 = uncorr_Obj;
        end
        
        % define condition
        if general_data(triali,1) == 0
            condition = 'immed same';
        elseif general_data(triali,1) == 1
            condition = 'immed diff';
        elseif general_data(triali,1) == 2
            condition = 'del same';
        elseif general_data(triali,1) == 3
            condition = 'del diff';
        end
        
        % define if it was correct/incorrect/missed according to PsychoPy code
        if general_data(triali,4) == 0
            response = 'missed';
        elseif general_data(triali,4) == 1
            response = 'correct';
            trajColor = 'parula';
        elseif general_data(triali,4) == -1
            response = 'incorrect';
            trajColor = 'hot';
        end
        
        % distance between square and triangle
        SqTr_distance = sqrt((x_corr-x_uncorr_obj)^2+(y_corr-y_uncorr_obj)^2);
        
        % ploting
        subploti = subploti + 1;
        ax = subplot(5,Ntrials/5,subploti); hold on
        plot(0,0, 'k+', 'LineWidth', 1, 'MarkerSize', 6) % cross in the middle
        plot(x_corr, y_corr, ['k' obj1],'LineWidth', 1,'MarkerSize', 5) % correct object
        plot(x_uncorr_obj, y_uncorr_obj, ['k' obj2], 'LineWidth', 1,'MarkerSize', 5) % the second object
        
        % area around the objects for correct response according to the PsychoPy code version from 10.12.2020
        patch([x_corr-0.105 x_corr-0.105 x_corr+0.105 x_corr+0.105],[y_corr-0.105 y_corr+0.105 y_corr+0.105 y_corr-0.105],'g', 'FaceAlpha',.1, 'EdgeColor', 'g')
        patch([x_uncorr_obj-0.105 x_uncorr_obj-0.105 x_uncorr_obj+0.105 x_uncorr_obj+0.105],[y_uncorr_obj-0.105 y_uncorr_obj+0.105 y_uncorr_obj+0.105 y_uncorr_obj-0.105],'r', 'FaceAlpha',.1, 'EdgeColor', 'r')
        
        % area around the objects for correct response according to the new PsychoPy code version
%         patch([x_corr-SqTr_distance/4 x_corr-SqTr_distance/4 x_corr+SqTr_distance/4 x_corr+SqTr_distance/4],[y_corr-SqTr_distance/4 y_corr+SqTr_distance/4 y_corr+SqTr_distance/4 y_corr-SqTr_distance/4],'g', 'FaceAlpha',.1, 'EdgeColor', 'g')
%         patch([x_uncorr_obj-SqTr_distance/4 x_uncorr_obj-SqTr_distance/4 x_uncorr_obj+SqTr_distance/4 x_uncorr_obj+SqTr_distance/4],[y_uncorr_obj-SqTr_distance/4 y_uncorr_obj+SqTr_distance/4 y_uncorr_obj+SqTr_distance/4 y_uncorr_obj-SqTr_distance/4],'r', 'FaceAlpha',.1, 'EdgeColor', 'r')
%         
        scatter(x, y, 5, 1:length(x), 'filled'); % trajectory of joystick
        colormap(ax,trajColor)
        set(gca, 'xlim', [-0.5 0.5], 'ylim', [-0.5 0.5], 'xtick', [], 'ytick', []), box on
        axis square
        title([num2str(triali) ', ' condition ', ' response])
    end
    
    % save the plot
    %set(fig, 'Visible', 'off'); % hide the figure
    imFilename = sprintf('block_%2d', blocki);
    fullimFilename = fullfile(path, imFilename);
    print(fig,fullimFilename,'-djpeg', '-r300'); % save the figure
    close(fig); % close figure
end
end