#coding=gbk
# encoding:gbk

import sys,os
import urllib
import common

def main(argv):
    """
        main
    """
    print common.normpath("files_of_down")

    print "start..."
    tup_ret = urllib.urlretrieve("http://market.finance.sina.com.cn/downxls.php?date=2012-10-19&symbol=sh600048"\
                      ,"f:\\coding\\python\\Python_Script\\sina_download_xls\\files_of_down\\test2_1.xls")

    print tup_ret

    print "end..."
	
if __name__=="__main__":
    main(sys.argv[1:])

