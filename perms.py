import itertools
import sys
from itertools import product, permutations

def main():
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
    for peak in range(0, n+1):
        dictionary[peak] = []
        dictionary_pos[peak] = []
        dictionary_neg[peak] = []
    for perm in permutations_list:
        perm.insert(0,0)
        peaks = 0
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
    print("---------------------------")

    for key in dictionary_pos:
        print("Now we will count the number of P_n,k + with", key, "peaks that have various descents.")
        dictionary_pos_des = {}
        
        for des in range(0, n+1):
            dictionary_pos_des[des] = []
        for perm in dictionary_pos[key]:
            des = 0
            for j in range(0, len(perm)-1):
                if (perm[j] > perm[j+1]):
                    des += 1
            dictionary_pos_des[des].append(perm)

        for key in dictionary_pos_des:
            print("# of P_n,k + with", key, "descent(s) is ", len(dictionary_pos_des[key]))
        print("---------------------------")

    for key in dictionary_neg:
        print("Now we will count the number of P_n,k - with", key, "peaks that have various descents.")
        dictionary_neg_des = {}
        
        for des in range(0, n+1):
            dictionary_neg_des[des] = []
        for perm in dictionary_neg[key]:
            des = 0
            for j in range(0, len(perm)-1):
                if (perm[j] > perm[j+1]):
                    des += 1
            dictionary_neg_des[des].append(perm)

        for key in dictionary_neg_des:
            print("# of P_n,k - with", key, "descent(s) is ", len(dictionary_neg_des[key]))
        print("---------------------------")

    calculate = input("Do you want to calculate a single term for n+1? Y/N ")
    if (calculate == "Y"):
        n = int(input("Enter your n (should be one more than originally entered): "))
        j = int(input("Enter your j: "))
        k = int(input("Enter your k: "))
        sign = input("Enter + or -: ") 
        # print(n, j, k, sign) 

        if (sign == "+"):
            j_peaks_pos = make_dict_pos(n,j,k, dictionary_pos)
            jm1_peaks_pos = make_dict_pos(n,j-1,k, dictionary_pos)
            jm1_peaks_neg = make_dict_neg(n,j-1,k,dictionary_neg)

            p_nm1_j_k_pos = len(j_peaks_pos[k])
            p_nm1_j_km1_pos= len(j_peaks_pos[k-1])
            p_nm1_jm1_k_pos = len(jm1_peaks_pos[k])
            p_nm1_jm1_km1_pos = len(jm1_peaks_pos[k-1])
            p_nm1_jm1_k_neg = len(jm1_peaks_neg[k])

            total_pos = (2*j+1)*p_nm1_j_k_pos + (2*j)*p_nm1_j_km1_pos + (2*k-2*j+2)*p_nm1_jm1_k_pos + (2*n-2*j-2*k+2)*p_nm1_jm1_km1_pos + p_nm1_jm1_k_neg
            print("P_n,j,k +  = ", total_pos)
        
        if (sign == "-"):
            j_peaks_neg = make_dict_neg(n,j,k, dictionary_neg)
            jm1_peaks_neg = make_dict_neg(n,j-1,k, dictionary_neg)
            j_peaks_pos = make_dict_pos(n,j,k,dictionary_pos)

            p_nm1_j_k_neg = len(j_peaks_neg[k])
            p_nm1_j_km1_neg= len(j_peaks_neg[k-1])
            p_nm1_jm1_k_neg = len(jm1_peaks_neg[k])
            p_nm1_jm1_km1_neg = len(jm1_peaks_neg[k-1])
            p_nm1_j_km1_pos = len(j_peaks_pos[k-1])

            total_neg = (2*j+2)*p_nm1_j_k_neg + (2*j+1)*p_nm1_j_km1_neg + (2*k-2*j)*p_nm1_jm1_k_neg + (2*n-2*j-2*k+2)*p_nm1_jm1_km1_neg + p_nm1_j_km1_pos
            print("P_n,j,k -  = ", total_neg)

    polynomial = input("Do you want to calculate a polynomial? Y/N ")
    if (polynomial == "Y"):
        n = int(input("Enter your n (should be same as originally entered): "))
        sign = input("Enter + or -: ")
        pos_poly = []
        if (sign == "+"):
            for k in range(0, n+1):
                for j in range(0, k+1):
                    # print("j: ", j, "k: ", k)
                    j_peaks_pos = make_dict_pos(n,j,k, dictionary_pos)
                    p_n_j_k_pos = len(j_peaks_pos[k])
                    # print(str(p_n_j_k_pos))
                    pos_poly.append(str(p_n_j_k_pos))
                    pos_poly.append("s^" + str(j) + "t^" + str(k) + "+")
            # print(pos_poly)
            final_pos = ""
            for c in pos_poly:
                final_pos += c
            print(final_pos)
        else:
            for k in range(0, n+1):
                for j in range(0, k+1):
                    j_peaks_neg = make_dict_pos(n,j,k, dictionary_neg)
                    p_n_j_k_neg = len(j_peaks_neg[k])
                    pos_poly.append(str(p_n_j_k_neg))
                    pos_poly.append("s^" + str(j) + "t^" + str(k) + "+")
            # print(pos_poly)
            final_neg = ""
            for c in pos_poly:
                final_neg += c
            print(final_neg)
    
                    
                
def make_dict_pos(n, j,k,dictionary_pos):
    dictionary_pos_des = {}
    for des in range(0, n+1):
        dictionary_pos_des[des] = []
        
    for perm in dictionary_pos[j]:
        des = 0
        for j in range(0, len(perm)-1):
            if (perm[j] > perm[j+1]):
                des += 1
        dictionary_pos_des[des].append(perm)
    return dictionary_pos_des

def make_dict_neg(n, j,k,dictionary_neg):
    dictionary_neg_des = {}
    for des in range(0, n+1):
        dictionary_neg_des[des] = []
    for perm in dictionary_neg[j]:
        des = 0
        for j in range(0, len(perm)-1):
            if (perm[j] > perm[j+1]):
                des += 1
        dictionary_neg_des[des].append(perm)
    return dictionary_neg_des
    
if __name__ == "__main__":
    main()
