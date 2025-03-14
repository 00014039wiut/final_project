import psycopg2
import utils

conn = psycopg2.connect(database='new_db',
                        user='postgres',
                        password='Sql7575',
                        host='localhost',
                        port=5432
                        )

cur = conn.cursor()

create_users_table = """create table users(
    id serial primary key ,
    username varchar(100) not null unique ,
    password varchar(255) not null ,
    role varchar(20) not null ,
    status varchar(30) not null ,
    login_try_count int not null 
);
"""

create_todos_table = """create table todos(
    id serial PRIMARY KEY,
    name varchar(100) not null ,
    todo_type varchar(15) not null,
    user_id int references users(id)
);
"""


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result

    return wrapper


def create_table():
    cur.execute(create_users_table)
    cur.execute(create_todos_table)
    conn.commit()


@commit
def migrate():
    insert_into_users = """
    insert into users (username, password, role, status,login_try_count) 
    values (%s,%s,%s,%s,%s);

    """
    data = ('admin', utils.hash_password('123'), 'ADMIN', 'ACTIVE', 0)
    cur.execute(insert_into_users, data)


def init():
    # create_table()
    migrate()


if __name__ == '__main__':
    init()
