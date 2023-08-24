# Import the required modules
from tkinter import Image
import mysql.connector
import base64
import io
from PIL import Image
# For security reasons, never expose your password

# Create a connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="database@9440672439",
    database="regist"
)

cursor = mydb.cursor()
  
# Prepare the query
query = 'SELECT * FROM files'
  
# Execute the query to get the file
cursor.execute(query)
  
data = cursor.fetchall()

#print(data[0][2])
  
# The returned data will be a list of list
image = data[0][2]
  
# Decode the string
binary_data = base64.b64decode(image)
  
# Convert the bytes into a PIL image
image = Image.open(io.BytesIO(binary_data))
  
# Display the image
image.show()
