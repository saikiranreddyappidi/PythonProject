# Import the required modules
import mysql.connector
import base64
import io

# For security reasons, never expose your password

# Create a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="database@9440672439",
    database="regist"
)

# Create a cursor object
cursor = mydb.cursor()

# Open a file in binary mode
file = open('icon.png','rb').read()

# We must encode the file to get base64 string
file = base64.b64encode(file)

# Sample data to be inserted
args = ('icon', file)

# Prepare a query
query = 'INSERT INTO files(file_name,document) VALUES(%s, %s)'

# Execute the query and commit the database.
cursor.execute(query,args)
mydb.commit()
