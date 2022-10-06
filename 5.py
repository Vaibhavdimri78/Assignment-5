#taking a 4 digit number and printing its first three digits from left
'''
print("enter a 4 digit number\n")
n = int(input())
b=n//10
print(b)
# Question 2
c=b%10
print(c)
#3 swapping the data
print("enter the values")
a= int(input())
b= int(input())
print("the values of a is %d and b is %d are"%(b,a))

#4
print("Enter the base and power of the numbers")
x,n=float(input()),float(input())
print("the %f^%f is "%(x,n),x**n)

#5
print("Enter a 3 digit number\n")
n=input()
print(n[-1])    #to print first number from right
print(n[-2])    #to print middle number
print(n[-3])    #to print third number
'''
print("l1 is list natural numbers")
print("enter the number you want to check")
n=int(input())
l1=[1,2,3,4,5,6,8,9,10]
print(n in l1)