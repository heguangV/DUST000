import string

def read_file(file):
    """接收文件名为参数，读取文件中的数据到字符串中，返回这个字符串"""
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def classify_char(txt):
    """接收字符串为参数，依序返回大写字母、小写字母、数字、空格、和其他字符数量"""
    upper, lower, digit, space, other = 0, 0, 0, 0, 0
    for ch in txt:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
        elif ch.isdigit():
            digit += 1
        elif ch.isspace():
            if ch == ' ':
                space += 1
            else:
                other += 1
        else:
            other += 1

    return upper, lower, digit, space, other

if __name__ == '__main__':
    filename = input()              # 读入文件名
    text = read_file(filename)      # 调用函数读文件中的内容为字符串
    classify = classify_char(text)  # 调用函数分类统计字符数量
    print('大写字母{}个,小写字母{}个,数字{}个,空格{}个,其他{}个'.format(*classify))