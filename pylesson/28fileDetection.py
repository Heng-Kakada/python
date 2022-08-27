import os


path = "/Users/hengkakada/Desktop/personal/file"


# check location exists or not

if os.path.exists(path):
    print("That location exists!")
    # check file
    if os.path.isfile(path):
        print("that is a file")
    # check folder
    if os.path.isdir(path):
        print("that is a folder")
else:
    print("That location doesn't exists")
