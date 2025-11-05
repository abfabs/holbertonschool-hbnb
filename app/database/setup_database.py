import mysql.connector
import os
from pathlib import Path

class DatabaseSetup:
    def __init__(self, host='localhost', user='root', password='', database='hbnb_db'):
        """Initialize database connection parameters"""
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
    
    def connect(self):
        """Connect to MySQL server"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            self.cursor = self.connection.cursor()
            print(f"✓ Connected to MySQL server")
        except mysql.connector.Error as err:
            print(f"✗ Error connecting to MySQL: {err}")
            raise
    
    def create_database(self):
        """Create the database if it doesn't exist"""
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            self.connection.commit()
            print(f"✓ Database '{self.database}' created/verified")
        except mysql.connector.Error as err:
            print(f"✗ Error creating database: {err}")
            raise
    
    def use_database(self):
        """Select the database"""
        try:
            self.cursor.execute(f"USE {self.database}")
            print(f"✓ Using database '{self.database}'")
        except mysql.connector.Error as err:
            print(f"✗ Error selecting database: {err}")
            raise
    
    def execute_sql_file(self, file_path):
        """Execute SQL commands from a file"""
        try:
            with open(file_path, 'r') as sql_file:
                sql_commands = sql_file.read()
            
            # Split by semicolon and execute each statement
            statements = sql_commands.split(';')
            for statement in statements:
                statement = statement.strip()
                if statement:
                    self.cursor.execute(statement)
            
            self.connection.commit()
            print(f"✓ Successfully executed SQL file: {file_path}")
        except Exception as err:
            print(f"✗ Error executing SQL file {file_path}: {err}")
            raise
    
    def test_crud_operations(self):
        """Test CRUD operations on the created schema"""
        print("\n--- Testing CRUD Operations ---")
        
        # READ: Verify admin user
        print("\n1. Testing READ - Admin User:")
        self.cursor.execute(
            "SELECT id, first_name, last_name, email, is_admin FROM user WHERE email = 'admin@hbnb.io'"
        )
        admin = self.cursor.fetchone()
        if admin:
            print(f"  ✓ Admin user found: {admin}")
        else:
            print(f"  ✗ Admin user not found")
        
        # READ: Verify amenities
        print("\n2. Testing READ - Amenities:")
        self.cursor.execute("SELECT id, name FROM amenity")
        amenities = self.cursor.fetchall()
        print(f"  ✓ Found {len(amenities)} amenities:")
        for amenity in amenities:
            print(f"    - {amenity[1]} (ID: {amenity[0]})")
        
        # CREATE: Insert a test user
        print("\n3. Testing CREATE - Insert Test User:")
        import uuid
        test_user_id = str(uuid.uuid4())
        try:
            self.cursor.execute(
                "INSERT INTO user (id, first_name, last_name, email, password, is_admin) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (test_user_id, 'Test', 'User', 'test@example.com', 'hashedpassword', False)
            )
            self.connection.commit()
            print(f"  ✓ Test user created successfully")
        except Exception as err:
            print(f"  ✗ Error creating test user: {err}")
        
        # UPDATE: Update test user
        print("\n4. Testing UPDATE - Update Test User:")
        try:
            self.cursor.execute(
                "UPDATE user SET first_name = %s WHERE id = %s",
                ('UpdatedTest', test_user_id)
            )
            self.connection.commit()
            print(f"  ✓ Test user updated successfully")
        except Exception as err:
            print(f"  ✗ Error updating test user: {err}")
        
        # DELETE: Delete test user
        print("\n5. Testing DELETE - Delete Test User:")
        try:
            self.cursor.execute("DELETE FROM user WHERE id = %s", (test_user_id,))
            self.connection.commit()
            print(f"  ✓ Test user deleted successfully")
        except Exception as err:
            print(f"  ✗ Error deleting test user: {err}")
        
        # Verify constraints
        print("\n6. Testing Constraints:")
        
        # Test unique email constraint
        print("  - Testing UNIQUE email constraint...")
        try:
            self.cursor.execute(
                "INSERT INTO user (id, first_name, last_name, email, password, is_admin) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (str(uuid.uuid4()), 'Duplicate', 'Email', 'admin@hbnb.io', 'password', False)
            )
            self.connection.commit()
            print(f"    ✗ Constraint violation not caught!")
        except mysql.connector.Error:
            print(f"    ✓ UNIQUE constraint working (duplicate email rejected)")
    
    def display_table_structure(self):
        """Display the structure of all tables"""
        print("\n--- Database Schema Structure ---\n")
        
        tables = ['user', 'place', 'amenity', 'review', 'place_amenity']
        
        for table in tables:
            print(f"Table: {table}")
            print("-" * 60)
            self.cursor.execute(f"DESCRIBE {table}")
            columns = self.cursor.fetchall()
            for col in columns:
                print(f"  {col[0]:20} | {col[1]:30} | {col[2]}")
            print()
    
    def close(self):
        """Close database connection"""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("✓ Database connection closed")

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    
    # Initialize database setup
    db_setup = DatabaseSetup(
        host='localhost',
        user='root',
        password='root',
        database='hbnb_db'
    )
    
    try:
        # Connect and create database
        db_setup.connect()
        db_setup.create_database()
        db_setup.use_database()
        
        # Execute schema and initial data scripts
        schema_file = script_dir / 'schema.sql'
        initial_data_file = script_dir / 'initial_data.sql'
        
        if schema_file.exists():
            db_setup.execute_sql_file(str(schema_file))
        else:
            print(f"✗ Schema file not found: {schema_file}")
        
        if initial_data_file.exists():
            db_setup.execute_sql_file(str(initial_data_file))
        else:
            print(f"✗ Initial data file not found: {initial_data_file}")
        
        # Display table structure
        db_setup.display_table_structure()
        
        # Test CRUD operations
        db_setup.test_crud_operations()
        
    except Exception as err:
        print(f"Setup failed: {err}")
    finally:
        db_setup.close()

if __name__ == "__main__":
    main()
