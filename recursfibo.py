fibo = int(input("Enter final term number of sequence"))

def recurfibo(fibo):
    if fibo in {0, 1}:  # Base case
        return 1
    return recurfibo(fibo - 1) + recurfibo(fibo - 2)  # Recursive case

for x in range(fibo):
    print(recurfibo(x))