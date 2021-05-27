# user={'name':'saurabh','age':'20'}
# print(user)

#   #   # ALTERNATE METHOD #  #  #
# user=dict(name= 'saurabh',age= 18)
# print(user)

# user_info={}                             # how to add data in the empty dictionary
# user_info['name']='saurabh'
# user_info['age']=19
# print(user_info)

# user_info={                                # how to ADD data in dic
#     'name':'saurabh',
#     'age': 19,
#     'fav_games': ['pubg','pull'],
# }  
# user_info['fav_songs']=['song1','song2']
# user_info['fav_movies']=['harry','series']
# print(user_info)

# user_info={                                # How to delete data from dict.  POP method
#     'name':'saurabh',
#     'age': 19,
#     'fav_games': ['pubg','pull'],
#     'fav_heroes':['ajay','varun'],
#  }  
# user_info.pop('name')
# print(user_info)


# user_info={                                     # to add data through UPDATE METHOD               
#     'name':'saurabh',                             # ERROR  120
#     'age':19,   
#     'fav_game':('pubg','pull'),
# }
# more_info={'fav_movie':'coco'}
# user_info.update({more_info})
# print(user_info)

# FROMKEYS
# d={'name' : 'unknown', 'age' : 'unknown'}    # to print in this format
# d=dict.fromkeys({'name', 'age','height'},'unknown')    # FROMKEYS
# d=dict.fromkeys(range(1,11),'unknown')      # using range function in the dictonries
# print(d)

# GET METHODS
d={'name':'unknown','age' : 'unknown'}
print{d.get('name')}


