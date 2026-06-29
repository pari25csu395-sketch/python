def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(10)


def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))



# sum of first n natural numbers

def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(10)
print(sum)

    
    
    