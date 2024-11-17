# Write a function called greet that takes two arguments: name str and age int 
# the fuction should return a str message in format 
# "Hello, [name]! You are [age] years old."

def greet(name: str, age: int) -> str:
    '''
    :param name: str
    :param age: int
    :return: str formated greating.
    '''
    return f"Hello, {name}! You are {age} years old."

from faker import Faker
import random
fake = Faker() 
# Generate a list of 10 fake names 
gen_number:int = 10
fake_names:list[str] = [fake.name() for _ in range(gen_number)]
random_list:list[int] = [round(random.uniform(1, 122)) for _ in range(gen_number)]

for age, name in zip(random_list,fake_names):
    print(greet(name, age))