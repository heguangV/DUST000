import string

def vigenere_encryption(text, key):
    """接收明文字符串和密钥字符串为参数，返回加密后的字符串.
    加密时字母和数字以外的其他字符原样输出。
    数字加密时，根据对应的密钥字符在字母表中的偏移量对10取模得到数字的偏移量。
    例如当前数字为1，对应的密钥字母是R,R的偏移量是17，对10取模为7，1 2 3 4 5 6 7 8 9 0 中序号为7的数字是8，加密结果即为8"""
    lower_tab = string.ascii_lowercase  # 小写字母
    upper_tab = string.ascii_uppercase  # 大写字母
    digit_tab = string.digits
    cypher = ""
    for x in text:
        if x in lower_tab:
            index = lower_tab.index(x)
            key_char = key[0]
            key = key[1:] + key_char
            key_index = lower_tab.index(key_char.lower())
            new_index = (index + key_index) % 26
            cypher = cypher + lower_tab[new_index]
        elif x in upper_tab:
            index = upper_tab.index(x)
            key_char = key[0]
            key = key[1:] + key_char
            key_index = upper_tab.index(key_char.upper())
            new_index = (index + key_index) % 26
            cypher = cypher + upper_tab[new_index]
        elif x in digit_tab:
            index = digit_tab.index(x)
            key_char = key[0]
            key = key[1:] + key_char
            if key_char.isalpha():
                key_index = (ord(key_char.lower()) - ord('a')) % 10
                new_index = (index + key_index) % 10
                cypher = cypher + digit_tab[new_index]
            else:
                new_index = key_char
                if new_index > 9:
                    new_index = new_index % 10
                cypher = cypher + digit_tab[new_index]
        else:
            cypher = cypher + x       
    return cypher
    


if __name__ == '__main__':
    secret_key = input()
    plain_text = input()
    plain_to_cipher_text = vigenere_encryption(plain_text, secret_key)
    print(f'加密后得到的密文是{plain_to_cipher_text}')