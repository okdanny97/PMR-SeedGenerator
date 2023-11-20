import xml.etree.ElementTree as ET

from peewee import *
from playhouse.migrate import *
from .db import db
from .map_meta import MapMeta


class MapArea(Model):
    area_id = IntegerField()
    map_id = IntegerField()
    ordering = IntegerField()

    name = CharField(null=True)
    verbose_name = CharField(null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_verbose_name(cls, name) -> str:
        verbose_name = MapMeta.get(MapMeta.name == name).verbose_name
        return verbose_name

    class Meta:
        database = db
