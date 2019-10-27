# -*- coding: utf-8 -*-

"""

Created on Wed May 22 17:47:21 2019

 

@author: 376020

"""

#1

 

#A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT. The trace of Robot movement is as given following:

#UP 5

#DOWN 3

#LEFT 3

#RIGHT 2

#The numbers after directions are steps. Write a program to compute the distance current position after sequence of movements.

 

import math

import re


inputs = [

'UP 5' ,

'DOWN 3' , 

'LEFT 3' ,

'RIGHT 2' 

]

 

x_cord, y_cord = 0, 0

up_by, down_by, left_by, right_by = 0,0,0,0

 

for entry in inputs:

    digitregex = re.compile(r'\d')

    mo = digitregex.search(entry)

    if entry[:2] == 'UP':

        up_by +=  int(mo.group())

    elif entry[:4] == 'DOWN':

        down_by += int(mo.group())

    elif entry[:4] == 'LEFT':

        left_by += int(mo.group())

    elif entry[:5] == 'RIGHT':

        right_by += int(mo.group())

    

    x_cord = right_by - left_by

    y_cord = up_by - down_by

    

 

print('entries are ',up_by, down_by,left_by,right_by)

 

print('current position after sequence of movements is (%d,%d)' % (x_cord,y_cord))

 

distance_covered = math.floor(math.sqrt((x_cord**2)+(y_cord**2)))

 

print('The distance covered by robot from the current position is ',distance_covered)


 

 

# -*- coding: utf-8 -*-

"""

Created on Wed May 22 19:14:15 2019

 

@author: 376020

"""

 

import re

 

XYZ_data = ['XYZ corporations','Information Technology','$627,432,327','67316981376']

 

search_regex = re.compile(r'Information')

 

for item in XYZ_data:

    flag ='Not found'    

    mo = search_regex.search(item)

    if mo == None:

        continue

    else:

        flag = 'Found'

        break

 

        

 

if flag == 'Found':

    print('The pattern is found')

else:

    print('The pattern is not found')


 

 

# -*- coding: utf-8 -*-

"""

Created on Wed May 22 18:46:57 2019

 

@author: 376020

"""

 

#2. 

#

#Data of XYZ company is stored in sorted list. Write a program for searching specific data from that list. 

#

#Hint: Use if/elif to deal with conditions. 

 

import datetime

 

now = datetime.datetime.now()

 

#now = datetime.datetime(2019, 5, 22, 2, 1, 19, 116957)

 

mp = datetime.datetime.strftime(now, '%H %p')

 

print(mp)

 

mp_list = mp.split()

 

#

#if ( (int(mp_list[0]) >= 6) and (int(mp_list[0]) < 18 )) :

#    print('Its day time')

#else:

#    print('Its night time')

#

#    

 

if 6< int(mp_list[0]) < 18 :

    print('Its day time')

else:


    print('Its night time')

 

# -*- coding: utf-8 -*-

"""

Created on Wed May 22 20:54:53 2019

 

@author: 376020

"""

 

# 4

 

# Write a program to find distance between two locations when their latitude and longitudes are given. 

#

# Hint: Use math module. 

 

 

import math

 

#Haversine

#formula:            a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)

#             c = 2 ⋅ atan2( √a, √(1−a) )

#             d = R ⋅ c

 

#lat1 = 52

#lat2 = 67

#long1 = 110

#long2 = 78

 

def distance_from_lat_long(lat1=0,lat2=0,long1=0,long2=0):    

    

    lat1_radians = math.radians(lat1)

    lat2_radians = math.radians(lat2)

    

    long1_radians = math.radians(long1)

    long2_radians = math.radians(long2)

    

    

    

    diff_lat = (lat2_radians - lat1_radians)

    diff_long = (long2_radians - long1_radians)

    

    #diff_lat_sq = diff_lat * diff_lat

    #diff_long_sq = diff_long * diff_long

    

    a = ((math.sin(diff_lat/2) * math.sin(diff_lat/2)) + (((math.cos(lat1_radians)) * (math.cos(lat2_radians))) * ((math.sin(diff_long/2) * math.sin(diff_long/2)))))

    

    c = 2 * (math.atan2(math.sqrt(a),math.sqrt(1-a)))

    

    R = 6371 # Radius of the earth in km

    

    d = R * c

    

    return d

 

 

 

if __name__ == '__main__':

    distance_in_KM = distance_from_lat_long(lat1=52,lat2=67,long2=78,long1=110)

    print('The distance by latitude and longitude is ',distance_in_KM)


 

 

# -*- coding: utf-8 -*-

"""

Created on Wed May 22 21:37:15 2019

 

@author: 376020

"""

#5. 

#Design a software for bank system. There should be options like cash withdraw, cash credit and change password. 

#According to user input, the software should provide required output. 

#

#Hint: Use if else statements and functions.

 

