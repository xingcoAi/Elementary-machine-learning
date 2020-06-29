#文件有打开有关闭
def read_file1():
    f = open("task_37.py", "r", encoding = "UTF-8")
    #print(f.read())#一次性读取所有内容,缺点为文件太大时占用内存
   # print(f.read(10))#读取字符大小
    while True:
        z = f.read(10)
        print(z)
        if z is "":
            break

    f.close()
# read_file1()

#with open帮我们自动关闭文件的输入输出流
def read_file2(filename:str) -> None:#括号里说明传入的
    #文件名变量为字符串型,->None表示函数无返回值
    with open(filename, "r", encoding="UTF-8") as f:
        lines = f.readlines()
        print(lines)

# read_file2("task_37.py")

#文件的写操作
def write_file():
    with open("1.txt", "w", encoding="UTF-8") as f:
        for i in range(100):
            f.write(str(i))
            f.flush()#将内存(缓存区)的数据写入到磁盘上

write_file()