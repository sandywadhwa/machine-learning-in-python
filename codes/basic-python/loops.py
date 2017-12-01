def print_one_to_n(n):
    for i in range(1, n):
        print("{0}".format(i))

def print_n_to_one(n):
    i = n
    while i>0:
        print("{0}".format(i))
        i-=1


print_one_to_n(10)
print_n_to_one(10)