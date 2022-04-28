fibo = int(input("Enter final term number of sequence"))

def iterfibo(fibo):
    next_term = 0
    prev_term = 0
    for x in range(0, fibo):  
        if(x == 0):
            next_term = 1
        else:
            temp = next_term
            next_term += prev_term
            prev_term = temp

        print (next_term)

iterfibo(fibo)
