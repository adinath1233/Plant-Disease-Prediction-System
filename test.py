from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://plant:plant@cluster0.xpustql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_names = client.list_database_names()

# Print list of databases
print("Available databases:")
for db_name in db_names:
    print(db_name)
