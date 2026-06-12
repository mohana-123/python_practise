# Phase-1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

'''
for i in range(11,0,-1):
    print(i)
'''
'''
for i in range(1,100):
    if i%2 == 0:
        print(i)
'''
'''
for i in range(1,100):
    if i%2 != 0:
        print(i)
'''

# Print multiplication table of a number
'''
n = int(input())
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
'''


# Print squares from 1 to n
'''
n = int(input())
# for i in range(1,n+1):
#     print(i**2)
print("\n".join(str(i**2) for i in range(1,n+1)))

'''

# Find sum of first n natural numbers
# Find sum of even numbers till n
# Find sum of odd numbers till n


# Find factorial of a number
'''
def fun(n):
    if n==1:
        return 1
    return n * fun(n-1)
n = int(input())
print(fun(n))
'''
'''
n = int(input())
k = 1
for i in range(1,n+1):
    k = k * i
print(k)
'''

# Count digits in a number
'''
n = int(input())
print(len(str(n)))
'''


# Reverse a number
'''
n = int(input())
n = list(str(n))
k = n[::-1]
print(''.join(k))
'''
'''
# another method
n = int(input())
sum = 0
for i in range(len(str(n))):
    digit = n%10
    sum = digit + sum*10
    n //= 10
print(sum)
'''



#  Find sum of digits
'''
n = int(input())
sum = 0
while n > 0:
    digit = n%10
    sum = sum + digit
    n = n // 10
print(sum)
'''


# Find product of digits
'''
n = int(input())
pro = 1
while n > 0:
    digit = n%10
    pro = pro * digit
    n = n // 10
print(pro)
'''

# Phase-2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Find smallest digit in a number
'''
n = int(input())
s = str(n)
smallest = s[0]

for digit in s:
    if digit < smallest:
        smallest = digit
print(int(smallest))
'''

# Find largest digit in a number
'''
n = int(input())
largest = 0
while n > 0:
    digit = n%10
    if digit > largest:
        largest = digit
    n = n//10
print(largest)
'''

# Check palindrome number
'''
# m-1
n = int(input())
print(str(n)[::-1])
'''
'''
# m-2
n = int(input())
reverse = 0
while n>0:
    digit = n%10
    reverse = digit + reverse*10
    n //= 10
print(reverse)
'''

# Check Armstrong number
'''
armstrong num = 153
1^3 + 5^3 + 3^3 = 153
'''
'''
n = int(input())
original_n = n
n_dig = len(str(n))
sum = 0
while n>0:
    digit = n%10
    sum = sum + digit**n_dig
    n //= 10

if original_n == sum:
    print("An Armstrong number")
else:
    print("not an Armstrong number")

print(sum)
'''

# Check prime number
'''
# method-1
n = int(input())

if n > 1:
    for i in range(2,n):
        if (n%i) == 0:
            print("not a prime")
            break
    else:
        print('a prime')
else:
    print("not a prime")

'''
'''
# method-2
n = int(input())
prime = True
if n<=1:
    prime = False
if n<=3:
    prime = True

for i in range(4,int(n**0.5)):
    if n%i == 0:
        prime = False
        break
prime = True

if prime == True:
    print("prime num")
else:
    print("not a prime")
'''

# Print all prime numbers till n
'''
n = int(input())
is_prime = [2,3]
for i in range(4,n+1):
    has_divisor = False
    for prime in is_prime:
        if i%prime == 0:
            has_divisor = True
            break
    if not has_divisor:
        is_prime.append(prime)
print(is_prime)
'''

# tip calculator, BMI calculator, seconds-to-hours converter.

# tip calculator
'''
amount_paid = int(input("Enter total amount: "))
tip_percentage = int(input("Enter the percentage of the tip: "))

total = amount_paid*(tip_percentage/100)
print(total+amount_paid)
'''
