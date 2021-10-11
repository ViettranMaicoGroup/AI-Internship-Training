'''
Câu 1: Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không phải bội số của 5,
nằm trong đoạn 2000 và 3200 (tính cả 2000 và 3200). Các số thu được sẽ được in thành chuỗi
rên một dòng, cách nhau bằng dấu phẩy.
'''
import math


def ex1():
    nums = []
    for num in range(2000, 3021):
        if num % 7 == 0 and num % 5 != 0:
            nums.append(str(num))
    print(','.join(nums))

'''
Câu 2: Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi
trên một dòng, phân tách bởi dấu phẩy. Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320.
'''
def ex2(n):
    if n ==0:
        return 1
    if n == 1:
        return 1
    return n*ex2(n-1)

'''
Câu 3: Với số nguyên n nhất định, hãy viết chương trình để tạo ra một dictionary chứa (i, i*i) như là số nguyên 
từ 1 đến n (bao gồm cả 1 và n) sau đó in ra dictionary này. 
Ví dụ: Giả sử số n là 8 thì đầu ra sẽ là: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}.
'''

def ex3(n):
    dict = {}
    for i in range(1, n+1):
        dict[i] = i*i
    return dict

'''
Câu 4: Viết chương trình chấp nhận một chuỗi số, phân tách bằng dấu phẩy từ giao diện điều
khiển, tạo ra một danh sách và một tuple chứa mọi số.
Ví dụ: Đầu vào được cung cấp là 34,67,55,33,12,98 thì đầu ra là:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
def ex4():
    input_string = input("Nhập vào chuỗi số:")
    nums = input_string.split(',')
    nums = tuple(nums)
    print(nums)
'''
Câu 5 :
Định nghĩa một class có ít nhất 2 method:
getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class.
Ví dụ: Chuỗi nhập vào là quantrimang.com thì đầu ra phải là: QUANTRIMANG.COM
'''
class ConvertString_ex5(object):
    def __init__(self):
        self.input_string= '';
    def input(self):
        self.input_string = input("Enter string:");

    def printString(self):
        print(self.input_string.upper())

'''
Câu 6: 
Viết một method tính giá trị bình phương của một số.
Gợi ý:
● Sử dụng toán tử **.
'''
def ex6(n):
    return n**2

'''
Câu 7: Python có nhiều hàm được tích hợp sẵn, nếu không biết cách sử dụng nó, bạn có thể đọc tài liệu trực tuyến
hoặc tìm vài cuốn sách. Nhưng Python cũng có sẵn tài liệu về hàm cho mọi hàm tích hợp trong Python. 
Yêu cầu của bài tập này là viết một chương trình để in tài liệu về một số hàm Python được tích hợp sẵn như abs(), int(), 
input() và thêm tài liệu cho hàm bạn tự định nghĩa.
'''

def ex7(n):
    #test
    # print(abs.__doc__)
    '''
     Return the square value of the argument
    '''
    return n*n

'''
Định nghĩa một lớp gồm có tham số lớp và có cùng tham số instance
Gợi ý:
- Khi định nghĩa tham số instance, cần thêm nó vào __init__
- Bạn có thể khởi tạo một đối tượng với tham số bắt đầu hoặc thiết lập giá trị sau đó.
'''
# Tham khảo từ link colab
class Person:
    #Định nghĩa class "name"
    name = "Person"

    def __init__(self, name = None):
        #self.name là biến instance
        self.name = name

'''
Câu 9: Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H]) (bằng chữ: Q bằng căn bậc hai của 
[(2 nhân C nhân D) chia H]. Với giá trị cố định của C là 50, H là 30. D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, 
các giá trị của D được phân cách bằng dấu phẩy.

Ví dụ: Giả sử chuỗi giá trị của D nhập vào là 100,150,180 thì đầu ra sẽ là 18,22,24.
'''
def ex9():
    C = 50
    H = 30
    # nums = input("Nhập vao dãy giá trị của D:").split(",")
    nums = [100,150,180]
    Qs = []
    for D in nums:
        Q = int(math.sqrt(((2 * C * int(D)) / H)))
        Q = str(Q)
        Qs.append(Q)
    print(",".join(Qs))

'''
Câu 10: Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một mảng 2 chiều. 
Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j.
Lưu ý: i=0,1,...,X-1; j=0,1,...,Y-1.
Ví dụ: Giá trị X, Y nhập vào là 3,5 thì đầu ra là: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
def ex10():
    rows = input("Input rows: ")
    columns = input("Input colums: ")
    array = [[0 for col in range(int(columns))] for row in range(int(rows))]

    for i in range(int(rows)):
        for j in range(int(columns)):
            array[i][j] = i*j
    return array

'''
Câu 11: Viết một chương trình chấp nhận chuỗi từ do người dùng nhập vào, phân tách nhau bởi dấu phẩy và in những từ đó 
thành chuỗi theo thứ tự bảng chữ cái, phân tách nhau bằng dấu phẩy.
Giả sử đầu vào được nhập là: without,hello,bag,world, thì đầu ra sẽ là: bag,hello,without,world.
'''
def ex11():
    inputs = [ inp for inp in input("Enter words:  ").split(",")]
    inputs.sort()
    print(inputs)

'''
Câu 12: Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa 
và in ra màn hình. Giả sử đầu vào là:
Hello world
Practice makes perfect

Thì đầu ra sẽ là:

HELLO WORLD
PRACTICE MAKES PERFECT
'''
def ex12():
    lines = []
    print("Enter string: ")
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    for line in lines:
        print(line.upper())

'''
Câu 13: Viết một chương trình chấp nhận đầu vào là một chuỗi các từ tách biệt bởi khoảng trắng, loại bỏ các từ trùng lặp, 
sắp xếp theo thứ tự bảng chữ cái, rồi in chúng.

Giả sử đầu vào là: hello world and practice makes perfect and hello world again

Thì đầu ra là: again and hello makes perfect practice world
'''

def ex13():
    words = [word for word in input("Enter String:").split(" ")]
    words = list(set(words))
    words.sort()
    print(" ".join(words))

'''
Câu 14: Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, 
kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.

Ví dụ đầu vào là: 0100,0011,1010,1001

Đầu ra sẽ là: 1010
'''
def ex14():
    values = []
    inputs = [x for x in input("Enter binary strings: ").split(',')]
    for p in inputs:
        intp = int(p, 2) ###
        if not intp % 5:
            values.append(p)

    print(','.join(values))

'''
Câu 15: Viết một chương trình tìm tất cả các số trong đoạn 1000 và 3000 (tính cả 2 số này) sao cho tất cả các chữ số trong 
số đó là số chẵn. In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
'''

def ex15():
    values = []
    for i in range(1000,3001):
        i = str(i)
        if (int(i[0]) %2 == 0) and (int(i[1]) % 2 == 0) and (int(i[2]) % 2 == 0) and (int(i[3]) % 2 == 0):
            values.append(i)

    print(','.join(values))

'''
Câu 16:
Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong
câu đó. Giả sử đầu vào sau được cấp cho chương trình: hello world! 123
Thì đầu ra sẽ là:
Số chữ cái là: 10
Số chữ số là: 3
'''
def ex16():
    string = input("Nhập vào chuỗi: ")
    words = 0
    numbers  = 0
    for word in string:
        if(word.isalpha()):
            words+=1
        if(word.isdigit()):
            numbers+=1
    print(f'Số chữ cái là {words}')
    print(f'Số chữ số là: {numbers}')

'''
Câu 17:
Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường.

Giả sử đầu vào là: Quản Trị Mạng
Thì đầu ra là:
Chữ hoa: 3
Chữ thường: 8
Gợi ý:
Trong trường hợp dữ liệu đầu vào được nhập vào chương trình nó nên được giả định
là dữ liệu được người dùng nhập vào từ giao diện điều khiển.
'''
def ex17():
    string = input("Nhập vào chuỗi: ")
    lower = 0
    upper = 0
    for word in string:
        if (word.islower()):
            lower += 1
        if (word.isupper()):
            upper += 1
    print(f'Số chữ thường là {lower}')
    print(f'Số chữ hoa là: {upper}')

'''
Câu 18: Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng.
Giả sử a được nhập vào là 1 thì đầu ra sẽ là: 1234
'''
def ex18():
    a = int(input("Enter a number:"))
    n1 = a
    n2 = 10*a + a
    n3 = 100*a + 10*a + a
    n4 = 1000*a + 100*a + 10*a + a
    print(n1 + n2 + n3 + n4)

'''
Câu 19: Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào.
Giả sử đầu vào là: 1,2,3,4,5,6,7,8,9 thì đầu ra phải là: 1,3,5,7,9
'''

def ex19():
    string_num = input("Enter string: ")
    nums = [int(num) for num in string_num.split(",")]
    fixed_num = []
    for num in nums:
        if(num %2 == 1):
            fixed_num.append(str(num))
    # print(fixed_num)
    print(','.join(fixed_num))

'''
Câu 20: Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên nhật ký giao dịch được nhập vào từ giao diện điều khiển.

Định dạng nhật ký được hiển thị như sau:

D 100
W 200

(D là tiền gửi, W là tiền rút ra).

Giả sử đầu vào được cung cấp là:

D 300

D 300

W 200

D 100

Thì đầu ra sẽ là:

500
'''
def ex20():
    accountBalance = 0
    while True:
        string = input("Enter in transaction log: ")
        if not string:
            break
        values = string.split(" ")
        operator = values[0]
        numbers = int(values[1])
        if operator == "D":
            accountBalance += numbers
        if operator == "W":
            accountBalance -= numbers
        else:
            pass

    print(accountBalance)

'''
Câu 21:Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Viết chương trình để kiểm tra tính hợp lệ của 
mật khẩu mà người dùng nhập vào.
Các tiêu chí kiểm tra mật khẩu bao gồm:

Ít nhất 1 chữ cái nằm trong [a-z]
Ít nhất 1 số nằm trong [0-9]
Ít nhất 1 kí tự nằm trong [A-Z]
Ít nhất 1 ký tự nằm trong [$ # @]
Độ dài mật khẩu tối thiểu: 6
Độ dài mật khẩu tối đa: 12
Chương trình phải chấp nhận một chuỗi mật khẩu phân tách nhau bởi dấu phẩy và kiểm tra xem chúng có đáp ứng những tiêu chí trên hay không. Mật khẩu hợp lệ sẽ được in, mỗi mật khẩu cách nhau bởi dấu phẩy.

Ví dụ mật khẩu nhập vào chương trình là: ABd1234@1,a F1#,2w3E*,2We3345

Thì đầu ra sẽ là: ABd1234@1
'''
def ex21():
    import re
    passwords = input("Enter password: ")
    items = [word for word in passwords.split(",")]
    valid_passwords = []
    for item in items:
        if not re.search("[a-z]", item):
            continue
        if not re.search("[A-z]", item):
            continue
        if not re.search("[0-9]", item):
            continue
        if not re.search("[$ # @]", item):
            continue
        if len(item) < 6 or len(item)>12:
            continue
        else:
            pass
        valid_passwords.append(item)
    print(','.join(valid_passwords))

'''
Câu 22:
Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là
string, age và height là number. Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp
là:
Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên
> tuổi > điểm.
Nếu đầu vào là:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Thì đầu ra sẽ là:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''

def ex22():
    from operator import itemgetter
    words = []
    while True:
        string = input("Enter input: ")
        if not string:
            break
        words.append(tuple(string.split(",")))
    print(sorted(words, key=itemgetter(0,1,2)))

'''
Câu 23: Xác định một class với generator có thể lặp lại các số nằm trong khoảng 0 và n, và chia hết cho 7.
'''
def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

def ex23():
    n = int(input('Nhập số n: '))
    for i in putNumbers(n):
        print(i)

'''
Câu 24: Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên (0,0). Robot có thể di chuyển theo hướng UP, DOWN, LEFT và RIGHT 
với những bước nhất định. Dấu di chuyển của robot được đánh hiển thị như sau:

UP 5

DOWN 3

LEFT 3

RIGHT 3

Các con số sau phía sau hướng di chuyển chính là số bước đi. Hãy viết chương trình để tính toán khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, sau khi robot đã di chuyển một quãng đường. Nếu khoảng cách là một số thập phân chỉ cần in só nguyên gần nhất.

Ví dụ: Nếu tuple sau đây là input của chương trình:

UP 5
DOWN 3
LEFT 3
RIGHT 2

thì đầu ra sẽ là 2.
'''

def ex24():
    import math
    pos = [0, 0]
    while True:
        s = input("Enter road: ")
        if not s:
            break
        movement = s.split(" ")
        direction = movement[0]
        steps = int(movement[1])
        if direction == "UP":
            pos[0] += steps
        elif direction == "DOWN":
            pos[0] -= steps
        elif direction == "LEFT":
            pos[1] -= steps
        elif direction == "RIGHT":
            pos[1] += steps
        else:
            pass

    print(int(round(math.sqrt(pos[1] ** 2 + pos[0] ** 2))))

'''
Câu 25: Viết chương trình tính tần suất các từ từ input. Output được xuất ra sau khi đã sắp xếp theo bảng chữ cái.

Giả sử input là: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

Thì output phải là:

2:2

3.:1

3?:1

New:1

Python:5

Read:1

and:1

between:1

choosing:1

or:2

to:1
'''

def ex25():
    freq = {}
    line = input("Enter input: ")
    for word in line.split():
        freq[word] = freq.get(word, 0) + 1

    words = sorted(freq.keys())

    for w in words:
        print("%s:%d" % (w, freq[w]))

'''
Câu 26:Viết chương trình nhập một danh sách các số, sau đó in ra màn hình số lớn nhất và số nhỏ nhất trong danh sách.
Giả sử input là:  
3 8  10 15 4  
Thì output phải là:  
15  
3  

'''
def ex26():
    nums = input("Enter number string:")
    nums = [int(n) for n in nums.split()]

    print(max(nums))
    print(min(nums))
if __name__ == '__main__':

    # ex1() #Run ex1
    # print(ex2(8)) #Run ex2
    # print(ex3(8)) #Run ex3
    # ex4() #Run ex4
    #Run ex5
    # somethings = ConvertString_ex5()
    # somethings.input()
    # somethings.printString()
    #Run ex6
    # print(ex6(8))
    #Run ex7
    # print(ex7(8))
    # print(ex7.__doc__)
    #Run ex8
    # jeffrey = Person("Jeffrey")
    # print(f"{Person.name} name is {jeffrey.name}")
    #
    # nico = Person()
    # nico.name = "Nico"
    #
    # print(f"{Person.name} name is {nico.name}")
    #Run ex9
    # ex9()
    #Run ex10
    # print(ex10())
    #Run ex11
    # ex11()
    #Run ex12
    # ex12()
    #Run ex13
    # ex13()
    #Run ex14
    # ex14()
    #Run ex15
    # ex15()
    #Run ex16
    # ex16()
    #Run ex17()
    # ex17()
    #Run ex18()
    # ex18()
    #Run ex19
    # ex19()
    #Run ex20
    # ex20()
    #Run ex21
    # ex21()
    #Run ex22
    # ex22()
    #Run ex23
    # ex23()
    #Run ex24
    # ex24()
    #Run ex25
    # ex25()
    #Run ex26
    ex26()