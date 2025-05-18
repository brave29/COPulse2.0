from datetime import datetime

print("test program2 - ", datetime.now())

with open ("databaseUsers.txt",'r') as file:
    var = file.read()
    print(var)
    file.close()
    pass