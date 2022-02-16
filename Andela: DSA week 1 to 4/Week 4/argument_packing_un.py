def sum_of_squares(*lst):
    "Computes the sum of squares of arbitrary number of arguments"
    s=0
    for x in lst:
        s += x**2
    return s

print(sum_of_squares(-2))
print(sum_of_squares(-2,4,5))

lste = [2,3,4]
#unpack list first
print(sum_of_squares(*lste))


lst=[1,5,8]
print("With list unpacked as arguments to the functions:", sum_of_squares(*lst))
# print(sum_of_squares(lst))    # Does not work correctly