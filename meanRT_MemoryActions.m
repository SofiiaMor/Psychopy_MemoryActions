% average RT and accuracy in MemoryActions test
% first, load data to matlab
% e.g. load('D:\eeg\motol\PsychoPydata\MemoryActions\ma201211_MemoryActions.mat')

% get the general behavioral data (matrix separately)
beh_data = MemoryActions.Gdata;

% only main session without training
% RT
RTcorr_imm_same = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==0 & beh_data(:, 4)==1, 5);
RTstart_imm_same = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==0 & beh_data(:, 4)==1, 6);

RTcorr_imm_diff = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==1 & beh_data(:, 4)==1, 5);
RTstart_imm_diff = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==1 & beh_data(:, 4)==1, 6);

RTcorr_del_same = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==2 & beh_data(:, 4)==1, 5);
RTstart_del_same = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==2 & beh_data(:, 4)==1, 6);

RTcorr_del_diff = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==3 & beh_data(:, 4)==1, 5);
RTstart_del_diff = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==3 & beh_data(:, 4)==1, 6);

% accuracy
accur_imm_same = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==0, 4);
success_imm_same = sum(accur_imm_same==1)/numel(accur_imm_same)*100;

accur_imm_diff = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==1, 4);
success_imm_diff = sum(accur_imm_diff==1)/numel(accur_imm_diff)*100;

accur_del_same = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==2, 4);
success_del_same = sum(accur_del_same==1)/numel(accur_del_same)*100;

accur_del_diff = beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==3, 4);
success_del_diff = sum(accur_del_diff==1)/numel(accur_del_diff)*100;

%% ploting
figure(1), clf
subplot(211)
x = categorical({'immed same','immed diff','del same','del diff'});
bar(x,[mean(RTcorr_imm_same,'omitnan'), mean(RTstart_imm_same,'omitnan'); mean(RTcorr_imm_diff,'omitnan'), mean(RTstart_imm_diff,'omitnan');...
    mean(RTcorr_del_same,'omitnan'), mean(RTstart_del_same,'omitnan'); mean(RTcorr_del_diff,'omitnan'), mean(RTstart_del_diff,'omitnan')]);

% xn = 1:8;
% errorbar(xn,[mean(RTcorr_imm_same,'omitnan') mean(RTstart_imm_same,'omitnan') mean(RTcorr_imm_diff,'omitnan') mean(RTstart_imm_diff,'omitnan')...
%     mean(RTcorr_del_same,'omitnan') mean(RTstart_del_same,'omitnan') mean(RTcorr_del_diff,'omitnan') mean(RTstart_del_diff,'omitnan')],...
%     [std(RTcorr_imm_same,'omitnan') std(RTstart_imm_same,'omitnan') std(RTcorr_imm_diff,'omitnan') std(RTstart_imm_diff,'omitnan')...
%     std(RTcorr_del_same,'omitnan') std(RTstart_del_same,'omitnan') std(RTcorr_del_diff,'omitnan') std(RTstart_del_diff,'omitnan')],'.')
ylabel('mean RT, sec');
legend('RT correct', 'RT start')
title('RT')

subplot(212)
bar(x,[success_imm_same; success_imm_diff; success_del_same; success_del_diff], 0.3, 'FaceColor', [0 0.45 0.55])
ylabel('accuracy, %');
title('accuracy')
