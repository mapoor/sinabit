#coding=gbk
# encoding:gbk

import os
import time
import urllib

SINA_URL = "http://market.finance.sina.com.cn/downxls.php?date=%s&symbol=%s"
SAVE_POS = "sina_download_xls"

def abspath(path):
    """Provide the canonical form of the path suitable
    """
    return os.path.abspath(os.path.realpath(path))

def getdate():
    """Get current date and format output %Y-%m-%d
    """
    return time.strftime("%Y-%m-%d", time.localtime())

def gettbname(code):
    """Get table name
    """
    sdate = getdate().replace('-','')
    return "t_%s_%s" % (code, sdate)

def getfname(code):
    """Get xls filename
    """
    sdate = getdate().replace('-','')
    return "%s_%s.xls" % (code, sdate)

def getfpath(code):
    """Get xls filepath
    """
    return os.path.join(abspath(SAVE_POS), getfname(code))

def downxls(code, date=None):
    """Download specific file from dn_url and save file in sv_url
    """
    dn_url = ""
    if date is None:
        dn_url = SINA_URL % (getdate(), code)
    else:
        sp_date = "%s%s%s"%(date[:4],date[4:6],date[6:])
        dn_url = SINA_URL % (sp_date, code)
    sv_url = getfpath(code)
    return urllib.urlretrieve(dn_url, sv_url)

