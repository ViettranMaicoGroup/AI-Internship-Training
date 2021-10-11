'''
Câu 1: Viết hàm kiểm tra số nguyên tố, có tham số truyền vào là một số nguyên bất kì và trả về
True nếu đó là số nguyên tố, ngược lại trả về False.
'''

def check_prime_num(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input("Enter number to check: "))
    if check_prime_num(n) == True:
        print(f'{n} is prime number!')
    else:
        print(f'{n} is not prime number!')