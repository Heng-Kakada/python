# String slicing : create a substring by extracting elements from another string indexing[] or slicing{}
# [start:stop:step]

name = "heng kakada"

# start run from 0 < stop indexing
x = name[:4]

y = name[5:]

z = name[0:11:2]

reverse = name[::-1]

print(reverse)

# slicing

web = "https://google.com"

# start from 8 to -4 or equal to 14 and run up by 1

google = slice(8, -4, 1)

print(web[google])

