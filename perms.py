import itertools
import sys
from itertools import product, permutations

args = sys.argv

n = int(args[1])
a_list = []

# Regular permutations
# for num in range(1, n+1):
#     a_list.append(num)
# permutations_object = itertools.permutations(a_list)
# permutations_list = list(permutations_object)

# Signed permutations
signed_ints =[]
for i in range(1, n+1):
	signed_ints.append([-1*i,i])

# Create a list of all ordered signed permutations.
product_list = map(list,list(product(*signed_ints)))

permutations_list = []
for ordered_perm in product_list:
	permutations_list += map(list,list(permutations(ordered_perm)))

print("Number of signed permutations of length ", n, ": ", len(permutations_list))

dictionary = {}
dictionary_pos = {}
dictionary_neg = {}
for peak in range(0, n):
    dictionary[peak] = []
    dictionary_pos[peak] = []
    dictionary_neg[peak] = []
for perm in permutations_list:
    perm.insert(0,0)
    peaks = 0
    pos_peaks = 0
    neg_peaks = 0
    for j in range(1, len(perm)-1):
        if (perm[j - 1] < perm[j]) and (perm[j] > perm[j + 1]):
            peaks += 1
    dictionary[peaks].append(perm)
    if (perm[1] > 0):
        dictionary_pos[peaks].append(perm)
    if (perm[1] < 0):
        dictionary_neg[peaks].append(perm)


# print(permutations_list)
print("for 0 peaks: 2^(n-1) = ", 2**(n-1))
print("---------------------------")

for key in dictionary:
    print("# of P_n,k with", key, "peak(s) is ", len(dictionary[key]))
print("---------------------------")
for key in dictionary_pos:
    print("# of P_n,k + with", key, "peak(s) is ", len(dictionary_pos[key]))
print("---------------------------")
for key in dictionary_neg:
    print("# of P_n,k - with", key, "peak(s) is ", len(dictionary_neg[key]))

