function [ ] = plotFigs( EEG, chan, win, save )
%PLOTFIGS Summary of this function goes here
%   Detailed explanation goes here

% 4 13 17 20 26

t = win(1):1/EEG.fs:win(2)-1/EEG.fs;

h = figure; ind = 1;
plot(t, mean(EEG.SMpCp(chan,:,:),3), 'k'); hold on
plot(t, mean(EEG.SMpCn(chan,:,:),3), 'k:');
plot(t, mean(EEG.SMnCp(chan,:,:),3), 'k-.');
plot(t, mean(EEG.SMnCn(chan,:,:),3), 'k--');
title([{'Attended motion and color Standards'}, {strcat('Channel: ', EEG.chanLabels{chan})}]);
xlabel('time (s)'); ylabel('voltage (\muV)'); grid;
legend('M+/C+','M+/C-','M-/C+','M-/C-')
if save
    saveas(h, strcat(['(',num2str(ind),')'], EEG.chanLabels{chan}), 'jpg'); ind = ind + 1;
end
% plot data: Attended motion and shape Standards 
h = figure;
plot(t, mean(EEG.SMpSp(chan,:,:),3), 'k'); hold on
plot(t, mean(EEG.SMpSn(chan,:,:),3), 'k:');
plot(t, mean(EEG.SMnSp(chan,:,:),3), 'k-.');
plot(t, mean(EEG.SMnSn(chan,:,:),3), 'k--');
title([{'Attended motion and shape Standards'}, {strcat('Channel: ', EEG.chanLabels{chan})}]);
xlabel('time (s)'); ylabel('voltage (\muV)'); grid;
legend('M+/S+','M+/S-','M-/S+','M-/S-')
if save
    saveas(h, strcat(['(',num2str(ind),')'], EEG.chanLabels{chan}), 'jpg'); ind = ind + 1;
end
% plot data: Motion attention effects (with color selection)
h = figure;
plot(t, mean(EEG.SMpCp(chan,:,:),3) - mean(EEG.SMnCp(chan,:,:),3), 'k'); hold on
plot(t, mean(EEG.SMpCn(chan,:,:),3) - mean(EEG.SMnCn(chan,:,:),3), 'k:');
title([{'Motion attention effects (with color selection)'}, {strcat('Channel: ', EEG.chanLabels{chan})}]);
xlabel('time (s)'); ylabel('voltage (\muV)'); grid;
legend('(M+/C+)-(M-/C+)','(M+/C-)-(M-/C-)');
if save
    saveas(h, strcat(['(',num2str(ind),')'], EEG.chanLabels{chan}), 'jpg'); ind = ind + 1;
end

% plot data: Motion attention effects (with color selection)
h = figure;
plot(t, mean(EEG.SMpSp(chan,:,:),3) - mean(EEG.SMnSp(chan,:,:),3), 'k'); hold on
plot(t, mean(EEG.SMpSn(chan,:,:),3) - mean(EEG.SMnSn(chan,:,:),3), 'k:');
title([{'Motion attention effects (with shape selection)'}, {strcat('Channel: ', EEG.chanLabels{chan})}]);
xlabel('time (s)'); ylabel('voltage (\muV)'); grid;
legend('(M+/S+)-(M-/S+)','(M+/S-)-(M-/S-)');
if save
    saveas(h, strcat(['(',num2str(ind),')'], EEG.chanLabels{chan}), 'jpg'); ind = ind + 1;
end

% plot data: Motion attention effects (with color selection)
h = figure;
plot(t, mean(EEG.SMpCp(chan,:,:),3) - mean(EEG.SMpCn(chan,:,:),3), 'k'); hold on
plot(t, mean(EEG.SMnCp(chan,:,:),3) - mean(EEG.SMnCn(chan,:,:),3), 'k:');
title([{'Color attention effects'}, {strcat('Channel: ', EEG.chanLabels{chan})}]);
xlabel('time (s)'); ylabel('voltage (\muV)'); grid;
legend('(M+/C+)-(M+/C-)','(M-/C+)-(M-/C-)');
if save
    saveas(h, strcat(['(',num2str(ind),')'], EEG.chanLabels{chan}), 'jpg'); ind = ind + 1;
end

% plot data: Motion attention effects (with color selection)
h = figure;
plot(t, mean(EEG.SMpSp(chan,:,:),3) - mean(EEG.SMpSn(chan,:,:),3), 'k'); hold on
plot(t, mean(EEG.SMnSp(chan,:,:),3) - mean(EEG.SMnSn(chan,:,:),3), 'k:');
title([{'Shape attention effects'}, {strcat('Channel: ', EEG.chanLabels{chan})}]);
xlabel('time (s)'); ylabel('voltage (\muV)'); grid;
legend('(M+/S+)-(M+/S-)','(M-/S+)-(M-/S-)');
if save
    saveas(h, strcat(['(',num2str(ind),')'], EEG.chanLabels{chan}), 'jpg'); ind = 0;
end

end

