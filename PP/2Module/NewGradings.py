from statistics import mean, stdev

import numpy
import pandas

menu = '''0.Exit\n1.Get marks(Individual student with sum)\n2.Get marks(Individual Exam)
3.Add student\n4.Get Grade Sheet\n5.Summary statistics '''


def getinput():
	try:
		choice = int(input("Enter your choice"))
		if choice <= 5:
			return choice
		else:
			raise ValueError
	except:
		print("Enter a valid choice.Integer format(0,1,2,..,5)")
		getinput()


def main(arr):
	print(menu)
	choice = getinput()
	student = ["student" + str(i) for i in range(int(arr.size / arr[0].size))]
	if choice == 0:
		exit(2)
	elif choice == 1:
		gradesheet = {"Student Name": student}
		exam = ["Exam" + str(i) for i in range(3)]
		exam_wise = arr.transpose()
		for i, j in zip(exam, exam_wise):
			gradesheet.update({i: j})
		result_sum = []
		for i in arr:
			result_sum.append(sum(i))
		gradesheet.update({"Sum": result_sum})
		print(pandas.DataFrame(gradesheet))
	elif choice == 2:
		exam = ["Exam" + str(i) for i in range(3)]
		examname = numpy.append(numpy.array(exam).reshape(3, 1), arr.transpose(), axis=1)
		print(pandas.DataFrame(examname))
	elif choice == 3:
		arr = numpy.append(arr, numpy.random.randint(0, 10, (1, 3)), axis=0)
		print("Added student marks: ", arr[-1])
	elif choice == 4:
		print("Grade sheet: ")
		gradesheet = {"Student Name": student}
		exam = ["Exam" + str(i) for i in range(3)]
		exam_wise = arr.transpose()
		for i, j in zip(exam, exam_wise):
			gradesheet.update({i: j})
		print(pandas.DataFrame(gradesheet))
	else:
		print("Summary statistics for each exam: ")
		results = [[], [], [], []]
		for i in arr.transpose():
			results[0].append(min(i))
			results[1].append(max(i))
			results[2].append(mean(i))
			results[3].append(stdev(i))
		exam = ["Exam" + str(i) for i in range(3)]
		df = {"Exam Name": exam,
		      "Minimum": results[0],
		      "Maximum": results[1],
		      "Mean": results[2],
		      "Standard Deviation": results[3]}
		print(pandas.DataFrame(df))
	main(arr)


if __name__ == '__main__':
	arr = numpy.random.randint(15, 25, (4, 3))
	main(arr)
