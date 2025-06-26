#!/usr/bin/env python
"""
Entry point script for the Echo gRPC server.
Used as the PyInstaller and Nuitka entry point.
"""

from hsu_echo.py.control.serve_echo import serve_echo
from super_handler import SuperHandler

def serve():
    handler = SuperHandler()
    serve_echo(handler)

if __name__ == "__main__":
    serve() 