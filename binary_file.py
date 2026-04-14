# Step 1: Write data to binary file
file = open("sample.bin", "wb")   # wb = write binary
data = b"Hello, this is binary data.\n"
file.write(data)
file.close()

# Step 2: Read data from binary file
file = open("sample.bin", "rb")   # rb = read binary
content = file.read()
print("Reading file:")
print(content)
file.close()

# Step 3: Append data to binary file
file = open("sample.bin", "ab")   # ab = append binary
file.write(b"This is appended data.\n")
file.close()

# Step 4: Read again after appending
file = open("sample.bin", "rb")
content = file.read()
print("\nAfter appending:")
print(content)
file.close()