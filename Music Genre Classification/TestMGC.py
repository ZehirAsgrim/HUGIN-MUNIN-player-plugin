# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:31:42 2018

@author: Lulu
"""
import json
import scipy.io
from svmutil import *

# input features
user = input('User name: ')
filename = input('Music name to classify: ')
print('1=blues 2=classical 3=country 4=disco 5=hiphop\n6=jazz 7=metal 8=pop 9=reggae 10=rock')
guess = int(input('Music genre you guess: '))
features = scipy.io.loadmat(filename+'.mat')
print(filename)
Test850 = features['Test8502']


j = 0
temp850Fea = {}
while (j < 850):
    #temp[:,i]
    temp850Fea[j] = Test850[j]
    j = j + 1

x = [temp850Fea]
y = [guess] # 2 represent classic

#load well pre-trained SVM model
m = svm_load_model('MGC.model')

# output classification result
p_label, p_acc, p_val = svm_predict(y, x, m, '-b 1')
path = 'C:\\Users\\USER\\genre_'+user+'@'+filename+'.txt'
with open(path, 'w') as fp:
    if p_label[0] == 1 :
        print('{"musicgenre":"blues"}\n')
        fp.write('{"musicgenre":"blues"}\n')
    elif p_label[0] == 2 :
        print('{"musicgenre":"classical"}\n')
        fp.write('{"musicgenre":"classical"}\n')
    elif p_label[0] == 3 :
        print('{"musicgenre":"country"}\n')
        fp.write('{"musicgenre":"country"}\n')
    elif p_label[0] == 4 :
        print('{"musicgenre":"disco"}\n')
        fp.write('{"musicgenre":"disco"}\n')
    elif p_label[0] == 5 :
        print('{"musicgenre":"hiphop"}\n')
        fp.write('{"musicgenre":"hiphop"}\n')
    elif p_label[0] == 6 :
        print('{"musicgenre":"jazz"}\n')
        fp.write('{"musicgenre":"jazz"}\n')
    elif p_label[0] == 7 :
        print('{"musicgenre":"metal"}\n')
        fp.write('{"musicgenre":"metal"}\n')
    elif p_label[0] == 8 :
        print('{"musicgenre":"pop"}\n')
        fp.write('{"musicgenre":"pop"}\n')
    elif p_label[0] == 9 :
        print('{"musicgenre":"reggae"}\n')
        fp.write('{"musicgenre":"reggae"}\n')
    else :# if p_label[0] == 10
        print('{"musicgenre":"rock"}\n')
        fp.write('{"musicgenre":"rock"}\n')
