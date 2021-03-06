import json

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase

from common.config import *

db = SqliteExtDatabase(getConfig().get("database_file"))

class BaseModel(Model):
    class Meta:
        database = db
        
    def __str__(self):
        r = {}
        for k in self._data.keys():
          try:
             r[k] = str(getattr(self, k))
          except:
             r[k] = json.dumps(getattr(self, k))
        return str(r)        

def getDb():
    return db;
        