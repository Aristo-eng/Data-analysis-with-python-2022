# Python-in-a-nutshell
## _A one go to for python summary_

A complete repository containing all necessary tools to:
● Familiarize myself with Python
● Improve my algorithms and data structure skills
● Learning has been supported by Andela Team Rwanda

Content has some:
- Python code
- HTML notes 
- ✨ Exercises and solutions  ✨

## Week One

 Basics of python, different data structures that can be used to store data. Implement different methods used to manipulate these data structures and examine their efficiency. Understand the advantages and applications of different data structures. Learn how to
 approach open ended problems and select appropriate data structures based on requirements.

### Python Fundementals 

- Flow control
- Loops
- Functions
- Data types and variables
- Manipulation & usage and operators

### Basic DS
- Tuples, Sets, Dictionaries
- Linked lists (linked list types & operations)
- Queues (queues operations & queues types)
- Hash table

## Week Two

 Learn and implement basic algorithms such as searching and sorting on different data structures and examine the efficiency of these algorithms. Use recursion to implement these algorithms. Learn advanced data structures such as trees and graphs, implement different methods used to manipulate these data structures, examine their efficiency. Learn how to approach open ended problems and select which data structure to use based on requirements

 ## Week Three

 Go into recursivity in python. Implemented a factorial solution using recursivity. 

  ## Week Four

  - format printing
  - decision making (if)
  - repetitive tasks (loops)
  - functions
   - argument packing and unpacking
   - named argument in function
   - sum of sqaures passing list
   - sum of sqaures passing arbitrary argument
   - the Euclidean distance
  - rebind variables
  
  

 ## Exercises

 Added solution for different exercises in Python 

### Exercise 1 (hello world)

Fill in the missing piece in the solution stub file hello_world.py in folder src to make it print the following:

Hello, world!

Make sure you use correct indenting. You can run it with command python3 src/hello_world.py. 

### Exercise 2 (compliment)

Fill in the stub solution to make the program work as follows. The program should ask the user for an input, and the print an answer as the examples below show.

What country are you from? Sweden
I have heard that Sweden is a beautiful country.

What country are you from? Chile  
I have heard that Chile is a beautiful country.


### Exercise 3 (multiplication)

Make a program that gives the following output. You should use a for loop in your solution.

4 multiplied by 0 is 0
4 multiplied by 1 is 4
4 multiplied by 2 is 8
4 multiplied by 3 is 12
4 multiplied by 4 is 16
4 multiplied by 5 is 20
4 multiplied by 6 is 24
4 multiplied by 7 is 28
4 multiplied by 8 is 32
4 multiplied by 9 is 36
4 multiplied by 10 is 40


### Exercise 4 (multiplication table)

In the main function print a multiplication table, which is shown below:

   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100

For example at row 4 and column 9 we have 4*9=36.

Use two nested for loops to achive this. Note that you can use the following form to stop the print function from automatically starting a new line:

print("text", end="")
print("more text")

textmore text

Print the numbers in a field with width four, so that the numbers are nicely aligned. 


### Exercise 5 (two dice)

Let us consider throwing two dice. (A dice can give a value between 1 and 6.) Use two nested for loops in the main function to iterate through all possible combinations the pair of dice can give. There are 36 possible combinations. Print all those combinations as (ordered) pairs that sum to 5. For example, your printout should include the pair (2,3). Print one pair per line.

### Exercise 6 (triple square)

Write two functions: triple and square. Function triple multiplies its parameter by three. Function square raises its parameter to the power of two. For example, we have equalities triple(5)==15 and square(5)==25.

Part 1.

In the main function write a for loop that iterates through values 1 to 10, and for each value prints its triple and its square. The output should be as follows:

triple(1)==3 square(1)==1
triple(2)==6 square(2)==4
...

Part 2.

Now modify this for loop so that it stops iteration when the square of a value is larger than the triple of the value, without printing anything in the last iteration.

Note that the test cases check that both functions triple and square are called exactly once per iteration.

### Exercise 7 (areas of shapes)

Create a program that can compute the areas of three shapes, triangles, rectangles and circles, when their dimensions are given.

An endless loop should ask for which shape you want the area be calculated. An empty string as input will exit the loop. If the user gives a string that is none of the given shapes, the message “Unknown shape!” should be printed. Then it will ask for dimensions for that particular shape. When all the necessary dimensions are given, it prints the area, and starts the loop all over again. Use format specifier f for the area.

What happens if you give incorrect dimensions, like giving string "aa" as radius? You don't have to check for errors in the input.

Example interaction:

Choose a shape (triangle, rectangle, circle): triangle
Give base of the triangle: 20
Give height of the triangle: 5
The area is 50.000000
Choose a shape (triangle, rectangle, circle): rectangel
Unknown shape!
Choose a shape (triangle, rectangle, circle): rectangle
Give width of the rectangle: 20
Give height of the rectangle: 4
The area is 80.000000
Choose a shape (triangle, rectangle, circle): circle
Give radius of the circle: 10
The area is 314.159265
Choose a shape (triangle, rectangle, circle): 

### Exercise 8 (solve quadratic)

In mathematics, the quadratic equation $ax2+bx+c=0$ can be solved with the formula $x=\frac{-b\pm \sqrt{b^2 -4ac}}{2a}$

​​

Write a function solve_quadratic, that returns both solutions of a generic quadratic as a pair (2-tuple) when the coefficients are given as parameters. It should work like this:

print(solve_quadratic(1,-3,2))<br>
(2.0,1.0)<br>
print(solve_quadratic(1,2,1))<br>
(-1.0,-1.0)<br>

You may want to use the math.sqrt function from the math module in your solution. Test that your function works in the main function!


### Exercise 9 (merge)

Suppose we have two lists L1 and L2 that contain integers which are sorted in ascending order. Create a function merge that gets these lists as parameters and returns a new sorted list L that has all the elements of L1 and L2. So, len(L) should equal to len(L1)+len(L2). Do this using the fact that both lists are already sorted. You can’t use the sorted function or the sort method in implementing the merge method. You can however use these sorted in the main function for creating inputs to the merge function. Test with a couple of examples in the main function that your solution works correctly.

Note: In Python argument lists are passed by reference to the function, they are not copied! Make sure you don't modify the original lists of the caller.

### Exercise 10 (detect ranges)

Create a function named detect_ranges that gets a list of integers as a parameter. The function should then sort this list, and transform the list into another list where pairs are used for all the detected intervals. So 3,4,5,6 is replaced by the pair (3,7). Numbers that are not part of any interval result just single numbers. The resulting list consists of these numbers and pairs, separated by commas. An example of how this function works:

print(detect_ranges([2,5,4,8,12,6,7,10,13]))
[2,(4,9),10,(12,14)]

Note that the second element of the pair does not belong to the range. This is consistent with the way Python's range function works. You may assume that no element in the input list appears multiple times.