if __name__ == '__main__':
    n = int(input().strip())

    if 1 <= n <= 100: 
        if n != 0 and n % 2 == 1: 
            print("Weird")
        elif n % 2 == 0:
            if 2 <= n <= 5 or n > 20:
                print("Not Weird")
            elif 6 <= n <= 20:
                print("Weird")
    else:
        print("Input is out of range")