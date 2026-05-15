# 1. Create a list of 5 fruits and print the list.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)


# 2. Add a new fruit to the end of the list using append().
fruits.append("fig")
print(fruits)


# 3. Insert a fruit at position 2 in your list.
fruits.insert(2, "grape")
print(fruits)


# 4. Remove the last item from the list using pop().
removed_fruit = fruits.pop()
print(fruits)


# 5. Remove a specific fruit from the list using remove().
fruits.remove("banana")
print(fruits)


# 6. Create a list of numbers and sort it in ascending order.
numbers = [42, 7, 19, 88, 3, 19]
numbers.sort()
print(numbers)


# 7. Reverse the order of a list using reverse().
numbers.reverse()
print(numbers)


# 8. Count how many times a number appears in a list using count().
nineteen_count = numbers.count(19)
print(nineteen_count)


# 9. Find the index of a specific element in a list using index().
position_of_fortytwo = numbers.index(42)
print(position_of_fortytwo)

position_of_banana = fruits.index("cherry")
print(position_of_banana)

# 10. Create two lists and combine them into one list.
animals = ["cat", "dog", "bird", "fish", "goat", "pig"]


combined_list = fruits+ animals
print(combined_list)
