import  os

from tkinter import filedialog
global file_path

file_path=''
global tmp
tmp=bytes(1024)


def openbinFile():

    '打开文件'
    global file_path

    file_path = filedialog.askopenfilename(title='选择文件',initialdir=(os.path.expanduser('C:/')),filetypes=[('BIN', 'bin')])
    print('打开文件：', file_path)
    return file_path



def readFile(file_path,data):
    global tmp
    '读入文件'
    if file_path is not None:
        with open(file_path, mode='rb') as file:
            #读出原来的内容
            print(file.name)
            filedata= file.read()
            tmp=filedata
            print(tmp)

            file.close()

def getFile_target_path(file_path,Folderpath):
    path=os.path.dirname(file_path)
    filename=file_path[len(path):]
    targetpath=Folderpath+'/'+filename
    return  targetpath

def writeFile(file_target_path,data):

    global tmp
    if file_target_path is not None:
            fo=open(file_target_path,'wb')
            print(tmp)
            fo.write(data)
            fo.write(tmp)

            print('写入成功')
            fo.close()





            # file.write(data)
            # file.append(tmp)

