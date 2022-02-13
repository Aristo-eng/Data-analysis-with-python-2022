def main():
    number = input('Give an integer: ')
    number = int(number)
    if (number)<0:
        print('The absolute value of %i is %i' %(number, number*-1))
    else:
        print('The absolute value of %i is %i' %(number, number*1))



if __name__=="__main__":
    main()
