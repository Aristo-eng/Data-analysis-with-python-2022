#!/usr/bin/env python3

def main():
    # Enter your solution here
    n = 4
    for i in range(0,11):
        out = repr(n) +' multiplied by '+repr(i)+ ' is '+ repr(n*i)
        print(out)

if __name__ == "__main__":
    main()