import re

 

def banksystem(username,password):

    if ((re.match(r'[a-zA-Z0-9#$\*&]{12,20}',password)) and (username.isalnum())):

            print('Validation successful')

            display(username)

    else:

            print('Not a valid password or password')

            

def display(user):

    print('Welcome to our bank system ',user)

    print('Please perform any of the follwing activities by entering the options.\n1. Cash Withdraw\n2. Cash Credit\n3. Change Password\n')

    option = input('Enter your response: ')

    if int(option) == 1:

        amount_to_withdraw = int(input('Enter the amount to withdraw: '))

        cashwithdraw(amount_to_withdraw)

    elif int(option) == 2:

        amount_to_credit = int(input('Enter the amount to credit: '))

        cashcredit(amount_to_credit)

    elif int(option) == 3:

        changepwd()

 

 

 

def cashwithdraw(amount):

    print('Transaction success. Please collect your money of %d'% amount)

 

def cashcredit(amount):

    print('Transaction success. Your credit of money %d has been recevied '% amount)

 

def changepwd():

    new_password = input('Enter your new password: ')

    confirm_password = input('Confirm your new password again: ')

    if new_password == confirm_password:

        if re.match(r'[a-zA-Z0-9#$\*&]{12,20}',new_password):

            print('Password has been updated successfully')

                       

    else:

        print('Your password entered twice is not matching')

 

 

banksystem('Pavi91','12jkdh9$*83267')

 

 

        

        

    


    

 

# -*- coding: utf-8 -*-

"""

Created on Wed May 22 22:35:28 2019

 

@author: 376020

"""

 

# 6. 

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 

# between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 

 

def findnumbers(lower_limit=0,upper_limit=100):

    l=[]

    for num in range(lower_limit,upper_limit+1):

        if (num%7 == 0) and (num%5 != 0):

            l.append(str(num))

    #print(','.join(str(l)))

    print(l)

    print(','.join(l))

 


findnumbers(2000,3200)   

 

# -*- coding: utf-8 -*-

"""

Created on Wed May 22 22:47:29 2019

 

@author: 376020

"""

 

# 7 

# Write a program which can compute the factorial of a given numbers. Use recursion to find it. 

# Hint: Suppose the following input is supplied to the program: 

# 8 

# Then, the output should be: 

# 40320 

 

def factorial(n):

    fact = 1

    for num in range(n,0,-1):

        fact *= num

    return fact

 

fact_of_num = factorial(6)

print('The Factorial is %d.'% (fact_of_num))

 

#####################

 

#fact_of_num = list((map(lambda x:x*x,[1,2,3,4,5,6,7])))

#

#print(fact_of_num)

#

####################

#

#fact_of_num = list((filter(lambda x:x%5==2,[1,2,3,4,5,6,7])))

#

#print(fact_of_num)

 

#################

 

from functools import reduce

 

def fact_inreduce(n):    

    fact_of_num = reduce((lambda n,k:n*k),list(range(n,0,-1)))

    print('The Factorial is %d from the reduce and lambda functions.'% (fact_of_num))

 


fact_inreduce(6)

 

# -*- coding: utf-8 -*-

"""

Created on Wed May 22 23:28:54 2019

 

@author: 376020

"""

 

#8

 

#Write a program that calculates and prints the value according to the given formula: 

#

#Q = Square root of [(2 * C * D)/H] 

 

#Following are the fixed values of C and H: C is 50. H is 30.


#D is the variable whose values should be input to your program in a comma- separated sequence. 

 

#Example: 

#Let us assume the following comma separated input sequence is given to the program: 

#100,150,180 

#The output of the program should be: 

#18,22,24 

 

import math

 

comma_sep_input = '100,150,180'

 

def calc_compute(input_numbers):

    C = 50 ; H = 30 ; Q = 0 ; Q_list=[]

    print(input_numbers)

    input_numbers = str(input_numbers)

    print(input_numbers)

    input_numbers_split = input_numbers.split(',')

    print(input_numbers_split)

    for num in input_numbers_split:

        print(int(num))

        Q = round(math.sqrt((2*C*int(num))/H))

        print(Q)

        Q_list.append(Q)

    print(Q_list)

    

    print(','.join(map(str,Q_list)))

    

calc_compute(comma_sep_input)


 

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 13:33:47 2019

 

@author: 376020

"""

 

#9

#Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 

#The element value in the i-th row and j-th column of the array should be i*j. 

#

#Note: i=0,1.., X-1; j=0,1,¡Y-1. 

#Example: 

#Suppose the following inputs are given to the program: 

#3,5 

#Then, the output of the program should be: 

#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

 

 

def array_generator(X=3,Y=3):

    arr = [];temp=[]

    for i in range(0,X):

        for j in range(0,Y):

            print(i,j)

            temp.append(i*j)

        print(temp)

        if len(temp) >0:

            arr.append(temp)

            temp=[]

    

    print(arr)

    

 

array_generator(X=3,Y=5)


    

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 13:47:36 2019

 

@author: 376020

"""

