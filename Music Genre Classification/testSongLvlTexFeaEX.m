function feature = testSongLvlTexFeaEX(filename)
%filename = 'blues.00000.au';

[x,fs] = audioread(filename);
[S,F,T] = spectrogram(x,hamming(1024),512);
%resolution_spec = 11025/513;
%% print spectrogram into 7 bands
    % a total spectrogram

figure; 
imagesc(T,F,20*log10(abs(S)+eps));axis xy; colormap(jet)
set(gca,'position',[0 0 1 1])
axis off;
axis normal;

figurename = strcat(filename,'.png');

try
    saveas(gcf,figurename);
catch
    saveas(gcf,figurename);
end



%% gray-scale
Imag = imread(figurename);
grayscale = rgb2gray(Imag);
%{
figure
imshow(grayscale)
set(gca,'position',[0 0 1 1])
axis off;
axis normal;
figurename = strcat(filename,'.gray','.png');
saveas(gcf,figurename);
%}
%resolution_gray = 11025/656;
%% divide into 7 sub-bands
%0 to 200 Hz
g1 = grayscale(1:11,:);
%200 to 400 Hz
g2 = grayscale(12:23,:);
%400 to 800 Hz
g3 = grayscale(24:47,:);
%800 to 1600 Hz
g4 = grayscale(48:95,:);
%1600 to 3200 Hz
g5 = grayscale(96:190,:);
%3200 to 8000 Hz
g6 = grayscale(191:476,:);
% and 8000 to 11025 Hz.
g7 = grayscale(477:656,:);

%% Gabor filter
%£f ? {2.5, 5, 7.5, 10, 12.5} and £c ? {0?, 30?, 60?, 90?, 120?, 150?}.
feature = zeros(420,1);
feature_dim = 1;

wavelength = [2.5, 5, 7.5, 10, 12.5];
orientation  = [0, 30, 60, 90, 120, 150];
% 0-200
i = 1;
while i <= 5
    j = 1;
    while j <= 6
        [mag, ~] = imgaborfilt(g1,wavelength(i),orientation(j));
        magmean = mean2(mag);
        magstd = std2(mag);
        feature(feature_dim) = magmean;
        feature(feature_dim+210) = magstd;
        feature_dim = feature_dim + 1;
        j = j + 1;
    end
    i = i + 1;
    
end
% 200-400
i = 1;
while i <= 5
    j = 1;
    while j <= 6
        [mag, ~] = imgaborfilt(g2,wavelength(i),orientation(j));
        magmean = mean2(mag);
        magstd = std2(mag);
        feature(feature_dim) = magmean;
        feature(feature_dim+210) = magstd;
        feature_dim = feature_dim + 1;
        j = j + 1;
    end
    i = i + 1;
    
end
% 400-800
i = 1;
while i <= 5
    j = 1;
    while j <= 6
        [mag, ~] = imgaborfilt(g3,wavelength(i),orientation(j));
        magmean = mean2(mag);
        magstd = std2(mag);
        feature(feature_dim) = magmean;
        feature(feature_dim+210) = magstd;
        feature_dim = feature_dim + 1;
        j = j + 1;
    end
    i = i + 1;
    
end
% 800-1600
i = 1;
while i <= 5
    j = 1;
    while j <= 6
        [mag, ~] = imgaborfilt(g4,wavelength(i),orientation(j));
        magmean = mean2(mag);
        magstd = std2(mag);
        feature(feature_dim) = magmean;
        feature(feature_dim+210) = magstd;
        feature_dim = feature_dim + 1;
        j = j + 1;
    end
    i = i + 1;
    
end
% 1600-3200
i = 1;
while i <= 5
    j = 1;
    while j <= 6
        [mag, ~] = imgaborfilt(g5,wavelength(i),orientation(j));
        magmean = mean2(mag);
        magstd = std2(mag);
        feature(feature_dim) = magmean;
        feature(feature_dim+210) = magstd;
        feature_dim = feature_dim + 1;
        j = j + 1;
    end
    i = i + 1;
    
end
% 3200-8000
i = 1;
while i <= 5
    j = 1;
    while j <= 6
        [mag, ~] = imgaborfilt(g6,wavelength(i),orientation(j));
        magmean = mean2(mag);
        magstd = std2(mag);
        feature(feature_dim) = magmean;
        feature(feature_dim+210) = magstd;
        feature_dim = feature_dim + 1;
        j = j + 1;
    end
    i = i + 1;
    
end
% 8000-11025
i = 1;
while i <= 5
    j = 1;
    while j <= 6
        [mag, ~] = imgaborfilt(g7,wavelength(i),orientation(j));
        magmean = mean2(mag);
        magstd = std2(mag);
        feature(feature_dim) = magmean;
        feature(feature_dim+210) = magstd;
        feature_dim = feature_dim + 1;
        j = j + 1;
    end
    i = i + 1;
    
end










