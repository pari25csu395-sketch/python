# function defination
def cal_sum(a, b): #parameters
    return a+b
sum = cal_sum(33,2) #function calling ; arguments
print(sum)


def cal_avg(a, b, c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
    
cal_avg(2,2,2)



# wap to print the length of the list

fruit = ["mango", "pineapple", "litchi", "banana", "dragon"]
names = ["pari", "ishaan","parth","nischay"]

def print_len(fruit):
    print(len(fruit))


print_len(fruit)
print_len(names)




# wap to print the el of list in a single line

def print_list(list):
    for items in list:
        print(items, end=" ")

print_list(names)



# wap to find the factorial of n

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
        
cal_fact(5)


# wap to convert usd into inr

def usd_to_inr(usd):
    inr = usd*94
    print("USD = ", usd ,"INR = ", inr)
    return inr

usd_to_inr(25)

