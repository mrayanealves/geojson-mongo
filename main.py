from pymongo import MongoClient

try:
    mongo_client = MongoClient('mongodb://localhost:27017/')
    print("MongoDB connected successfully.")
except:
    print("Could not connect to MongoDB")

db = mongo_client.geojason
collection = db.restaurants

# Item 1: Convert the coordinates of restaurants for default GeoJSON
resp = collection.find()
restaurants = []

# Turning return into a list with dictionaries
for doc in resp:
    restaurants.append(doc)

# Converting the document for default GeoJSON
for restaurant in restaurants:
    if restaurant['address']['coord'] == []:
        restaurant['loc'] = {'type': 'Point', 'coordinates': [0, 0]}
    else:
        restaurant['loc'] = {'type': 'Point', 'coordinates': restaurant['address']['coord']}

    del restaurant['address']['coord']

# Overriding these modifications in the database
for restaurant in restaurants:
    collection.replace_one({"_id": restaurant['_id']}, restaurant)

#Item 2: Create a index 2dsphere for the new field
resp = collection.create_index([('loc', '2dsphere')])

#Item 3: List the restaurants within 1 kilometer of Port Authority Bus Terminal (NY) (Point: -73.9929943, 40.7571707)
resp = collection.find({'loc': {'$near': {'$geometry': {'type': 'Point', 'coordinates': [-73.9929943, 40.7571707]}, '$minDistance': 0, '$maxDistance': 1000}}}) 
restaurant_near = []

for doc in resp:
    restaurant_near.append(doc)

print(restaurant_near)