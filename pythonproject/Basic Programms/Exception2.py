try:
    klu1=open("file.txt","w+")
    try:
        klu1.write("xyz")
    finally:
        klu1.close()
except IOError:
    print("File not Found")
else:
    print("The file opened successfully")
    klu1.close()