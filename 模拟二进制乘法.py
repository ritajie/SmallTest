'运算器的乘法是通过加法和移位实现的，这里尝试模拟一下"二进制的乘法"
2018/9/28 22:00 哈尔滨 路小鹿'


def to2(num):
    ''' 十进制转二进制
        参数类型int，返回长度为8的字符串：00001111'''
    return bin(num)[2::].zfill(8)


def to10(num):
    ''' 二进制转十进制
        参数长度为8的字符串，返回int'''
    return int(num, 2)


def Cheng(num1, num2):
    # 1.转成二进制
    num1_2 = to2(num1)
    num2_2 = to2(num2)
    # 2.进行二进制的乘法
    # 2.1新建8个字符串，每个字符串要么是num1_2+'0'*index，要么是‘00000000’
    sum_arr = list()
    for index, ch in enumerate(num2_2[::-1]):
        if ch == '0':
            sum_arr.append('00000000')
        elif ch == '1':
            sum_arr.append(num1_2+'0'*index)
    # 2.2对sum_arr里的八个字符串进行错位相加，得出一个粗糙的二进制结果：00004321
    fake_ans = [0]*8
    for index, s in enumerate(sum_arr):
        # s: 00001010
        for i in [-1, -2, -3, -4, -5, -6, -7, -8]:
            fake_ans[i] = int(fake_ans[i])+int(s[i])
    # 2.3完美fake_ans
    for i in [-1, -2, -3, -4, -5, -6, -7, -8]:
        if fake_ans[i] > 1:
            # 需要进位的数
            temp = int(fake_ans[i] / 2)
            fake_ans[i] %= 2
            fake_ans[i-1] += temp
        # print(i, fake_ans)

    return to10(''.join([str(i) for i in fake_ans]))


if __name__ != '__main__':
    Cheng(3, 3)


if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f'{i}*{j}={Cheng(i, j)}', end='\t')
        print()


