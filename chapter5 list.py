# numbers=[1,2,3,4]      
# print(numbers)

# alternate to print an single
# numbers=[1,2,3,4]
# print(numbers[2])

# words=["one","two","three"]
# print(words)

# mixed=[1,2,"three",2.3]
# print(mixed)
# mixed[1]="saurabh"          # to exange the data of the list
# print(mixed)

# fruits=["grapes","orange"]        # PROGRAM TO ADD DATA IN AN LIST
# fruits.append("mango")
# print(fruits)

# fruits=[]                       # TO ADD DATA IN AN EMPTY LIST OF ANYTHING
# fruits.append("mango") 
# fruits.append("orange")
# fruits.append("grapes")
# print(fruits)

# fruits=["mango","grapes"]        # PROGRAM TO INSERT ANY DETAILS AT ANY POSITION
# fruits.insert(1,"orange")
# print(fruits)

# fruits1=["mango","orange"]         # PROGRAM TO ADD ANY TWO DETAILed LIST
# fruits2=["grapes","onion"]
# fruits=fruits1+fruits2
# print(fruits)

# fruits=["mango","orange","grapes"]         # PROGRAM TO DELETE ANY DATA FROM LIST
# # fruits.pop(1)                     # POP METHOD
# # del fruits[1]                      # DELETE METHOD
# # fruits.remove('orange')         # REMOVE METHOD   TO USEFULLL
# print(fruits)

# fruits =["mango","apple","grapes","orange","kiwi","coconut"]   # program TO KNOW ABOUT ANYTHNG IN THE LIST
# if "mango" in fruits:
#      print(" present")
# else:
#     print("not present")

# fruits=["apple","orange","banana","apple","guava"]    # PROGRAM TO COUNT ANYTHING IN THE LIST
# print(fruits.count("apple"))

# fruits=["appele","banana","mango","orange","grapes"]        # TO ARRANGE THE PROGRAM IN AN ALFABETICAL ORDER
# fruits.sort()
# print(fruits)

# numbers=[1,3,1,5,9,3]         # PROGRAM TO ARRANGE THE THE NUMBERS IN ASSENDING ORDER
# numbers.sort()
# print(numbers)

# numbers=[1,3,4,5,2,7,8,5]        # PROGRAM TO CLEAR THE LIST OF NUMBERS   VIDEO==90
# numbers.clear()
# print(numbers)

# numbers=[1,3,4,7,2]              # PROGRAM TO COPY  THE NUMBERS
# numbers_copy=numbers.copy()
# print(numbers_copy)

# kit1=["bat","ball","football"]           # program of IS vs EQUAL
# kit2=["bat","ball","football"]
# kit3=["hockey","chess","carrum"]          # VIDEO = 91
# print(kit1==kit2)
# print(kit1==kit3)
# print(kit1 is kit2)           # this gives false becoz they are in different place and in different memory


# name,age=input("enter your name and age").split(",")
# print(name)                                               # SPLIT AND JOIN METHOD
# print(age)                                   #VIDEO 92         
# user=["saurabh","24"]                          
# print(",".join(user))

# LIST ARE MUTABLE
# STRINGS ARE INMUTABLE (i.e IT CAN NOT BE CANGED)  Ex. we can not any chracter in the strigs but can add in the list

# fruits=["apple","banana","orange","grapes"]
# for fruit in fruits:                          # LOOPING in the list using (FOR LOOP)
#     print(fruit)

# matrix=[[1,2,3],[3,4,5],[7,4,9,1]]           # LIST INSIDE LIST
# print(matrix[0])         # we can seperatly print the strings position or also can print whole string
# for sublist in matrix:   # using this we can print whole string seperatly in sequence
#     for i in sublist:   # ,,, , , , , , , , , , , ,  ,, , , , , , , , , , , , , , , , ,
#         print(i)

# s="string"                # PROGRAM TO KNOW WHAT TYPE OF STRING IS!
# print(type(s))        
                          
# matrix=[1,2,3,4]           # ,,,,,,,,,,,,,,,,,,,,,,, 
# print(type(matrix))

# n=input("enter the string of numbers[a,b,c]")
# for 