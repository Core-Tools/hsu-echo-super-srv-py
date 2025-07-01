# HSU Example3 Srv Py

HSU Repository Portability Framework - Approach 3 (Multi-Repository + Single-Language)

This is a **Python server implementation** repository for the HSU Example3 demonstration, showing how to structure a focused service implementation that can work independently while following HSU patterns.

## Features

- gRPC-based Echo service server implementation in Python
- Cross-platform build system with HSU Universal Makefile
- Repository-portable code structure for multi-repo scenarios
- Nuitka binary compilation support
- Modern Python packaging with pyproject.toml

## Related Repositories

This server implementation works with:
- `hsu-example3-common` - Shared API definitions and client implementations  
- `hsu-example3-srv-go` - Go server implementation (alternative)

## Quick Start

```bash
# Install dependencies
make py-install

# Build the project
make build

# Run the server
make run-srv

# Build binary with Nuitka
make py-nuitka-build
```

To test the server, use clients from the `hsu-example3-common` repository.

## Documentation

For comprehensive documentation, setup guides, and framework details, see:
https://github.com/Core-Tools/docs/blob/main/README.md

## Repository Structure

This repository demonstrates **Approach 3**: Multi-Repository + Single-Language, specifically the **focused service implementation** pattern with Python, showing how to create standalone, deployable services while maintaining repository portability.