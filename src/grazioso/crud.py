"""
CURD operations for teh Grazioso Salvare animal shelter database.

This module provides a class for performing CRUD (Create, Read, Update, Delete)
operations on a MongoDB database. It is designed to be imported and used by other
Python scripts to interact with animal shelter data.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import PyMongoError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class AnimalShelter:
    """
    A class to interact with MongoDB database containing animal shelter data.

    This class implements CRUD operations for the database to allow for creating,
    reading, updating, and deleting animal records.
    """

    def __init__(
        self,
        username: str,
        password: str,
        host: str = "localhost",
        port: int = 27017,
        db_name: str = "AAC",
        collection_name: str = "animals",
    ) -> None:
        """
        Initialize the AnimalShelter with MongoDB connection details.

        Args:
            username: MongoDB user username
            password: MongoDB user password
            host: MongoDB server hostname (default: localhost)
            port: MongoDB server port (default: 27017)
            db_name: Name of the database to use (default: AAC)
            collection_name: Name of the collection to use (default: animals)
        """

        # Store connection parameters
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.collection_name = collection_name

        # Initialize connection
        self.client: Optional[MongoClient[Dict[str, Any]]] = None
        self.db: Optional[Database[Dict[str, Any]]] = None
        self.collection: Optional[Collection[Dict[str, Any]]] = None

        # Connect to database
        try:
            self._connect()
            logger.info(f"Successfully connected to MongoDB at {host}:{port}")
        except PyMongoError as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise

    def _connect(self) -> None:
        """
        Establish connection to the MongoDB database.

        Raises:
            PyMongoError: If connection to MongoDB fails
        """
        connection_string = (
            f"mongodb://{self.username}:{self.password}@{self.host}:{self.port}"
        )
        self.client = MongoClient(connection_string)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

        # Test connection
        self.client.admin.command("ping")

    def create(self, data: Dict[str, Any]) -> bool:
        """
        Insert a document into the MongoDB collection.

        Args:
            data: Dictionary containing the data to insert

        Returns:
            bool: True if successful, False otherwise

        Example:
            >>> shelter = AnimalShelter("username", "password")
            >>> new_animal = {
                "animal_id": "A123",
                "name": "Rover",
                "animal_type": "Dog"
            }
            >>> shelter.create(new_animal)
            True
        """
        if not data or self.collection is None:
            logger.warning("Cannot create empty document or collection not initialized")
            return False

        try:
            result = self.collection.insert_one(data)
            logger.info(f"Document inserted with ID: {result.inserted_id}")
            return bool(result.acknowledged)
        except PyMongoError as e:
            logger.error(f"Error inserting document: {e}")
            return False

    def read(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Query for documents from the MongoDB collection.

        Args:
            query: Dictionary containing the query parameters

        Returns:
            List of documents matching the query,
            or empty list if none found or error occurs

        Example:
            >>> shelter = AnimalShelter("username", "password")
            >>> animals = shelter.read({"animal_type": "Dog"})
            >>> len(animals)
            42
        """
        if self.collection is None:
            logger.warning("Collection not initialized")
            return []
        try:
            cursor = self.collection.find(query)
            result = list(cursor)
            logger.info(f"Query returned {len(result)} documents")
            return result
        except PyMongoError as e:
            logger.error(f"Error reading documents: {e}")
            return []

    def update(
        self, query: Dict[str, Any], update_data: Dict[str, Any], multi: bool = False
    ) -> int:
        """
        Update documents in the MongoDB collection.

        Args:
            query: Dictionary containing the query parameters
            update_data: Dictionary containing the update operations
            multi: If True, update all matching documents, otherwise update only one

        Returns:
            int: Number of documents modified

        Example:
            >>> shelter = AnimalShelter("username", "password")
            >>> shelter.update({"animal_id": "A123"}, {"$set": {"name": "Max"}})
            1
        """
        if not query or not update_data or self.collection is None:
            logger.warning("Query, update data, or collection cannot be empty")
            return 0

        try:
            if multi:
                result = self.collection.update_many(query, update_data)
            else:
                result = self.collection.update_one(query, update_data)

            logger.info(f"Modified {result.modified_count} documents")
            return result.modified_count
        except PyMongoError as e:
            logger.error(f"Error updating documents: {e}")
            return 0

    def delete(self, query: Dict[str, Any], multi: bool = False) -> int:
        """
        Remove documents from the MongoDB collection.

        Args:
            query: Dictionary containing the query parameters
            multi: If True, delete all matching documents, otherwise delete only one

        Returns:
            int: Number of documents deleted

        Example:
            >>> shelter = AnimalShelter("username", "password")
            >>> shelter.delete({"animal_id": "A123"})
            1
        """
        if not query or self.collection is None:
            logger.warning("Query or collection cannot be empty")
            return 0

        try:
            if multi:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)

            logger.info(f"Deleted {result.deleted_count} documents")
            return result.deleted_count
        except PyMongoError as e:
            logger.error(f"Error deleting documents: {e}")
            return 0

    def close(self) -> None:
        """
        Close the MongoDB connection.
        """
        if self.client:
            self.client.close()
            logger.info("MongoDB connection closed")
