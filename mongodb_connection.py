"""
MongoDB Connection Program
A comprehensive Python program for connecting to MongoDB and performing CRUD operations.
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
import os


class MongoDBConnection:
    """Class to handle MongoDB connection and operations."""
    
    def __init__(self, connection_string=None, database_name="mydatabase"):
        """
        Initialize MongoDB connection.
        
        Args:
            connection_string: MongoDB connection URI. 
                              If None, defaults to local MongoDB.
            database_name: Name of the database to use.
        """
        if connection_string is None:
            # Default local MongoDB connection
            self.connection_string = "mongodb://localhost:27017/"
        
        self.database_name = database_name
        self.client = None
        self.db = None
        self.connect()
    
    def connect(self):
        """Establish connection to MongoDB."""
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.database_name]
            print(f"Successfully connected to MongoDB!")
            print(f"Database: {self.database_name}")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            raise
    
    def get_collection(self, collection_name):
        """Get or create a collection."""
        return self.db[collection_name]
    
    def insert_one(self, collection_name, document):
        """Insert a single document."""
        collection = self.get_collection(collection_name)
        result = collection.insert_one(document)
        return result.inserted_id
    
    def insert_many(self, collection_name, documents):
        """Insert multiple documents."""
        collection = self.get_collection(collection_name)
        result = collection.insert_many(documents)
        return result.inserted_ids
    
    def find_one(self, collection_name, query):
        """Find a single document."""
        collection = self.get_collection(collection_name)
        return collection.find_one(query)
    
    def find_all(self, collection_name, query=None, limit=0):
        """Find all documents matching the query."""
        collection = self.get_collection(collection_name)
        if query is None:
            query = {}
        if limit > 0:
            return collection.find(query).limit(limit)
        return list(collection.find(query))
    
    def update_one(self, collection_name, query, update_data):
        """Update a single document."""
        collection = self.get_collection(collection_name)
        result = collection.update_one(query, {"$set": update_data})
        return result.modified_count
    
    def update_many(self, collection_name, query, update_data):
        """Update multiple documents."""
        collection = self.get_collection(collection_name)
        result = collection.update_many(query, {"$set": update_data})
        return result.modified_count
    
    def delete_one(self, collection_name, query):
        """Delete a single document."""
        collection = self.get_collection(collection_name)
        result = collection.delete_one(query)
        return result.deleted_count
    
    def delete_many(self, collection_name, query):
        """Delete multiple documents."""
        collection = self.get_collection(collection_name)
        result = collection.delete_many(query)
        return result.deleted_count
    
    def close(self):
        """Close the MongoDB connection."""
        if self.client:
            self.client.close()
            print("MongoDB connection closed.")


def demonstrate_crud_operations():
    """Demonstrate basic CRUD operations with MongoDB."""
    
    # Create connection
    mongo = MongoDBConnection(database_name="testdb")
    
    # Define collection name
    collection_name = "users"
    
    # CREATE - Insert documents
    print("\n--- CREATE Operations ---")
    
    # Insert single document
    user1 = {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 25,
        "city": "New York"
    }
    inserted_id = mongo.insert_one(collection_name, user1)
    print(f"Inserted user with ID: {inserted_id}")
    
    # Insert multiple documents
    users = [
        {"name": "Jane Smith", "email": "jane@example.com", "age": 30, "city": "Los Angeles"},
        {"name": "Bob Johnson", "email": "bob@example.com", "age": 35, "city": "Chicago"},
        {"name": "Alice Brown", "email": "alice@example.com", "age": 28, "city": "Houston"}
    ]
    inserted_ids = mongo.insert_many(collection_name, users)
    print(f"Inserted {len(inserted_ids)} users")
    
    # READ - Query documents
    print("\n--- READ Operations ---")
    
    # Find one
    user = mongo.find_one(collection_name, {"name": "John Doe"})
    print(f"Found user: {user}")
    
    # Find all
    all_users = mongo.find_all(collection_name)
    print(f"Total users: {len(all_users)}")
    for u in all_users:
        print(f"  - {u['name']}, {u['email']}, Age: {u['age']}")
    
    # Find with filter
    young_users = mongo.find_all(collection_name, {"age": {"$lt": 30}})
    print(f"Users under 30: {len(young_users)}")
    
    # UPDATE - Modify documents
    print("\n--- UPDATE Operations ---")
    
    # Update one
    modified = mongo.update_one(
        collection_name, 
        {"name": "John Doe"}, 
        {"age": 26}
    )
    print(f"Modified {modified} document(s)")
    
    # Update many
    modified = mongo.update_many(
        collection_name, 
        {"city": "New York"}, 
        {"country": "USA"}
    )
    print(f"Modified {modified} document(s) with country USA")
    
    # DELETE - Remove documents
    print("\n--- DELETE Operations ---")
    
    # Delete one
    deleted = mongo.delete_one(collection_name, {"name": "Jane Smith"})
    print(f"Deleted {deleted} document(s)")
    
    # Delete many
    deleted = mongo.delete_many(collection_name, {"age": {"$gt": 40}})
    print(f"Deleted {deleted} document(s) with age > 40")
    
    # Show final collection
    print("\n--- Final Collection ---")
    final_users = mongo.find_all(collection_name)
    print(f"Total users remaining: {len(final_users)}")
    for u in final_users:
        print(f"  - {u['name']}, {u['email']}, Age: {u['age']}, City: {u.get('city', 'N/A')}")
    
    # Close connection
    mongo.close()


def simple_connection_example():
    """Simple example for basic MongoDB connection."""
    
    # Connect to MongoDB (local instance)
    client = MongoClient("mongodb://localhost:27017/")
    
    # Access database
    db = client["mydatabase"]
    
    # Access or create collection
    collection = db["mycollection"]
    
    # Insert a document
    document = {"name": "Test", "value": 123}
    result = collection.insert_one(document)
    print(f"Inserted document ID: {result.inserted_id}")
    
    # Find documents
    for doc in collection.find():
        print(doc)
    
    # Close connection
    client.close()
    print("Connection closed.")


if __name__ == "__main__":
    print("=" * 50)
    print("MongoDB Connection Program")
    print("=" * 50)
    
    # Check if pymongo is installed
    try:
        import pymongo
        print("pymongo is installed!")
        
        # Run the demonstration
        demonstrate_crud_operations()
        
    except ImportError:
        print("pymongo is not installed.")
        print("Installing pymongo...")
        os.system("pip install pymongo")
        print("Please run the program again.")
