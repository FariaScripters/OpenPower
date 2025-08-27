# AI Agent Instructions for OpenPower

## Project Overview
OpenPower is a general-purpose AI agent system focused on providing:
- Universal Browser Automation Server with unified REST API
- Support for multiple browser automation frameworks (e.g. Playwright)
- Secure sandbox environment for tools and operations
- User-friendly interface for creating and managing AI agents

## Key Components

### 1. Browser Automation Server
- Provides unified REST API interface
- Integrates multiple browser automation frameworks
- Primary framework: Playwright
- Real-time viewing and takeover capabilities

### 2. Sandbox Environment
- Docker-based isolated environments for each task
- Base image: Ubuntu 22.04
- Pre-configured with essential tools:
  - Python 3.10.12
  - Node.js 20.18.0
  - Chrome/Chromium for browser automation
  - Chinese language support
- Security boundaries enforced through Docker containerization

### 3. Task Management System
- Session history via MongoDB/Redis
- Support for background tasks
- Conversation management with interruption capabilities
- File upload/download support

### 4. Infrastructure
- Minimal deployment requiring only LLM service
- Multilingual support (English/Chinese)
- User authentication system
- Tools integration:
  - Terminal access
  - Browser automation
  - File operations
  - Web search
  - External MCP tool integration

## Development Guidelines
As an AI agent, focus on:
- Clean separation between browser automation API and sandbox components
- Security-first approach in feature implementation
- RESTful API design principles
- Docker best practices for sandbox environment
- Proper error handling and task isolation

## Development Workflow
1. Environment Setup
   - Build using provided Dockerfile
   - Configure package mirrors (Aliyun for apt/pip/npm)
   - Set up Python virtual environment

2. Running Services
   - Managed via supervisord
   - Exposed ports: 8080, 9222, 5900, 5901
   - Support for Xvfb and VNC for browser automation

## Conventions
1. Docker Configuration
   - Non-interactive installation (DEBIAN_FRONTEND=noninteractive)
   - User: ubuntu (with sudo privileges)
   - Working directory: /app

2. Security
   - Sandbox hostname isolation
   - Proper user permissions
   - Controlled external access

## Integration Points
1. Browser Automation Frameworks
   - Primary: Playwright
   - Chrome/Chromium integration
   - VNC/Xvfb for headless operation

2. REST API
   - Task management endpoints
   - Browser automation controls
   - File operation interfaces

3. UI Components
   - Built with shadcn/ui components
   - AI-powered elements for chat/response handling
   - Interactive web preview capabilities

## Roadmap Features
- Web Interface: Polished, responsive design
- API Access: Developer-friendly programmatic access
- Advanced Task Planning: Multi-step task capabilities
- Customizable Agents: Domain-specific agent creation
- Collaboration Features: Team-based agent sharing

Feel free to suggest additions or modifications as the project evolves.