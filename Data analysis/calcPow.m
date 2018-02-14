function [ data_out ] = calcPow( data, window, chan, epoch_st, fs )
%CALCPOW Summary of this function goes here
%   Detailed explanation goes here

win = (window + abs(epoch_st)) * fs;
data_out = squeeze(mean(data(chan, win(1):win(2), :),2));

end

