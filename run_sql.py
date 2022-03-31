import os
from django.db import connection
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

def my_custom_sql(sql_file_name):

    with connection.cursor() as cursor:
        sql_file = open(sql_file_name,encoding='UTF-8')
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)

def make_fake_id_column(table_name):
    with connection.cursor() as cursor:
        column_name = 'fake_id'
        
        sqlite_script = f'''
        ALTER TABLE {table_name} ADD COLUMN {column_name} INT;
        UPDATE {table_name} SET {column_name}=0;
        '''

        cursor.executescript(sqlite_script)


make_fake_id_column("bible_korHRV")
        
my_custom_sql("korHRV.sql")


