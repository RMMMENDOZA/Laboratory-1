file = input("Enter the file name: ")
text_file = open(file, "r")
lines = text_file.readlines()
print (len(lines))
while True:
    linenumber = int(input("Please enter a line number or press 0 to quit:  "))
    if linenumber == 0:
        print("Closing the program")
        break
    elif 1 <= linenumber <= len(lines) :
      print (lines[linenumber- 1])
    else:
        print("Please enter valid line number")
text_file.close()
