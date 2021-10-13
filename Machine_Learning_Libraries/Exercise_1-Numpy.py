import numpy as np


def matrix_multiplier(A, B):
    return A@B


def find_matrix_b(A):
    A[A % 2 == 0] = 1
    A[A !=1] = 0
    return A


def check_prime_num(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return 1
    else:
        return 0


def check_diagonal_primes(A):
    A_FLIP = np.fliplr(A)
    diag_of_a_flip = A_FLIP.diagonal()
    vfunc = np.vectorize(check_prime_num)
    return (diag_of_a_flip, np.count_nonzero(vfunc(diag_of_a_flip)))


if __name__ == "__main__":
    np.random.seed(42) #make the randomness unchanged
    #a
    MATRIX_1  = np.random.rand(3, 4) #initilize a float matrix in range [0,1] with the shape (3, 4)
    MATRIX_2= np.random.rand(4, 4) #initilize a float second matrix in range [0,1] with the shape (4, 4)
    print(MATRIX_1)
    print(MATRIX_2)
    print(matrix_multiplier(MATRIX_1, MATRIX_2))
    #b
    MATRIX_A = np.random.randint(1, 10, (4, 4)) #initilize a integer matrix in range [1,10] with the shape (4, 4)
    print(MATRIX_A)
    print(find_matrix_b(MATRIX_A))
    #c
    (diag, count) = check_diagonal_primes(MATRIX_A)
    print(diag)
    print(count)


