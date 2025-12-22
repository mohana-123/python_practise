# d-1
# 10:20 => 12:00

# code-31: Replace all 0’s with 1 in a given integer ===========================================================================
# 1230050 => 1231151
'''
n = input()
e = n
for i in n:
    if i == '0':
        e = e.replace(i,'1')
print(e)
'''
'''
n = list(input())
s = ''

for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
    s = s + n[i]
print(s)

'''


# d-2

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


# code-33: Count possible decoding of a given digit sequence =================================================================


'''
Possible decoding (1, 3, 1,)    = ACA
Possible decoding (13, 1)   = MA
So, the total possible decoding's of sequence 131 is 2.
'''


# alpha_digit = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N',

#             }


# code- 42 : Prime Number using recursion ================================================================================================

# prime Number using recursion
'''
def prime(n,i =2):
    if n < 2:
        False
    if n%i == 0:
        return False
    if i*i > n:
        return True
    return prime(n,i+1)

n = 20
print(prime(n))
'''