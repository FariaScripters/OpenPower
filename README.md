# OpenPower

![Python Package using Anaconda](https://github.com/FariaScripters/OpenPower/actions/workflows/python-package-conda.yml/badge.svg)
![Publish Python Package](https://github.com/FariaScripters/OpenPower/actions/workflows/python-publish.yml/badge.svg)
[![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev)

A versatile AI agent system providing universal browser automation with a unified REST API.

## Features

- Universal Browser Automation Server with unified REST API (port 8080)
- Support for multiple browser automation frameworks (e.g. Playwright)
- Secure sandbox environment for tools and operations
- User-friendly interface and API access

## Installation

### Using pip

```bash
pip install openpower
```

### Using Conda

```bash
conda env create -f environment.yml
conda activate openpower
```

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python src/server.py
```

The server will start on `http://localhost:8080`

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/FariaScripters/OpenPower.git
cd OpenPower
```

2. Create and activate conda environment:
```bash
conda env create -f environment.yml
conda activate openpower
```

3. Install development dependencies:
```bash
pip install -r requirements.txt
```

4. Run tests:
```bash
pytest tests/
```

## Docker Support

Build and run using Docker:

```bash
docker compose up
```

Or build specific services:

```bash
docker compose -f docker/docker-compose.ai.yml up
```

## Project Structure

```
OpenPower/
├── docker/                 # Docker configuration files
├── src/                    # Source code
│   ├── mcp_server.py      # MCP server implementation
│   ├── models.py          # Data models
│   └── server.py          # Main server application
├── tests/                 # Test suite
└── tools/                 # Utility tools and helpers
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security

For security concerns, please open an issue or contact the maintainers directly.

## CI/CD Workflows

This project uses several GitHub Actions workflows:

1. **Python Package using Anaconda**: Tests the package on multiple Python versions using Conda
2. **Publish Python Package**: Automatically publishes to PyPI on new releases
3. **SLSA Provenance**: Generates SLSA Level 3 provenance for releases

## Status

- Package Build: ![Python Package using Anaconda](https://github.com/FariaScripters/OpenPower/actions/workflows/python-package-conda.yml/badge.svg)
- Package Publish: ![Publish Python Package](https://github.com/FariaScripters/OpenPower/actions/workflows/python-publish.yml/badge.svg)
- SLSA Level: [![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev)