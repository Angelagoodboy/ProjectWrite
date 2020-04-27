from  tkinter import filedialog
import  OpenFile,struct
import struct

def get_BMWSTM32():
    return  0b000001
def get_BMW8823():
    return  0b000010
def get_Audi_high():
    return  0b010000
def get_Audi_low():
    return 0b010001
def get_Audi_Q7():
    return 0b010010
def get_LEUX():
    return 0b010100
def get_BMW_NBT():
    return 0b011000
def get_BMW_CIC():
    return 0b011001
def get_benz_1():
    return 0b011100
def get_benz_2():
    return 0b011101


    #字典方式实现switch#
    #"宝马STM32F105RBT6", "宝马8823", "8368奥迪高配", "8368奥迪低配","8368奥迪Q7换屏","8368雷克萨斯","8368宝马NBT","8368宝马CIC","8368奔驰1" "8368奔驰2"

switcher={
    '宝马STM32F105RBT6': get_BMWSTM32(),
    '宝马8823':get_BMW8823(),
    '8368奥迪高配':get_Audi_high(),
    '8368奥迪低配':get_Audi_low(),
    '8368奥迪Q7换屏':get_Audi_Q7(),
    "8368雷克萨斯":get_LEUX(),
    '8368宝马NBT':get_BMW_NBT(),
    '8368宝马CIC':get_BMW_CIC(),
    '8368奔驰1':get_benz_1(),
    '8368奔驰2':get_benz_2()



    }
def intToBytes(value, length):
    result = []
    for i in range(0, length):
        result.append(value >> (i * 8) & 0xff)
    result.reverse()
    return result
class CommboxEvent:


    Folderpath = ''

    head = intToBytes(0xff55,2)  # 头
    data_frame_length = intToBytes(0x99,1)   # 数据帧总长度
    cmd = intToBytes(0x86,1)  # 命令位cmd
    command_class = intToBytes(0x0000000,4)  # 命令类容4字节
    written_head = 'GPMCU_H'.encode('utf-8')
    writeen_bit =bytes(3)  # 根据车型的可变解码器号3字节
    target=bytes(16)


    def _init_(self):
            print('')

    def comboxselectEvent(self,value):
        #完成数据准备

        print('选择下拉列表框值为',value)
        self.writeen_bit=bin(switcher[value])
        self.target=struct.pack(bin(0xff55),bin(0x99),bin(0x86),bin(0x0000000),self.written_head,self.writeen_bit)

        print('self.target')


        print(self.target)


    def btn_browse(self):

        print('浏览文件夹')
        self.Folderpath = filedialog.askdirectory()
        #print('浏览文件夹',Folderpath)
    def btn_configure(self):

        print('点击按钮')


        '写入到文件'
        TargetData=OpenFile.readFile(OpenFile.file_path,self.target)
        TARGET_PATH=OpenFile.getFile_target_path(OpenFile.file_path,self.Folderpath)
        OpenFile.writeFile(TARGET_PATH,self.target)


