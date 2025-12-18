# Day-1 ######################################################################################################################

# code-1: check weather a number is odd or even using bitwise operators =========================================================
'''
num = int(input())
print("Odd") if num&1 == 1 else print("Even")
'''

# code-2: Find the Sum of The First N Natural Numbers =============================================================================
# n = int(input())

# Method 1 : Using for Loop
'''
s=0
for i in range(1,n+1):
    s += i
print(s)
'''
# Method 2 : Using Formula for the Sum of Nth Term
# print(int(n*(n+1)/2))

# Method 3 : Using Recursion

'''
def fun(n):
    if n == 0:
        return False
    elif n == 1:
        return 1
    else:
        return n + fun(n-1)

print(fun(n))
'''


# code-3: Find the Sum of the Numbers in a Given Range ==========================================================================
# Example
# Input : 2 5
# Output : 14

# Method 1: Using Brute Force
# num1,num2 = map(int, input().split())
# s=0
# for i in range(low,high+1):
#     s += i
# print(s)

# Method 2: Using the Formula
# low = (num1*(num1+1)/2) - num1
# high = num2*(num2+1)/2
# print(high-low)


# Method 3: Using Recursion

'''def resum(sum,num1,num2):
    if num1 > num2:
        return sum
    return num1 + resum(sum,num1+1,num2)

sum = 0
print(resum(sum,num1,num2))'''


# code-4: Leap Year Program ==================================================================================================

'''y = int(input())
if (y%400 == 0) or (y%4 == 0 and y%100 != 0):
    print("leap")
else:
    print("not leap")'''

# code-5: Check Whether a Number is a Prime or Not ==========================================================================================
# brute force
'''n = int(input())
f = 0
if n > 2:
    for i in range(2,n):
        if n%i == 0:
            f=1
            break

print(f"{n} is a prime") if f==0 else print(f"{n} is not a prime")'''

# op by n/2

'''n= int(input())
f = 0
if n < 3:
    print("prime number")

for i in range(3, int(math.sqrt(n)+1)):
    if n%i == 0:
            f=1
            break
print(f"{n} is a prime") if f==0 else print(f"{n} is not a prime")'''

# by skipping even interation

'''n= int(input())
f = 0
if n < 3:
    print("prime number")

for i in range(3, int(math.sqrt(n)+1),2):
    if n%i == 0:
            f=1
            break
print(f"{n} is a prime") if f==0 else print(f"{n} is not a prime")'''


# recurssion

'''
n = int(input())

def checkprime(n,i=2):
    if n == i:
        return True
    if n % i == 0:
        return False
    if n<2:
        return False
    return checkprime(n,i+1)

if checkprime(n) == True:
    print("a prime number")
else:
    print("Not a prime")
'''


# code-6: Find the Prime Numbers in a Given Range ==============================================================================
'''
n1,n2= map(int, input().split())
f=0
p = [2,3]
for num in range(n1,n2+1):
    f=0
    if num <= 3:
        continue

    for i in range(2, int(math.sqrt(num)+1)):
        if num%i == 0:
            f=1
            break

    if f == 0:
        p.append(num)

print(p)
'''


# code-7: Find the sum of the Digits of a Number ============================================================================

# num = int(input())
'''
n = len(str(num))
s=0
for i in range(n):
    d = int(num%10)
    s += d
    num = num/10
    
print(s)
'''

# only in python string extraction
'''s = 0
for i in str(num):
    s += int(i)
print(s)'''

# Day-2 #####################################################################################################################

# code-8: Find the Reverse of a Number ==================================================================================

# m-1
'''
s = int(input())
print(str(s)[::-1])
'''
# m-2
'''
n = 123
rev = 0
while n>0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10
print(rev)
'''
# m-3 Recurssion
'''
def fun(n, rev):
    if n == 0:
        return rev
    digit = n%10
    rev = rev * 10 + digit
    return fun(n//10, rev)

n = 12345
rev = 0 
print(fun(n,rev))
'''

# m-4
'''
n = 123
r = ''
for i in str(n):
    r = i+r
print(r)
'''

# code-9: Check Whether or Not the Number is a Palindromer =======================================================================

# Example
# Input : 1221
# Output : Palindrome

