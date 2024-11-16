#!/usr/bin/python3
"""
Test script for the BaseModel class.
"""

from models.base_model import BaseModel

# Create a new instance
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89

# Print initial instance
print(my_model)

# Save and print instance again
my_model.save()
print(my_model)

# Convert instance to dictionary and print
my_model_json = my_model.to_dict()
print(my_model_json)

# Print JSON keys and their types
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
