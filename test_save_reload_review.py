#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
review = Review()
review.user_id = "custom user id"
review.place_id = "custom place id"
review.text = "Oklahoma is a nice place"
review.save()
print(review)

print("-- Create a new User 2 --")
review2 = Review()
review2.user_id = "pelemense"
review2.place_id = "USA_ID"
review2.text = "I love to be in usa"
review2.save()
print(review2)