# m-1
'''
n = 12321
t = n
reverse = 0
while t>0:
    remainder = int(t%10)
    reverse = (reverse*10) + remainder
    t = t//10
print(reverse)
print("it is palindrome") if n == reverse else print("not a palindrome")
'''

# m-2

# n = 1221
# str_n = str(n)
# print(str_n)
# print("Palindrome") if str(n)[::-1] == str(n) else print("not a palindrome")

# m-3

# rev = ''.join(reversed(str_n))
# print(rev)
# if str_n == rev:
#     print("palindrome")
# else:
#     print("not a palindrome")


# b = str(1234)
# a = reversed(b)
# print(a)



# code-10: Check Whether a Given Number is an Armstrong Number or Not =======================================================

# m-1:

# list of armstrong numbers: 370, 371, 1634

'''
import math
n = input()
l = len(n)
temp = n
sum = 0
for i in n:
    sum += math.pow(int(i),l)
print("yes! it is armstrong!") if int(sum) == int(n) else print("Not an armstrong.")
'''


# code-11: Find the Fibonacci Series up to Nth Term ==============================================================================

# m-1:
'''
num = 10
n1,n2 = 0,1
print(n1,n2,end=' ')
for i in range(2,10):
    n3 = n1+n2
    n1 = n2
    n2 = n3
    print(n3,end=' ')
print()
'''

# m-2:

# Python program to print Fibonacci Series
'''
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        return (fibonacciSeries(i - 1) + fibonacciSeries(i - 2))

num=20
if num <=0:
    print("Please enter a Positive Number")
else:
    print("Fibonacci Series:", end=" ")
for i in range(num):
    print(fibonacciSeries(i), end=" ")
'''

# code-12: Find the Nth Term of a Fibonacci Series ==========================================================================

'''
n = 5
if n<2:
    print(n)
arr = [0,1]
for i in range(1,n):
    arr.append(arr[i] + arr[i-1])
print(arr[n-1])
'''


# code-13: Factorial of a Number =================================================================================
# m-1
'''
n = int(input())
fac = 1
i=1
while i<=n:
    fac = fac*i
    i = i+1
print(fac)
'''
# m-2: recurrsive method
'''
def fac(n):
    if n == 1:
        return n
    return n * fac(n-1)

n=int(input())
if n < 0:
    print("Try again! please enter non-negative number next time.")
else:
    print(f"the factorial of {n} is {fac(n)}")
'''


# code-14: Find the Power of a Number ==========================================================================

# m-1: simple iteration
'''
num, power = map(int, input().split())
o = 1
for i in range(1,power+1):
    o = (o * num)
print(o)
'''

# m-2: recurssion
'''
def fun(num, power):
    if power == 0:
        return 1
    else:
        return num * fun(num,power-1)
    
num, power = map(int, input().split())
print(fun(num,power))
'''

# Day-3 #######################################################################################################################

# code-15: Find the Factors of a Number ==========================================================================

'''
n = int(input())
f = []
for i in range(1,int(math.sqrt(n))+1):
    if n%i == 0:
        f.append(i)
        # if i != n//i:
        #     f.append(n//i)
f.sort()
print(*(k for k in f))
'''


# code-16: Find the Prime Factors of a Number =============================================================================
'''
def pf(n):
    if n < 4:
        return n
    arr = []
    while n > 1:
        for i in range(2, int(2+n//2)):
            if i == (1 + n // 2):
                arr.append(n)
                n = n // n
            if n % i == 0:
                arr.append(i)
                n = n // i
                break
    return arr

n = 210
print(pf(n))
'''
'''
def fact(a):
    l = []
    for i in range(1,int(math.sqrt(a))+1):
        if a % i == 0:
            l.append(i)
            if i != a//i:
                l.append(a//i)
    return sorted(l)

def prime(n):
    su = 0
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            su += 1
            break
    if su == 0:
        return True
    else:
        return False

a = int(input())
l = fact(a)
print(l)
for i in l:
    if prime(i):
        print(i,end=" ")
'''


# code-17 -22: Strong Number Program ============================================================================

'''
Example
Input : 145
Output : It's a Strong Number.
Explanation : Number = 145
145 = 1! + 4! + 5!
145 = 1 + 24 + 120
'''
'''
def factorial(n):
    m = 1
    for i in range(1,n+1):
        m = m*i
    return m

num = 145
k = 0
for j in str(num):
    k = k + factorial(int(j))
print(k)

if num == k:
    print("Yes")
else:
    print("no")
'''

