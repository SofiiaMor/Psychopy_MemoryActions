% average RT and accuracy in MemoryActions test
% get the general behavioral data (matrix separately)
beh_data = MemoryActions.Gdata;

main_RT_corr_imm_same = mean(beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==0 & beh_data(:, 4)==1, 5), 'omitnan');
main_RT_start_imm_same = mean(beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==0 & beh_data(:, 4)==1, 6), 'omitnan');

main_RT_corr_imm_diff = mean(beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==1 & beh_data(:, 4)==1, 5), 'omitnan');
main_RT_start_imm_diff = mean(beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==1 & beh_data(:, 4)==1, 6), 'omitnan');

main_RT_corr_del_same = mean(beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==2 & beh_data(:, 4)==1, 5), 'omitnan');
main_RT_start_del_same = mean(beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==2 & beh_data(:, 4)==1, 6), 'omitnan');

main_RT_corr_del_diff = mean(beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==3 & beh_data(:, 4)==1, 5), 'omitnan');
main_RT_start_del_diff = mean(beh_data(beh_data(:, 3) > 0 & beh_data(:, 1)==3 & beh_data(:, 4)==1, 6), 'omitnan');

figure(1), clf
x = categorical({'immed same','immed diff','del same','del diff'});
h = bar(x,[main_RT_corr_imm_same main_RT_start_imm_same; main_RT_corr_imm_diff main_RT_start_imm_diff; main_RT_corr_del_same main_RT_start_del_same; main_RT_corr_del_diff main_RT_start_del_diff]);
ylabel('mean RT, sec');
legend('RT correct', 'RT start')
title('patient ma201211')