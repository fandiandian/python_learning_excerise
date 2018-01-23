
# 倒序排列
'''
# inverse permutation
# 将一个数组进行倒序

n =  int(input('确定数组的长度：\n'))

a = [i for i in range(n)]
b = [0 for i in range(n)]
print(a)
for ii in range(n):
    b[n-ii-1] = a[ii]
print(b)

for i in range(n):
    if a[b[i]] == b[a[i]] == n-i-1:
        print(True)
'''
        
# 这个是书上的解答，有点理解不了 
'''      
import stdio
import sys
import stdarray

# Accept a permutation of integers from the command line and write the
# inverse permutation to standard output.

# Accept the permutation.
perm = []
for i in range(1, len(sys.argv)):
    perm += [int(sys.argv[i])]
n = len(perm)

# Make sure the permutation is valid.
exists = stdarray.create1D(n, False)
for i in range(n):
    if (perm[i] < 0) or (perm[i] >= n) or exists[perm[i]]:
        stdio.writeln("Not a permutation")
        sys.exit(0)
    exists[perm[i]] = True

# Invert the permutation.
permInverted = [0] * n
for i in range(n):
    permInverted[perm[i]] = i

# Write the inverted permutation.
for element in permInverted:
    stdio.write(str(element) + ' ')
stdio.writeln()
'''

# 哈达玛矩阵
# Hadamard matrix
# 已提取成单独文件


ll = [1,3,5,7,3,7,8,9,0,4,4]
n = 2
def nn(ll):
    return ll.sort()

nn(ll)
print(ll)    
