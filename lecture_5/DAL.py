import sqlite3


def get_connection(db_path):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Exception as e:
        print('There was some kind of exception!')
        print(e)
    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


def insert_student(conn, name, age, profession):
    student = (name, age, profession)
    sql = ''' INSERT INTO students(name,age,profession)
                  VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid


query_table = '''CREATE TABLE IF NOT EXISTS students (
	id integer PRIMARY KEY,
	name text NOT NULL,
	age int,
	profession text
);'''

if __name__ == '__main__':
    conn = get_connection(r"C:\Users\Borat\int_database.db")
    # create_table(conn, query_table)
    insert_student(conn, "hello", 5, 'Programmer')
