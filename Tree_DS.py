# #********************PROGRAM TO IMPLEMENT BINARY SEARCH TREE***********
# class BST:     #TAKE A A suitable class name
#     def __init__(self, key):    #init method is special method of class it is called when object is created, it will be called automatically after the object is created
                
                                   # this meth0d allows the class too intialize the attribute of class    #(self) represent the object itself
#         self.key = key            # here in program every node is an object.
#         self.lchild = None
#         self.rchild = None

# root = BST(10)
# print(root.key)
# print(root.lchild)
# print(root.rchild)
# root.lchild = BST(5)
# print(root.key)
# print(root.lchild)

##****************PROGRAM TO IMPLEMENT BST "INSERTION METHOD"******************

from itertools import count
from threading import currentThread


class BST:
    def __init__(self,key):   #here self is nothing but an root object
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self, data):
        if self.key is None:
            self.key = data
            return

        if self.key ==data:    #Here we are checking for duplicate values!
            return

        if self.key > data:
            if self.lchild:     #here it will check whether left-child has node? if NONE then condition fails..
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)   
        else:
            if self.rchild:
                self.rchild.insert(data)  #it is an recursive call here this function will pause the execution and re-execute the whole program for that particular
            else:
                self.rchild = BST(data)   #here, BST is class name and we are passing data here means we are creating an object.
                                   # and whenever we create an object from BST class , all the fields of BST will initialized automatically.
    
    def search(self, data):          #****************WRITE A PROGRAM FOR SEARCH OPERATION IN BST*************
        if self.key== data:
                print("node is found")
                return
        if self.key > data:
                if self.lchild:
                    self.lchild.search(data)
                else:
                    print("node is not present")
        if self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else :
                print("node is not present")

    def preorder(self):     #********************BST- PRE-ORDER TRAVERSAL******************///
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):          #***IN-ORDER TRAVERSAL..
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end = " ") 
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

    def delete(self, data):                  #*****DELETE OPERATION**************THIS METHOD WORKS FOR GRAPH WITH TWO 2 CHILD NODES..
        if self.key is None:
            print("Tree is empty!")
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given Node is Not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given Node is Not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp= self.lchild
                self= None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self

    def min_node(self):
        current = self
        while current.lchild:
            current= current.lchild
        print("node with smallest key is:", current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("node with max key is:", current.key)

    # def delete(self, data,curr):                  #*****DELETE OPERATION**************THIS METHOD WORKS FOR all cases...!.!
    #     if self.key is None:
    #         print("Tree is empty!")
    #         return
    #     if data < self.key:
    #         if self.lchild:
    #             self.lchild = self.lchild.delete(data,curr)
    #         else:
    #             print("Given Node is Not present in the tree")
    #     elif data > self.key:
    #         if self.rchild:
    #             self.rchild = self.rchild.delete(data,curr)
    #         else:
    #             print("Given Node is Not present in the tree")
    #     else:
    #         if self.lchild is None:
    #             temp = self.rchild
    #             if data == curr:
    #                 self.key = temp.key
    #                 self.lchild = temp.lchild
    #                 self.rchild = temp.rchild
    #                 temp = None
    #                 return
    #             self = None
    #             return temp
    #         if self.rchild is None:
    #             temp= self.lchild
    #             if data == curr:
    #                 self.key = temp.key
    #                 self.lchild = temp.lchild
    #                 self.rchild = temp.rchild
    #                 temp = None
    #                 return
    #             self= None
    #             return temp
    #         node = self.rchild
    #         while node.lchild:
    #             node = node.lchild
    #         self.key = node.key
    #         self.rchild = self.rchild.delete(node.key, curr)
    #     return self
    
    

root = BST(10)   #here we are creating an object/NOde with value 10.  now, it will call initialization method so we will get a node!      #execution of program starts from here! we are creating an object from this BST class the object name is "root" and here i am passing the value of data as NONE 
                 # when we create an object from BST class by default initialization method will be called and it will initialize lchild and rchild and key of root
list1 = [20,4]
for i in list1:            #it will insert the value one by one!
    root.insert(i) 
# root.search(60)
# root.preorder()
print("in-order")
root.inorder()
# print('\n') 
# print("post_order")
# root.postorder()
# print('\n')

# if count(root) > 1:                #*******ERROR in deletion operation....
#     root.delete(10, root.key)
# else:
#     print("can't perform deletion operation")

# print("delete")
# root.delete(30)

print("after deleting ")
root.inorder()


root.min_node()
root.max_node()
