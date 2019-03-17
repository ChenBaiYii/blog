#!/usr/bin/python3
#

from peewee import SqliteDatabase, Model, CharField, DateField, TextField

db = SqliteDatabase('people.db')


class PersonInfo(Model):
    name = CharField()
    birthday = DateField()
    location = CharField()
    info = TextField()

    class Meta:
        database = db