# code-18 -22: Perfect Number Program ============================================================================

'''
Example
Input : 28
Output : It's a Perfect Number
Explanation : Number = 28
28 = 1 + 2 + 14 + 4 + 7
as the number 28 has factors 1, 2, 4, 7 and 14.
We sum them up and check whether they match the original number. 
'''
'''
def fac(n):
    f = []
    for i in range(1,int(math.sqrt(n))+1):
        if n%i == 0:
            f.append(i)
            if i != n//i:
                f.append(n//i)
    f.sort()
    f.remove(n)
    return f

n = int(input())
if n == sum(fac(n)):
    print(f"yes {n} is a Perfect number")
else:
    print("Nope its not a Perfect number")
'''


# code-19 -22: Check for Perfect Square Program ============================================================================
'''
n = int(input())

if math.floor(math.sqrt(n)) == math.ceil(math.sqrt(n)):
    print("Perfect square")
else:
    print("Not a Perfect square")
'''

# code-20 -22: Automorphic number Program ============================================================================

'''
Example
Input : number = 5
Output : It's an Automorphic number.
Explanation : Number = 5
Square of number = 25
as the square of the number ends with the number itself, It's an Automorphic number.
'''

'''
n = int(input())
sq = n ** 2
print(sq)
a = str(sq)

if str(sq)[-len(str(n))::] == str(n):
    print(f"{n} is a Automorphic number")
else:
    print(f"{n} is not a Automorphic number")
'''


# code-21 -22: Harshad Number Program ============================================================================

'''
Example
Input : 21
Output : Yes ' It's a Harshad Number.
Explanation : The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad Number.
'''
'''
n = int(input())
t = n
sum = 0
while t>0:
    digit = t%10
    sum = digit + sum
    t = t//10

print(sum)
print(n%sum)
if n%sum == 0:
    print(f"Hurray! {sum} is a Harshad number!")
else:
    print(f"No! {sum} is a not Harshad number")
'''

# Day-4 #######################################################################################################################

# code-22: Abundant Number in Python ===============================================================================================
'''
Example
Input : Number = 12
Output : Yes, It's an Abundant Number
Explanation : The Factors for the number 12 are, 1, 2, 3, 4 and 6. We don't want to include the number itself.
Now the sum of the factors except the number itself is :
1 + 2 + 3 + 4 + 6 = 16
as the number 16>12 , the number itself.
It's an abundant number.
'''
'''
n = int(input())
t = n

a=[]
for i in range(1,t):
    if t%i == 0:
        a.append(i)
        
# print(a)
# print(sum(a))

print("abundant number!") if sum(a) > n else print("not an abundant number")
'''


# code-23: check whether two numbers are Friendly Pair in Python ===============================================================================================

'''
Example
Input : 6 28
Output : Yes, they are a friendly pair
Explanation : The factors of 6 and 28 except the numbers themselves are 1, 2, 3 and 1, 2, 4, 7, 14 respectively.
Now the sum of factors of both the numbers are 6 and 28 respectively. 
When we divide the sums with the numbers we get 1 and 1 respectively. 
As the ratio of both the number match, they are considered as a friendly pair.
'''

'''
m,n = map(int, input().split())
t = n

def factors_of_num(t):
    a=[]
    for i in range(1,t):
        if t%i == 0:
            a.append(i)
    return a

print(sum(factors_of_num(m)))
print(sum(factors_of_num(n)))


if (m+n)//(sum(factors_of_num(m))+sum(factors_of_num(n))) == 1:
    print(f"yes! {m}, {n} are friendly numbers")
else:
    print(f"No. {m}, {n} are not friendly numbers")
'''


# code-24: hcm of Two Numbers in Python ===============================================================================================
'''
# my approach
m,n = map(int, input().split())

def factors_of_num(t):
    a=[]
    for i in range(1,t):
        if t%i == 0:
            a.append(i)
    return a

x = (factors_of_num(m))
y = (factors_of_num(n))

print(x)
print(y)
'''

'''
n1, n2 = map(int, input().split())

hcf = 1

# Note down the highest number that divides both num1 & num2
for i in range(1,min(n1,n2)):
    if n1%i == 0 and n2%i == 0:
        hcf = i
print(hcf)
'''


