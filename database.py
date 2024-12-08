import sqlite3

def create_database(db_name):
    try:
        # Connect to SQLite database or create it if it doesn't exist
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # Create table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                image BLOB NOT NULL,
                result TEXT NOT NULL
            );
        ''')

        # Commit changes and close connection
        conn.commit()
        conn.close()
        print("Database created successfully!")
    except sqlite3.Error as e:
        print("Error:", e)

# Replace 'your_database_name.db' with your desired database name
create_database('your_database_name.db')
