# Example: Creating a list with more than 5 numbers
numbers = [3, 7, 12, 25, 42, 56, 89]
print("List with more than 5 numbers:", numbers)

# Add a new element to the list
numbers.append(100)
print("List after adding a new element:", numbers)

# Delete an element from the list (for example, remove 25)
numbers.remove(25)
print("List after deleting an element:", numbers)

# Calculate the sum and average of the list using a for loop (without sum() or len())
sum_for = 0
count = 0
for num in numbers:
	sum_for += num
	count += 1
print("Sum of the list (for loop):", sum_for)

if count > 0:
	average_for = sum_for / count
	print("Average value of the list (for loop):", average_for)
else:
	print("Cannot calculate average of an empty list.")
