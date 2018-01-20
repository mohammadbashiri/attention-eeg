%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
%
% Data analysis of dataset HRI full study
% Preprocessing and data preparation
%
% Input:    raw data provided by S. Ehrlich
% Output:   EEGLAB like data format 
%
% Author: Stefan Ehrlich
% Last revised: 21.06.2016
%
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


clear all
close all

inpath = strcat(pwd,'\data\');
outpath = strcat(pwd,'\data_pp1\');

% List of filenames of all subjects
datasets = {'s02_shooter','s02_robot',...
    's03_shooter','s03_robot',...
    's04_shooter','s04_robot',...
    's05_shooter','s05_robot',...
    's06_shooter','s06_robot',...
    's07_shooter','s07_robot',...
    's08_shooter','s08_robot',...
    's09_shooter','s09_robot',...
    's10_shooter','s10_robot',...
    's11_shooter','s11_robot',...
    's12_shooter','s12_robot',...
    's13_shooter','s13_robot'};

for s = 1:length(datasets)

    %% Load dataset
    filename = strcat(datasets{s},'.vhdr');
    EEG = pop_fileio(strcat(inpath,filename));
    
    EEG_ = pop_select(EEG,'channel',[31 32]); % extract PD channels
    EEG = pop_select(EEG,'nochannel',[31 32]); % remove PD channels
    EEG.data_pd = EEG_.data;
    clear EEG_
    
    %% Bandpass filtering
    EEG = pop_eegfiltnew(EEG,1,40)      
    
    EEG_ = pop_select(EEG,'channel',[5 16 25]); % extract EOG channels
    EEG.data_eog = EEG_.data;
    clear EEG_
    
    EEG.chanlocs = pop_chanedit(EEG.chanlocs,...
    'lookup','C:\Daten\MATLABToolboxes\eeglab13_1_1b\plugins\dipfit2.3\standard_BESA\standard-10-5-cap385.elp');
%      EEG.chanlocs = pop_chanedit(EEG.chanlocs,...
%      'lookup','E:\BCI\eeglab13_3_2b\plugins\dipfit2.3\standard_BESA\standard-10-5-cap385.elp');



    %% bad channel detection and interpolation
    [EEG_,EEG.reject.indelec] = pop_rejchan(EEG,'elec',[1:4,6:15,17:24,26:30],...
        'threshold',5,'norm','on','measure','kurt');
    EEG.chanrej = EEG.reject.indelec;
    EEG = pop_interp(EEG,EEG.reject.indelec,'spherical')
    clear EEG_

    %% automatic EOG artifact correction
    Cnn = EEG.data_eog*EEG.data_eog'; % auto covariance matrix of eog channels
    Cny = EEG.data*EEG.data_eog'; % cross covariance matrix of eog and eeg channels
    b = Cny*inv(Cnn); % compute weighting matrix
    
    %EEG.data_uncorr = EEG.data; % save uncorrected data
    EEG_ = EEG;
    EEG_.data = EEG.data-b*EEG.data_eog; % subtract eye-blinks with respective weighting 
    
    EEG_ = pop_select(EEG_,'nochannel',[5 16 25]); % remove EOG channels
    
    %% re-referencing to CAR
    EEG_ = pop_reref(EEG_,[]);
    %EEG_ = pop_resample(EEG_,500)
    
    %% ICA decomposition
    %EEG_ = pop_runica(EEG_, 'extended',1,'interupt','on'); % ica decomposition

    pop_saveset(EEG_,'filepath',outpath,'filename',strcat(datasets{s},'.set'))
    
    clear EEG
    clear EEG_

end