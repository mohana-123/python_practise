# code-30:Addition of two fractions ======================================================================================
'''
import math
print("enter the numerator and denomenator of 1st fraction ",end='')
n1,d1 = map(int, input().split())

print("enter the numerator and denomenator of 2nd fraction ",end='')
n2,d2 = map(int, input().split())

print(f"the fractions are {n1}/{d1} and {n2}/{d2}")

n = (n1*d2) + (n2*d1)
d = d2*d1

g = math.gcd(n,d)

print(f"the addition of {n1}/{d1} and {n2}/{d2} are {n//g}/{d//g}")
'''


'''
from fractions import Fraction

print("enter the numerator and denomenator of 1st fraction ",end='')
n1,d1 = map(int, input().split())
f1 = Fraction(n1,d1)

print("enter the numerator and denomenator of 2nd fraction ",end='')
n2,d2 = map(int, input().split())
f2 = Fraction(n2,d2)

r = f1+f2
print(r)
'''


# code-31: Replace all 0’s with 1 in a given integer ===========================================================================
'''
n = input()
n1 = n.replace('0','1')
print(n1)
'''

'''
n = input()
#converting into string
n=str(n) 
#then into the list
n=list(n)
r="" #empty string for addind it the item of list
for i in range(len(n)):
    #if we find '0' we will replace it with '1'
    if(n[i]=='0'):
        n[i]='1'
    r=r + n[i]  #creating the new integer 
  
print("Converted number is :",int(r))
'''

# code-32: Can a number be expressed as a sum of two prime numbers ============================================================
'''
import math
num = int(input(f"Insert the num: "))

# find the primes in a range
primes = [2,3]

for n in range(4,num):
    f = 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            f = 1
            break
    if f == 0:
        primes.append(n)
# print(primes)

# check the sum pairs

# for m in range(len(primes)):
#     for n in range(1, len(primes)):
#         if primes[m] + primes[n] == num:
#             print(primes[m], primes[n])

for p in primes:
    if p > num//2:
        break
    if num-p in primes:
        print(p, num-p)
'''

# code-33:Count possible decoding of a given digit sequence =================================================================
'''
concepts
Possible decoding (1, 3, 1,)    = ACA
Possible decoding (13, 1)   = MA
So, the total possible decoding’s of sequence 131 is 2.
'''

# n = 123
'''r = 0
for i in range(len(str(n))):
    d = n%10
    r = r + d
    n = n//10
print(r)'''

'''
def fun(n):
    if n == 0:
        return 0
    return n%10 + fun(n//10)

print(fun(123))
'''

# code-34:Calculate the number of digits in an integer ====================================================================
'''
n = int(input())
c = 0
for i in range(len(str(n))):
    c += 1
print(c)
'''


# code-35:Convert digit/number to words ===========================================================================
'''
 Taking input as a string from the user.
 Check the length of the input.
 if the length is zero print empty and if the length is greater than 4 print "give a string of specific length"
 if length id between 1 - 4, Create arrays for different values.
 Checking the length of the string.
 According to the place of the digit, we will show the output.
'''

'''
def convert_to_words(num):
 
    l = len(num)
 
    # Base cases
    if (l == 0):
        print("empty string")
        return
 
    if (l > 4):
        print("Length more than 4 is not supported")
        return
 
    single_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
 
    two_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
 
    tens_multiple = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
 
    tens_power = ["hundred", "thousand"]
 
    print(num, ":", end=" ")
 
    if (l == 1):
        print(single_digits[ord(num[0]) - 48])
        return
 
    x = 0
    while (x < len(num)):
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                print(single_digits[ord(num[x]) - 48],
                      end=" ")
                print(tens_power[l - 3], end=" ")
 
            l -= 1
 
        else:
 
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 +
                       ord(num[x+1]) - 48)
                print(two_digits[sum])
                return
 
            elif (ord(num[x]) - 48 == 2 and
                  ord(num[x + 1]) - 48 == 0):
                print("twenty")
                return
 
            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    print(tens_multiple[i], end=" ")
                else:
                    print("", end="")
                x += 1
                if(ord(num[x]) - 48 != 0):
                    print(single_digits[ord(num[x]) - 48])
        x += 1
 
 
# Driver Code
convert_to_words(input()) 
'''
# felt very difficult still i must understand




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
'''


# code- 39 : Finding number of integers which has exactly x divisors

# in between 1-7 how many numbers are having the factors of exactly 2
# 2,3,4,5 are the number which has exactly 2 factors those are 1 and itself

# number = 7
# divisors = 2

# count = 0




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