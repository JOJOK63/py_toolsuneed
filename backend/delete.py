from tinydb import TinyDB, Query, where

db = TinyDB('db.json', indent=4)

# Insert data
db.insert({"name": "John", "score": 12})
db.insert_multiple([{"name": "Jane", "score": 10}, {"name": "Bob", "score": 8}])

# Get data
User = Query()
john = db.search(User.name == "John")
jhon_unique = db.get(User.name == "John")
print(john)
print(jhon_unique)

high_score = db.search(User.score > 10)
print(high_score)

db.update({"score": 15}, where('name') == 'Bob')

db.remove(where('name') == 'John')

all = db.all()
print(all)
print(len(db))
print(db.contains(User.name == "Jane"))
print(db.count(where('score') > 10))


print(type(type))