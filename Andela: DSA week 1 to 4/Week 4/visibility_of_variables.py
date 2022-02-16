i=2 
k= 2          # global variable
def f():
    global k
    k=5
    i=3       # this creates a new variable, it does not rebind the global i
    print(i)  # This will print 3   
    print(k)  # This will print 5
f()
print(i)      # This will print 2
print(k)      # This will print 5
