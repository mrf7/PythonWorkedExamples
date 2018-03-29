### Problem in F17: 26.5.5) Fix Names
### Problems in F18:  45.5) Fix Names

### Learning Objectives:
- Properly open and close a file
- Process multiline file
- Iterate over the lines of a file

## 0) Read Problem
You have a file called `grades.txt` (shown below) that contains every student's grade on a recent test, along with their name. To see if you need to apply a curve, you need to know the average grade for all the students. Find the average grade and print it. 

**Link to grade.txt**

## 1) Interpret the Problem
This problem requires us to get the grades students scored from `grades.txt` and calculate the average. First, we need to see what `grades.txt` looks like. After opening `grades.txt`, we see it has a student's name and grade on each line. The name and grade are separated by a colon (':'). Generally, the file looks something like this:

	Michael:90
	Steven:70
	Logan:67
	...
Since each line holds information for exactly one student, we need to look at each line. We can do this with a `for` loop.
Once we get the individual lines, we see the name and grade are separated by a colon. To get the grade, we can use the string method `split()`.

To determine the average, we can use the Sum and Count patterns. We will find the sum of all of the grade then divide the sum by the number of grades in the file. 

## 2) Setting up Sum and Count Variables
For the Sum and Count pattern, we need to create the variables storing the sum and count before our loop begins.

	sum = 0
	count = 0
## 3) Opening a File
Working with files in python is just like working with files normally, we first have to open the file. To open a file in python, we use the open() function. This function takes the name of the file as a string and returns a file object representing the open file. We need to save this file so we can close it later:

	gradesFile = open('grades.txt')
	
## 4) Iterate Over Lines in a File
To look at each line of a file, we can iterate over a file object, which is the return value of the `open()` function. 

	for line in gradeFile:
		...
This for loop will iterate over the file, line by line. 

## 5) Extract from the String
Now that we have a line of the file, we need to get the grade. Since the student's name and grade are separated by a colon, we can use the `split()` method to separate them. The split method takes the character that separates the different parts of the string and returns a list of each of those part. So if `line` was `"Michael:90", 

	line.split(":")
returns the list `["Michael":"90"]`. To get the grade from this list, we can use the index 1

	line.split(":")[1]
Notice that the second item in the list is `"90"`, which has quotation marks. This means it is a string, which makes sense because it was originally part of a string. To convert this string to a number, we can use the `int()` function, which takes a string and parse an integer out of it. 

	grade = int(line.split(":")[1])
	
## 6) Update the Sum
Now that we have the grade as an int, we can add it to our running sum

	sum = sum + grade
## 7) Increment the Count
Every time we add a grade to the sum, we need to increase our count by one 

	count = count + 1
## 8) Close the File
Once our `for` loop finishes, we are finished with `grades.txt`, so we should close it. This is done with the `close` method. 

	gradeFile.close()

## 9) Calculate the Average
Once we've determined the sum and count of all the grades in the file, we can calculate the average using by dividing the sum by the count.

	average = sum/count

## 10) Print the Result
Now that we've determined the average, we can print it so we know if the test should be curved.

	print(average)
	
## Solution)
	sum = 0
	count = 0
	gradesFile = open('grades.txt')
	for line in gradeFile:
		grade = int(line.split(":")[1])
		sum = sum + grade
		count = count + 1
	gradeFile.close()
	average = sum/count
	print(average)
