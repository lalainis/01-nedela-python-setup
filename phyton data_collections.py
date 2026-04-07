
numbers = [3, 7, 12, 25, 42, 56, 89]

# Pretty print the list
print("List:")
for n in numbers:
    print(n, end=" ")
print()  # Newline

# Calculate sum and average
sum_for = 0
count = 0
for num in numbers:
    sum_for += num
    count += 1
print("Summa:", sum_for)
if count > 0:
    average_for = sum_for / count
    print("Avarage:", average_for)
else:
    print("Avarage: Cannot calculate average of an empty list.")

# Print first 3 and last 3 elements
print("First 3 elements from the list:", numbers[:3])
print("Last 3 elements from the list:", numbers[-3:])

numbers.append(100)
print("List after adding a new element:", numbers)

numbers.remove(25)
print("List after deleting an element:", numbers)

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

pairs = []
for num in [3, 7, 12, 25, 42, 56, 89]:
    if num % 2 == 0:
        pairs.append(num)
print("Even (pair) numbers in the original list:", pairs)

original_numbers = [3, 7, 12, 25, 42, 56, 89]
first_three = original_numbers[:3]
last_two = original_numbers[-2:]
print("First 3 elements:", first_three)
print("Last 2 elements:", last_two)

second_numbers = original_numbers[1::2]
print("Each second number of the original list:", second_numbers)

vocabulary = {
  	"Anna": 90,
	"Janis": 70,
	"Liga": 100,
	"Andris": 80,
	"Zane": 95,
	"Marta": 85,
	"Pēteris": 85,
	"Ilze": 75,
	"Dainis": 65,
	"Laura": 92,
	"Juris": 88,
}
print("Vocabulary with names and grades:", vocabulary)

for name, grade in vocabulary.items():
    print(f"{name}: {grade}")

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
