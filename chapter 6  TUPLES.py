# tuples are used to store data like list.
#tuples can store any data type,
# TUPELS are immutible i.e  once you created it then you can not change it.

# n=("saurabh","yadav")
# n[0]=("ji")    # after assigning this touples will give ERROR becaus we can not add any data
# print(n)

# # LOOPING WITH TUPLES
# mixed=(1,2,3,4)
# for i in mixed:
#     print("i")         # here while loop can also be used.

# TUPLES WITH ONE ELEMENT
# mixed=(1,)                      # ,(comma) is used to  lets the computer know that it is tuples
# words=("saurabh,")
# print(mixed)
# print(words)

# # TUPLES WITHOUT PARANTHESIS
# mixed="yamaha","apache","duke","kawasakninja"
# print(mixed)
 
# # TUPLES UNPACKING
# vehicles = ("car","bike","baggi","thar")                     
# vehicles1, vehicles2, vehicles3, vehicles4= (vehicles)
# print(vehicles3)

# # LIST INSIDE TUPLES  
# favorites=("mango","orange","grapes",["banana","coconut"])   # ERROR
# favorites[1].pop()
# print(favorites)
  
def func(int1,int2):           #FUNCTION return two values
    add= int1 + int2
    multiply=int1*int2
    return add,multiply
print(func(2,9))

