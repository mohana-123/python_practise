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


# code- 37 : Finding Number of times x digit occurs in a given input

'''
Input : 
Enter a number : 897982
Enter the digit : 9
Output :  
2
Explanation : The digit 9 occurs twice
'''
'''
num = input("Enter a number : ")
n = input("Enter the digit : ")
c = 0
for i in num:
    if i == n:
        c += 1
print(f"The digit {n} occurs {c} times")
'''


def occurrances(n, d):
    count = 0
 
    while (n > 0):
        if(n % 10 == d):
            count = count + 1
  
        n = n // 10
 
    return(f"The digit {d} occurs {count} times")
    
d = 2
n = 828282
print(occurrances(n, d))



# code- 39 : Finding number of integers which has exactly x divisors


# code- 40 : Finding Roots of a quadratic equation ==========================================================================

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