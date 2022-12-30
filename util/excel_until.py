#coding = utf-8

import xlrd

class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = "F:/selenium_python_DataDriver/config/ddtexcel.xls"
        if index == None:
            index = 0    
        self.data = xlrd.open_workbook(excel_path)    # 打开Excel文件读取数据
        self.table = self.data.sheets()[index]        # 获取excel中第[index-1]表格； 如：self.data.sheets()[0]获取第一个sheet表格
        self.rows = self.table.nrows                  # 获取行数


    def get_data(self):
        result=[]
        for i in range(self.rows):
            table_list = self.table.row_values(i)                  # 获取第i行数据； 如table.row_values(rowx=0, start_colx=0, end_colx=None) 获取指定行中的数据并以列表的形式返回    
            result.append(table_list)
        return result










