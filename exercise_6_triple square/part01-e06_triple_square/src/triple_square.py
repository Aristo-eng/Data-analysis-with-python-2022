#!/usr/bin/env python3

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



    