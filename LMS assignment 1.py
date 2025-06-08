def low(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)
    print()

def up(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        spaces = "  " * (n - i)
        stars = "* " * i
        print(spaces + stars)
    print()

def pyra(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "* " * i
        print(spaces + stars)
    print()

rows = int(input("Enter the number of rows: "))
print()
low(rows)
up(rows)
pyra(rows)
