import sqlite3
import os
import sys
import hashlib
from passlib.hash import pbkdf2_sha256
from sqlite3 import Error


class DB:

    tables = []

    def __init__(self):
        self.conn = self.create_connection()
        self.reload_tables()

    def get_tables(self):
        return self.tables

    # Creates connection to the Database
    def create_connection(self):
        path = 'db/controller/my_db.db'
        con = None
        try:
            con = sqlite3.connect(path)
            print("Connection to SQLite DB was successful.")
        except Error as e:
            print(f"The error '{e}' occured.")

        return con

    # Reloads the tables and also updates tables data container as this is reliable info
    def reload_tables(self):
        self.init_data_containers()
        for x in self.tables:
            x = x + ".txt"
            if x == 'table_names.txt':
                continue
            tx = "db/controller/tables/" + x
            with open(tx, 'r') as fr:
                data = fr.read()
                self.execute_query(data)
                fr.close()
        print("Tables updated...")

    def drop_tables(self):
        for x in self.tables:
            self.execute_query("DROP TABLE " + x)

    def execute_query(self, query):
        cursor = self.conn.cursor()
        try:
            cursor.execute(query)
            self.conn.commit()
            print("Query was successfully executed.")
        except Error as e:
            print(f"The error '{e}' occurred")

    def execute_read_query(self, query):
        cursor = self.conn.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            if not result:
                raise Error('Your query returned no result...')
            else:
                return result
        except Error as e:
            print(e)

    def pb_sha256(self, t):
        return pbkdf2_sha256.hash(t, rounds=200000, salt_size=16)

    def verify_hash256(self, t, h):
        return pbkdf2_sha256.verify(t, h)

    def truncate_tables(self):
        for x in self.tables:
            self.execute_query("DELETE FROM %s;" % x)

    def reset(self):
        self.init_data_containers()
        self.truncate_tables()
        self.drop_tables()
        self.reload_tables()

    def init_data_containers(self):
        tbls = os.listdir('db/controller/tables')
        for x in tbls:
            if x == 'table_names.txt':
                continue
            self.tables.append(x.split(".")[0])

    def create_login(self):
        try:
            self.execute_query("INSERT INTO logins VALUES('%s', '%s');" % (
                input("Enter your username: "), self.pb_sha256(input("Enter your password: "))))
        except Error as e:
            print(f"Error '{e}' occurred.")


if __name__ == '__main__':
    db = DB()