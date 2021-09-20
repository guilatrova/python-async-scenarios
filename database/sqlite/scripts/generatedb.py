import sqlite3
import os.path
from contextlib import closing

DB = "../slow.db"
BASE_CREATE_SCRIPT = "./brazil-create-db.sql"
INSERT_SCRIPT = "./brazil-insert-cities.sql"
REPEAT_INSERT = 400


def create_db(cursor: sqlite3.Cursor) -> None:
    with open(BASE_CREATE_SCRIPT, "r") as sql:
        cursor.executescript(sql.read())

    print("Database created!")


def count_cities(cursor: sqlite3.Cursor) -> int:
    return cursor.execute("SELECT count(*) from cities").fetchone()[0]


def main():
    db_already_created = os.path.isfile(DB)

    with closing(sqlite3.connect(DB)) as db:
        with closing(db.cursor()) as cursor:
            if not db_already_created:
                create_db(cursor)

            with open(INSERT_SCRIPT, "r", encoding="utf8") as sql:
                insert_script = sql.read()

            for i in range(1, REPEAT_INSERT + 1):
                cursor.executescript(insert_script)
                cities = count_cities(cursor)
                print(f"#{i}: Reinserted! Now you have {cities} cities")


if __name__ == "__main__":
    main()
