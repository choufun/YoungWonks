from pymongo import MongoClient
from pprint import pprint



def list_databases(client):
    ''' A database is not created until it gets content. '''
    print('Databases:')
    for db in client.list_database_names():
        print("   %s" %(db))
    print()


def list_collections(db):
    ''' A collection is not created until it gets content. '''
    print('Collections:')
    for col in db.list_collection_names():
        print("   %s" %(col))
    print()


client = MongoClient("mongodb://127.0.0.1:27017")


with client:
    list_databases(client)

    ''' MongoDB create database command: $ mongo youngwonks '''
    
    new_db  = client["youngwonks"]
    

    ''' insert a single document into a collection '''
    
    student = {"name": "Anonymous", "grade": "?"}
    new_colA = new_db["students"]    
    new_colA.insert_one(student)
    

    ''' insert multiple documents into a collection '''
    
    teachers = [{"name": "Steven Chou",     "level": "Middle"},
               {"name": "Richard Lin",     "level": "College"},
               {"name": "Jullian Harriot", "level": "High"}]
    new_colB = new_db["teachers"]
    new_colB.insert_many(teachers)


    list_databases(client)
    list_collections(new_db)

    new_db.drop_collection("students")
    new_db.drop_collection("teachers")

    client.drop_database("youngwonks")

    
