#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
def avgNum(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num+ i

    avg = sum_num/ len(num)
    return avg

print('The avg is: ',round(avgNum([3,3,5,6,7,4,3,2,3]),4))


# In[2]:


#2
a = eval(input('Enter value 1: '))
b = eval(input('Enter value 2: '))

c = a,b = b,a
print(c)


# In[3]:


#3
def Series(num, num_range):
    str_n = str(num)
    sums = num

    sum_str = str(num)
    for i in range(1, num_range):
        # making n, nn, nnn...
        sum_str = sum_str + str_n
        sums = sums + int(sum_str)

    return sums

# Driver Code
num = eval(input('Enter number: '))
num_range = eval(input('Enter range: '))
total = Series(num, num_range)
print(total)


# In[3]:


#4
#Write Python Program to Convert Decimal to Binary, Octal and Hexadecimal and vice versa without using built in functions.
option = input('Press:1 = Decimal To Binary, Binary To Decimal,  Press:2 = Octal To HexaDecimal HexaDecimal To Octal: ')
if option == '1':
    decimal_or_binary = input('Press: 1 = Decimal To Binary Or Press: 2 = Binary to Decimal: ')
    if decimal_or_binary == '1':
        decimal = int(input('Enter decimal: '))
        print('In Binary: {:b}'.format(decimal))
        
    if decimal_or_binary == '2':
        binary = int(input('Enter binary: '))
        print('In Decimal {:d}'.format(binary))
    
elif option == '2':
    octal_or_hexa = input('Press:1 = Octal To Hexa Or Press: 2 = Hexa To Octal: ')
    if octal_or_hexa == '1':
        octal = int(input('Enter octal: '))
        print('In Hexa(lowerCase): {:x}, (upperCase): {:X}'.format(octal,octal))
    
    if octal_or_hexa == '2':
        hexa = int(input('Enter hexa decimal: '))
        print('In Octal: {:o}'.format(hexa))

        
else:
    print('Invalid option Selected!')


# In[62]:


## 5
def reverse(num):
    num = str(num)
    rev_num = num[::-1]
    return(rev_num)

num = int(input('Enter number: '))
x = reverse(num)
print(x)


# In[36]:


# 6
#Write Python Program to Check Whether a Number is Positive or Negative
num = float(input('Enter a number: '))
if num > 0 :
    print(num,' is Postive')
elif num == 0:
    print('Zero is neither Postive Nor Negative')
else:
    print(num, ' is Negative')


# In[8]:


#7
#Write Python Program to Take in the Marks of 5 Subjects and Display the Grade
sub1 = float(input('Enter marks of Subject 1: '))
sub2 = float(input('Enter marks of Subject 2: '))
sub3 = float(input('Enter marks of Subject 3: '))
sub4 = float(input('Enter marks of Subject 4: '))
sub5 = float(input('Enter marks of Subject 5: '))

obtained = sub1 + sub2 + sub3 + sub4 + sub5
total = 500       #100 marks for each subject

if obtained < 100:
    grade = 'F'
if obtained >= 200:
    grade = 'C'
if obtained >= 300:
    grade = 'B'
if obtained >= 400:
    grade = 'A'
if obtained >= 500:
    grade = 'A+'
if obtained > 501:
    print('Invalid obtained marks enterred!')
    grade = 'No Grade'
    obtained = 'No marks'
else:
    pass

print(f'Marks: {obtained}\nGrade: {grade}')


# In[2]:


#8
starting_range= int(input('Enter Starting range: '))
ending_range = int(input(("Enter Ending range: ")))
n = int(input('Enter number: '))
for i in range(starting_range,ending_range+1):
    if i%n == 0:
        print(i, end= ',')


# In[10]:


#9
def quotientDivisor(n1,n2):
    divisor = n1
    quotient = n1//n2
    print(f'Divisor: {divisor}\nQuotient: {quotient}')

n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
x = quotientDivisor(n1,n2)
print(x)


# In[7]:


#10
a = int(input('Enter value 1: '))
b = int(input('Enter value 2: '))
c = int(input('Enter value 3: '))
data = []
data.append(a)
data.append(b)
data.append(c)

for num1 in range(0,3):
    for num2 in range(0,3):
        for num3 in range(0,3):
            if num1!=num2 and num2!= num3 and num3 != num1:
                print(data[num1],data[num2],data[num3])


# In[14]:



#11
#Write Python Program to Print Odd Numbers Within a Given Range
def oddNum(num_range):
    for i in range(0,num_range):
        if i % 2:
            print('odd number: ',i)
        else:
            pass

num_range = eval(input('Enter range: '))
function_oddNum = oddNum(num_range)
print(function_oddNum)


# In[48]:


#12
def sumDigit(n):
    sum_n = 0
    for i in str(n):
        sum_n = sum_n + int(i)
    return(sum_n)

n = int(input('Enter Digits: '))
x = sumDigit(n)
print('Sum of digits',x)


# In[85]:


#13
def smallestDivisor(n):
    lst = []
    for i in range(2,n+1):
        if n%i:
            lst.append(i)
            
    return 'Smallest Divisor of:',n,'is ',lst[0]
    
    
n = eval(input('Enter number: '))
x = smallestDivisor(n)
print(x)


# In[24]:


#14
##Write Python Program to Count the Number of Digits in a Number
def countDigit(number):
    count= 0
    while number > 0:
        count = count+ 1
        number=  number//10
        
    return count

#driverCode        
number = int(input('Enter number: '))
x = countDigit(number)    
print('Digit Count: ',x)


# In[22]:


###### 15
#Write Python Program to Check if a Number is a Palindrome
def palindrome(num):
    num = num.casefold()
    rev_num = num[::-1]
    if num == rev_num:
        return(num,'is Palindrome')
    else:
        return(num,'is Normal number')

num = input('Enter number: ')
res = palindrome(num)
print(res)


# In[97]:


#16
#Write Python Program to Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50.
def AreNotDivisible():
    for i in range(1,51):
        if i % 2 == 0 or i % 3 ==0:
            pass
            
        else:
            print(i)
AreNotDivisible()


# In[2]:


#17
#Write Python Program to Read a Number n And Print the Series "1+2+…..+n= "
def series(n):
    for i in range(1,n,1):
        print(i, end = '+')
        
series(7)


# In[29]:


#18
def SummationPattern(n):
    for i in range(1,n):
        for j in range(1,n):
            print(j*i, end=' ')
        print('\n')
        
        
SummationPattern(5)


# In[80]:


#19
def matrix(n):
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                print("1", sep=' ',end=' ')
            else:
                print("0",sep= ' ',end= ' ')
        print('\n')
        
        
        
matrix(4)


# In[43]:


#20
def starPattern(n):
    for i in range(1,n):
        for j in range(1,n-i):
            print('*', sep=' ',end=' ')
            
        print('\n')
        
starPattern(8)


# In[75]:


#21
def SieveOfEratosthenes(number):
    
    if number > 0:
        for i in range(2,number):
            if number%i == 0:
                break
        else:
            print(number)
            

SieveOfEratosthenes(7)


# In[ ]:




