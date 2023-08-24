from statistics import mean, stdev

import numpy
import pandas


def add_student(studentMarks):
	return numpy.append(studentMarks, numpy.random.randint(10, 15, (1, 4)), axis=0)


arr = numpy.random.randint(15, 25, (3, 4))
flag = True
while flag:
	results = [[], [], [], []]
	stud = ["student1", "student2", "student3", "student4"]
	Exam = ["Exam1", "Exam2", "Exam3"]
	for i in arr:
		results[0].append(min(i))
		results[1].append(max(i))
		results[2].append(mean(i))
		results[3].append(stdev(i))
	# print(results)
	student_individual = arr.transpose()
	student_total = []
	for i in student_individual:
		student_total.append(sum(i))
	print(student_total)
	df = pandas.DataFrame(
		{"Student Name": stud, "Exam1": arr[0], "Exam2": arr[1], "Exam3": arr[2], "Sum": student_total})
	print(df)
	# print(results)
	result_df = pandas.DataFrame({"Exam": Exam,
	                              "Minimum": results[0],
	                              "Maximum": results[1],
	                              "Average": results[2],
	                              "Standard Deviation": results[3]
	                              })
	print(result_df)
	while True:
		print("0.Exit", "1.Add student", sep="\n")
		# try:
		choice = 1  # int(input("Enter your choice: "))
		if choice == 0:
			exit(0)
		elif choice == 1:
			print(arr, stud)
			arr = numpy.append(arr, numpy.random.randint(10, 15, (3, 1)), axis=1)
			stud.append("student" + str(len(stud) + 1))
			print(arr, stud)
			break
		else:
			print("Enter the choice from the given options")
		# except:
			print("Enter a valid choice")
