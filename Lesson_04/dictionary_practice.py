#1:Convert two list into a dict
key=['Ten','Twenty','Thirty']
values=[10,20,30]

a_dict = dict(zip(key, values))

print('Dictionary after convert:', a_dict)
print('------------------')

#2: Frome two dictionaries, merge into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy ()
dict3.update(dict2)

print(dict3)
print('-----------------')
#3:Print the value of key 'physics' from the below dict
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

print('the value of key physics is', sampleDict['class']['student']['marks']['physics'])
print('-----------------')

#4:Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

ex4_dict = dict.fromkeys(employees, defaults)

print(ex4_dict)
print('---------------')

#5:Create a dictionary by extracting the keys from a given dictionary
sample_dict1 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys_extract = ["name", "salary"]

ex5_dict ={}
for i in keys_extract:
    ex5_dict[i]=sample_dict1[i]


print('new dict after extracting: ',ex5_dict)
print('-----------------')

#6:Delete a list of keys from a dictionary
sample_dict2 = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys_remove = ["name", "salary"]

for x in keys_remove: 
    del sample_dict2[x]

print('dict after removal:', sample_dict2)
print('---------------')

#7:Check if value 200 exists in the following dictionary
sample_dict3 = {'a': 100, 'b': 200, 'c': 300}
for x in sample_dict3.values():
    if x == 200: 
        print('True')
    
print('-----------------')

#8:Rename a key city to a location in the following dictionary
sample_dict4 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict4['location'] = sample_dict4.pop('city')

print(sample_dict4.items())
print('-------------------------')

#9:Get the key of a minimum value from the following dictionary
sample_dict5 = {
  'Physics': 10,
  'Math': 65,
  'history': 75
}

min_in_dict = []
for x in sample_dict5.values(): 
    min_in_dict.append(x)

print(min(min_in_dict))
print('-------------------------')

#10:Change Brad’s salary to 8500 in the following dictionary.
sample_dict6 = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

for k1,v1 in sample_dict6.items():
     for k2,v2 in v1.items():
        if v2 == 'Brad': 
            sample_dict6[k1]['salary'] = 8500

print(sample_dict6)