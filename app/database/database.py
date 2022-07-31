"""App Database module to manage mysql connections"""
from typing import Any
import mysql.connector


class DatabaseDriver:
    def __init__(self, config: object) -> None:
        self.config = {
            "user": config.DB_USER,
            "password": config.DB_PASSWORD,
            "host": config.DB_HOST,
            "port": config.DB_PORT,
            "database": config.DB_NAME,
        }

    def get_connection(self) -> Any:
        """returns a connection from the database"""
        self.connection = mysql.connector.connect(**self.config)
        return self.connection

    def close_connection(self) -> None:
        self.connection.close()


class Queryhole:
    def __init__(self, db_driver):
        self.db_driver = db_driver
        self.connection = db_driver.get_connection()

    def make_query(self, query: str) -> list[tuple]:
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        return result