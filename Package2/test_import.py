#1 write a python program to read file sample.json. display all distance information and name of location 
import json


def op_1():
    with open('sample.json', 'r', encoding='utf-8') as a:
        obj = json.load(a)
        print(obj)

op_1()
