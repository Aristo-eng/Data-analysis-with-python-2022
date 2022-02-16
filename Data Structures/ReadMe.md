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

