#!/usr/bin/env python3

# Exercise 6 (triple square)
# Write two functions: triple and square. Function triple multiplies its
# parameter by three. Function square raises its parameter to the power
# of two. For example, we have equalities triple(5)==15 and
# square(5)==25.
#
#
# Part 1.
#
# In the main function write a for loop that iterates through values 1
# to 10, and for each value prints its triple and its square. The output
# should be as follows:
#
#
# triple(1)==3 square(1)==1
# triple(2)==6 square(2)==4
# ...
# Part 2.
#
# Now modify this for loop so that it stops iteration when the square of
# a value is larger than the triple of the value, without printing
# anything in the last iteration.
#
#
# Note that the test cases check that both functions triple and square
# are called exactly once per iteration.





def square(x):
    return x**2

def triple(x):
    return x*3

def answ(i,t,s):
    print(f"triple({i})=={t} square({i})=={s}")

def main():
    for i in range(1,11):
        t = triple(i)
        s = square(i)
        

        if(s>t):
            break;

        answ(i,t,s)
        
if __name__ == "__main__":
    main()



    