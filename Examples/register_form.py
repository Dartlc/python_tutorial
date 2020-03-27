import datetime
import uuid

import pymysql


class RegisterForm:

    def __init__(self, name: str, age: str):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age
        self.created_at = datetime.datetime.now()
        self.db = pymysql.connect('localhost', 'sudhagar', 'sudhagar@1995', 'register')
        self.x = self.db.cursor()
        self.x.execute("USE register")

    def create_table(self):
        try:
            self.x.execute("CREATE TABLE student_register(id varchar(120), name varchar(30), age char(20), created_at "
                           "varchar(30))")
        except Exception as e:
            print(f"error is occurred {e}")

    def insert_records(self):
        self.x.execute(
            "INSERT INTO student_register(id, name, age, created_at) VALUES ('%s', '%s', '%s', '%s')" % (
            self.id, self.name, self.age, self.created_at))
        self.db.commit()

    def exit_db(self):
        self.db.close()


if __name__ == '__main__':
    obj = RegisterForm(name='sudhagar', age='24')
    obj.insert_records()
    obj.exit_db()
