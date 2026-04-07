
numbers = [3, 7, 12,16, 25, 42, 56, 66, 77, 89]

# Pretty print the list
print("\n============================")
print("   Saraksts ar skaitļiem")
print("============================")
#print(f"Saraksts: {numbers}")

sum_for = 0
count = 0
for num in numbers:
	sum_for += num
	count += 1

if count > 0:
	average_for = sum_for / count
else:
	print("Nevar aprēķināt vidējo vērtību tukšam sarakstam.")
print(f"Summa: {sum_for} | Vidējā vērtība: {average_for:.2f}")

sum_for = 0
pairs = []
for num in numbers:
	if num % 2 == 0:
		pairs.append(num)
print(f"Pāra skaitļi sarakstā: {pairs}")

print(f"Pirmie 3 elementi: {numbers[:3]} | Pēdējie 3 elementi: {numbers[-3:]}")

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
print("\n================================")
print(" Vārdnīca ar vārdiem un atzīmēm")
print("================================")
print(f"{'Vārds':<10} | Atzīme")
print("--------------------------------")

for name, grade in vocabulary.items():
	print(f"{name:<10} | {grade}")

max_grade = -1
max_student = None
for name, grade in vocabulary.items():
    if grade > max_grade:
        max_grade = grade
        max_student = name
if max_student is not None:
    print(f"\nStudents ar augstāko atzīmi: {max_student}, atzīme: {max_grade}")
else:
    print("\nNav atrasti studenti.")

print("\nStudenti ar atzīmi >= 80:")
count = 1
for name, grade in vocabulary.items():
    if grade >= 80:
        print(f"{count}. {name:<10} | {grade}")
        count += 1
