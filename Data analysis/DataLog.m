% in this piece of code we take the logged data and divide it into:

% 1 - TrtMposCpos (standard M+/C+) -> attended motion + attended color
% 2 - TrtMposCneg
% 3 - TrtMnegCpos
% 4 - TrtMnegCneg
% 5 - TrtMposSpos
% 6 - TrtMposSneg
% 7 - TrtMnegSpos
% 8 - TrtMnegSneg
% 
% 11 - StdMposCpos (standard M+/C+) -> attended motion + attended color
% 12 - StdMposCneg
% 13 - StdMnegCpos
% 14 - StdMnegCneg
% 15 - StdMposSpos
% 16 - StdMposSneg
% 17 - StdMnegSpos
% 18 - StdMnegSneg

% while importing the data (drag and drop). Make sure to select "Text" for
% the feat1 column

trial_labels = zeros(trial(end),1);


%% start inserting the corresponding number for all the trials
% for that we should loop through the trials

for i = 1:numel(trial_labels)
    if (stim_type(i)==3) % standard
        if strcmp(mode1{i},'motion-color')

            if ((shift(i) == feat2(i)) && strcmp(color1{i},feat1{i}))      % stdMposCpos
                trial_labels(i) = 11;
            elseif ((shift(i) == feat2(i)) && ~strcmp(color1{i},feat1{i})) % stdMposCneg
                trial_labels(i) = 12;
            elseif ((shift(i) ~= feat2(i)) && strcmp(color1{i},feat1{i}))  % stdMnegCpos
                trial_labels(i) = 13;
            elseif ((shift(i) ~= feat2(i)) && ~strcmp(color1{i},feat1{i})) % stdMnegCpos
                trial_labels(i) = 14;
            end

        elseif strcmp(mode1{i},'motion-shape')

            if ((shift(i) == feat2(i)) && strcmp(num2str(shape1(i)), feat1(i)))      % stdMposSpos
                trial_labels(i) = 15;
            elseif ((shift(i) == feat2(i)) && ~strcmp(num2str(shape1(i)), feat1(i))) % stdMposSneg
                trial_labels(i) = 16;
            elseif ((shift(i) ~= feat2(i)) && strcmp(num2str(shape1(i)), feat1(i)))  % stdMnegSpos
                trial_labels(i) = 17;
            elseif ((shift(i) ~= feat2(i)) && ~strcmp(num2str(shape1(i)), feat1(i))) % stdMnegSpos
                trial_labels(i) = 18;
            end

        end
        
    elseif (stim_type(i)==9) % target
        if strcmp(mode1{i},'motion-color')

            if ((shift(i) == feat2(i)) && strcmp(color1{i},feat1{i}))      % trtMposCpos
                trial_labels(i) = 1;
            elseif ((shift(i) == feat2(i)) && ~strcmp(color1{i},feat1{i})) % trtMposCneg
                trial_labels(i) = 2;
            elseif ((shift(i) ~= feat2(i)) && strcmp(color1{i},feat1{i}))  % trtMnegCpos
                trial_labels(i) = 3;
            elseif ((shift(i) ~= feat2(i)) && ~strcmp(color1{i},feat1{i})) % trtMnegCpos
                trial_labels(i) = 4;
            end

        elseif strcmp(mode1{i},'motion-shape')

            if ((shift(i) == feat2(i)) && strcmp(num2str(shape1(i)), feat1(i)))      % stdMposSpos
                trial_labels(i) = 5;
            elseif ((shift(i) == feat2(i)) && ~strcmp(num2str(shape1(i)), feat1(i))) % stdMposSneg
                trial_labels(i) = 6;
            elseif ((shift(i) ~= feat2(i)) && strcmp(num2str(shape1(i)), feat1(i)))  % stdMnegSpos
                trial_labels(i) = 7;
            elseif ((shift(i) ~= feat2(i)) && ~strcmp(num2str(shape1(i)), feat1(i))) % stdMnegSpos
                trial_labels(i) = 8;
            end
            
        end
    end
end

