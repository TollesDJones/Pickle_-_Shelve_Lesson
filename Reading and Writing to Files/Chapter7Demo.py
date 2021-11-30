
# Reading form text files
# Opening & Closing Files

"""


"""
# open(File name, Access mode) function receives 2 parameters:
print("Opening and closing the file.")
text_file = open("read_it.txt", "r")
text_file.close()

"""
Text File Access Modes

    Read Only (‘r’) : 
    Open text file for reading. The handle is positioned at the beginning of the file.
    If the file does not exists, raises I/O error. This is also the default mode in which file is opened.
    
    Read and Write (‘r+’) : 
    Open the file for reading and writing. The handle is positioned
    at the beginning of the file. Raises I/O error if the file does not exists.
    
    Write Only (‘w’) : 
    Open the file for writing. For existing file, the data is truncated and over-written.
    The handle is positioned at the beginning of the file. Creates the file if the file does not exists.
    
    Write and Read (‘w+’) :
    Open the file for reading and writing. For existing file,
    data is truncated and over-written. The handle is positioned at the beginning of the file.
    
    Append Only (‘a’) : 
    Open the file for writing. The file is created if it does not exist. 
    The handle is positioned at the end of the file. The data being written will be inserted
    at the end, after the existing data.
    
    Append and Read (‘a+’) : 
    Open the file for reading and writing.
    The file is created if it does not exist. The handle is positioned at the end of the file.
    The data being written will be inserted at the end, after the existing data.
"""


