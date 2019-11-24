#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:19:09 2019

@author: raulf
"""
"""
import matplotlib.pyplot as plt
im=plt.imread('92.png')
im2=plt.imread('themap.jpg')
plt.figure()
plt.imshow(im2)
plt.figure()
plt.imshow(im)
import cv2

im2=cv2.resize(im2,(922,1376))
plt.figure()
plt.imshow(im2)

files=im2.shape[0]
columnes=im2.shape[1]
i=0
while i <files:
    j=0
    while j<columnes:
        if im2[i,j,1]==255:
            im[i,j,0]=0
            im[i,j,1]=0
            im[i,j,2]=0
        j+=1
    i+=1
plt.figure()
plt.imshow(im)
plt.savefig('92f.jpg', format='jpg',quality=95)
"""
#%%

a=open('codes3.txt')
txt=''
a=a.readlines()
for i in a:
    txt+=i

dic={}
dic['0']=[0,0,0]
dic['1']=[0,0,0]
dic['2']=[0,0,0]
dic['3']=[0,0,0]
dic['4']=[0,0,0]
dic['5']=[0,0,0]
dic['6']=[0,0,0]
dic['7']=[0,0,0]
dic['8']=[0,0,0]
dic['9']=[0,0,0]

for i in a[:-1]:
    dic[i[0]][0]+=1
    dic[i[1]][1]+=1
    dic[i[2]][2]+=1
    
#%%
from collections import defaultdict
import math
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper
dic=defaultdict(float)
file=open('a.txt')
file=file.readlines()
money=0
for i in file:
    o=i.split('|')
#    money+=float(o[3])*float(o[4])*(1-(float(o[5])/100)-float(o[6])/100)
    money+=float("{0:.2f}".format(float(o[3])*float(o[4])*(1-float(o[5])/100)*(1-float(o[6])/100)))

    dic[str(o[1])]+=float(o[3])*float(o[4])*(1.00-float(o[5])/100)*(1-float(o[6])/100)
#    dic[str(o[1])]+=float(o[3])*float(o[4])*(1-float(o[5])/100-float(o[6])/100)
    
file1=open('b.txt')
file1=file1.readlines()

money1=0
for i in file1:
    o=i.split('|')
    money1=dic[str(o[0])]*(1-float(o[4])/100)*(1-float(o[5])/100)+money1
#%%

dic=defaultdict(float)
file=open('a.txt')
file=file.readlines()
money=0


for i in file:
    o=i.split('|')
#    money+=float(o[3])*float(o[4])*(1-(float(o[5])/100)-float(o[6])/100)
    money+=truncate((float(o[3])*float(o[4])*(1-float(o[5])/100)*(1-float(o[6])/100)),2)+0.01

    dic[str(o[1])]+=truncate((truncate(float(o[3])*float(o[4])*(1-float(o[5])/100)+0.01,2))*(1-float(o[6])/100)+0.01,2)
#    dic[str(o[1])]+=float(o[3])*float(o[4])*(1-float(o[5])/100-float(o[6])/100)
    
file1=open('b.txt')
file1=file1.readlines()

money1=0
for i in file1:
    o=i.split('|')
    money1=truncate(truncate(truncate(dic[str(o[0])]*(1-float(o[4])/100)+0.01,2)*(1-float(o[5])/100)+0.01,2)+money1,2)
#%%
dic=defaultdict(float)
file=open('ba.txt')
file=file.readlines()
money=0
for i in file:
    o=i.split('|')
    dic[str(o[1])]+=float("{0:.2f}".format(float(o[3])*float(o[4])*(1-float(o[5])/100)*(1-float(o[6])/100)))
    
file1=open('bb.txt')
file1=file1.readlines()

money1=0
for i in file1:
    o=i.split('|')
    money1=dic[str(o[0])]*(1-float(o[4])/100)*(1-float(o[5])/100)+money1
    
    
#%%
dic=defaultdict(float)
file=open('ba.txt')
file=file.readlines()
money=0
for i in file:
    o=i.split('|')
    dic[str(o[1])]+=truncate((truncate(float(o[3])*float(o[4])*(1-float(o[5])/100)+0.01,2))*(1-float(o[6])/100)+0.01,2)

file1=open('bb.txt')
file1=file1.readlines()
money2=0.00
for i in file1:
    o=i.split('|')
    money2=truncate(truncate(truncate(dic[str(o[0])]*(1-float(o[4])/100)+0.01,2)*(1-float(o[5])/100)+0.01,2)+money2,2)

print(money2-money1)
