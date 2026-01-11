#!/usr/bin/python3
from models.tmp_base_model import *
from models.tmp_base_model import BaseModel

class BaseModelSub(BaseModel):
    def save(self):
        # This will fail IF datetime is not imported via *
        self.updated_at = datetime.utcnow()

try:
    b = BaseModelSub()
    b.save()
    print("OK")
except Exception as e:
    # If it crashes before print, we get 0 chars
    pass