# Method 2: Euclidean Algorithm: Repeated Subtraction
'''
num1 = 36
num2 = 60
a = num1
b = num2

while num1 != num2:
    if num1 > num2:
        num1 -= num2
    else:
        num2 -= num1

print("GCD of", a, "and", b, "is", num1)
'''

# Method 4: Modulo Recursive Euclidean Algorithm: Repeated Subtraction

# This method improves complexity of repeated subtraction
# By efficient use of modulo operator in euclidean algorithm
'''
def getGCD(a, b):
    return b == 0 and a or getGCD(b, a % b)


num1 = 36
num2 = 60

print("GCD of", num1, "and", num2, "is", getGCD(num1, num2))
'''


# code-25: LCM of two numbers in Python =====================================================================================
'''
n1, n2 = map(int, input().split())

lcm = 1

# Note down the highest number that divides both num1 & num2
for i in range(max(n1, n2), 1 + (n1 * n2)):
    if i % n1 == i % n2 == 0:
        lcm = i
        break
print(lcm)
'''

'''
num1 = 58
num2 = 78
for i in range(max(num1, num2), 1 + (num1 * num2), max(num1, num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        break

print("LCM of", num1, "and", num2, "is", lcm)
'''
'''
def getHCF(num1, num2):
    while num1!=num2:
        if num1>num2:
            num1-=num2
        else:
            num2-=num1
    return num1


num1 = 12
num2 = 14

# Calculating HCF here
hcf = getHCF(num1, num2)

# LCM formula
lcm = (num1*num2)//hcf

print("LCM of", num1, "and", num2, "is", lcm)
'''
# the most effective code
'''
num1 = 58
num2 = 78

def getHCF(a, b):
    if b == 0:
        return a
    else:
        return getHCF(b, a % b)


hcf = getHCF(num1, num2)

# LCM formula
lcm = (num1 * num2) // hcf
print("The hcf is :", lcm)
'''

# print(math.lcm(58,78))


# code-26: Binary To Decimal Conversion in Python =====================================================================================

# multiply every digit by 2 to the power of digit place and add them
'''
binary=input()
b=binary[::-1]
decimal=0
for i in range(len(binary)):
    decimal=decimal+int(b[i])*(2**i)
print(decimal)
'''


'''
binary_val = 1001000101
n = binary_val
s = 0
base = 1
while n > 0:
    digit = n%10
    s = s + (digit * base)
    n = n//10
    base = base*2

print(f"Binary Number is {binary_val} and Decimal Number is {s}")
'''
'''
binary_val = 1001000101

decimal_val = int(str(binary_val),2)

print(decimal_val)
'''

# code-27: Python Program for Permutations In Which N People Can Occupy R Seats In A Classroom ================================
'''
no_of_students = int(input())
no_of_seats = int(input())
result = math.factorial(no_of_students)/math.factorial(no_of_students - no_of_seats)
print(result)
'''

# code-28: Maximum Number Of Handshakes in Python ==========================================================================
'''
# number of people
N = int(input())

# formula
no_of_handshakes = int(N * ((N - 1) / 2))

# print number of handshakes
print('Maximum number of handshakes possible for', N, 'people are', no_of_handshakes)
'''


# Day-5 #######################################################################################################################

# code-29:Calculating the area of circle using Python ======================================================================
'''
radius = 3
pie = math.pi
area = pie * (radius ** 2)
print(round(area, 2))
'''



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

# code-32: Can a number be expressed as a sum of two prime numbers ============================================================
'''
num = int(input(f"Insert the num: "))

# find the primes in a range
primes = [2,3]

for n in range(2,num+1):
    f = 0
    if n <= 3:
        continue

    for i in range(2,n):
        if n%i == 0:
            f = 1
            break
    if f == 0:
        primes.append(n)
# print(primes)

# check the sum pairs

for m in range(len(primes)):
    for n in range(1, len(primes)):
        if primes[m] + primes[n] == num:
            print(primes[m], primes[n])
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
def convert_to_word(num):
    l = len(num)

    if l == 0:
        return "enter anything to test it out bro!!!"
    else:
        if l > 4:
            print("give a string of length < 3")
            return
        
        else:
            pass

num = input()
print(convert_to_word(num))
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

