% example of trajectory for one specific trial

% number of trial
triali = 65;

% get the general behavioral data (matrix separately)
general_data = MemoryActions.Gdata;
% get coordinates data
joy_coordinates = MemoryActions.CoordData; % frames x (x,y,t) x trials
corr_coordinates =  MemoryActions.Coord_correct;

% get joystick's coordinates and time for one trial
x = squeeze(joy_coordinates(:,1,triali)); % x
y = squeeze(joy_coordinates(:,2,triali)); % y
t = squeeze(joy_coordinates(:,3,triali)); % t

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

% distance between square and triangle
SqTr_distance = sqrt((x_corr-x_uncorr_obj)^2+(y_corr-y_uncorr_obj)^2);

%% plot
figure(3),clf, hold on
plot(x, y, 'r', 'LineWidth', 1.5) % trajectory of joystick
set(gca, 'xlim', [-0.5 0.5], 'ylim', [-0.5 0.5], 'xtick', [], 'ytick', []), box on
axis square
plot(0,0, 'k+', 'LineWidth', 1.5, 'MarkerSize', 13) % cross in the middle
plot(x_corr, y_corr, ['m' obj1],'LineWidth', 1.5,'MarkerSize', 13) % correct object - magenta
plot(x_uncorr_obj, y_uncorr_obj, ['k' obj2], 'LineWidth', 1.5,'MarkerSize', 13) % the second object - black

% % area around the objects for correct response according to the PsychoPy code version from 10.12.2020 
% patch([x_corr-0.105 x_corr-0.105 x_corr+0.105 x_corr+0.105],[y_corr-0.105 y_corr+0.105 y_corr+0.105 y_corr-0.105],'g', 'FaceAlpha',.2)
% patch([x_uncorr_obj-0.105 x_uncorr_obj-0.105 x_uncorr_obj+0.105 x_uncorr_obj+0.105],[y_uncorr_obj-0.105 y_uncorr_obj+0.105 y_uncorr_obj+0.105 y_uncorr_obj-0.105],'r', 'FaceAlpha',.2)

% area around the objects for correct response according to the PsychoPy code version from 19.01.2021
patch([x_corr-SqTr_distance/4 x_corr-SqTr_distance/4 x_corr+SqTr_distance/4 x_corr+SqTr_distance/4],[y_corr-SqTr_distance/4 y_corr+SqTr_distance/4 y_corr+SqTr_distance/4 y_corr-SqTr_distance/4],'g', 'FaceAlpha',.2)
patch([x_uncorr_obj-SqTr_distance/4 x_uncorr_obj-SqTr_distance/4 x_uncorr_obj+SqTr_distance/4 x_uncorr_obj+SqTr_distance/4],[y_uncorr_obj-SqTr_distance/4 y_uncorr_obj+SqTr_distance/4 y_uncorr_obj+SqTr_distance/4 y_uncorr_obj-SqTr_distance/4],'r', 'FaceAlpha',.2)

%% a video of joystick movement
% write a video of joystick movements
% first plot
figure(2), clf, hold on
x0 = 0;
y0 = 0;
h = plot(x0, y0, 'bo', 'MarkerSize', 3, 'MarkerFaceColor', 'b'); % trajectory of joystick - start
set(gca, 'xlim', [-0.5 0.5], 'ylim', [-0.5 0.5], 'xtick', [], 'ytick', []), box on
axis square
plot(0,0, 'k+', 'LineWidth', 1.5, 'MarkerSize', 13) % cross in the middle
plot(x_corr, y_corr, ['m' obj1],'LineWidth', 1.5,'MarkerSize', 13) % correct object - magenta
plot(x_uncorr_obj, y_uncorr_obj, ['k' obj2], 'LineWidth', 1.5,'MarkerSize', 13) % the second object - black
% setup movie
mov = VideoWriter(['trial' num2str(triali) '.avi']);
mov.FrameRate = 60;
open(mov)

% create data
for framei=1:length(x)
    % draw the data in the axis
    x0 = [x0 x(framei)];
    y0 = [y0 y(framei)];
    set(h, 'XData', x0)
    set(h, 'YData', y0)
    % update movie frame
    writeVideo(mov, getframe(gcf));
    pause(.01)
end
% write out movie
close(mov)


%% interpolation
corr_zoneX = [x_corr-SqTr_distance/4 x_corr-SqTr_distance/4 x_corr+SqTr_distance/4 x_corr+SqTr_distance/4];
corr_zoneY = [y_corr-SqTr_distance/4 y_corr+SqTr_distance/4 y_corr+SqTr_distance/4 y_corr-SqTr_distance/4];

[x_inter,y_inter] = intersections(x,y,corr_zoneX,corr_zoneY);
hold on
plot(x_inter, y_inter, 'ko', 'LineWidth', 1.5, 'LineStyle', 'None')





% the timing of each frame
frame_diff = diff(t);

