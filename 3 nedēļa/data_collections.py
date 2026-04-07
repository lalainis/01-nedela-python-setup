# Example: Creating a list with more than 5 numbers
numbers = [3, 7, 12, 25, 42, 56, 89]
print("Saraksts ar vairāk nekā 5 skaitļiem:", numbers)

# Add a new element to the list
numbers.append(100)
print("Saraksts pēc jauna elementa pievienošanas:", numbers)

# Delete an element from the list (for example, remove 25)
numbers.remove(25)
print("Saraksts pēc elementa dzēšanas:", numbers)

# Calculate the sum and average of the list using a for loop (without sum() or len())
sum_for = 0
count = 0
for num in numbers:
	sum_for += num
	count += 1
print("Saraksta summa (for cikls):", sum_for)

if count > 0:
	average_for = sum_for / count
	print("Vidējā vērtība sarakstā (for cikls):", average_for)
else:
	print("Nevar aprēķināt vidējo vērtību tukšam sarakstam.")

# Filter and print only the even (pair) numbers from the original list
pairs = []
for num in [3, 7, 12, 25, 42, 56, 89]:
    if num % 2 == 0:
        pairs.append(num)
print("Pāru (even) skaitļi sākotnējā sarakstā:", pairs)

# Slicing: first 3 and last 2 elements from the original list
original_numbers = [3, 7, 12, 25, 42, 56, 89]
first_three = original_numbers[:3]
last_two = original_numbers[-2:]
print("Pirmie 3 elementi:", first_three)
print("Pēdējie 2 elementi:", last_two)

# Print each second number from the original list
second_numbers = original_numbers[1::2]
print("Katrs otrais numurs no sākotnējā saraksta:", second_numbers)

#B daļa — Vārdnīcas

# Vocabulary with 3 names and grades
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
print("Bibliotēka ar vārdiem un atzīmēm:", vocabulary)

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
	print(f"Students ar augstāko atzīmi: {max_student} ({max_grade})")
else:
	print("Nav atrasts neviens students.")
	
	#C daļas uzdevums