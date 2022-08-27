# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

# L = local
# E = enclosing
# G = global
# B = Built-in


name = "brain1"  # global scope (available inside & outside functions)


def display_name():
    name = "brain2"  # local scope (available only in this function)
    print(name)


display_name()
print(name)  # global scope
