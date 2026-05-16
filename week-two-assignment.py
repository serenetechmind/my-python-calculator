# 1. Create a list of 5 fruits and print only the ones that are NOT 'Apple'.
fruits = ["Apple", "Banana", "Cherry", "Mango", "Pear"]
for fruit in fruits:
    if fruit != "Apple":
        print(fruit)


# 2. Loop through a list of drinks and print 'I love this drink!' when the item is 'Juice'.
drinks = ["Water", "Soda", "Juice", "Coffee", "Tea"]
for drink in drinks:
    if drink == "Juice":
        print("I love this drink!")


# 3. Create a string with your favorite word and print each letter on a new line.
word = "operation"
for letter in word:
    print(letter)


# 4. Modify your loop so that it skips printing the letter 'e'.
for letter in word:
    if letter == "e":
        continue
    print(letter)


# 5. Write a loop that prints numbers from 5 to 15.
for num in range(5, 16):
    print(num)


# 6. Print only numbers divisible by 3 between 1 and 30.
for num in range(1, 31):
    if num % 3 == 0:
        print(num)


# 7. Create a list of names and print only names longer than 4 characters.
names = ["Ali", "Bob", "Charlie", "David", "Grace"]
for name in names:
    if len(name) > 4:
        print(name)


# 8. Loop through a word and count how many times the letter 'o' appears.
counter = 0
for letter in word:
    if letter == "o":
        counter = counter + 1
print(f"The letter 'o' appears {counter} times in '{word}'.")


# 9. Write a loop that prints numbers from 10 down to 1.
for num in range(10, 0, -1):
    print(num)


# 10. Create a list of 5 items and stop the loop completely when you reach the third item.
for i in range(len(drinks)):
    print(drinks[i])
    if i == 2: 
        break  
