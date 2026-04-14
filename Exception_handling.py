filename = input("Enter file name: ")

try:
    f = open(filename, "r")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("No permission to read file")