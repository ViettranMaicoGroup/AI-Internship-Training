'''
Câu 3: Viết hàm xuất ra màn hình một kim tự tháp có tham số truyền vào bằng số tầng, tầng dưới sẽ ít hơn tầng trên.
VD: tham số truyền vào là 3
                    * * * * *
                      * * *
                        *
'''

def drawing_pyramid(n):
    for i in range(n, 0, -1):
        s = n - i
        k = s * " "
        print(k, end='')
        print(((2 * i) - 1) * '*')

if __name__ == '__main__':
    drawing_pyramid(3)