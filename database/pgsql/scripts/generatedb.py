from contextlib import closing
import psycopg2

BASE_CREATE_SCRIPT = "./brazil-create-db.sql"
INSERT_SCRIPT = "./brazil-insert-cities.sql"
REPEAT_INSERT = 1000


def create_db(cursor: psycopg2.extensions.cursor) -> None:
    with open(BASE_CREATE_SCRIPT, "r") as sql:
        cursor.execute(sql.read())

    print("Database created!")


def count_cities(cursor: psycopg2.extensions.cursor) -> int:
    cursor.execute("SELECT count(*) from cities")
    return cursor.fetchone()[0]


def main() -> None:
    connect_args = dict(
        host="localhost",
        database="postgres",
        user="postgres",
        password="pythonasync"
    )

    with closing(psycopg2.connect(**connect_args)) as db:
        with closing(db.cursor()) as cursor:
            create_db(cursor)

            with open(INSERT_SCRIPT, "r", encoding="utf8") as sql:
                insert_script = sql.read()

            for i in range(1, REPEAT_INSERT + 1):
                cursor.execute(insert_script)
                cities = count_cities(cursor)
                print(f"#{i}: Reinserted! Now you have {cities} cities")

            db.commit()


if __name__ == "__main__":
    main()
