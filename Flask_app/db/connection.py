import psycopg2


def get_connection():
    return psycopg2.connect(
        host="my_postgres_container",
        database="iauro",
        user="root",
        password="2020"
    )