import mysql.connector

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",  
            user="root",  # Change if your MySQL user is different
            password="W7301@jqir#",  # Replace with your MySQL password
            database="BankerDB"
        )
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

# Test connection
if __name__ == "__main__":
    conn = connect_db()
    if conn and conn.is_connected():
        print("Connected to MySQL!")
        conn.close()