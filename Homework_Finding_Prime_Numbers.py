#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Homework #2
# This code is intented to find if a number is prime or not.

All_Numbers = []
Divider = [2,3,5,7]
Prime_Numbers = []
N = ()
        
def Prime_Number_Check (x):
    counter = 0
    for i in Divider:
        if (x%i) != 0:
            counter += 1
            # print (str(i)+"lklklk"+str(counter))
            if counter == 4 :
                Prime_Numbers.append(x) 
        elif x == i:
            Prime_Numbers.append(x)
    return x

counter = 1
while counter <= 20 and N != 0 :
    N = input ("Please enter a number or '0' to finish:")
    while not N.isdigit ():
        N = input ("%s is not a number! \n Please enter a valid number:" %N)
    else :
        N = int(N)
        All_Numbers.append (N)
    counter += 1

print ("Numbers entered:",All_Numbers)
[Prime_Number_Check (x) for x in All_Numbers]
print ("Prime numbers are:",Prime_Numbers)


# In[ ]:




