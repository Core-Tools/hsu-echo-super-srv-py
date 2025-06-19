#!/usr/bin/env python
"""
Entry point script for the Echo gRPC server.
Used as the PyInstaller and Nuitka entry point.
"""

from hsu_core.py.control.server import Server
from hsu_core.py.control.def_handler import register_grpc_default_server_handler as register_core_grpc_default_server_handler
from hsu_echo.py.control.handler import register_grpc_server_handler as register_echo_grpc_server_handler
from super_handler import SuperHandler

def serve():
    """Main entry point for the Echo gRPC server"""
    import argparse

    parser = argparse.ArgumentParser(description="Echo gRPC Server")
    parser.add_argument("--port", type=int, default=50055, help="Port to listen on")
    args = parser.parse_args()
    
    server = Server(args.port)

    handler = SuperHandler()
    register_core_grpc_default_server_handler(server.GRPC())
    register_echo_grpc_server_handler(server.GRPC(), handler)

    server.run(None)

if __name__ == "__main__":
    serve() 