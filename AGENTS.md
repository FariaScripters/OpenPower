# OpenPower Agent Configuration

## Project Overview
OpenPower is a general-purpose AI agent system that provides:
- Universal Browser Automation Server with unified REST API (port 8080)
- MCP (Model Context Protocol) server integration (port 8081)
- Sequential Thinking MCP server (port 8082)
- Support for multiple AI models and browser automation frameworks
- Secure sandbox environment for tools and operations

## Environment Setup
```bash
# Build and start all services
docker compose up -d

# Verify services are running
curl http://localhost:8080/.well-known/agent.json  # Browser Automation
curl http://localhost:8081/.well-known/mcp.json    # MCP Server
curl http://localhost:8082/.well-known/mcp.json    # Sequential Thinking
```

## Available Models
The system supports multiple AI models through Docker Model Runner:

### SmolLM2 (360M-Q4_K_M)
- Size: 258.1 MB
- Use case: Efficient on-device inference
- Configuration:
```yaml
models:
  smollm2:
    source: ai/smollm2:360M-Q4_K_M
    config:
      temperature: 0.7
      top_p: 0.9
```

### SmolLM3
- Size: 1.8 GB
- Features: Improved instruction following and reasoning
- Configuration:
```yaml
models:
  smollm3:
    source: ai/smollm3
    config:
      temperature: 0.8
      top_k: 40
```

## MCP Tools

### Browser Automation Tool
- Endpoint: `http://localhost:8080/tools/browser`
- Capabilities:
  - Web navigation
  - Screenshot capture
  - Element interaction
  - Form filling

### Sequential Thinking Tool
- Endpoint: `http://localhost:8082/tools/sequentialthinking`
- Features:
  - Dynamic thought sequences
  - Branching and revision tracking
  - Context maintenance
  - Hypothesis generation and verification
- Parameters:
```json
{
  "thought": "string",
  "thought_number": "integer",
  "total_thoughts": "integer",
  "next_thought_needed": "boolean",
  "branch_from_thought": "integer?",
  "branch_id": "string?",
  "is_revision": "boolean?",
  "needs_more_thoughts": "boolean?",
  "revises_thought": "integer?"
}
```

## Development Guidelines

### Code Style
- Python:
  - Black formatter
  - Type hints required
  - Async/await for I/O operations
- Docker:
  - Multi-stage builds
  - Non-root user execution
  - Volume management for persistence

### Testing Instructions
```bash
# Run all tests
pytest tests/

# Run specific test category
pytest tests/test_browser.py
pytest tests/test_mcp.py

# Run with coverage
pytest --cov=src tests/
```

### Security Considerations
1. Model Runner Security:
   - Verify model signatures using COSIGN
   - Use resource limits in compose.yaml
   - Enable GPU isolation when available

2. MCP Server Security:
   - All tools must implement rate limiting
   - Validate input parameters
   - Use secure token authentication

3. Browser Automation Security:
   - Sandbox each browser instance
   - Clear context between sessions
   - Implement request timeouts

## Common Operations

### Adding a New Tool
1. Create tool class in `/tools` directory
2. Implement MCP interface
3. Register in `tools/__init__.py`
4. Add configuration to `compose.yaml`

### Model Management
```bash
# List available models
curl http://localhost:8080/v1/models

# Check model status
curl http://localhost:8080/v1/models/{model_id}/status

# Run inference
curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "ai/smollm2", "messages": [{"role": "user", "content": "Hello"}]}'
```

### Tool Integration
New tools should follow the MCP specification:
```python
class CustomTool(Tool):
    def __init__(self):
        super().__init__(
            name="tool-name",
            description="Tool description"
        )
    
    async def execute(self, params: Dict[str, Any]) -> Any:
        # Implement tool logic
        pass
```

## Deployment Notes
- Environment Variables:
  - `MCP_SERVER_PORT`: Port for MCP server (default: 8081)
  - `MODEL_RUNNER_URL`: URL for model runner service
  - `DISPLAY`: Required for browser automation (default: :99)

- Resource Requirements:
  - SmolLM2: 512MB RAM minimum
  - SmolLM3: 2GB RAM minimum
  - Browser Automation: 1GB RAM per instance
  - GPU acceleration recommended for model inference

## Troubleshooting
1. Model Loading Issues:
   - Check model cache volume permissions
   - Verify GPU drivers if using acceleration
   - Confirm model signature verification

2. Browser Automation Issues:
   - Ensure Xvfb is running (`ps aux | grep Xvfb`)
   - Check browser logs in container
   - Verify network access from container

3. MCP Server Issues:
   - Validate tool registration
   - Check port availability
   - Monitor resource usage
