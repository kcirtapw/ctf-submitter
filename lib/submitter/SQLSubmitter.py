from .Submitter import Submitter

from sqlalchemy.ext.sqlsoup import SqlSoup

class SQLSubmitter (Submitter):
    def __init__(self, con_string):
        self._soup = SqlSoup(con_string)

    def _proc_flag(self, flag):
