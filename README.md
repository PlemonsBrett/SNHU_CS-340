# Animal Shelter Database CRUD Module

## Project Overview

This project implements a Python module that provides CRUD (Create, Read, Update, Delete) functionality for an animal shelter database. The module is designed to serve as middleware between MongoDB and client applications, offering reusable code that manages animal records in a standardized and efficient manner.

## Purpose

The development of this CRUD module serves several important purposes:

1. To create a reusable library of code that acts as middleware between the database server and client applications
2. To provide standardized methods for interacting with the animal shelter database following industry best practices
3. To enable flexible data management that can potentially support multiple applications accessing the same database
4. To establish a foundation for future development
5. To enhance code maintainability and testing efficiency through modular, well-documented components

As the course materials emphasize, reusable code has numerous advantages in modern development environments. Organizations often need a database to serve multiple applications, and a well-designed middleware layer makes this possible while also allowing for potential future transitions to different database implementations.

## MongoDB Driver Selection

This project uses **PyMongo**, the official MongoDB driver for Python. PyMongo was chosen for several reasons:

1. **Comprehensive API**: PyMongo provides a complete set of tools for interacting with MongoDB
2. **Official Support**: As the official driver, it's regularly updated and maintained by MongoDB
3. **Performance**: It offers optimized performance for database operations
4. **Clear Documentation**: Extensive documentation makes implementation straightforward
5. **Industry Standard**: It's widely used in production environments, making the code more maintainable

## CRUD Operations

The AnimalShelter class provides four primary methods for interacting with the database:

### Create
- **Function**: `create(data)`
- **Purpose**: Inserts a new document into the specified MongoDB collection
- **Parameters**: Dictionary containing the animal data to insert
- **Returns**: Boolean indicating whether the insertion was successful
- **Usage Example**:
  ```python
  shelter.create({"animal_id": "A123456", "name": "Buddy", "animal_type": "Dog"})
  ```

### Read
- **Function**: `read(query)`
- **Purpose**: Retrieves documents from the collection based on query criteria
- **Parameters**: Dictionary containing the MongoDB query parameters
- **Returns**: List of documents matching the query criteria
- **Usage Example**:
  ```python
  results = shelter.read({"animal_type": "Dog", "breed": "Labrador"})
  ```

### Update
- **Function**: `update(query, update_data, multi=False)`
- **Purpose**: Modifies existing documents in the collection
- **Parameters**: 
  - `query`: Dictionary containing selection criteria
  - `update_data`: Dictionary containing update operations
  - `multi`: Boolean indicating whether to update multiple documents (default: False)
- **Returns**: Number of documents modified
- **Usage Example**:
  ```python
  count = shelter.update({"animal_id": "A123456"}, {"$set": {"name": "Max"}})
  ```

### Delete
- **Function**: `delete(query, multi=False)`
- **Purpose**: Removes documents from the collection
- **Parameters**: 
  - `query`: Dictionary containing selection criteria
  - `multi`: Boolean indicating whether to delete multiple documents (default: False)
- **Returns**: Number of documents deleted
- **Usage Example**:
  ```python
  count = shelter.delete({"animal_id": "A123456"})
  ```

## How to Use the Module

### Installation

1. Ensure you have MongoDB installed and running on your system
2. Import the Austin Animal Center Outcomes dataset into MongoDB
3. Create a user account with appropriate permissions for database access
4. Install the required Python libraries:
   ```bash
   pip install pymongo pydantic
   ```

### Basic Usage

```python
from grazioso.crud import AnimalShelter

# Create a new instance with MongoDB connection details
shelter = AnimalShelter(
    username="aacuser",
    password="password",
    host="localhost",
    port=27017,
    db_name="AAC",
    collection_name="animals"
)

# Create a new animal record
new_animal = {
    "animal_id": "A123456",
    "name": "Buddy",
    "animal_type": "Dog",
    "breed": "Labrador Retriever",
    "color": "Black"
}
success = shelter.create(new_animal)

# Read animal records
dogs = shelter.read({"animal_type": "Dog"})

# Update a record
modified_count = shelter.update(
    {"animal_id": "A123456"},
    {"$set": {"name": "Max"}}
)

# Delete a record
deleted_count = shelter.delete({"animal_id": "A123456"})

# Close the connection when done
shelter.close()
```

## Module Implementation Details

The CRUD module is implemented using object-oriented programming principles. Key features of the implementation include:

1. **Connection Management**: The module handles MongoDB connection establishment and authentication
2. **Exception Handling**: Robust error handling ensures the application can respond gracefully to failures
3. **Logging**: Comprehensive logging provides visibility into operations for debugging and monitoring
4. **Type Checking**: Strong type hints help catch errors before runtime
5. **Data Validation**: Optional integration with Pydantic models for data validation

## Data Import and Authentication Screenshots

Below are screenshots of the data import process and authentication setup. These demonstrate that the MongoDB database has been properly configured with the Austin Animal Center dataset and user authentication.

Importing the dataset using `mongoimport`

![Importing the dataset using mongoimport](images/ImportingDataSet.png)

Creating a new user

![Creating a new user](images/CreatingUser.png)

Setting Environment Variables and Connecting as New User

![Setting environment variables and connecting as the new user](images/SettingEnvironmentVariablesConnectingAsNewUser.png)

Testing New User DB Access

![Testing new user database access](images/TestingDBAccess.png)

## CRUD Functionality Demonstration

The following screenshots show the successful execution of CRUD operations using the module:

![Import module and setup test environment](images/ImportModuleAndConnectToDB.png)

![Testing Create Functionality](images/TestCreateFunctionality.png)

![Testing Read Functionality](images/TestReadFunctionality.png)

![Testing Read Multiple Functionality](images/TestReadingMultipleDocuments.png)

![Testing Update Functionality](images/TestUpdate.png)

![Testing Update Many Functionality](images/TestUpdateMany.png)

![Testing Delete and Delete Many Functionality](images/TestDeleteAndDeleteMany.png)

![Testing with invalid input](images/HandleInvalidInput.png)

![Close connection and clean up](images/CleanupAndClose.png)

## Dash User Interface

The following screenshots show the successful execution of the Dash user interface within the Jupyter Notebook:

![Header and table data](images/DashScreenshots/Table%20and%20Header.png)

![Interactive Map and Pie Chart](images/DashScreenshots/PieChartAndMap.png)

## Development and Testing

The project includes a Jupyter Notebook for testing all CRUD functionality. This notebook demonstrates:

1. Creating new animal records
2. Querying for specific animals and collections of animals
3. Updating animal records (both single and batch updates)
4. Deleting animal records (both single and batch deletions)
5. Error handling for invalid inputs

To run the tests, open the `tests/test_crud.ipynb` notebook and execute each cell sequentially.

## Contact

Your Name: Brett Plemons