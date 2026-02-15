"""Create database tables for development.

Run: python -m ui.app.create_db
"""
from .db import get_engine
from .models import Base


def main():
    engine = get_engine()
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Done.")


if __name__ == "__main__":
    main()
