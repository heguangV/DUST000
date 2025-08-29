def leap(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判断这个日期中的年份是否为闰年
    返回值为布尔型。
    @参数 current_date：表示日期，字符串类型
    闰年的判定方法是：能被400整除或能被4整除且同时不能被100整除的是闰年。
    """
    year = int(current_date[:4])
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False



def legal_judge(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判定日期的合法性，返回值为布尔型。
    1，3，5，7，8，10，12月各31天，4，6，9，11各30天，闰年2月29天，平年2月28天。
    @参数 current_date：表示日期，字符串类型
    """
    year = int(current_date[:4])
    month = int(current_date[4:6])
    day = int(current_date[6:8])
    if month < 1 or month > 12:
        return False
    if day < 1:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return False
    elif month == 2:
        if leap(current_date):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True



def days_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，若月份合法，返回这个月份有多少天的整数，
    否则返回字符串"'**月份数字不合法'"，**表示月份。
    参数 current_date：表示日期，字符串类型
    """
    month = int(current_date[4:6])
    if month < 1 or month > 12:
        return f'{month}月份数字不合法'
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if leap(current_date):
            return 29
        else:
            return 28



def name_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，返回这个月份对应的英文单词及其缩写形式。
    9月缩写为'Sept.',此时返回值为：'September','Sept.'
    """
    month = int(current_date[4:6])
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    month_abbrs = [
        "Jan.", "Feb.", "Mar.", "Apr.", "May", "Jun.",
        "Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."
    ]
    if 1 <= month <= 12:
        return month_names[month - 1], month_abbrs[month - 1]



def separate_date(current_date, symbol):
    """接收一个用8个字符表示日期的字符串和一个符号为参数，返回用该符号分隔的日期，字符串类型。
    @参数 current_date：表示日期，字符串类型
    @参数 symbol：分隔符号，字符串类型
    例如传入'20201031'和"/",返回字符串'2020/09/09'
    """
    year = current_date[:4]
    month = current_date[4:6]
    day = current_date[6:8]
    return f'{year}{symbol}{month}{symbol}{day}'



def test(current_date):
    if leap(current_date):
        print(f'{current_date[:4]}年是闰年')
    else:
        print(f'{current_date[:4]}年不是闰年')
    days = days_of_month(current_date)
    print(f'{current_date[:4]}年{int(current_date[4:6])}月有{days}天')
    print(separate_date(current_date, sign))
    if legal_judge(current_date):
        print(f'{current_date}是合法日期')
    else:
        print(f'{current_date}是非法日期')
    month_name, month_abbr = name_of_month(current_date)
    print(f'{int(current_date[4:6])}月英文是{month_name}，缩写为{month_abbr}')


if __name__ == '__main__':
    CurrentDate = input()
    sign = input()
    test(CurrentDate)