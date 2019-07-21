'''
Created on Apr 3, 2019

@author: Torikul
'''
from random import*
A = []
lis = []
for i in range(100):
    x = random()
    A.append(round(x,2))

start = 0.0
End = 0.1
Oi_Ei = []

for i in range(10):
    temp = []
    for v in A:
        if(v > start and v <= End):
            temp.append(v)
    lis.append(temp)
    start = End
    End = End + 0.1

for v in lis:
    Oi_Ei.append(((len(v)-10)*(len(v)-10))/10)
    
print('result = ' , sum(Oi_Ei))