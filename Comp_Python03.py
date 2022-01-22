# #if- statement
# age= input("enter your age")
# age = int(age)
# if age >=14:
#     print('you are above 14')

#PASS STATEMENT*****  using Pass Statement we can remove ERROR form our code
#let us suppose we write an program incomplete but we want to continue with next one 
#then using pass statement will avoid error!
#EX....
# # x= 18
# if x>18:
#     pass

#44******IF-else statement
# age = int(input("enter your age"))
# if(age>= 14):
#     print("you can play BGMI")
# else:
#     print("You can't play BGMI")

#45 ask user to input a guess number and check!....
# number = 43
# user = int(input("enter an number between 1-100"))
# if(user == number):
#     print("You win and guess write number")
# else:
#     if (number > user):
#         print("too low")
#     else:
#        print("too high") 

#47 &--operator, or --operator
# name = "saurabh"
# age= 20
# if name== 'saurabh' and age== 20:   # and # or  !
#     print("true")
# else:
#     print("false")

#48-- ask user his name if name starts with a 0r A and age is greater than 20 then he can watch coco movie else he can not watch movies

# name= input("enter your name")
# age= int(input("enter your age"))
# if((name[0] == 'a' or name[0]=='A') and age>10):
#     print("you can watch coco movie")
# else:
#     print("your can't watch coco movie")

#50-- If - elif else statement
# #QUES: ask user his age if age is between 1-3 then free ticket....
# age= int(input('enter your age'))
# if(age>=1 and age <=3):
#     print("you can watch show free")
# elif(age>=4 and age <=10):
#     print("You have to pay 150")
# elif(age>=11 and age <=60):
#     print("You have to pay 250")
# elif(age>=60):
#     print("you have to pay 200")
# else:
#     print("Enter a valid number")

#51--- In keywords:  this key word is used to check whether the character is present in string or not present
# name = "saurabh"
# if 'a' in name:
#     print("a is present")
# else:
#     print("not present")

#52=== CHECK EMPTY OR NOT***** it is to check whether string is empty or not 
# name ="saurabh"
# if name:                #**here it will check the name block whether their is charcters in string or Not!
#     print("string is not empty")
# else:
#     print("string is empty")
 
#53 --- While loop:************

# i=1 
# while i<=10:
#     print("saurabh")
#     i= i+1

#54****SUM OF NUMBERS USING WHILE LOOP:
# i=1
# total=0
# while i<=10:
#     total= total + i   # we can also write it as: total += i
#     i= i+1
# print(total)

#55-- QUES; ask user an number n and add upto n!
# n = int(input("enter the number upto which you want to add"))
# i =1
# total = 0
# while i<=n:
#     total = total + i
#     i= i+1 
# print(total)

 #57********************EXERCISE 04
 #QUES: ask user a number and find its sum.
# n= input("enter the number")
# n= (int(n[0])+ int(n[1]) + int(n[2]) + int(n[3]))
# print(n)
#******OR*****
# number= input("enter a number")
# i=0
# total =0
# while i< len(number):
#     total = total + int(number[i])
#     i= i+1
# print(total)

#59*****ask user for name and print count of each words!

# name= "saurabh"
# temp_var = ""
# i=0
# while i<len(name):
#     if name[i] not in temp_var:
#         temp_var = temp_var + name[i]
#         print(f'{name[i]} : {name.count(name[i])}')
#     i = i+1



























