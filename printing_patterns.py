# a = [1, 2, 3, 4, 5, 6]
# p = []
# i = 1
# j = 3
# s = 0
# for i in range(len(a)+1):
#     s = a[i] + a[i+1]
#     p.append(s)
# print(p)


# p = sum(nums[i:j+1])

# s=0
# for a in range(i,j+1):
#     s += p[a]
# print(s)





# date: 27/11/2025 =================================================================================


# m = 5

# for i in range(m):
#     for j in range(i+1):
#         print("* ", end='')
#     print()


# for i in range(1,m+1):
#     for j in range(1,i+1):
#         print(j,"", end='')
#     print()

# c = chr(65)
# # print(c)
# for i in range(m):
#     for j in range(i+1):
#         print(chr(65+i),"", end='')
#     print()
# o/p:
# A
# B B
# C C C
# D D D D
# E E E E E

# for i in range(m):
#     for j in range(i+1):
#         print(chr(65+j),"", end='')
#     print()
# o/p:
# A 
# A B
# A B C
# A B C D 
# A B C D E


# for i in range(m,-1,-1):
#     for j in range(i+1):
#         print("* ", end='')
#     print()
# O/P:
# * * * * *
# * * * *
# * * *
# * *
# *


# for i in range(m,-1,-1):
#     for j in range(1,i+1):
#         print(j," ",end='')
#     print()
    
# o/p:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


# for i in range(m):
#     for j in range(m-i):
#         print("  ",end='')
#     for j in range(i+1):
#         print("* ",end='')
#     for k in range(i):
#         print("* ",end='')
#     print()

# o/p:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *



'''
for i in range(1,m+1):
    print("  "*(m-i),end='')
    for j in range(i,i+i):
        print(j,end=' ')
    for j in range(i+i-2,i-1,-1):
        print(j,end=' ')

    print()
'''



# o/p:
#         1 
#       2 3 2 
#     3 4 5 4 3 
#   4 5 6 7 6 5 4 
# 5 6 7 8 9 8 7 6 5

'''
for i in range(m+1,1,-1):
    for j in range(1,i):
        print(j,'',end='')
    print()
'''
# o/p:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

'''
for i in range(m):
    for j in range(i+1):
        print('  ',end='')
    for j in range(m-i):
        print('* ',end='')
    for k in range(m-1,i,-1):
        print('* ',end='')
    print()
'''
# o/p:
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *




# pascals traingle:
# o/p:
#            1
#          1   1
#        1   2   1
#      1   3   3    1
#    1  4    6   4   1
#  1  5   10   10  5   1










r = 5

# for i in range(r):
#     for j in range(r):
#         print("*",end=' ')
#     print()


# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()


for i in range()