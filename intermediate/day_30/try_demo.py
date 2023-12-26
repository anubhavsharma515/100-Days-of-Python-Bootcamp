
try:
    file = open("try_demo.txt")
    a_dict = {"key": "value"}
    print(f"{a_dict['foo']}")
# the argumnet after the except keyword
# is the return message of the error
except FileNotFoundError as err:
    file = open("try_demo.txt", "w")
    file.write("Something")
    print("Created new file and wrote to it.")
except KeyError as err:
    print(f"Key {err} not found.")
# try jumps here if no exceptions
else:
    content = file.read()
    print(content)
#this code runs no matter what happens
#not often used
finally:
    file.close()
    print("File was closed.")

