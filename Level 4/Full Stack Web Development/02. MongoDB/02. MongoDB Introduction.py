import pymongo
from pprint import pprint

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

pprint(dir(client), indent=4)
print(client.server_info)
