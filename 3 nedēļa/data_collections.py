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

# Filter and print only the even (pair) numbers from the original list
pairs = []
for num in [3, 7, 12, 25, 42, 56, 89]:
    if num % 2 == 0:
        pairs.append(num)
print("Even (pair) numbers in the original list:", pairs)

# Slicing: first 3 and last 2 elements from the original list
original_numbers = [3, 7, 12, 25, 42, 56, 89]
first_three = original_numbers[:3]
last_two = original_numbers[-2:]
print("First 3 elements:", first_three)
print("Last 2 elements:", last_two)

# Print each second number from the original list
second_numbers = original_numbers[1::2]
print("Each second number of the original list:", second_numbers)

#B daļa — Vārdnīcas

# Vocabulary with 3 names and grades
vocabulary = {
	"Anna": 9,
	"Janis": 7,
	"Liga": 10,
	"Andris": 8,
}
print("Vocabulary with names and grades:", vocabulary)

# Iteration with for name, grade in vocabulary.items()
for name, grade in vocabulary.items():
	print(f"{name}: {grade}")

# Find and print the student with the highest grade using a for loop
max_grade = -1
max_student = None
for name, grade in vocabulary.items():
	if grade > max_grade:
		max_grade = grade
		max_student = name
if max_student is not None:
	print(f"Student with the highest grade: {max_student} ({max_grade})")
else:
	print("No students found.")
