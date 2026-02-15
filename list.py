#Create and access list elements
print("1.1 Create and Access List Elements")
my_list = [10, 20, 30, 40, 50]
print("Created List:", my_list)
print("Access Element at Index 2:", my_list[2])


#Add and Remove list elements
print("\n1.2 Add and Remove List Elements")
my_list.append(60)
print("List After Adding 60:", my_list)

my_list.insert(2, 25)
print("List After Inserting 25 at Index 2:", my_list)

my_list.remove(30)
print("List After Removing 30:", my_list)

popped_element = my_list.pop()
print("Popped Element:", popped_element)
print("List After Popping Last Element:", my_list)


#Sort list elements
print("\n1.3 Sort List Elements")
my_list.sort()
print("List After Sorting in Ascending Order:", my_list)

my_list.sort(reverse=True)
print("List After Sorting in Descending Order:", my_list)


#Reverse list elements
print("\n1.4 Reverse List Elements")
my_list.reverse()
print("List After Reversing:", my_list)