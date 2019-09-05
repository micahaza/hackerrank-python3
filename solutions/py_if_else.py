def if_else():
    n = int(input().strip())
    if n % 2 == 1:  # odd
        print("Weird")
    else:  # even
        if n > 20:
            print("Not Weird")
        if n in range(2, 6):
            print("Not Weird")
        if n in range(6, 21):
            print("Weird")
