### Problem in F17: 26.5.4) Plus or Minus
### Problem in S18: 45.4) Plus or Minus 

## Learning Objectives
- Properly open and close a file
- Read the contents of a text file
- Iterate over the characters in a file 
- Implement the count loop pattern

## 0) Read Problem
You want to see how random a coin flip really is. To test this, you flip a coin until your hand gets tired. To record the results, you have a text document open and every time you flip you type either H or T, for heads or tails. After you spend all day flipping a coin, you realize you don't want to count all the H's and T's to check if they are equal as expected. You save your file as `coin.txt` and decide to let python do the work for you. 

Count the number of all H's and T's in the file `coin.txt`. To determine the probability, you will also need to know the total number of tosses you made since you lost count in the 200's. After counting the number of heads, tails, and tosses, print the probability of heads and the probability of tails. Probability of heads is simply the number of heads divided by the total number of tosses and you can do the same for tails. 

*LINK TO COIN.TXT*

## 1) Interpret the Problem
For this problem we can use the count and filter loop patterns to count the number of H's and T's.
	
The first thing we should do is open `coin.txt` so we understand the format of the file. When we do this we see the file is entirely on one line. The contents of the file look something like this 
	
	
	HHTHHTTTHHTTHTHTTHHHHTHTTT...
Since the file is only one line, we need to look at each character in the file, not each line. This means instead of just iterating over the result of the call to `open()`, we should use `read()` to read all the text in the file and get it as a string. Then we can iterate over the string to check every character of the text. 

## 2) Opening a File
Working with files in python is just like working with files normally, we first have to open the file. To open a file in python, we use the `open()` function. This function takes the name of the file as a string and returns a file object representing the open file. We need to save this file so we can close it later:

	coinFile = open('coin.txt')
## 3) Read the File
If we were to iterate over `coinFile` with `for flip in coinFile`, we would iterate over every line in the file. Since `coin.txt` is a single, massive line and we want every character of it, this doesn't work. To iterate over each character, we need the contents of  the file as a string. To get the file as a string, we use the `read()` function. The read function takes an open file object and returns a string of all the contents of that file. We save the result in a string variable which is what we will use in our for loop. 

	coinString = coinFile.read()
## 4) Closing the File
Now that we've read the contents of the file into a string, we don't need to have the file open anymore. You should always close a file once you are done with it. This is done with the `close()` method. Keep in mind that after closing a file, the file is not usable so make sure you close your files only after you are done using them

	coinFile.close()

	
## 5) Iterate Over Character's in a File
Now that we have the contents of the file in a string, we can use a for loop to iterate over each character in the file. 

	for flip in coinString:
		...
## 6) Initializing Count Variables
Before we start our loop, we want to set up our variables for everything we need to count. We need to keep track of the number of heads, the number of tails, and the total number of flips. These variables should be created before our loop.

	numHeads = 0
	numTails = 0 
	numFlips = 0
	for flip in coinString:
		...
## 7) Implement Count Pattern
In our loop, we need to count the flips. Let's start with the easiest count to do: numFlips. Since every character is a flip, we should increment numFlips every time our loop runs. 

	for flip in coinString:
		numFlips = numFlips + 1

## 8) Implement the Filter Pattern
Finding the number of heads and number of tails is a bit trickier. We should increment `numHeads` only if flip is `"H"` and numTails only if flip is `"T"`. This can be done with a simple if statement.

	if flip == "H":
		numHeads = numHeads + 1
	elif flip == "T":
		numTails = numTails + 1
		
## 9) Calculating Probability
To calculate the probability of heads and tails, we have to divide numHeads and numTails by numFlips. This will give us a number between 0 and 1 that represents the probability a coin flip is heads or tails, respectively.

	probHeads = numHeads / numFlips
	probTails = numTails / numFlips
If we have a perfectly fair coin, the probability should be .5 for both, meaning the coin has an equal chance of flipping heads and tails. Since this is the real world, we'll probably get numbers that are slightly off. 

## 10) Printing Results
Now the only thing left to do is print the probabilities we calculated to see how close to perfectly random our coin tosses were. Since probHeads and probTails are floats, we need to convert them to string using the `str()` method. 

	print("Heads: " + str(probHeads))
	print("Tails: " + str(probTails))

## Solution
	coinFile = open("coin.txt")
	coinString = coinFile.read()
	coinFile.close()

	numHeads = 0 
	numTails = 0
	numFlips = 0
	for flip in coinString: 
		numFlips = numFlips + 1
		if flip == "H":
			numHeads = numHeads + 1
		elif flip == "T":
			numTails = numTails + 1
	
	probHeads = numHeads / numFlips
	probTails = numTails / numFlips
	print("Heads: " + str(probHeads))
	print("Tails: " + str(probTails))

When we run this with the file above, the output we get is 

	Heads: 0.5202020202020202
	Tails: 0.4797979797979798
Which means about 52% of the flips were heads and 48% were tails. 
