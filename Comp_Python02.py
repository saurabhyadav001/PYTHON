# first_name = "saurabh"
# last_name = 'yadav'
# full_name = first_name + " " + last_name   #STRING CONCATINATION.
# print(full_name)
#wE CAN'T ADD ANY Number ex..3 with  an string
# print(first_name + 3)  ****ERROR
# print(first_name + "3") **No-- Error
#print(first_name + str(3)) ***No--Error
# print('saurabh '*3) #here it will print the string 3 times
 
#*****21 USER INPUR function
#Input function always take input in form of String
# name = input("type your name")
# print(name)
# age = input("enter your age")
# print('your age is' + ' ' + age)

#22 INT FUNCTION
# num_one = int(input("enter a number"))
# num_two = int(input("enter a number"))
# total = num_one + num_two
# print(total)
# num_one = float(8)
# num_two = int(10)
# print(num_one + num_two)
#we cant add an integer with an string!
#23 MORE ABOUT VARIABLES*******how to do various operations in an single line

# name, age = "saurabh"  , '20'
# print(name + ' '+ age)
# x=y=z= 2   # example..
# print(x+y+z)

#24 *****TWO OR MORE INPUT IN ONE LINE******
# name, age= input('enter your name and age').split(' ') #The Python split() method
# # divides a string into a list. Values in the resultant list are separated based on a separator character.
# print(name)
# print(age)

#25*******STRING FORMATING********** using it reduces number of lines of codes
#STRING FORMATING NE HAMARA KAAM AASAN KR DIYA..
# name = 'saurabh'
# age = 20
# # print('hellow {} your age is {}'.format(name, age))
# print(f'hellow {name} your age is {age}')   #****This syntax is can also be used for string formating

#QUES: ask user to enter 3 numbers and then find its average!
# num_one = int(input("enter number one"))
# num_two = int(input("enter number two"))
# num_three = int(input("enter number three"))
# total = ((num_one + num_two + num_three) / 3)
# print(total)


#27 NHI SMJHA.
# num1, num2, num3 = input("enter three numbers comma separated").split(",")
# print(f'average of three numbers :{(int(num1) + int(num2) + int(num3) /3)}')

#/******STRING INDEXING   28*****
# language = 'saurabh'
# print(language[3])  #print any position  # if we find any index out of range it will show error
# print(language[-1])  # print last character

#29*******STRING SLICING******** it is used to print more than one character
 
# lang = 'saurabh'
# print(lang[0:2])  #SYNTAx, start arguments: stop arguments
# print(lang[1:])   # if we do not put stop arguments then it will print the entire string
# print(lang[:4])

#29 STEP ARGUMENTS*******
# lang = 'saurabh'
# print(lang[1:4:2])  #here using step arg. we can avoid 1 -1 charcters of string
# print(lang[6::-1])  # IT WILL REVERSE THE STRING*******
# print(lang[-1::-1])    # IT WILL REVERSE THE STRING*******

#V-31 ask  user name and print back user name in reverse order
# name = input("enter Your name")
# print(name[::-1])

#33 STRING METHOD*********
# name = "saurabh"
# # print(len(name))    #******.len function
# length = len(name)  #we can also put them in an variable then print the length
# print(length)

# print(name.lower()) # lower method will print the given string in small words!
# print(name.upper()) #upper method will print the string in capital words
# print(name.title())  #tittle method will give first character as capital char!
# print(name.count('a'))  #count method to count number of any character in the string.

#34
# name = input("enter Your name")
# length= len(name)
# print(name)
# print(length)
# print(name.count('a'))

#36**SOLVE PROBLEM WITH SPACES USING STRIP METHOD******
 
# name=  '        saurabh      '
# dots = '.................'
# print(name.lstrip() + dots)  #lstrip() method is used to remove left spaces
# print(name.rstrip() + dots)  #rstrip() method is used to remove right spaces
# print(name.strip()+ dots)   #strip() method is used to remove all spaces
# print(name.replace(" ","")+ dots)  # as strip method not removes the internal spaces to we can use replace method to replace splaces!

#37 ****FIND AND REPLACE METHOD *****
# string = "i am an student of jeet jodhpur and i am from cse branch"
# # print(string.replace("i", "saurabh", 1))  # here 1 means replace the string one time only!
# print(string.find("from"))  # To find position of any char in string

#38 CENTER METHOD****
# name = "saurabh"
# print(name.center(9, '*'))


# #QUES: ask user name and add 
# name= input("enter your name")
# print(name.center(len(name)+ 8, '*'))

#39 STRINGS ARE IMMUTABLE --means once string is created then it can't be changed , yes we can replace the 
#characters but when again we try to print the string it will give same string! as it was..

