
''' 1. From two lists, create a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
'''
#1 



keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_1 = dict(zip(keys, values))
#-------------------------------
'''2. Frome two dictionaries, merge into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
'''
#2 
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict_2 = dict1.update(dict2) 
#------------------------------------------------

'''3. Print the value of key 'physics' from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
'''
#3 
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['physics'])
#------------------------------------------------------

'''4. Initialize dictionary with default values
Given:
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Expected output:
{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
'''
#4
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
dict_4 = dict.fromkeys(employees, defaults)
print(dict_4)

'''5. Create a dictionary by extracting the keys from a given dictionary
Given:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
Keys to extract
keys = ["name", "salary"]
Expected output:
{'name': 'Kelly', 'salary': 8000}
'''
#5
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]

new_dict = dict()
for x in keys :
    new_dict.update({x: sample_dict[x]})

print(new_dict)

#---------------------------------------
'''6. Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
Keys to remove
keys = ["name", "salary"]
Expected output:
{'city': 'New york', 'age': 25}
'''
#6
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# key to remove
keys = ["name", "salary"]

for k in keys :
    sample_dict.pop(k)

print(sample_dict)
#---------------------------------------------------------

'''7. Check if value 200 exists in the following dictionary.
Given:
sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:
200 present in a dict
'''
#7
sample_dict = {'a': 100, 'b': 200, 'c': 300}
i = 200 
if i in sample_dict : 
    print(f'{i} present in a dict')

#----------------------------------------------------------

'''8. Rename a key city to a location in the following dictionary
Given:
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Expected output:
{'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''
#8 
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
#-----------------------------------------------------

'''9. Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
'''
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sample_dict), key=sample_dict.get())

#---------------------------------------------
'''10. Change Brad’s salary to 8500 in the following dictionary.
Given:
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
Expected output:
{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
'''
#10
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

for k1,v1 in sample_dict.items() :
    for k2,v2 in v1 :
        if v2 == 'Brad':
            sample_dict[k1]['salary'] = 8500 

print('the dict after change is',sample_dict)





