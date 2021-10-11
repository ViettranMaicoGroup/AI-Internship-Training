'''
Câu 2: Viết hàm tìm bội chung nhỏ nhất, có tham số truyền vào là 2 số nguyên dương và
trả về bội chung nhỏ nhất của 2 số đó.
'''

def find_lcm(a,b):
    if not (a > 0 and b >0):
        print("Invalid number!")
    if a == 0 or b == 0:
        return 0
    else:
        multiplier = a * b
        for i in range(1, multiplier + 1):
            if i % a == 0 and i % b == 0:
                return i
if __name__ == '__main__':
    a  = int(input("Enter number a: "))
    b = int(input("Enter number b: "))

    print(f"LCM of {a} and {b} is: {find-lcm(a,b)}")
