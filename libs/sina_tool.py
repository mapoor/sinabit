#coding = gbk
# encoding: gbk

import optparse
import readxls
from common import *


if __name__ == '__main__':
    parser = optparse.OptionParser('%prog  [options] arg1  arg2')
    parser.add_option('-t', '--today',
                        help = 'import detail data of stock code to db',
                        action = 'store_true', dest = "is_today")

    parser.add_option('-d', '--date',
                        help = 'import detail data to db of specific date',
                        action = 'store', type='string', metavar='DATE',
                        dest = "sp_date")

    parser.add_option('-c', '--code',
                        help = 'import detail data to db of specific stock code',
                        action = 'store', type='string', metavar='STKCODE',
                        dest = "stk_code")
 
    parser.add_option('-q', '--query',
                        help = 'query detail recode of specific stock',
                        action = 'store_false', dest = "is_query")
    options, args = parser.parse_args()

    if (not (options.is_today is None) ^ (options.sp_date is None)):
        parser.print_help()

    if options.stk_code is not None: 
        if options.is_today is True:
            tup_ret = downxls(options.stk_code)
        else:
            tup_ret = downxls(options.stk_code, sp_date)
        xls = getfpath(options.stk_code)
        rdxls = CReadXlsFile(xls)
        recodes = rdxls.get_xl_table()
        db = CDataBase()
        db.create(gettbname())
        db.insert_all(recodes)

#    if options.stk_code_q is not None:
   
