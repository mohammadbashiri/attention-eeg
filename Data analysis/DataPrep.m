
clear all
close all

inpath = strcat('.\Data\EEG\');
outpath = strcat('.\Data\EEG_PreProcessed\');

% List of filenames of all (or one) subjects
datasets = {'Subject01_s01_40block_each50trial',...
            'Subject02_s01_40block_each50trial',...
            'Subject03_s01_40block_each50trial'};

%% Information about recording
% this information must be filled depending on you electrode configuration
% while recording
channels       = 1:32;            
disabled_chans = [18];
ref_chans      = [10, 21];
channels([disabled_chans ref_chans]) = [];
channels_ind   = 1:length(channels);
% channels_now   = [channels' channels_ind'];
EOGs = [channels_ind(channels==5), channels_ind(channels==27)]; % EOGs = [5, 27]
channels_noEOG = channels_ind;
channels_noEOG(EOGs) = [];
% we can use EOGs and channels_noEOG as the variable for the code

%% data preparation
for s = 1:length(datasets)
    
    %% Load dataset
    filename = strcat(datasets{s},'.vhdr');
    EEG = pop_fileio(strcat(inpath, filename));
    
    % electrode 30 -> markers
    % why 30? in total 32 eletrodes. 2 for ref, 1 is disabled -> 29. That
    % leaves 30 for the markers/parallel.
    
%     EEG_ = pop_select(EEG,'channel',[30]);   % extract PD channels
%     EEG  = pop_select(EEG,'nochannel',[30]); % remove PD channels
%     EEG.data_pd = EEG_.data;
%     clear EEG_
    
    %% Bandpass filtering
    EEG = pop_eegfiltnew(EEG,1,20);    
    
    EEG_ = pop_select(EEG,'channel',[5 24]); % extract EOG channels
    EEG.data_eog = EEG_.data;
    clear EEG_
    
    EEG.chanlocs = pop_chanedit(EEG.chanlocs,...
    'lookup','.\Dependencies\eeglab14_1_1b\plugins\dipfit2.3\standard_BESA\standard-10-5-cap385.elp');


    %% bad channel detection and interpolation
    
    % does this remove anything? NO, it is rejecting and then
    % interpolating!
    
    [EEG_,EEG.reject.indelec] = pop_rejchan(EEG,'elec',[1:4,6:23,25:29],...
        'threshold',5,'norm','on','measure','kurt');
    EEG.chanrej = EEG.reject.indelec;
    EEG = pop_interp(EEG,EEG.reject.indelec,'spherical');
    clear EEG_

    %% automatic EOG artifact correction
    Cnn = EEG.data_eog*EEG.data_eog'; % auto covariance matrix of eog channels
    Cny = EEG.data*EEG.data_eog';     % cross covariance matrix of eog and eeg channels
    b = Cny*inv(Cnn); % compute weighting matrix
    
    %EEG.data_uncorr = EEG.data; % save uncorrected data
    EEG_ = EEG;
    EEG_.data = EEG.data-b*EEG.data_eog; % subtract eye-blinks with respective weighting 
    
    EEG_ = pop_select(EEG_,'nochannel',[5 24]); % remove EOG channels
    
    % TODO: compare the EEG with EEG_ to see if blink was rmeoved or
    % suppressed
    
    % At this point we have done the correction and do not need the EOG
    % channels anymroe, so removed them.
    
    %% re-referencing to CAR
%     EEG_ = pop_reref(EEG_,[]);
    
    %% resampling
    %EEG_ = pop_resample(EEG_,500)
    
    %% ICA decomposition
    %EEG_ = pop_runica(EEG_, 'extended',1,'interupt','on'); % ica decomposition

    pop_saveset(EEG_,'filepath',outpath,'filename',strcat(datasets{s},'.set'))
    
    clear EEG
    clear EEG_

end