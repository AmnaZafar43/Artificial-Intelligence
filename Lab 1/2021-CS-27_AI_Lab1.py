#!/usr/bin/env python
# coding: utf-8

# # <center>Artificial Intelligence</center>  <center>Fall 2023</center>
# ## Lab 01
# #### Name: Amna Zafar
# #### Roll number: 2021-CS-27
# 

# Take weight in kgs and convert it into pounds. 1 pound = 1 kg 2.2046 **(2 marks)**

# In[1]:


w = input("Enter weight in kg's ")
p = float(w)*2.20462
print("Weight in pounds is: ",p)


# Calculate the cost of all the items in a shopping cart. **(2 marks)**

# In[2]:


prices =[20,50,80,10,56,89]
sum = 0
for x in prices:
    sum = sum+x
print("Sum of items is ",sum)


# Write a function that returns the maximum of two numbers. **(2 marks)**

# In[3]:


def my_function():
    return "amna",123
print(my_function())


# Write a function called **deepmind** that takes a number  **(4 marks)**
# * If the number is divisible by 3, it should return deep.
# * If it is divisible by 5, it should return mind.
# * If it is divisible by both 3 and 5, it should return deepmind.
# * Otherwise, it should return the same number.
# 
# 
# 

# In[4]:


def deepmind(num):
    if(num%3==0 and num%5==0):
        return "deepmind"
    elif(num%5==0):
        return "mind"
    elif(num%3==0):
        return "deep"
    else:
        return num
number = int(input("Enter a number "));
deepmind(number);
print(deepmind(number));

listA =  [1,2,3,4,5,6,7,8,9,10]  
# 
# If an element of **listA** is smaller than 5, replace it with 0. And if an element of x is bigger than 5, replace it with 1. (**2 marks**)

# In[5]:


for i in range(len(listA)):
    if listA[i] < 5:
        listA[i] = 0
    else:
        listA[i] = 1
print(listA)


# Compute the square of **listA** elements in one line. (**2 marks**)
# 

# In[6]:


listA = [1,2,3,4,5,6,7,8,9,10]
square = []
for i in listA:
    square.append(i*i)
print(square)


# Concatenate b1 and b2. (**2 marks**)

# In[7]:


b1 = ['Hello', 'in','first']
b2 = ['Students','the','recitation']
print(b1 + b2)


# Create a dictionary of student **Ali** where the keys are courses and values are total and obtaining marks in each course. Print the dictionary items subjects wise **(2 marks)**

# In[8]:

ali = {
  "course1":"80/100",
  "course2":"30/100",
  "course3":"90/100",
}
print(list(ali.items())[0])

# Create a class 'calculator' with the following functions to compute i) addition, ii) subtraction, iii)multiplication, iv)division and v)square
# between two numbers. **(2 marks)**

# In[9]:


