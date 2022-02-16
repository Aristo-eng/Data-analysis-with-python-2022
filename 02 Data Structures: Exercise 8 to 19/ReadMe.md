# Data structures

The main data structures in Python are strings, lists, tuples, dictionaries, and sets. We saw some examples of lists, when we discussed for loops. And we saw briefly tuples when we introduced argument packing and unpacking. Let's get into more details now.

## Sequences

### list

A list contains arbitrary number of elements (even zero) that are stored in sequential order. The elements are separated by commas and written between brackets. The elements don't need to be of the same type. An example of a list with four values:

[2, 100, "hello", 1.0]

### tuple

A tuple is fixed length, immutable, and ordered container. Elements of tuple are separated by commas and written between parentheses. Examples of tuples:

(3,)               # a singleton
(1,3)              # a pair
(1, "hello", 1.0); # a triple

As we can see, both lists and tuples can contain values of different type.

List, tuples, and strings are called sequences in Python, and they have several 

## commonalities:


- their length can be queried with the len function
- min and max function find the minimum and maximum element of a sequence, and 
- sum adds all the elements of numbers together
- Sequences can be concatenated with the + operator, and repeated with the * operator: "hi"*3=="hihihi"
- Since sequences are ordered, we can refer to the elements of a sequences by integers using the indexing notation: "abcd"[2] == "c"
- Note that the indexing begins from 0
- Negative integers start indexing from the end: -1 refers to the last element, -2 refers to the second last, and so on


Above we saw that we can access a single element of a sequence using indexing. If we want a subsequence of a sequence, we can use the slicing syntax. A slice consists of elements of the original sequence, and it is itself a sequence as well. A simple slice is a range of elements:

s="abcdefg"
s[1:4]

'bcd'

Note that Python ranges exclude the last index. The generic form of a slice is sequence[first:last:step]. If any of the three parameters are left out, they are set to default values as follows: first=0, last=len(L), step=1. So, for instance "abcde"[1:]=="bcde". The step parameter selects elements that are step distance apart from each other. For example:

print([0,1,2,3,4,5,6,7,8,9][::3])

[0, 3, 6, 9]

## Modifying lists

We can assign values to elements of a list by indexing or by slicing. An example:

L=[11,13,22,32]
L[2]=10          # Changes the third element
print(L)

[11, 13, 10, 32]

Or we can assign a list to a slice:

L[1:3]=[4]
print(L)

[11, 4, 32]

We can also modify a list by using mutating methods of the list class, namely the methods:
* append, 
* extend,
* insert,
* remove,
* pop, 
* reverse, 
* and sort. 

Try Python's help functionality to find more about these methods: e.g. help(list.extend) or help(list).

## Generating numerical sequences

Trivial lists can be tedious to write: [0,1,2,3,4,5,6]. The function range creates numeric ranges automatically. The above sequence can be generated with the function call range(7). Note again that then end value is not included in the sequence. An example of using the range function:

L=range(3)
for i in L:
    print(i)
Note that L is not a list!
print(L)

0
1
2
range(0, 3)

So L is not a list, but it is a sequence. We can for instace access its last element with L[-1]. If really needed, then it can be converted to a list with the list constructor:

L=range(10)
print(list(L))

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

The range function works in similar fashion as slices. So, for instance the step of the sequence can be given:

print(list(range(0, 7, 2)))

[0, 2, 4, 6]
Sorting sequences