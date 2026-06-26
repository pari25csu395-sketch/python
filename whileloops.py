count = 1
while count <=5:
    print(count)
    count +=1

print("loop ended")

# wap tp print numbers from 1 to 100

count = 1
while count<=100:
    print (count)
    count +=1 

# wap to print num from 100 to 1

count = 100
while count>=1:
    print (count) 
    count -=1

# wap to print multiplication table of a number entered by user 

n = int (input("Enter a number to print its multiplication table: ")) 

i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i +=1

# print elements of a list using while loop

nums= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#traverse
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1


#search pf a num x i the flwing tuple

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = 49
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("Found at idx", i)
    i+=1


