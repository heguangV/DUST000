def read_file(filename):
    """接收一个文件名为参数，数据类型为字符串类型，文件编码为utf-8，
    返回值为列表，列表元素为将文件每一行根据逗号切分成的列表"""
    with open(filename, 'r', encoding='utf-8') as file: 
        file_to_list = [line.strip().split(',') for line in file] 
# 文件全部内容读取出来放入列表中，每个元素为一行字符串
    return file_to_list             # 以列表形式返回文件中的数据
####### END HELPER FUNCTIONS ####################


def student_id(ls_student, ls_school, ls_major): 
    """参数为三个文件对象，依序分别由读学生信息、学院信息和专业信息文件获得。返回值为列表，为包含了新生成的学号的学生信息列表。"""
    student_detail=[]
    for x in range(0,len(ls_student)): 
        if ls_student[x][1] == '男' or ls_student[x][1] == '女':# 取出学生信息
            birth_year = ls_student[x][5][-2:]  # 取出生年份
            for y in range(0,len(ls_school)):
                if ls_student[x][2] == ls_school[y][0]:
                    school_code = ls_school[y][1]  # 取学院代码
                    break
            for z in range(0,len(ls_major)):
                if ls_student[x][3] == ls_major[z][0]:
                    major_code = ls_major[z][1]  # 取专业代码
                    break
            class_code = ls_student[x][4][-4:]  # 取班级代码 
            rank = 1
        for xx in range(x):
            if ls_student[xx][4] == ls_student[x][4]:
                rank += 1
        student_id = f"012{birth_year}{school_code}{major_code}{class_code}{rank:02d}"
        student_with_id = [student_id] + ls_student[x] 
        student_detail.append(student_with_id)
    return student_detail      # 返回加了学号的学生信息列表


def student_info(stu_name, ls_student):
    """参数为学生名字字符串和学生的信息列表，返回值为该学生的详细信息"""
    for x in range(0,len(ls_student)):
        if stu_name == ls_student[x][1]:
            return ls_student[x]


def classmate(stu_class, ls_student):
    """参数为学生班级和学生信息列表，返回值为同班同学的信息列表"""
    a=[]
    for x in range(0,len(ls_student)): 
        if stu_class == ls_student[x][5]:
            a.append(ls_student[x])
    return a



if __name__ == '__main__':
    stuName = input()                                                  # 输入学生姓名
    stuClass = input()                                                 # 输入班级
    student_list = read_file('studentList.csv')[1:]             # 获得学生信息列表
    school_code = read_file('schoolCode.csv')                   # 获得学院信息列表
    major_code = read_file('MajorCode.csv')                     # 获得专业信息列表
    studentDetail = student_id(student_list, school_code, major_code)  # 调用函数计算ID并插入到列表中
    print(*student_info(stuName, studentDetail))                       # 输出学生信息
    ls_classmate = classmate(stuClass, studentDetail)                  # 返回同班同学信息列表
    for classmate in ls_classmate:                                     # 逐个输出同学信息
        print(*classmate)