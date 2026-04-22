#Adrian Pagsuyuin
#List Activities

print("\n#Activity 1: Create a List")
my_fruits = ["Apple", "Banana", "Cherry"]
print(my_fruits)

print("\n#Activity 2: Access Items")
fruits = ["apple", "banana", "cherry"]

#print first item (index 0)
print(fruits[0])

#print last item (index -1)
print(fruits[-1])

print("\n#Activity 3: List Length")
colors = ["red", "blue", "green", "yellow"]

#use len()
print(len(colors))

print("\n#Activity 4: Change Item")
fruits = ["apple", "banana", "cherry"]

fruits[1] = "orange"
print(fruits)

print("\n#Activity 5: Add Items")
fruits = ["apple", "banana"]

#Add "mango" to the end
fruits.append("mango")

#Insert "grape" at index 1
fruits.insert(1, "grape")

print(fruits)

print("\n#Activity 6: Remove Items")
fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")  #this Removes "banana"
fruits.pop()             #and this removes the last item ("cherry")

print(fruits) #Output would be ['apple']

print("\n#Activity 7: For Loop")
animals = ["dog", "cat", "bird"]

for x in animals:
    print(x) #kapag walang indention mag eerror result siya

print("\n#Activity 8: With Index")
numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, ":", value) #kapag walang indention mag eerror result siya

print("\n#Activity 9: Check if Item Exists")
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Yes, banana is in the list") #kapag walang indention mag eerror result siya

print("\nActivity 10: Sorting")
numbers = [5, 2, 9, 1]

#Sort ascending
numbers.sort()
print("Ascending:", numbers)  #Output: [1, 2, 5, 9]

#Sort descending
numbers.sort(reverse=True)
print("Descending:", numbers) #Output: [9, 5, 2, 1]

#Activity 11: Copy List
list1 = ["a", "b", "c"]

#Creates a copy of list1 into list2
list2 = list1.copy()

print("list2:", list2) # Output: ['a', 'b', 'c']
