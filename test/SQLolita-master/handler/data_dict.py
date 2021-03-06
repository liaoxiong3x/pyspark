# coding=utf-8
# Created by Tian Yuanhao on 2016/4/12.
from frontend.nodes import AttrType


class DataDict:
    def __init__(self, file_path):
        self.dict = {"A": AttrType("age", "INT", "0")}
        self.file_path = file_path
        self.load_data()

    def has_table(self, table_name):
        if table_name in self.dict.keys():
            return True
        else:
            return False
        # return self.dict.has_key(table_name)

    def table_attr_names(self, table_name):
        return [attr.attr_name for attr in self.dict[table_name] if attr.attr_type != "PK"]

    def attr_type(self, table_name, attr_name):
        return self.dict[table_name].attr_type

    def tables_name(self):
        return self.dict.keys()

    def load_data(self):
        f = open(self.file_path, "a+")
        table_name = "default"
        while True:
            line = f.readline()
            if not line: break
            if len(line) == "\n": continue

            if line[0] == '[':
                table_name = line[1:-2]
            elif len(line) > 1:
                items = line[:-1].split()
                if not self.dict.has_key(table_name):
                    self.dict[table_name] = [AttrType(*items)]
                else:
                    self.dict[table_name] += [AttrType(*items)]
        f.close()

    def write_back(self):
        text = ""
        for key, val in self.dict.items():
            text += "[" + key + "]\n"
            for type in val: text += str(type) + "\n"
            text += "\n"
        f = open(self.file_path, "w")
        f.write(text)
        f.close()


if __name__ == '__main__':
    data = DataDict("../database/dict.txt")
    # print data.tables_name()

    # data.dict = {
    #     "A" : [AttrType("age", "INT", 0), AttrType("name", "CHAR", 10)],
    #     "B" : [AttrType("age", "INT", 0), AttrType("name", "CHAR", 10), AttrType("age", "PK", 0)]
    # }
    # data.write_back()

