clear,close all

%% §ìdataset¤ºªº¯S¼x
features = zeros(850,1);
file = 'test';
filename = strcat(file, '.wav');
gabor = 1;
mfcc = 1;
beat = 1;
%% Song-level texture feature
if gabor == 1
    a = testSongLvlTexFeaEX(filename);
end

%% MFCC
if mfcc == 1
	auFile = char(filename);
	display(auFile);
	au=myAudioRead(auFile);
	opt=mgcFeaExtract('defaultOpt');
	b=mgcFeaExtract(au, opt, 1);
    b = b(1:10);
end

%% Beat-level texture features
if beat == 1
    c = testBeatLvlFeaEx(filename);
end

Test8502 = [a(1:210,:);c(1:210,:);a(211:420,:);c(211:420,:);b];

save (file, 'Test8502')
%d = [features(1:210,:);BeatLevelFeatures(1:210,:);features(211:420,:);BeatLevelFeatures(211:420,:);mfccfeatures];














