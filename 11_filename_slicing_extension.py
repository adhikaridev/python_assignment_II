# 11. Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?

filename = input("Enter a filename with three-letter extension: ")
extension = filename[-3:]
print("Extension: ", extension)
print("File name without extension: ", filename[:-4])
# The code works on filenames of arbitrary length and three-letter extension
