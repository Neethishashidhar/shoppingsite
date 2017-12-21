import random
import string

from django.db import models


class OrderField(models.Field):

    def __init__(self, *args, **kwargs):
        self.max_length = 8
        self.auto_created = True
        self.editable = False
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'char(25)'

    def get_prep_value(self, value):
        con = string.ascii_letters + string.digits
        return ''.join(random.choice(con) for _ in range(8))
