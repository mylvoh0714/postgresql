import sys
import io
import psycopg2 as pg
import psycopg2.extras
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
db_connector = {
    'host' : 'localhost',
    'user' : 'postgres',
    'dbname' : 'postgres',
    'port' : '5432',
    'password' : 'fkgp5482'
}

connect_string = "host={host} user={user} \
dbname={dbname} password={password} port={port}".format(**db_connector)
print(connect_string)


def select():
    with pg.connect(connect_string) as conn:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        sql = "SELECT * FROM students"

        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            print(f'{type(row)}: ' , end = '')
            print(row)

def insert(dbname, values):
    conn = pg.connect(connect_string)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # TODO:
    line_count = 0

    for row in values:
        line_count += 1
        if line_count == 1:
            continue
        sql = "INSERT INTO {dbname} VALUES ('{sid}','{passwd}','{sname}','{sex}', {major_id},'{tutor_id}',{grade})".format(dbname=dbname, sid=row[0], passwd=row[1], sname=row[2], sex=row[3], major_id=row[4], tutor_id=row[5], grade=row[6])
        print(sql)
        cur.execute(sql)
    print(f"{line_count} lines processed.")

    conn.commit()
    conn.close()


def read_csv():
    filepath = 'dbapp_practice\\students.csv'
    #with open(filepath, encoding ='utf-8') as read_file:
    read_file = open(filepath, encoding='utf-8')
    reader = csv.reader(read_file, delimiter = ',')

    result = []
    for row in reader:
        result.append(row)

    read_file.close()
    print(type(result))
    insert('students',result)


if __name__ == "__main__":
    select()
    #insert()
    #read_csv()
