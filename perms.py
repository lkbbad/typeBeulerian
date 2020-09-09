import itertools
import sys

args = sys.argv

n = int(args[1])
a_list = []
for num in range(1, n+1):
    a_list.append(num)

permutations_object = itertools.permutations(a_list)
permutations_list = list(permutations_object)

# FINDING ONE PEAK
# count = 0
# for perm in permutations_list:
#     found = False
#     for j in range(1, len(perm)-1):
#         if (perm[j - 1] < perm[j]) and (perm[j] > perm[j + 1]):
#             if not found:
#                 found = True
#                 count += 1
#                 # print(perm)
#             else:
#                 count -= 1
#                 # print('NOT ', perm)
#                 break
# print(count)

dictionary = {}
for peak in range(0, n):
    dictionary[peak] = []
for perm in permutations_list:
    peaks = 0
    for j in range(1, len(perm)-1):
        if (perm[j - 1] < perm[j]) and (perm[j] > perm[j + 1]):
            peaks += 1
    dictionary[peaks].append(perm)


print("for 0 peaks: 2^(n-1) = ", 2**(n-1))
print("---------------------------")

for key in dictionary:
    print("# of perms with", key, "peak(s) is ", len(dictionary[key]))

