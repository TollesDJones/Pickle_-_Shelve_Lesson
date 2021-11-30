import pickle

"""
Python pickle module is used for serializing and de-serializing python object structures. 
The process to converts any kind of python objects (list, dict, etc.) into byte streams (0s and 1s) 
is called pickling or serialization or flattening or marshalling. We can converts the byte stream 
(generated through pickling) back into python objects by a process called as unpickling.

Why Pickle?: In real world scenario, the use pickling and unpickling are widespread
as they allow us to easily transfer data from one server/system to another and then
store it in a file or database.
"""

# Original List
mylist = ['a', 'b', 'c', 'd']

# Opening the file in Binary mode (wb) a new file named “datafile.txt” is created
with open('datafile.txt', 'wb') as f:
    pickle.dump(mylist, f)

# Unpickle the datafile
f = open ("datafile.txt", "rb")
pickled_content = pickle.load(f)
print(pickled_content)

