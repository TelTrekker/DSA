# Create a list of your favorite fruits
fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Watermelon']

# Print the entire list
print("List of Fruits:", fruits)

# Add a new fruit to the list
fruits.append('Mango')
print("After Adding Mango:", fruits)

# Remove a fruit from the list
fruits.remove('Banana')
print("After Removing Banana:", fruits)

# Check if a fruit is in the list
if 'Grapes' in fruits:
  print("Grapes are in the list!")

# Find the index of a specific fruit
index_of_orange = fruits.index('Orange')
print("Index of Orange:", index_of_orange)

# Change the value of a specific element
fruits[0] = 'Pineapple'
print("After Changing First Element to Pineapple:", fruits)
