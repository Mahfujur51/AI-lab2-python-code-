'''
Created on 22 Feb. 2019

@author: Mahfujur
'''
a = 5
c = 3
z0 = 7
m = 16
zp = z0
n = []
i = 0

while i<30: 
    zi = (a*zp+c)%m
    zp = zi

    if zi in n:
            #print(len(n))
        break
    #n1 = yield zi
    n.append(zi)
        #n.append(n1)
    i = i+1

print ("Random Numbers are :")
for i in range(0,len(n)):
    print ( n[i])
    
    
