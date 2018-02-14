function [ perf, perc_rejected, correct_trials ] = eval_performance( flash1_lat, resp_lat, trialtype, t_win, nt_win )
%EVAL_PERFORMANCE returns the performance of the subject and also return
%the trials that must be considered in later analysis

correct_trials = trialtype; %zeros(1, numel(EEG(1).flash1_lat));
target_win     = t_win;
nontarget_win  = nt_win;

% check through all flash1 latency for target stimuli
for i = 1:numel(flash1_lat)
    
    if trialtype(i) == 1 % check if this trial is a target
        
        if sum((resp_lat > flash1_lat(i) + target_win(1)) & (resp_lat < flash1_lat(i) + target_win(2)))
            continue;
        else
            correct_trials(i) = -1;
        end
        
    else
        
        if sum((resp_lat > flash1_lat(i) + nontarget_win(1)) & (resp_lat < flash1_lat(i) + nontarget_win(2)))
            correct_trials(i) = -1; 
        else
            continue;
        end
        
    end
end

perf = sum(correct_trials == 1) / sum(trialtype == 1);
perc_rejected = sum(correct_trials == -1) / length(trialtype);

end

