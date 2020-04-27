import  os
from tkinter import filedialog
global file_path


def openbinFile():

    '打开文件'
    global file_path

    file_path = filedialog.askopenfilename(title='选择文件',initialdir=(os.path.expanduser('C:/')),filetypes=[('BIN', 'bin')])
    print('打开文件：', file_path)
    return file_path



def writeFile(file_path,data):
    '写入文件'
    tmp=bytes(1024)
    if file_path is not None:
        with open(file_path, mode='rb') as file:
            #读出原来的内容
            print(file.name)
            filedata= file.readline()
            temp=filedata
            print(filedata)


            # file.write(data)
            # file.append(tmp)

