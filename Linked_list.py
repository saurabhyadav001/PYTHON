#traversal of LINKED LIST********
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def print_LL(self):
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data)
#                 n= n.ref

# LL1= LinkedList()
# LL1.print_LL()

#*******INSERTION OF ELEMENT AT THE BEGINNING OF LINKED LIST**************
# class Node:             #STEP!-- using node class create a node!
#     def __init__(self,data): #pass the parameters like data
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None 
#     def print_LL(self):                      #tRAVERSAL OPERATION
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data)
#                 n= n.ref
#     def add_begin(self, data):
#         new_node= Node(data)
#         new_node.ref = self.head
#         self.head= new_node

# LL1= LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.print_LL()


#adding element at the last of the linked list*********************

# class Node:                  #STEP!-- using node class create a node!
#     def __init__(self,data): #pass the parameters like data
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None 
#     def print_LL(self):                      #tRAVERSAL OPERATION
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data)
#                 n= n.ref
#     def add_begin(self, data):
#         new_node= Node(data)
#         new_node.ref = self.head
#         self.head= new_node
    
#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n= self.head
#             while n.ref is not None:
#                 n= n.ref
#             n.ref = new_node

# LL1= LinkedList()
# LL1.add_begin(10)
# LL1.add_begin(20)
# LL1.add_begin(45)
# LL1.add_end(60)
# LL1.print_LL()


#*************INSERTING ELEMENTS AFTER THE GIVEEN NODI IN THE LINKED LIST!

# class Node:                  #STEP!-- using node class create a node!
#     def __init__(self,data): #pass the parameters like data
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None 
#     def print_LL(self):                      #tRAVERSAL OPERATION
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data)
#                 n= n.ref
#     def add_begin(self, data):
#         new_node= Node(data)
#         new_node.ref = self.head
#         self.head= new_node
    
#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n= self.head
#             while n.ref is not None:
#                 n= n.ref
#             n.ref = new_node
    
#     def add_after(self, data, x):
#         n= self.head
#         while n is not None:
#             if x==n.data:
#                 break
#             n= n.ref
#         if n is None:
#             print("node is not present in LL")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node

# LL1= LinkedList()
# LL1.add_begin(10)
# LL1.add_end(60)
# LL1.add_after(500, 20)
# LL1.print_LL()

#**************INSERTION OF ELEMENTS BEFORE AN ELEMENT*****************************
# class Node:                  #STEP!-- using node class create a node!
#     def __init__(self,data): #pass the parameters like data
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None 
#     def print_LL(self):                      #tRAVERSAL OPERATION
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data)
#                 n= n.ref
#     def add_begin(self, data):
#         new_node= Node(data)
#         new_node.ref = self.head
#         self.head= new_node
    
#     def add_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n= self.head
#             while n.ref is not None:
#                 n= n.ref
#             n.ref = new_node
    
#     def add_after(self, data, x):
#         n= self.head
#         while n is not None:
#             if x==n.data:
#                 break
#             n= n.ref
#         if n is None:
#             print("node is not present in LL")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node

#     def add_before(self,data,x):
#         if self.head is None:
#             print("Linked List is empty!")
#             return
#         if self.head.data==x:
#             new_node = Node(data)
#             new_node.ref = self.head
#             self.head = new_node
#             return
#         n = self.head
#         while n.ref is not None:
#             if n.ref.data==x:
#                 break
#             n = n.ref        
#         if n.ref is None:
#             print("Node is not found!")
#         else:
#             new_node = Node(data)
#             new_node.ref = n.ref
#             n.ref = new_node     

# LL1= LinkedList()
# LL1.add_begin(10)
# LL1.add_end(60)
# LL1.add_after(500, 20)
# LL1.add_before(555, 60)
# LL1.print_LL()


#**********************add element to the empty linked list**********

# class Node:                  #STEP!-- using node class create a node!
#     def __init__(self,data): #pass the parameters like data
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None 
#     def print_LL(self):                      #tRAVERSAL OPERATION
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data)
#                 n= n.ref
#     def insert_empty(self, data):
#         if self.head is None:
#             new_node = Node(data)
#             self.head = new_node
#             self.head = new_node
#         else:
#             print("linked list is not empty!")
# LL1 = LinkedList()
# LL1.insert_empty(10)
# LL1.insert_empty(20)
# LL1.print_LL()



#********************DELETION operation in Linked LIst*****************************

#***********Delete the first node of in linked list******

# class Node:                  
#     def __init__(self,data): 
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None 
#     def print_LL(self):               
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data)
#                 n= n.ref

#     def add_begin(self, data):
#         new_node= Node(data)
#         new_node.ref = self.head
#         self.head= new_node

#     def delete_begin(self):
#         if self.head is None:
#             print("LL is empty so we can't delete nodes!")
#         else :
#             self.head = self.head.ref
# LL1 = LinkedList()
# LL1.add_begin(20)
# LL1.add_begin(50)
# LL1.delete_begin()
# LL1.print_LL()


#****************DELETE THE LAST NODE IN LINKED LIST******************
#APPROACH:-- 1-check whether the LL is empty or not.
#            2- goto to second last element and make its ref NULL!
#  

# class Node:                  
#     def __init__(self,data): 
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def __init__(self):
#         self.head = None 
#     def print_LL(self):               
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n= self.head
#             while n is not None:
#                 print(n.data)
#                 n= n.ref

#     def add_begin(self, data):
#         new_node= Node(data)
#         new_node.ref = self.head
#         self.head= new_node

#     def delete_begin(self):
#         if self.head is None:
#             print("LL is empty so we can't delete nodes!")
#         else :
#             self.head = self.head.ref
#     def delete_end(self):
#         if self.head is None:
#             print("LL is empty so we cant delete nodes!")
#         else:
#             n= self.head
#             while n.ref.ref is not None:
#                 n= n.ref
#             n.ref = None
# LL1 = LinkedList()
# LL1.add_begin(20)
# LL1.add_begin(50)
# # LL1.delete_begin()
# LL1.delete_end()
# LL1.print_LL()


#************DELETE ELEMENT FROM MIDDLE OF THE LINKED LIST**************
#Approach-- 1- check whether LL is empty or not!
        # 2--- if not empty we can perform deletion operation
        # 3-- if the LL is not empty check whether the given node is 1st node! 
        # if yes I.e we have to delete first node then head to point the 2nd node!
        #if not 1st node then go to the previous node of the given node, and change its reference! to the next node.

class Node:                  
    def __init__(self,data): 
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None 
    def print_LL(self):               
        if self.head is None:
            print("linked list is empty")
        else:
            n= self.head
            while n is not None:
                print(n.data)
                n= n.ref

    def add_begin(self, data):
        new_node= Node(data)
        new_node.ref = self.head
        self.head= new_node

    def delete_begin(self):
        if self.head is None:
            print("LL is empty so we can't delete nodes!")
        else :
            self.head = self.head.ref
    def delete_end(self):
        if self.head is None:
            print("LL is empty so we cant delete nodes!")
        else:
            n= self.head
            while n.ref.ref is not None:
                n= n.ref
            n.ref = None
    
    def delete_by_value(self,x):
        if self.head is None:
            print("can't delete LL is empty!")
            return
        if x==self.head.data:
            self.head = self.head.ref
            return
        n= self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n= n.ref
        if n.ref is None:
            print("nod is not present!")
        else:
            n.ref = n.ref.ref
LL1 = LinkedList()
LL1.add_begin(20)
LL1.add_begin(50)
# LL1.delete_begin()
# LL1.delete_end()
LL1.delete_by_value(20)
LL1.print_LL()
