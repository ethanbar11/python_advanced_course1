import os


class FileDB:
    def __init__(self, db_path):
        # Assuming db_path is to text file.
        counter_path = os.path.splitext(db_path)[0] + '_counter.txt'
        try:
            self.conn = open(db_path, 'a')
            counter_file = open(counter_path, 'r')
            self.counter = int(counter_file.read())
            counter_file.close()
        except Exception as e:
            self.conn = open(db_path, 'w')
            self.counter = 0


def get_connection(db_path):
    return FileDB(db_path)


def insert_message(file_db, sender, message):
    file_db.counter += 1
    file_db.conn.write('{}\t {}\t{}\n'.format(file_db.counter, sender, message))
    file_db.conn.flush()