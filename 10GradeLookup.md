### Problem in F17: 24.3.4) Multiple Returns, 24.3.1) Dictionaries vs. Tuples
### Problems in F18: 43.4) Multiple Returns, 43.1) Dictionaries vs. Tuples 

### Learning Objectives:
- Return multiple value from a function using a tuple
- Assign multiple variables on one line using a tuple return value
- Access the values of a dictionary in a function
- Access values in a Dictionary of Dictionaries complex data structure. 
- Concatenate string literals and string variables 

## 0) Read problem
Below is a dictionary of dictionaries representing the students in a class. The keys of the dictionary correspond to the students' pid's, while the values correspond do information about the student, such as their name, their classes, and their grades. Create a function called `get_grade` that takes a single student dictionary and returns their name and grade in CS1064 as a tuple. Call this function on one of the students and assign the result to two variables. Print those variables with "has a" in between (e.g. `"Michael has a 94"`). 

	students = { 
		"mrf7": {
			"pid": "mrf7",
			"name": "Michael",
			"year": "Senior",
			"courses": {
				"MATH1225": 85,
				"CS1064": 94,
				"GEOG1014": 100,
				"CHEM1035": 80
			}
		},
		"bob123": {
			"pid":"bob123",
			"name": "Bob",
			"year": "Sophomore",
			"courses": {
				"ACIS1504": 70,
				"APS1074": 80,
				"CS1064": 87,
				"DASC1464":90
			}
		}, 
	}
				
## 1) Interpret the problem
The first part of this problem requires us to write a function called `get_grade` that takes a dictionary representing a student and returns the student's name and grade in CS1064 as a tuple. This will require us to make a multilevel dictionary access. The second part says we need to call our function on a single student dictionary, so we will have to pull one out of the `students` dictionary using the pid. Finally we need to concatenate strings to produce the proper output. 

## 2) Understand the Data Structure
The `students` data structure is a dictionary of dictionaries. Each of the internal dictionaries represents a student and has the keys "pid", "name", "year", and "courses". The values for the pid, name, and year keys are string and the value for the courses key is another dictionary.   

The dictionary corresponding to the courses key uses the course name as the keys and the grade as the values. 

## 3) Create function header
Our function needs to be called `get_grade` and take a single parameter holding a student dictionary. So a reasonable parameter name could simply be `student`. 

	def get_grade(student): 
		...
		
## 4) Get a value from a dictionary
The name of the student is stored in the student dictionary under the `"name"` key. To retrieve it all we have to do is perform a simple dictionary access and store the result in a variable. 

	name = student["name"]

## 5) Get a value from a dictionary within a dictionary
The next piece of information we need is the student's grade in CS1064. To obtain this we first need to get the dictionary of courses from the student dictionary 
	
	student["courses"]
From the dictionary of courses, we need to get the value for the key "CS1064" and save it in a variable.

	grade = student["courses"]["CS1064"]

## 6) Return a tuple
Now that we have to two pieces of information that we need, we need to return both values. This can be done by returning a tuple. With a tuple we can return multiple values that can be stored in multiple variables when our function is called. To create a tuple, we simply put write our values separated by a comma, likes this:

	return name, grade
	
## 8) Store multiple return values
When we call our function, we need to give it a dictionary representing a student. We can get this by doing a dictionary access on the `students` dictionary. Let's use Bob in our test.

	get_grade(students["bob123"])

The problem says that we should store the two return values from our function in two separate variables. We do this the same was as we create a tuple, simply separating our variables by commas. 

	name, grade = get_grade(students["bob123"])
This will store the first value returned by our function in name, and the second value in grade. 

## 9) Concatenate the string 
This problem requires us to print messages of the form `"[Name] has a [Grade]"`. Since we already have name and grade, we can simply concatenate the strings using the `+` operator. However, since grade is a number and not a string, we need to use `str` to convert it to a string. 

	name + " has a " + str(grade)
To see if our function produced the right output, we print the result

	print(name + " has a " + str(grade))

## Solution

	def get_grade(student): 
		name = student["name"]
		grade = student["courses"]["CS1064"]
		return name, grade
		
	students = { 
		"mrf7": {
			"pid": "mrf7",
			"name": "Michael",
			"year": "Senior",
			"courses": {
				"MATH1225": 85,
				"CS1064": 94,
				"GEOG1014": 100,
				"CHEM1035": 80
			}
		},
		"bob123": {
			"pid":"bob123",
			"name": "Bob",
			"year": "Sophomore",
			"courses": {
				"ACIS1504": 70,
				"APS1074": 80,
				"CS1064": 87,
				"DASC1464":90
			}
		}, 
	}
	name, grade = get_grade(students["bob123"])
	print(name + " has a " + str(grade))
