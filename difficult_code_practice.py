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

def encodenum(s,a):
    cnt = [0] * (a+1)           
    cnt[0], cnt[1] = 1,1

    for k in range(2,a+1):
        cnt[k] = 0
        cnt[k] = cnt[k-1]

        if s[k-2] == '1' or (s[k-2] == '2' and s[k-1] < '7'):
            cnt[k] += cnt[k-2]
    return cnt[a]

s = "12321"
print(encodenum(s,len(s)))

'''
[1,1,0,0,0,0]
 0 1 2 3 4 5

[1,1,1,0,0,0]
 0 1 2 3 4 5
'''

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



# code- 44 : smallest Element in an Array using Recursion ================================================================================================
