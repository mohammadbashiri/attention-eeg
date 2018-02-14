function [ window, p_values ] = calcPowMult2( EEG1, EEG2, win_start, win_len, epoch_win, test )
%CALCPOWMULT given window length and window starting point, it return the p
%values of the signal voltages for all channels and all windows until the
%end of the epoch

% example: when channel is 10, and for a specific window, we take the mean
% of that window for all trials. Hence, for a specific stimulus, we are 
% left with one vector which has the dimension of number of trials for that
% stimulus. And doing the same thing for another stimulus type, we now can
% compare them (i.e., unpaired ttest). This function does that for all 
% channels and all time window


% The difference of this over Mult is that this combines all subjects and
% then computes the p values

start = [win_start, win_start + win_len];
win_n = floor((epoch_win(2)-win_start)/win_len);
win_coef = (0:win_n-1)';
window = repmat(start, win_n, 1);
window = window + win_len.*win_coef;

fs = 1000;
p_values = zeros(size(EEG1{1},1), size(window,1));

for c = 1:size(EEG1{1},1)

    for w = 1:size(window,1)
        
        data1 = [];
        data2 = [];
        
        for s = 1:length(EEG1)
        
            win1 = calcPow(EEG1{s}, window(w,:), c, epoch_win(1), fs);
            win2 = calcPow(EEG2{s}, window(w,:), c, epoch_win(1), fs);
            
            data1 = [data1 win1'];
            data2 = [data2 win2'];
            
        end
        
        if strcmp(test, 'ttest')
%             disp('ttest')
            [~, p_values(c, w)] = ttest2(data1, data2);
        else
%             disp('anova')
            g1 = ones(1, length(data1));
            g2 = zeros(1, length(data2));
            group = [g1 g2];
            p_values(c, w) = anova1([data1 data2], group, 'off');
        end

    end

end
end



