# parent = {"child1" : {"name" : "James"} ,
#           "child2" : { "name" : "Jane"} }
# print(parent["child2"]["name"])  
# programs = {"school1" : {"name" : "Jkuates" , "time" : "8:00"} ,
          #  "school2" : {"name" : "stem" , "time" : "8:30"}}
# print(programs["school1"]["time"])
# car={
#     'model':'ford',
#     'year' : 1998,
#     'colour':'red',
#     'country':'Kenya'
# }
#accesing dictionary items
# print(car['country'])
# profile={}
# profile['username']='user123'
# profile['age']=23
# profile['repos']={'name':'python'}
# print(profile)
profile={}
def register():
    username=input('Enter username : ')
    email=input('Enter email : ')
    password=input('Enter password : ')
#storing in a dictonary
    profile['username']=username
    profile['email']=email
    profile['password']=password
def get_profile():
    print(profile)
def change_username():
    new_username=input('Enter new username : ')
    profile['username']=new_username
register()
get_profile()
change_username()
get_profile()


