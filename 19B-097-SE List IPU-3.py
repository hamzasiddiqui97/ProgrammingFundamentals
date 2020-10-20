#!/usr/bin/env python
# coding: utf-8

# In[16]:


##1
###Write Python Program to Find the Largest Number in a List
def LargestList(lst):
    lst_index = lst[0]
    for i in lst:
        if i > lst_index:
            lst_index = i
    return (lst_index)

lst = [2,3,435,34,22,2,-2]
func = LargestList(lst)
print('Largest Element: ',func)


# In[23]:


##2
##Write Python Program to Find the Second Largest Number in a List

def SecondLargestList(lst):
    lst = list(lst)
    lst.sort()
    a = lst[-2]
    return a
    
lst = [2,3,435,34,22,2,-2]
function = SecondLargestList(lst)
print('Second Largest Element: ',function)


# In[40]:


##3
### Write Python Program to Put Even and Odd elements in a List into Two Different Lists

def EvenOdd(lst):
    even = []
    odd = []
    
    for i in lst:
        if i % 2 == 0:
            even.append(i)
            
        else:
            odd.append(i)
            
    return 'Even: {} and Odd: {}'.format(even,odd)

EvenOdd([342,423,4,5,6,66,7,56])


# In[53]:


##4
##Write Python Program to Merge Two Lists and Sort it

def MergeList(list1, list2):
    a = list1 + list2
    a.sort()
    return a

MergeList([4,2,5,1,6],[1,3,4,5,6,7])


# In[9]:


##5
##Write Python Program to Sort the List According to the Second Element in Sublist

a = [2,3,4,5,6,7,8,9,5,433]
a.sort()
print(a[-2])


# In[10]:


##6


# In[21]:


##7
## Write Python Program to Sort a List According to the Length of the Elements
n = int(input('Enter num of elements: '))

lst = []
for i in range(1,n+1):
    
    element = input('Enter number: ')
    lst.append(element)
    
lst.sort(key=len)
print(lst)


# In[39]:


## 8 
###Write Python Program to Find the Union of two Lists
lst1 = [] 
lst2 = []


num1 = int(input('Enter number of element of list 1: '))
for i in range(1,num1+1):
    element1 = input('Enter element: ')
    lst1.append(element1)

    
num2 = int(input('Enter number of element of list 2: '))
for i in range(1, num2+1):
    element2 = input('Enter element: ')
    lst2.append(element2)

union = lst1 + lst2
    
print(list(set(union)))


# In[46]:


## 9
##Write Python Program to Find the Intersection of Two Lists
a = [1,2,3,4,11,22,33,44]
b = [1,2,3,4,5,6,7,8,9]
intersection = []
for i in a:
    for j in b:
        if i == j:
            intersection.append(i)
            
print('Intersection: ',list(set(intersection)))


# In[1]:


## 13
import random
num = int(input('Enter number of elements: '))
x = []
for i in range(num):
    x.append(random.randint(1,21))

print(x)


# In[ ]:





# In[18]:


### 16
##Write Python Program to Remove the Duplicate Items from a List
def Duplicate(lst):
    unique = set(lst)
    return list(unique)

lst = ['hamza','haris','hamza',34,5,2,3,3,3,3,21,2]
func = Duplicate(lst)
print(func)


# In[7]:


## Write Python Program to Read a List of Words and Return the Length of the Longest One

word_list = ['kangroo','generator']
longest = 0
for i in word_list:
    while len(i) > longest:
        longest += 1

print(longest,'is the longest length of the word:',i)


# In[ ]:




