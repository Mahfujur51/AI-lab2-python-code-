'''
Created on Mar 23, 2019

@author:Mahfujur
'''
import random as r

b=0;
c=0;
#print(x);
for i in range (10):
    x= r.random()
    if x <= 0.7:
        print("1");
        b=b+1
    else:
        print("0");
        c=c+1
        
print(b)
print(c)
    
