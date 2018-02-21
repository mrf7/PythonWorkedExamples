### Problem in F17: #16.5.3) Drinking Function, other if problems
### Problems in F18: #27) If statements 

## Learning Objectives:
- Define/Call a function
- Define/Call a function with multiple parameters of varied types
- Express logic structure as if statement
- Using boolean operators

## Problem: Create a function called `weekend_plan` that takes 2 paramaters. The first parameter should be a boolean that is true if you have homework due on monday and false otherwise, and an integer the represents your age. The function should capture the following logic

    If you have homework due,
        print "Do your homework!"
    If you don't have homework due and you are over 21,
        print "Tots happy hour!"
    If you don't have homework, but you are under 21,
        print "Play video games!"
        
You should call your function with your own values to test it. 

## Step 0: Understanding the problem: 
We need to create a function that takes two parameters, a boolean and an integer, and uses those values to dermine and print what we should do this weekend. This can be done using an if statement.

## Step 1: Creating the function header:
We need to create a function named `weekend_plan` that takes two parameters, a boolean that is true if you have homework and an integer representing your age. Since this function will be tested directly by unit tests, we need to make sure the order of the parameters is exactly as stated in the problem. Even though the functions have different types, Python will give values to parameters in the order they are given. If one call to your function expects the parameters to be in a different order than they are, you can have strange, sometimes hard to find bugs in your code. (For example, notice if you type print(True > 21) in python there is no error). With that in mind, our function header looks like:
    
    `def weekend_plan(has_homework, age): 

## Step 2: Creating the if statement: 
Now that we have our function header and the parameters `has_homwork` and `age`, we can create an if statement that captures the logic above. There are a lot of ways to construct this if statement that would work, but we want to find the way that requires writing the least amount of code. Notice that the second to results (Tots happy hour and Play video games) both need has_homework from the first part to be false. So if we put them into an else if, abbreviated `elif`, after checking `has_homework`, we only need to check it twice. 

    if has_homework:
        print("Do your homework!")
    elif ???   # Else if for tots    
    elif ???   # Else if for video games
    
Now we know the first else if will only be checked if `has_homework` is false, so we can simply check if you are at least 21 using the `>=` operator. 

    if has_homework:
        print("Do your homework!")
    elif age >= 21:
        print("Tots happy hour!)
    elif ???   # Else if for video games    
The final part of the if statement will only be checked if the first two failed, meaning `has_homework` and `age >= 21` are both false. Since that is the exact condition we need to print "Play video games", we don't need to check anything at all. Code under the `else` keyword only execute if everything else in the if statement was false. 

        if has_homework:
        print("Do your homework!")
    elif age >= 21:
        print("Tots happy hour!)
    else:
        print("Play video games!)
        
Step 2.5: Alternative if statements: 

 
