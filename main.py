"""Main Entry Point"""
from app.server.microserver import MicroServer

if __name__ == "__main__":
    server = MicroServer()
    server.serve()
