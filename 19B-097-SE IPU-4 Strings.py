#!/usr/bin/env python
# coding: utf-8

# In[1]:


###1
### Write Python Program to Replace all Occurrences of ‘a’ with $ in a String
s = input('Enter String: ')
for i in s:
    x = s.replace('a','$')

print(x)


# In[20]:


## 3

def Anagrams(string1,string2):

    if sorted(string1.casefold()) == sorted(string2.casefold()):   ##Sorted will sort strings into list by alphabets
        return 'Strings are Anagrams'
    else:
        return 'Strings are not Anagrams'

string1= input('Enter string')
string2 = input('Enter string')
test = Anagrams(string1,string2)
print(test)


# In[33]:


## 4
## Write Python Program to Form a New String where the First Character and the Last Character have been Exchanged
def ExchangedChar(string):
    
    first_index = string[0]
    last_index = string[-1]
    exchanged = last_index + string[1:-1] + first_index
    
    return exchanged

string = input('Enter string: ')
func = ExchangedChar(string)
print(func)


# In[32]:


## 5
## Write Python Program to Count the Number of Vowels in a String

def VowelCount(string):
    vowels = ['a','e','i','o','u']
    count = 0
    for i in string:
        if i.lower() in vowels:
            count += 1

    return count
string = input()
f = VowelCount(string)
print('Vowel Count:',f)


# In[55]:


## 6
## Write Python Program to Take in a String and Replace Every Blank Space with Hyphen

def ReplaceSpace(string):
    for i in string:
        if i == ' ':
            x = string.replace(' ','-')
            
            return x
string = input('Enter string: ')
func = ReplaceSpace(string)
print(func)


# In[59]:


## 7
# Write Python Program to Calculate the Length of a String Without Using a Library Function

def LenString(s):
    count = 0
    
    for i in s:
        count +=1
    
    return count
s = input('Enter string: ')
func = LenString(s)
print(func)


# In[51]:


## 8 
### Write Python Program to Remove the Characters of Odd Index Values in a String

def OddIndexStr(string):
    final = ""
    for i in range(len(string)):
        if i % 2 == 0:
            final = final + string[i]
    
    return final

string= input("Enter string:")

print(OddIndexStr(string))


# In[42]:


### 9
### Write Python Program to Calculate the Number of Words and the Number of Characters Present in a String
def CountCharAndWords(s):
    word = s.split(' ')
    count = 0
    for i in s:
        count += 1
    return 'Words: {} And Characters:{}'.format(len(word),count)

s = input('Enter string: ')
f = CountCharAndWords(s)
print(f)


# In[15]:


###10
### Write Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
def LargerString(string1,string2):
    count1 = 0
    count2 = 0
    for i in string1:
        count1 += 1
        
    for j  in string2:
        count2 += 1
    if count1 < count2:
        return string2

    elif count1 > count2:
        return string1
    else:
        return 'Both are same in length'

string1 = input('Enter String1: ')
string2 = input('Enter String2: ')
a = LargerString(string1,string2)
print(a)


# In[45]:


##11 
### Write Python Program to Count Number of Lowercase Characters in a String

def LowerCaseCount(string):
    count_lower = 0
    lo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in string:
        if i in lo:
            count_lower += 1
    return count_lower
string = input('Enter string: ')
f = LowerCaseCount(string)
print(f)


# In[11]:


### 12
### Write Python Program to Check if a String is a Palindrome or Not
def palindrome(string1, string2):
    a = string1[::-1]
    if string2.casefold() == a.casefold():
        return 'String is a Palindrome'
    
    else:
        return "String is not a Palindrome"

string1 = input('Enter String1: ')
string2 = input('Enter String2: ')
f = palindrome(string1, string2)
print(f)


# In[24]:


## 13
## Write Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String

string = 'Python is easy Programming Language'
upper = 0
lower = 0
up = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in string:
    if i in lo:
        lower += 1
    elif i in up:
        upper += 1
print('upper:',upper, 'lower:',lower)


# In[28]:


## 18
## Write Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String

def twoAlphaString(string):
    a = string[:2] + string[-2:]
    return a

string = input('Enter String: ')
fun = twoAlphaString(string)
print('New String: ',fun)


# In[ ]:


## 14
### Write Python Program to Check if a String is a Pangram or Not


# In[78]:


### 20
## Write Python Program to Check if a Substring is Present in a Given String
def SubStringCheck(string, sub_str):
    string = string.casefold()
    if(string.find(sub_str.casefold()) == -1):   ## find() will return -1 if it doesnot found any match.
          return "Substring not found in string"
    else:
          return "Substring in string"
        
string= input("Enter string:")
sub_str= input("Enter word:")
func = SubStringCheck(string, sub_str)
print(func)


# In[ ]:





# In[ ]:




