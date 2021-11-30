# Read It
# Demonstrates reading from a text file
import sys

print("Opening and closing the file.")
text_file = open("read_it.txt", "r")  # Requires two arguments (file, access mode)
text_file.close()  # Always close the file after you are done

# print("\nReading CHARACTERS from the file.")
# text_file = open("read_it.txt", "r")
# print(text_file.read(1))  # Passing an argument sets the number of characters to read
# print(text_file.read(5))  # Notice where this call started
# text_file.close()

# print("\nReading the ENTIRE file at once.")
# text_file = open("read_it.txt", "r")
# whole_thing = text_file.read()
# print(whole_thing)
# text_file.close()
#
# print("\nReading CHARACTERS from a LINE.")
# text_file = open("read_it.txt", "r")
# print(text_file.readline(1))
# print(text_file.readline(5))  # Again note where the cursor is...
# text_file.close()
#
# print("\nReading ONE LINE at a time.")
# text_file = open("read_it.txt", "r")
# print(text_file.readline())
# print(text_file.readline())  # Note the cursor position
# print(text_file.readline())
# text_file.close()
#
# print("\nReading the ENTIRE FILE into a list.")
# text_file = open("read_it.txt", "r")
# lines = text_file.readlines()  # 'lines' is a list and supports list operations
# print(lines)
# print(len(lines))
# for line in lines:
#     print(line)
# text_file.close()
#
# print("\nLooping through the file, line by line.")
# text_file = open("read_it.txt", "r")
# for line in text_file:
#     print(line)
# text_file.close()
#
# input("\n\nPress the enter key to exit.")
