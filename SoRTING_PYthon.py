# FUNCTION****---- A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application 
# and a high degree of code reusing.

#**************************************************BUBBLE SORTING:*****************************************************************
# def sort(nums):

#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp

# nums = [5, 3, 8, 6, 7, 2]
# sort(nums)
# print(nums)

#***************************************************Linear Search Using Python**********************************************************

# def search(list,n):
#     i=0
#     while i< len(list):
#         if list[i] ==n:
#             return True
#         i= i+1
#     return False


# list = [2,3,4,5,6,7,8,9]
# n=5
# if search(list, n):
#     print("found")
# else:
#     print("not found")


#******************************WRITE LINEAR SEARCH PROGRAM AND PRINT THE LOCATION AT WHICH VALUE IS FOUND?*******************************

# pos = -1
# def search(list, n):
#     i=0
#     while i<len(list):
#         if list[i] ==n:
#             globals() ['pos'] =i
#             return True
#         i = i+1
#     return False
# list = [1,2,3,4,5,6,7]
# n =5
# if search(list, n):
#     print("found at", pos)
# else:
#     print("not found")



#*****************************************************LINEAR SEARCH USING FOR LOOP:**********************************************

# def search(list,n):
#     for i in list:
#         if i==n:
#             return True

#     return False

# list = [10,20,30,40,50]
# n = 51
# if search(list,n):
#     print("Found")
# # else:
#     print("Not Found")

#***********************************************BINARY SEARCH USING PYTHON*******************************************************************
# pos = -1

# def search(list, n):

#     l = 0
#     u = len(list)-1

#     while l <= u:
#         mid = (l+u) // 2

#         if list[mid] == n:
#             globals()['pos'] = mid
#             return True
#         else:
#             if list[mid] < n:
#                 l = mid+1;
#             else:
#                 u = mid-1;

#     return False

# list = [4,7,8,12,45,99,102,702,10987,56666]
# n = 45

# if search(list, n):
#     print("Found at ",pos+1)
# else:
#     print("Not Found")


#***********************************************SELECTION SORT************************************************************

# list = [9,4,3,2,5,7,6]
# print(list)
# for i in range(len(list)):
#     min_val = min(list[i:])   #using min(), max() function we can directly find the smallest/ largest value
#     min_ind = list.index(min_val)   #usint .index func() we can directly find the indix of any specific number in the list.
#     temp = list[i]      #now swap them
#     list[i]= list[min_ind]
#     list[min_ind]= temp
# print(list)

# list =[34,22,11,56,43]        ##*****SELECtion sort  MOst FLEXIBLE and accuraTE PROGRAM
# print(list)
# for i in range(len(list)-1):
#     min_val = min(list[i:])
#     min_ind = list.index(min_val,i)
#     if list[i] != list[min_ind]:
#        temp = list[i]
#        list[i]=  list[min_ind]
#        list[min_ind] = temp
#        print(list)

# list = [64,3,67,33,2,22]    # IF we don't want to use min() function!
# print(list)
# for i in range(len(list)-1):
#     min_val = list[i]
#     for j in range(i+1, len(list)):
#         if list[j] < min_val:
#             min_val = list[j]
#     min_ind = list.index(min_val,i)
#     temp = list[i]
#     list[i]=  list[min_ind]
#     list[min_ind] = temp
#     print(list)


# a="abcdef">="abcd"
# print(a)

# def change(li):
#     li[1] = li[1] + 2
#     li =[3,3,3,4,5]
# li =[1,2,3,4,5]
# change(li)
# print(li)

# a= 10
# b=20
# multiple = a*b
# print("multiple")

li= ['abcd",def']      #**********
li.insert(4,5)
print(li)
         
# s= "abcd"
# b= s+2
# print(b)

# s= "abcdef"
# print(s[4:2:-1])

# n=25
# if n>=5:
#     print("greater than 5")
# elif n>=10:
#     print("greater than 10")
# elif n>=20:
#     print("greater than 20")
# else:
#     print("negative or less than 5")

# a= 14
# def f():
#     a=12
# f()
# print(a)

# if(10<0) and (0<-10):
#     print("A")
# elif(10>0) or False:
#     print("B")
# else:
#     print("c")

def function(a,b,c=1,d=5):      #**********************************
    return a+b+c+d
value = function(1,2,d=7)
print(value)

# a= int(input("enter a number "))
# b= int(input("enter a number"))
# c= a+b
# print(c)

a=10                   #********************************
id1 = id(a)
b= a+2-2
id2= id(b)

#************************************INSERTION SORT***************************************
from tempfile import tempdir
from turtle import right


# def insertion_sort(list):
#     for i in range(1,len(list)):
#         j=i
#         while list[j-1] > list[j] and j>0:
#             temp= list[j-1]
#             list[j-1]= list[j]
#             list[j]= temp
#             j=j-1
#         print(list)
            
# list = [12,21,32,23,1,2,2]
# insertion_sort(list)


#*************************MERGE SORT**************************************

# def mergesort(list1):
#     if len(list1)>1:
#         mid= len(list1)//2                       # These are dividing conditions:
#         left_list = list1[:mid]
#         right_list = list1[mid:]
#         mergesort(left_list)
#         mergesort(right_list)
#         i=0
#         j=0
#         k=0
#         while i<len(left_list) and j<len(right_list):              # These are merging conditions:
#             if left_list[i] < right_list[j]:
#                 list1[k] = left_list[i]
#                 i=i+1
#                 k=k+1
#             else:
#                 list1[k] = right_list[j]
#                 j= j+1
#                 k=k+1
#         while i<len(left_list):               #these conditions are to check whether any value is left or notkc  fv 
#             list1[k] = left_list[i]             
#             i= i+1
#             k=k+1
#         while j<len(right_list):
#             list1[k] = right_list[j]
#             j= j+1
#             k=k+1

# num= int(input("how many elements you want in list:"))
# list1 = [int(input()) for x in range(num)]
# mergesort(list1)    
# print("sorted list: ", list1)
