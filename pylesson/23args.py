# *args =   parameter that will pack all arguments into a tuple
#           useful so that a function can accept a varying amount of arguments

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6,7,8))

def add(*staff):
    sum = 0
    staff = list(staff)
    staff[0] = 0
    for i in staff:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))
