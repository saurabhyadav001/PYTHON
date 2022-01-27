# def add_node(v):
#     global node_count
#     if v in nodes:
#         print(v," is already present in the graph")
#     else:
#         node_count = node_count + 1
#         nodes.append(v)
#         for n in graph:
#             n.append(0)
#         temp = []
#         for i in range(node_count):
#             temp.append(0)
#             graph.append(temp)

# # def add_edge(v1,v2):         #THIS IS FOR UN-DIRECTED AND UN-WEIGHTED GRAPH 
# #     if v1 not in nodes:
# #         print(v1,"element is not present")
# #     elif v2 not in nodes:
# #         print(v2,"is not present")
# #     else:
# #         index1 = nodes.index(v1)
# #         index2 = nodes.index(v2)
# #         graph[index1] [index2] = 1
# #         graph[index2] [index1] = 1


# def add_edge(v1,v2,cost):         #THIS IS FOR UN-DIRECTED AND WEIGHTED GRAPH 
#     if v1 not in nodes:
#         print(v1,"element is not present")
#     elif v2 not in nodes:
#         print(v2,"is not present")
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1] [index2] = cost
#         graph[index2] [index1] = cost

# # def add_edge(v1,v2,cost):         #THIS IS FOR DIRECTED AND WEIGHTED GRAPH 
# #     if v1 not in nodes:
# #         print(v1,"element is not present")
# #     elif v2 not in nodes:
# #         print(v2,"is not present")
# #     else:
# #         index1 = nodes.index(v1)
# #         index2 = nodes.index(v2)
# #         graph[index1] [index2] = cost

        
# # def add_edge(v1,v2):         #THIS IS FOR DIRECTED AND UN-WEIGHTED GRAPH 
# #     if v1 not in nodes:
# #         print(v1,"element is not present")
# #     elif v2 not in nodes:
# #         print(v2,"is not present")
# #     else:
# #         index1 = nodes.index(v1)
# #         index2 = nodes.index(v2)
# #         graph[index1] [index2] = 1
# #         graph[index2] [index1] = 1


# def print_graph():
#     for i in range(node_count):
#         for j in range(node_count): 
#             print(format(graph[i] [j], "<3"), end =" ")
#         print() 

# nodes = []
# graph = []
# node_count = 0
# print("before adding nodes")
# print(nodes) 
# print(graph)
# add_node("A")
# add_node("B")
# add_node("D")
# # add_edge("A", "D")

# add_edge("A", "B", 10)
# add_edge("A", "D", 5)

# # print("after adding nodes")
# # print("nodes:",nodes)
# # print(graph)

# print_graph()




####*********PYTHON PROGRAM TO IMPLEMENT GRAPH INSERTION OPERATION IN ** ADJACENCY LIST

# def add_node(v):
#     if v in graph:
#         print(v," is already present in graph")
#     else:
#         graph[v] = []

# graph = {}
# add_node("A")
# add_node("B")
# print(graph)


# ********ADD EDGE -Un-directed UN-weighted Graph*******


def add_node(v):
    if v in graph:
        print(v," is already present in the graph")
    else:
        graph[v] = []

def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
graph = {}
add_node("A")
add_node("B")
add_edge("A", "B")
print(graph)


#************FOR undirected , Weighted graph

def add_node(v):
    if v in graph:
        print(v," is already present in the graph")
    else:
        graph[v] = []

def add_edge(v1, v2,cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        list1 = [v2, cost]
        list2 = [v1, cost]
        graph[v1].append(list1)
        graph[v2].append(list2)
    
graph = {}
add_node("A")
add_node("B")
add_edge("A", "B")
print(graph)


#*******for directed weighted graph********
def add_node(v):
    if v in graph:
        print(v," is already present in the graph")
    else:
        graph[v] = []

def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph: 
        print(v2, "is not present in the graph")
    else:
        list1 = [v2, cost]
        graph[v1].append(list1)
    
graph = {}
add_node("A")
add_node("B")
add_edge("A", "B")
print(graph)

#*****************DIRECTED UN-WEIGHTED GRAPH***************

def add_node(v):
    if v in graph:
        print(v," is already present in the graph")
    else:
        graph[v] = []

def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)
    
graph = {}
add_node("A")
add_node("B")
add_edge("A", "B")
print(graph)
