#coding=gbk
# encoding:gbk

from common import normpath
import sqlite3 as sqlite


DEAL_DETAIL_FIELDS = [
    ('id',           'integer primary key'),
    ('time_deal',    'text not null'),
    ('price_deal',   'real not null'),
    ('price_change', 'real not null'),
    ('amount_deal',  'text not null'),
    ('money_deal',   'text not null'),
    ('who_deal',     'integer not null'),
]
DEAL_DETAIL_KEYS = [f[0] for f in DEAL_DETAIL_FIELDS]


class CDataBase(object):

    def __init__(self, timeout=5.0):
        self.__connection = sqlite.connect('/db/library.db', timeout)
        self.__connection.text_factory = str
        self.__cursor = self.__connection.cursor()

    def create(self, table):
        setup_sql = "CREATE TABLE IF NOT EXISTS %s ("
        setup_sql += ', '.join([("%s %s"%f[:2]) for f in DEAL_DETAIL_FIELDS])
        setup_sql += ");"
        self.__cursor.execute(setup_sql)

    def insert(self, table, values):
        skey = ', ',join(DEAL_DETAIL_KEYS[1:])
        query = "INSERT INTO %s (%s) VALUES(?,?,?,?,?,?)" % (table, skey)
        self.__cursor.execute(query, tuple(values))

    def drop(self, table):
        query = "DROP TABLE [%s]" % (table)
        self.__cursor.execute(query)

    def count_wh(self, table, cmd):
        query = 'SELECT COUNT(*) FROM %s WHERE %s' % (table, cmd)
        self.__cursor.execute(query)
        return self.__cursor.fetchone()[0]

    def select_wh(self, table, cmd):
        query = 'SELECT name FROM %s WHERE %s' % (table, cmd)
        self.__cursor.execute(query)
        return self.__cursor.fetchall()


