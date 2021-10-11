import numpy as np


def matrix_multiplier(matrix_a, matrix_b):
    return matrix_a@matrix_b

def find_matrix_b(matrix_a):
    matrix_a[matrix_a % 2 == 0] = 1
    matrix_a[matrix_a !=1] = 0
    return matrix_a
def check_prime_num(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return 1
    else:
        return 0
def check_diagonal_primes(matrix_a):
    matrix_a_flip = np.fliplr(matrix_a)
    diag_of_a_flip = matrix_a_flip.diagonal()
    vfunc = np.vectorize(check_prime_num)
    return (diag_of_a_flip, np.count_nonzero(vfunc(diag_of_a_flip)))

if __name__ == "__main__":
    np.random.seed(42)
    #a
    matrix_1  = np.random.rand(3, 4)
    matrix_2 = np.random.rand(4, 4)
    print(matrix_multiplier(matrix_1, matrix_2))
    #b
    matrix_a = np.random.randint(1, 10, (4, 4))
    print(find_matrix_b(matrix_a))
    #c
    (diag, count) = check_diagonal_primes(matrix_a)
    print(diag)
    print(count)


