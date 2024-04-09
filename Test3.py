#!/usr/bin/env python
# coding: utf-8

# In[1]:


#person is senior citizen or not
x=int(input("enter the required number: "))
if x>=60:
    print("yes")
else:
    print("no")


# In[2]:


#wap to find largest no out of two num
x=int(input("enter the required number: "))
y=int(input("enter the required number: "))
if x>y:
    print("the largest number is: ",x)
elif y>x:
        print("the largest number is: ",y)
elif x==y:
    print("num are equal")


# In[3]:


#wap if user entered no. is positive or negative
x=int(input("enter the required number: "))
if x>0:
    print("num is +ve")
else:
    print("num is -ve")


# In[4]:


#wap num even or odd
x=int(input("enter the required number: "))
if x%2==0:
    print("even")
else:
    print("odd")


# In[5]:


#wap a no is divisible by both 2 and 3
x=int(input("enter the required number: "))
if x%2==0 and x%3==0:
    print("num is divisible by both 2 and 3")
elif x%2==0 and x%3 != 0:
    print("num is div by 2 only")
elif x%3==0 and x%2 != 0:   
    print("num is div by 3 only")
else:
    print("no result")


# In[6]:


#wap to find largest no out of three num
x=int(input("enter the required number: "))
y=int(input("enter the required number: "))
z=int(input("enter the required number: "))

if x>y and x>z:
    print("the largest number is: ",x)
elif y>x and y>z:
        print("the largest number is: ",y)
elif z>x and z>y:
            print("the largest number is: ",z)
else:
    print("num are equal")


# In[ ]:
 Given a list fruits = ['apple', 'banana', 'cherry'], how can you check if the string 'banana' is present in the list without using a loop?
l=['apple', 'banana', 'cherry']
if 'banana' in l:
    print("yes")
else:
    print("no")



