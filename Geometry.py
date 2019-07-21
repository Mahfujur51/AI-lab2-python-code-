'''
Created on Mar 23, 2019

@author: mahfujur
'''
import random as r
b=0;
for i in range (0,10):
    x=r.random()
    if (x <= 0.5):
        break
    else:
        print("0")
        b=b+1;
        

print(b)
    
