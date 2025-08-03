from src.database.initialise import initialise
from src.database.session import SessionLocal


# TODO - implement this seeder
def init() -> None:
    db = SessionLocal()
    initialise(db)


def main() -> None:
    init()


if __name__ == "__main__":
    main()
