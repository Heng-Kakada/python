# keyword arguments = arguments preceded by an identifier when we pass them to function.
# The order of the arguments doesn't matter, unlike position arguments.
# Python knows the names of the arguments that a function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


# last middle first all of this are identifier

hello(last="Code", middle="Dude", first="Bro")
