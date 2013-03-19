#coding = gbk
# encoding: utf-8
import os
import xlrd

class CReadXlsFile(object):
    def __init__(self,xl_path):
        self.xl_path = xl_path
        self.xl_table = []
        self._read_xls()
        pass
    
    def _init_log(self):
        logger = logging.getLogger()
        if not os.path.exists("./log/"):
            os.mkdir("./log/")
        log_fh = logging.FileHandler('log/output_log.txt')
        formatter = logging.Formatter('%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s')
        log_fh.setFormatter(formatter)
        logger.addHandler(log_fh)
        #logger.setLevel(logging.NOTSET)
        logger.setLevel(logging.INFO)
        self.logger = logger

    def _read_xls(self):
        work_book = xlrd.open_workbook(self.xl_path)
        work_sheet_names = work_book.sheet_names()
        work_sheet = work_book.sheet_by_index(1)
        nrows = work_sheet.nrows
        ncols = work_sheet.ncols
        xl_table = []
        # kick off table headlines
        for r in nrows-1:
            xl_table[r] = list(work_sheet.cell(rowx=r+1,colx=c).value for c in ncols) 
        
        # format cell of table
        convert_dic = {r"卖盘":'S',r"买盘":'B', r"中性盘":'SB'}
        for r in nrows-1:
            xl_table[r][5] = convert_dic.get(xl_table[r][5])
            if xl_table[r][2] == '--':
                xl_table[r][2] = ''

        
        self.xl_table = xl_table
        print 'read_xls end...'

    def get_xl_table(self):
        return self.xl_table


