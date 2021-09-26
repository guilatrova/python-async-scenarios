import timeit
import sqlite3
from contextlib import closing


DB = "../slow.db"
COLORS = [
    "\033[95m",
    "\033[94m",
    "\033[96m",
    "\033[92m",
    "\033[93m"
]
ENDC = "\033[0m"

SLOW_QUERY = """
    SELECT c.name, s.state FROM cities c
    JOIN states s ON  c.state_id = s.id
    WHERE s.state IN (
        SELECT state FROM states
    )
    ORDER BY s.long_name, c.name
"""
MEDIUM_QUERY = """
    SELECT c.name, s.state FROM cities c
    JOIN states s ON  c.state_id = s.id
    WHERE s.state like 'M%' OR s.state like '%P'
"""
FAST_QUERY = """
    SELECT c.name, s.state FROM cities c
    JOIN states s ON  c.state_id = s.id
    WHERE c.name like '%A'
"""


class Requester:
    rid: int = 0

    def __init__(self):
        Requester.rid += 1
        self.rid = Requester.rid
        self.color = COLORS[self.rid]

    def query_from_db(self, query: str) -> None:
        prefix = f"{self.color}R{self.rid}: "
        suffix = ENDC
        print(f"{prefix}Querying '{query}'{suffix}")

        with closing(sqlite3.connect(DB)) as db:
            with closing(db.cursor()) as cursor:
                rows = cursor.execute(query).fetchall()
                content = len(rows)

        print(f"{prefix}Query made! Db replied '{content}' rows{suffix}")


def main() -> None:
    r1 = Requester()
    r2 = Requester()
    r3 = Requester()

    print("=" * 10)
    starttime = timeit.default_timer()

    r1.query_from_db(SLOW_QUERY)
    r2.query_from_db(FAST_QUERY)
    r3.query_from_db(MEDIUM_QUERY)

    print("-" * 10)
    print(f"Time elapsed: {timeit.default_timer() - starttime}")
    print("=" * 10)

if __name__ == "__main__":
    main()
