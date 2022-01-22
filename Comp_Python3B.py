#INFINITE LOOP
# EX..
# i =0
# while i<=10:
#     print("saurabh")  # here infinite loop runs because we have't increment value of 'i'


# while(True):
#     print("saurabh")

#62 ****FOR LOOP****

# for i in range(10):  # for loop syntax is very simple and clear using 'range ' function only
#     print("saurabh")

# for i in range(1,10):   # we can also pass starting and end range in 'range' function
#     print(i)

#WAP. to find the sum form 1-10 numbers
# i=0
# total = 0
# for i in range(11):
#     total = total+ i
# print(total)
# i = i+1

#OR ASK INPUT FROM THE USER*** and find the sum!
# n= int(input('enter the number upto which you want to add the numbers'))
# total =0
# for i in range(0, n+1):
#     total = total + i
# print(total)
# i = i+1

#*******64***** WTP ask user a number and calculate the sum of digits--->
# n = input("enter a number")
# total =0
# for i in range(0, len(n)):
#     total = total + int(n[i])
# print(total)

#**PROGRAM TO ADD NUMBERS MANUALLEY
# total = 0
# for x in [1,2,3,4,5]:
#     total = total + x
# print(total)

# user = input("enter you name")
# temp_var = ""
# for i in range(0, len(user)):
#     if user[i] not in temp_var:
#       print(f"{user[i]} : {user.count(user[i])}")
#     temp_var = temp_var + user[i]

# #66 *** BREAK AND CONTINUE
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)

#continue
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

#67 EXERCISE 6
# winning_number = 43
# guess = 1
# number = int(input("guess a number between 1 and 100 : "))
# game_over = False

# while not game_over:
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         game_over= True
#     else:
#         if number < winning_number:
#             print("too low")
#             guess = guess +1
#             number = int(input("guess again : "))
#         else:
#             print("too high")
#             guess = guess +1
#             number = int(input("guess again: "))

# #Random NUmber*****
# import random
# winning_number = random.randint(1,100)
# guess = 1
# number = int(input("guess a number between 1 and 100 : "))
# game_over = False

# while not game_over:
#     if number == winning_number:
#         print(f"you win, and you guessed this number in {guess} times")
#         game_over= True
#     else:
#         if number < winning_number:
#             print("too low")
#             guess = guess +1
#             number = int(input("guess again : "))
#         else:
#             print("too high")
#             guess = guess +1
#             number = int(input("guess again: "))

#*****STEP ARGUMENTS********//\\
# for i in range(1,10):
#     print(i)

# for i in range(1,11,2):   # it will print odd numbers by escaping 1-1 numbers
#     print(i)

# for i in range(0,11,2):    #it will print even numbers by escaping 1-1 numbers
#     print(i)


# for i in range (10,1,-1):   # it will print number in reverse order!
#     print(i)

#71 FOR LOOP USING STRING!***
# name = 'saurabh'
# for i in range(len(name)):
#      print(name[i])

# name= 'saurabh'
# for i in name:
#     print(i)

number = input("enter a number : ")
total =0
for i in number:
    total = total + int(i)
print(total)




























