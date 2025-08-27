# OpenPower

<div align="center">

[![Python Package](https://github.com/FariaScripters/OpenPower/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/FariaScripters/OpenPower/actions/workflows/python-package-conda.yml)
[![PyPI](https://github.com/FariaScripters/OpenPower/actions/workflows/python-publish.yml/badge.svg)](https://pypi.org/project/openpower)
[![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev)

Universal browser automation with AI capabilities.
</div>

## Quick Start

```bash
# Install with pip
pip install openpower

# Or with conda
conda env create -f environment.yml
conda activate openpower

# Start server
python src/server.py
```

Server runs at `http://localhost:8080` 🚀

## Development

```bash
# Clone and setup
git clone https://github.com/FariaScripters/OpenPower.git
cd OpenPower
conda env create -f environment.yml

# Test
pytest tests/

# Docker
docker compose up
```

## Structure
```
src/
├── mcp_server.py    # MCP implementation
├── models.py        # Data models
└── server.py        # Main server
```

## Contributing

```bash
git checkout -b feature/amazing
git commit -m 'Add feature'
git push origin feature/amazing
```

<div align="center">

---

<div style="display: flex; align-items: center; justify-content: center; gap: 10px;">
  <span style="color: #006747;">■</span>
  <span style="color: #DA291C;">■</span>
</div>

[![Founded by Likhon Sheikh](https://img.shields.io/badge/Founder-Likhon%20Sheikh-blue?style=for-the-badge&logo=telegram)](https://t.me/likhonsheikh)

Made with 💚 in Bangladesh 🇧🇩

<img src="https://upload.wikimedia.org/wikipedia/commons/f/f9/Flag_of_Bangladesh.svg" width="25" alt="Bangladesh Flag">

[Security](https://github.com/FariaScripters/OpenPower/security) · 
[License](https://github.com/FariaScripters/OpenPower/blob/main/LICENSE)

</div>