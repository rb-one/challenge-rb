"""App Config"""
import os


class Config:
    """Config object to share configurations across the app"""
    
    def __init__(self):
    # Database
        self.DB_USER = os.environ.get('DB_USER')
        self.DB_PASSWORD = os.environ.get("DB_PASSWORD")
        self.DB_HOST = os.environ.get("DB_HOST")
        self.DB_PORT = os.environ.get("DB_PORT")
        self.DB_NAME = os.environ.get("DB_NAME")
