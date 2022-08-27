# Nested loop = “inner loop” will finish all of its iterations before finishing one iteration of “outer loop”


rows = int(input("How many row ?: "))
columns = int(input("How many colum ?: "))
symbol = input("How many row ?: ")

for i in range(rows):
    for j in range(columns):
        # end = not new line
        print(symbol, end="")
    print()
print("ending Loop")