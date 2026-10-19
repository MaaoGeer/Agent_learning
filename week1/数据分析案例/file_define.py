"""
    和文件相关的类定义
"""
import json

from data_define import Record


# 首先定义一个抽象类，确定需要那些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件数据，读到的每一条数据转为Record对象，将他们封装到list内返回即可"""
        pass


class TextReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件路径

    # 复写父类方法(实现抽象方法)
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f:
            line = line.strip()  # 消除读取到的每一行的/n
            data_list = line.split(",")
            record_list.append(Record(data_list[0], data_list[1], int(data_list[2]), data_list[-1]))

        f.close()
        return record_list


class JsonReader(FileReader):
    def __init__(self, path):
        self.path = path  # 定义成员变量，记录文件路径

    # 复写父类方法(实现抽象方法)
    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list: list[Record] = []
        for line in f:
            data_dict = json.loads(line)
            record_list.append(
                Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"]))

        f.close()
        return record_list


if __name__ == '__main__':
    test_file_reader = TextReader("E:/pytest/pythonProject/数据分析案例/2011年1月销售数据.txt")
    json_file_reader = JsonReader("E:/pytest/pythonProject/数据分析案例/2011年2月销售数据JSON.txt")
    list1 = test_file_reader.read_data()
    list2 = json_file_reader.read_data()
    for line in list1:
        print(line)
