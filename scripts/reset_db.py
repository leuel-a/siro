#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel

load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.models.user import User
from src.lib.utils import info

DATABASE_URL = os.getenv("DATABASE_URL", "")
engine = create_engine(DATABASE_URL)


def reset_database():
    """Drops all tables and recreates them.
    """
    info("Dropping all tables...\n")
    SQLModel.metadata.drop_all(engine)
    info("All tables dropped!!\n")


if __name__ == "__main__":
    reset_database()
