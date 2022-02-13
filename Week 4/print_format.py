a = "first"
b = "second"

print(a+b)
print("-".join([a,b,b,a]))

# use format syntax
print("%i plus %i is equal to %i" %(1,2,1+2))

# use format method
print("{} plus {} is equal to {}".format(1,5,1+5))

# use f-string
print(f"{1} plus {9} is equl to {1+9}")


print("%.1f %.2f %.3f" % (1.6, 1.7, 1.8))               # Old style
print("{:.1f} {:.2f} {:.3f}".format(1.6, 1.7, 1.8))     # newer style
print(f"{1.6:.1f} {1.7:.2f} {1.8:.3f}")                 # f-string


print("%s concatenated with %s produces %s" % ("water", "melon", "water"+"melon"))
print("{0} concatenated with {1} produces {0}{1}".format("water", "melon"))
print(f"{'water'} concatenated with {'melon'} produces {'water' + 'melon'}")

