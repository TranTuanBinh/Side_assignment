#1 write a python program to read file sample.json. display all distance information and name of location 

import json



def op_1(json_file_name):
        with open(json_file_name,'r') as a:
            obj = json.loads(a)
            feature = obj['result']
            for x in feature:
                print('distance:', x['distance'])
                print('name:', x['name'])
#2 write a program to 
# define a python object (dictionary) containt fields: location,gps (lat,lon) weather, date, population
def op_2(json_file_name):
        dict = {'location': 'hanoi', 
                'gps':{
                    'lat':35,
                    'lon':36},
                'weather': 'sunny',
                'date':'21/014/2001'}
# store a python object(dict) into a json file name sample_w.json:
        with open('sample_w.json', 'w') as b:

            b.write(dict)

#3 write a program to create a new json file from an existing json file (sample_w.json)
def op_3():
    with open('sample_w.json', 'r') as c: 
        c_obj = json.loads(c)
        with open('new_json_file', 'w') as d: 
            d.write(c_obj)
        


#4 write a program to add new items into existing file (users.json), user information will be input from keyboard 
'''
user.json 
[
    {
        'name' : 'john',
        'email': john@example.com,
        'age':18,
        'address': 'john street'
    
    },
    {
        'name':'su',
        'email':'su@example.com',
        'age':18,
        'address': 'su street'
    }
]
'''


#5 write a program to delete users which have age is a number input from keyboard from user.json file 