close all
clear all

%% Setting data file names

inpath    = strcat('.\Data\EEG_PreProcessed\');
filename  = {
    'Subject01_s01_40block_each50trial',...
    'Subject02_s01_40block_each50trial',...
    'Subject03_s01_40block_each50trial'
    };

for s = 1:length(filename)
    
    % loading the data
    datapath  = strcat(inpath, filename{s});
    dataset   = strcat(datapath, '.set');

    EEGstruct         = pop_loadset(dataset);
    
    % save the data in a structure array (s representing the subject index)
    EEG(s).data       = EEGstruct.data;
    EEG(s).fs         = EEGstruct.srate;
    EEG(s).chanLabels = {EEGstruct.chanlocs(:).labels};
    EEG(s).chanlocs   = EEGstruct.chanlocs;
    
    % epoch data
    epoch_win         = [-.2 .8];
    EEG_epo           = pop_epoch(EEGstruct, {'S  2'}, epoch_win); % Motion-Shape
    EEG(s).data_epo   = EEG_epo.data;
    
    % events info
    event_name        = {EEGstruct.event(:).type};
    event_lat         = [EEGstruct.event(:).latency] / EEG(s).fs; % latency in second
    EEG(s).flash1_lat = event_lat(find(strcmp('S  2', event_name))); 
    EEG(s).flash2_lat = event_lat(find(strcmp('S  5', event_name))); 
    EEG(s).resp_lat   = event_lat(find(strcmp('S 11', event_name))); 
    
end

clear datapath
clear dataset
clear inpath
clear filename
clear EEG_epo
clear EEGstruct

%% load the log data
% this step is manual
% drag and drop the text file and name them according to the sequence of
% subjects. For now, I have saved them in a .mat file (trialtype.mat)
load('trialtype.mat');
EEG(1).trialtype = trialtype1;
EEG(2).trialtype = trialtype2;
EEG(3).trialtype = trialtype3;

%% calculate performance and removing trials based on subject response
target_win    = [.2 1];
nontarget_win = [0 1];
for s = 1:length(EEG)
    [EEG(s).perf, EEG(s).rejected, EEG(s).trialtype] =...
        eval_performance(EEG(s).flash1_lat, EEG(s).resp_lat, EEG(s).trialtype, target_win, nontarget_win);
end

%% re-referencing to mean of 200 ms prior onset (this happens per stimulus)
for s = 1:length(EEG)
    win = [1/EEG(s).fs .2] * EEG(s).fs; % corresponds to first 200ms (-.2 to 0)
    EEG(s).data_epo = EEG(s).data_epo - mean(EEG(s).data_epo(:,win(1):win(2),:),2);
end
    
%% Separating data

for s = 1:length(EEG)

    EEG(s).TMpCp = EEG(s).data_epo(:,:,EEG(s).trialtype==1);
    EEG(s).TMpCn = EEG(s).data_epo(:,:,EEG(s).trialtype==2);
    EEG(s).TMnCp = EEG(s).data_epo(:,:,EEG(s).trialtype==3);
    EEG(s).TMnCn = EEG(s).data_epo(:,:,EEG(s).trialtype==4);
    EEG(s).TMpSp = EEG(s).data_epo(:,:,EEG(s).trialtype==5);
    EEG(s).TMpSn = EEG(s).data_epo(:,:,EEG(s).trialtype==6);
    EEG(s).TMnSp = EEG(s).data_epo(:,:,EEG(s).trialtype==7);
    EEG(s).TMnSn = EEG(s).data_epo(:,:,EEG(s).trialtype==8);
    EEG(s).SMpCp = EEG(s).data_epo(:,:,EEG(s).trialtype==11);
    EEG(s).SMpCn = EEG(s).data_epo(:,:,EEG(s).trialtype==12);
    EEG(s).SMnCp = EEG(s).data_epo(:,:,EEG(s).trialtype==13);
    EEG(s).SMnCn = EEG(s).data_epo(:,:,EEG(s).trialtype==14);
    EEG(s).SMpSp = EEG(s).data_epo(:,:,EEG(s).trialtype==15);
    EEG(s).SMpSn = EEG(s).data_epo(:,:,EEG(s).trialtype==16);
    EEG(s).SMnSp = EEG(s).data_epo(:,:,EEG(s).trialtype==17);
    EEG(s).SMnSn = EEG(s).data_epo(:,:,EEG(s).trialtype==18);

end

%% plotting averaged data (all the figures in the paper for a specific channel)

chan = 14;
subject = 2;
plotFigs(EEG(subject), chan, epoch_win, false)

%% Computing p values (unpaired ttest) - for one or all subjects

win_start = .048;
win_len = .024;
[window, p_values] = calcPowMult( {EEG(:).SMpSp}, {EEG(:).SMpSn}, win_start, win_len, epoch_win, 'ttest');

figure;
surf(window(:,1), 1:27, p_values); view(2);
xlabel('time (ms)'); ylabel('channel');
c = colorbar;
c.Label.String = 'P value';
axis tight; % shading interp

%% topography for one subject
s = 3;
window = [.552 .6];
data1 = zeros(27,1);  % we have 27 channels
data2 = zeros(27,1);
for chan = 1:27
    data1(chan) = mean(calcPow( EEG(s).SMpCp, window, chan, epoch_win(1), EEG(s).fs ));
    data2(chan) = mean(calcPow( EEG(s).SMnCp, window, chan, epoch_win(1), EEG(s).fs ));
end
figure;
topoplot(data1-data2,EEG(1).chanlocs,'maplimits',[-1 2])
colorbar

%% topogtaphy for all subjects (averaged)

window = [.384 .6];
data1 = zeros(27,1);
data2 = zeros(27,1);
for chan = 1:27
    for s = 1:length(EEG)
        data1(chan) = data1(chan) + mean(calcPow( EEG(s).SMpSp, window, chan, epoch_win(1), EEG(s).fs ))/length(EEG);
        data2(chan) = data2(chan) + mean(calcPow( EEG(s).SMpSn, window, chan, epoch_win(1), EEG(s).fs ))/length(EEG);
    end
end
figure;
topoplot(data1-data2,EEG(1).chanlocs,'maplimits',[-.6 .6])
c = colorbar;
c.Label.String = 'difference V';


%% plot specific channel average over all subjects
close all;
chan = 24;
win = [.168 .24];

data1 = [];
data2 = [];
for s = 1: length(EEG)
    t = epoch_win(1):1/EEG(s).fs:epoch_win(2)-1/EEG(s).fs;
    data1 = [data1 squeeze(EEG(s).SMpSp(chan,:,:))];
    data2 = [data2 squeeze(EEG(s).SMpSn(chan,:,:))];
end

% rectangle('Position',[win(1),-2,win(2)-win(1),5],'FaceColor',[0 .5 .5 .4],...
%     'EdgeColor','none'); hold on;

plot(t, mean(data1,2) - mean(data2,2), 'k'); grid; ylim([-2 3])
xlabel('time (ms)'); ylabel('voltage (\muV)')
% title([{'Motion attention effects (with color selection)'}, {strcat('Channel: ', EEG(s).chanLabels{chan})}]);
% legend('(M+/C+)-(M-/C+)', 'Location', 'northwest');

%% box plot for data
s = 2;
chan = 20;
window = [.12 .144];
data1 = calcPow(EEG(s).SMnCp, window, chan, epoch_win(1), EEG(s).fs);
boxplot(data1)





