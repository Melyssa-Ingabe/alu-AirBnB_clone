#!/usr/bin/python3
from models.tmp_base_model import *
from models.tmp_base_model import BaseModel

class BaseModelSub(BaseModel):
    def save(self):
        try:
            self.updated_at = datetime.utcnow()
            print("OK")
        except Exception as e:
            print(f"Error: {e}")

b = BaseModelSub()
b.save()
