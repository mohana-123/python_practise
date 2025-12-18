# Day-6 ##################################################################################################################
# code-36 :Counting number of days in a given month of a year ============================================================
'''
month = int(input())
year = int(input())
    
if((month==2) and ((year%4==0)  or ((year%100==0) and (year%400==0)))) :
    print("Number of days is 29")

elif(month==2) :
    print("Number of days is 28")

elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) :
    print("Number of days is 31")

else :
    print("Number of days is 30")
'''

'''
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month = 12
year=2025
    
if(month==2 and ((year%400==0) or ((year%100!=0) and (year%4==0)))) :
    print("Number of days is ", arr[month-1]+1)
    
else :
    print("Number of days is ", arr[month-1])
'''


# code-37 :Counting number of days in a given month of a year


# code- 38 : Finding Number of times x digit occurs in a given input

# code- 39 : Finding number of integers which has exactly x divisors


# code- 40 : Finding Roots of a quadratic equation

# x = [-b ± √(b² - 4ac)] / 2a
'''
import math

a = int(input())
b = int(input())
c= int(input())

q = int(math.sqrt(abs(b*b - 4*a*c)))

if q > 0:
    print("Roots are real and different ")
    print((-b + q)/(2 * a))
    print((-b - q)/(2 * a))
elif q == 0:
    print("Roots are real and same")
    print(-b / (2*a))
else:  # q<0
    print("Roots are complex")
    print(- b / (2*a), " + i", q)
    print(- b / (2*a), " - i", q)
'''

# r = 0
# for i in range(len(str(n))):
#     d = n%10
#     r = r + d
#     n = n//10
# print(r)

'''
def fun(n):
    if n == 0:
        return 0
    return n%10 + fun(n/10)

print(fun(123))
'''
