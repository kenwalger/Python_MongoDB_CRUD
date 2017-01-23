import pprint

from pymongo import MongoClient


__author__ = 'Ken W. Alger'


HOST = 'localhost'
PORT = 27017
client = MongoClient(HOST, PORT)
database = client.cookbook
recipes = database.recipes

# Create Document

recipe = {'title': 'chocolate milk',
          'description': 'Yummy drink',
          'ingredients': [
              {'name': 'milk', 'quantity': 8, 'unit of measure': 'ounce'},
              {'name': 'chocolate syrup', 'quantity': 2, 'unit of measure':
                  'ounce'}
          ],
          'yield': {'quantity': 1, 'unit': 'glass'},
          'prep time': 0,
          'cook time': 0,
          'author': 'Biff Tannen',
          'uploaded_by': 'kenwalger',
          }

recipes.insert_one(recipe)

# Read Document

print("\nPretty Print: \n")
pprint.pprint(recipes.find_one())

# Update Document

recipes.update_one({'title': 'chocolate milk'},
                   {'$set': {'author': 'George McFly'}
                    }
                   )
print("\nShould be George McFly: ")
pprint.pprint(recipes.find_one({'author': 'George McFly'}))

print("\nShould not be found")
pprint.pprint(recipes.find_one({'author': 'Biff Tannen'}))


# Delete Document

recipes.delete_one({'author': 'George McFly'})
print('Deleted the record:')
pprint.pprint(recipes.find_one())
