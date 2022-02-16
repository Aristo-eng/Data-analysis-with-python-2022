#!/usr/bin/env python3

def merge(L1, L2):
    L3 = L1+L2
    for j in range(len(L3)):
        for i in range(0, len(L3)-j-1):
            if L3[i]> L3[i+1]:
                L3[i],L3[i+1] = L3[i+1] , L3[i]
    return (L3)

def main():
    print((merge([1,2,3],[1,6,7])))


    pass


if __name__ == "__main__":
    main()