#

# 10 

# Write a program that accepts a comma separated sequence of words as input and prints the words in a 

# comma-separated sequence after sorting them alphabetically. 

# Suppose the following input is supplied to the program: 

# without,hello,bag,world 

# Then, the output should be: 

# bag,hello,without,world 

 

string = input('Enter a string separated by commas: ')

str_list = string.split(',')

 

str_list = sorted(str_list,reverse=False)

 


print(','.join(map(str,str_list)))

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 13:51:51 2019

 

@author: 376020

"""

# 11. 

# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 

#

# Suppose the following input is supplied to the program: 

# Hello world 

# Practice makes perfect 

# Then, the output should be: 

# HELLO WORLD 

# PRACTICE MAKES PERFECT 

 

def sentence_upper(sent):

    return sent.upper()

 

 

in_sent = '''

Hello world

Practice makes perfect

'''

 

output_sent = sentence_upper(in_sent)

 

print(output_sent)


 

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 13:56:17 2019

 

@author: 376020

"""

 

# 12 

# Write a program that accepts a sequence of whitespace separated words as input and 

# prints the words after removing all duplicate words and sorting them alphanumerically. 

#

# Suppose the following input is supplied to the program: 

# hello world and practice makes perfect and hello world again 

# Then, the output should be: 

# again and hello makes perfect practice world 

 

string = input('Enter a sequence of whitespace separated words: ')

 

if string !='':

    str_list = string.split(' ')

    print(str_list)

    str_list = set(str_list)

    print(' '.join(sorted(list(map(str,str_list)))))


 

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 14:05:08 2019

 

@author: 376020

"""

 

# 13  

# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and 

#then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. 

# Example: 

# 0100,0011,1010,1001 

# Then the output should be: 

# 1010 

 

numbers_in_seq = input('Enter a sequence of comma separated 4 digit binary numbers as its input: ')

 

out_num_list=[]

 

if numbers_in_seq != '':

    num_list = numbers_in_seq.split(',')

    for item in num_list:

        #print(item)

        if int(item,2) % 5==0:

            out_num_list.append(item)

            #print(item)

            

    print(','.join(map(str,out_num_list)))

    

 

# convert binary to decimal using int(number,2) -->You can use int and set the base to 2 (for binary):


 

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 14:30:14 2019

 

@author: 376020

"""

#

#14

#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 

#

#Suppose the following input is supplied to the program: 

#Hello world! 

#Then, the output should be: 

#UPPER CASE 1 

#LOWER CASE 9 

 

string = input('Enter a sentence to calculate the number of upper case letters and lower case letters: ')

 

upper_cnt=0 ;lower_cnt=0

for char in string:

    if char.isalpha():

        if char.isupper():

            upper_cnt += 1

        else:

            lower_cnt += 1

 

#print('There are %d upper case letter and %d lower case letters in your sentence. '%(upper_cnt,lower_cnt))

 

print('UPPER CASE '+str(upper_cnt)+'\nLOWER CASE '+str(lower_cnt))

 

 


 

 

# -*- coding: utf-8 -*-

"""

Created on Thu May 23 14:38:49 2019

 

@author: 376020

"""

 

#15

# Give example of fsum and sum function of math library. 

 

sum([0.1] * 10) == 1.0 #--> False

 

 

import math

 

math.fsum([0.1] * 10) == 1.0 #--> True

 

#When .1 is converted to 64-bit binary IEEE-754 floating-point, the result is exactly 

#0.1000000000000000055511151231257827021181583404541015625. When you add this individually 12 times, 

#various rounding errors occur during the additions, and the final sum is exactly 

#1.1999999999999999555910790149937383830547332763671875.

#

#Coincidentally, when 1.2 is converted to floating-point, the result is also exactly 

#1.1999999999999999555910790149937383830547332763671875. This is a coincidence because some of the rounding errors 

#in adding .1 rounded up and some rounded down, with the net result that 1.1999999999999999555910790149937383830547332763671875 

#was produced.

#

#However, if .1 is converted to floating-point and then added 12 times using exact mathematics, 

#the result is exactly 1.20000000000000006661338147750939242541790008544921875. Python’s math.fsum may produce this value 

#internally, but it does not fit in 64-bit binary floating-point, so it is rounded to 

#1.20000000000000017763568394002504646778106689453125.

#

#As you can see, the more accurate value 1.20000000000000017763568394002504646778106689453125 

#differs from the result of converting 1.2 directly to floating-point, 1.1999999999999999555910790149937383830547332763671875, 

#so the comparison reports they are unequal.

 

### math.fsum() is more accurate than sum() functions
