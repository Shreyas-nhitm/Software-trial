# Prints diamond pattern with 2n rows
def printdiamond(n):

    space = n - 1

    # run loop (parent loop)
    # till number of rows
    for i in range(0, n):

        # loop for initially space,
        # before star printing
        for j in range(0, space):
            print(" ", end="")

        # Print i+1 stars
        for j in range(0, i + 1):
            print("* ", end="")

        print()
        space -= 1

    # Repeat again in reverse order
    space = 0

    # run loop (parent loop)
    # till number of rows
    for i in range(n, 0, -1):

        # loop for initially space,
        # before star printing
        for j in range(0, space):
            print(" ", end="")

        # Print i stars
        for j in range(0, i):
            print("* ", end="")

        print()
        space += 1


def main():
    printdiamond(5)


if __name__ == "__main__":
    main()
