# AI Agent Instructions for OpenPower

## Project Overview
OpenPower is a general-purpose AI agent system focused on providing:
- Universal Browser Automation Server with unified REST API (port 8080)
- Support for multiple browser automation frameworks (e.g. Playwright)
- Secure sandbox environment for tools and operations
- User-fr

▲ AI Elements
AI Elements is a component library built on top of shadcn/ui to help you build AI-native applications faster.

Overview
AI Elements provides pre-built, customizable React components specifically designed for AI applications, including conversations, messages, code blocks, reasoning displays, and more. The CLI makes it easy to add these components to your Next.js project.

Installation
You can use the AI Elements CLI directly with npx, or install it globally:

# Use directly (recommended)
npx ai-elements@latest

# Or using shadcn cli
npx shadcn@latest add https://registry.ai-sdk.dev/all.json
Prerequisites
Before using AI Elements, ensure your project meets these requirements:

Node.js 18 or later
Next.js project with AI SDK installed
shadcn/ui initialized in your project (npx shadcn@latest init)
Tailwind CSS configured (AI Elements supports CSS Variables mode only)
Usage
Install All Components
Install all available AI Elements components at once:

npx ai-elements@latest
This command will:

Set up shadcn/ui if not already configured
Install all AI Elements components to your configured components directory
Add necessary dependencies to your project
Install Specific Components
Install individual components using the add command:

npx ai-elements@latest add <component-name>
Examples:

# Install the message component
npx ai-elements@latest add message

# Install the conversation component
npx ai-elements@latest add conversation

# Install the code-block component
npx ai-elements@latest add code-block
Alternative: Use with shadcn CLI
You can also install components using the standard shadcn/ui CLI:

# Install all components
npx shadcn@latest add https://registry.ai-sdk.dev/all.json

# Install a specific component
npx shadcn@latest add https://registry.ai-sdk.dev/message.json
Available Components
AI Elements includes the following components:

Component	Description
actions	Interactive action buttons for AI responses
branch	Branch visualization for conversation flows
code-block	Syntax-highlighted code display with copy functionality
conversation	Container for chat conversations
image	AI-generated image display component
inline-citation	Inline source citations
loader	Loading states for AI operations
message	Individual chat messages with avatars
prompt-input	Advanced input component with model selection
reasoning	Display AI reasoning and thought processes
response	Formatted AI response display
source	Source attribution component
suggestion	Quick action suggestions
task	Task completion tracking
tool	Tool usage visualization
web-preview	Embedded web page previews
Quick Start Example
After installing components, you can use them in your React application:

'use client';

import { useChat } from '@ai-sdk/react';
import {
  Conversation,
  ConversationContent,
} from '@/components/ai-elements/conversation';
import {
  Message,
  MessageContent,
} from '@/components/ai-elements/message';
import { Response } from '@/components/ai-elements/response';

export default function Chat() {
  const { messages } = useChat();

  return (
    <Conversation>
      <ConversationContent>
        {messages.map((message, index) => (
          <Message key={index} from={message.role}>
            <MessageContent>
              <Response>{message.content}</Response>
            </MessageContent>
          </Message>
        ))}
      </ConversationContent>
    </Conversation>
  );
}
How It Works
The AI Elements CLI:

Detects your package manager (npm, pnpm, yarn, or bun) automatically
Fetches component registry from https://registry.ai-sdk.dev/all.json
Installs components using the shadcn/ui CLI under the hood
Adds dependencies and integrates with your existing shadcn/ui setup
Components are installed to your configured shadcn/ui components directory (typically @/components/ai-elements/) and become part of your codebase, allowing for full customization.

Configuration
AI Elements uses your existing shadcn/ui configuration. Components will be installed to the directory specified in your components.json file.


Example Agent Card (.well-known/agent.json):
```json
{
    "capabilities": {
        "pushNotifications": true,
        "streaming": false
    },
    "defaultInputModes": ["text", "text/plain"],
    "defaultOutputModes": ["text", "text/plain"],
    "description": "A versatile agent that can solve various tasks using multiple tools",
    "name": "OpenPower Agent",
    "version": "1.0.0"
}
```

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

Example Task JSON:
```json
{
    "id": "task-123",
    "jsonrpc": "2.0",
    "method": "message/send",
    "params": {
        "message": {
            "messageId": "",
            "role": "user",
            "parts": [{"text": "example task"}]
        }
    }
}
```
AI Elements is a component library and custom registry built on top of shadcn/ui to help you build AI-native applications faster.

ai-sdk.dev/elements/overview

### 4. Agent Communication Protocol
- Implements A2A (Agent2Agent) Protocol standard
- Enables inter-agent communication and task delegation
- Supports agent collaboration without sharing internal memory
- Example endpoints:
  - `/.well-known/agent.json` - Agent capabilities
  - `/message/send` - Task execution
  - `/stream` - Real-time updates

Example Agent Executor:
```python
class OpenPowerAgentExecutor(AgentExecutor):
    def __init__(self):
        self.task_store = InMemoryTaskStore()
        self.browser_automation = BrowserAutomationServer()

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        # Handle incoming requests and tool execution
        result = await self.browser_automation.execute(context.message)
        await event_queue.enqueue_event(new_agent_text_message(result))

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        # Support task cancellation
        await self.browser_automation.cancel_task(context.task_id)
```

### 5. Model Context Protocol (MCP) Integration
- MCP server implementation for tool access
- Structured inputs/outputs for tool operations
- Support for external MCP-based tools

Example MCP Configuration:
```json
{
    "mcpServers": {
        "browserAutomation": {
            "type": "sse",
            "url": "http://localhost:8080/sse"
        }
    }
}
```

### 6. Infrastructure
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


Key aspects of system prompt XML:
System Prompt:
A system prompt is a foundational instruction set given to an AI model, often hidden from the end-user, that defines the AI's role, behavior, tone, and overall context for interactions. It acts as a guide for the AI's responses.
XML (Extensible Markup Language):
XML is a markup language used to structure data. It allows users to define custom tags to organize information hierarchically and clearly.
Application in AI:
When system prompts are defined using XML, it means that various components of the prompt, such as instructions, constraints, persona descriptions, or contextual information, are enclosed within specific XML tags. This provides a structured and organized way to convey complex instructions to the AI model.
Benefits of using XML in system prompts:
Clarity and Structure:
XML tags provide a clear and organized way to separate different parts of the prompt, making it easier for both humans and the AI to understand the intended instructions.
Modularity:
Complex prompts can be broken down into smaller, manageable sections using XML tags, improving maintainability and reusability.
Precision:
By explicitly defining sections with tags, ambiguities in instructions can be reduced, leading to more consistent and predictable AI responses.
Integration:
XML's widespread use in data interchange can facilitate the integration of system prompts with other systems or tools.
One of the standout features is the enhanced code blocks that allow for additional meta-information to be included. This is done by specifying details after the triple backticks, such as:

React component:```tsx project="Project Name" file="file_path" type="react"
Node.js code:```js project="Project Name" file="file_path" type="nodejs"
HTML page:```html project="Project Name" file="file_path" type="html"
Markdown document:```md project="Project Name" file="file_path" type="markdown"
Flowchart (Mermaid chart):```mermaid title="Example Flowchart" type="diagram"
Other code (non-executable or non-previewable):```python project="Project Name" file="file_name" type="code"
Chain of Thought (CoT) Integration
The system employs a Chain of Thought (CoT) approach for handling complex programming tasks. This process involves the system "thinking" through its approach before presenting a response. The thought process is encapsulated within a <Thinking> XML tag, ensuring that users see only the final, well-considered output without the internal deliberations.

Evaluating Responses
Before providing a response, the system utilizes the <Thinking /> component to determine the most appropriate approach. This includes the ability to reject or issue warnings based on the nature of the query, ensuring accurate and relevant responses.

Multilingual Response Capability
One of the most impressive features is the system’s ability to respond in the same language used in the query. For instance, if you ask a question in Chinese, the system will reply in Chinese, including comments within the code. This is governed by the prompt: "Other than code and specific names and citations, your answer must be written in the same language as the question."

Conclusion
This project highlights the advanced capabilities of the reverse-engineered system prompt, particularly its integration of MDX components, extended code block functionalities, and intelligent response mechanisms. Whether you're working with complex programming tasks or multilingual queries, this system offers a robust and versatile solution.


Example Security Implementation:
```python
# Sandbox security configuration
@app.before_request
def validate_sandbox():
    # Validate origin sandbox hostname
    if not is_valid_sandbox_origin(request.headers.get('Host')):
        abort(403)
    
    # Verify task isolation
    if not validate_task_boundaries(request.headers.get('X-Task-ID')):
        abort(401)

# Tool access control
def execute_tool(tool_name: str, params: dict):
    # Validate tool permissions
    if not has_tool_access(current_task.id, tool_name):
        raise SecurityException("Tool access denied")
```

## Development Workflow
1. Environment Setup
   - Build using provided Dockerfile
   - Configure package mirrors (Aliyun for apt/pip/npm)
   - Set up Python virtual environment

2. Running Services
   - Managed via supervisord
   - Exposed ports: 
     - 8080: Browser Automation API
     - 9222: Chrome DevTools
     - 5900, 5901: VNC for browser monitoring
   - Support for Xvfb and VNC for browser automation

Example supervisord.conf:
```ini
[program:xvfb]
command=/usr/bin/Xvfb :99 -screen 0 1024x768x24
autorestart=true

[program:browser-automation]
command=/usr/bin/python3 /app/server.py
environment=DISPLAY=:99
directory=/app
user=ubuntu
autorestart=true
```

## Conventions
1. Docker Configuration
   - Non-interactive installation (DEBIAN_FRONTEND=noninteractive)
   - User: ubuntu (with sudo privileges)
   - Working directory: /app

Example Dockerfile:
```dockerfile
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
ENV HOSTNAME=sandbox

# Create user ubuntu with sudo privileges
RUN useradd -m -d /home/ubuntu -s /bin/bash ubuntu && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/ubuntu

WORKDIR /app
```

2. Security
   - Sandbox hostname isolation
   - Proper user permissions
   - Controlled external access
   - Tool access validation
   - Task boundary enforcement

Example Security Headers:
```python
SECURITY_HEADERS = {
    'X-Frame-Options': 'DENY',
    'X-Content-Type-Options': 'nosniff',
    'X-XSS-Protection': '1; mode=block',
    'Content-Security-Policy': "default-src 'self'",
    'X-Task-ID': '<task_uuid>',
    'X-Sandbox-Origin': '<sandbox_hostname>'
}

## Integration Points
1. Browser Automation Frameworks
   - Primary: Playwright
   - Chrome/Chromium integration
   - VNC/Xvfb for headless operation

2. A2A Protocol Implementation
   - Server setup using Starlette/Uvicorn
   - Task management with DefaultRequestHandler
   - Event queue for message streaming
   
Example Server Setup:
```python
def create_server(host='0.0.0.0', port=8080):
    agent_card = AgentCard(
        name='OpenPower Agent',
        description='Browser automation and task management agent',
        url=f'http://{host}:{port}/',
        version='1.0.0',
        capabilities=AgentCapabilities(streaming=True),
        skills=[browser_automation_skill]
    )

    request_handler = DefaultRequestHandler(
        agent_executor=OpenPowerAgentExecutor(),
        task_store=InMemoryTaskStore()
    )

    server = A2AStarletteApplication(
        agent_card=agent_card,
        http_handler=request_handler
    )

    return server.build()

# Start server
uvicorn.run(create_server(), host='0.0.0.0', port=8080)
```
Build terminals in the browser

npm install @xterm/xterm
 First you need to install the module, we ship exclusively through npm so you need that installed and then add xterm.js as a dependency by running:

npm install @xterm/xterm
To start using xterm.js on your browser, add the xterm.js and xterm.css to the head of your html page. Then create a <div id="terminal"></div> onto which xterm can attach itself. Finally instantiate the Terminal object and then call the open function with the DOM object of the div.

<!doctype html>
  <html>
    <head>
      <link rel="stylesheet" href="node_modules/@xterm/xterm/css/xterm.css" />
      <script src="node_modules/@xterm/xterm/lib/xterm.js"></script>
    </head>
    <body>
      <div id="terminal"></div>
      <script>
        var term = new Terminal();
        term.open(document.getElementById('terminal'));
        term.write('Hello from \x1B[1;3;31mxterm.js\x1B[0m $ ')
      </script>
    </body>
  </html>
Real-world uses
Xterm.js is used in several world-class applications to provide great terminal experiences.
Sandpack Components
The <Sandpack /> component is made up of smaller parts that you can import separately to combine with your custom components.
 Sandpack Client
The bundler is wrapped by a small package called sandpack-client, which is framework agnostic and allowing you to tap into the bundler protocol.
 npm install @codesandbox/sandpack-react
 Live coding in the browser.
Run any JavaScript and Node.js app in any browser.
 To use Sandpack with CDN, simply include the Sandpack tag in your HTML file and specify the CDN imports inluding Sandpack and its dependencies.


<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
 
    <script type="importmap">
      {
        "imports": {
          "react": "https://esm.sh/react@18.2.0",
          "react-dom": "https://esm.sh/react-dom@18.2.0",
          "react-dom/": "https://esm.sh/react-dom@18.2.0/",
          "@codesandbox/sandpack-react": "https://esm.sh/@codesandbox/sandpack-react@2.8.0"
        }
      }
    </script>
 
    <script type="module">
      import React from "react";
      import { createRoot } from "react-dom/client";
      import { Sandpack } from "@codesandbox/sandpack-react";
 
      const root = createRoot(document.getElementById("root"));
      const sandpackComponent = React.createElement(
        Sandpack,
        { template: "react" },
        null
      );
      root.render(sandpackComponent);
    </script>
  </head>
 
  <body>
    <div id="root"></div>
  </body>
</html>

3. REST API
   - Task management endpoints
   - Browser automation controls
   - File operation interfaces

4. UI Components
   - Built with shadcn/ui components
   - AI-powered elements for chat/response handling
   - Interactive web preview capabilities

Once Model Runner is enabled, new API endpoints are available. You can use these endpoints to interact with a model programmatically.

Determine the base URL
The base URL to interact with the endpoints depends on how you run Docker:

Docker Desktop Docker Engine
From containers: http://model-runner.docker.internal/
From host processes: http://localhost:12434/, assuming TCP host access is enabled on the default port (12434).
Available DMR endpoints
Create a model:


POST /models/create
List models:


GET /models
Get a model:


GET /models/{namespace}/{name}
Delete a local model:


DELETE /models/{namespace}/{name}
Available OpenAPI endpoints
DMR supports the following OpenAPI endpoints:

List models:


GET /engines/llama.cpp/v1/models
Retrieve model:


GET /engines/llama.cpp/v1/models/{namespace}/{name}
List chat completions:


POST /engines/llama.cpp/v1/chat/completions
Create completions:


POST /engines/llama.cpp/v1/completions
Create embeddings:


POST /engines/llama.cpp/v1/embeddings
To call these endpoints via a Unix socket (/var/run/docker.sock), prefix their path with /exp/vDD4.40.

Note
You can omit llama.cpp from the path. For example: POST /engines/v1/chat/completions.

REST API examples
Request from within a container
To call the chat/completions OpenAI endpoint from within another container using curl:


#!/bin/sh

curl http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/smollm2",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
Request from the host using TCP
To call the chat/completions OpenAI endpoint from the host via TCP:

Enable the host-side TCP support from the Docker Desktop GUI, or via the Docker Desktop CLI. For example: docker desktop enable model-runner --tcp <port>.

If you are running on Windows, also enable GPU-backed inference. See Enable Docker Model Runner.

Interact with it as documented in the previous section using localhost and the correct port.


#!/bin/sh

  curl http://localhost:12434/engines/llama.cpp/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/smollm2",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
Request from the host using a Unix socket
To call the chat/completions OpenAI endpoint through the Docker socket from the host using curl:


#!/bin/sh

curl --unix-socket $HOME/.docker/run/docker.sock \
    localhost/exp/vDD4.40/engines/llama.cpp/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "ai/smollm2",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Please write 500 words about the fall of Rome."
            }
        ]
    }'
     
     
     Docker Model Runner makes it easy to test and run AI models locally using familiar Docker CLI commands and tools. It works with any OCI-compliant registry, including Docker Hub, and supports OpenAI’s API for quick app integration.
     Define AI Models in Docker Compose applications
Page options
Requires:
Docker Compose 2.38.0 and later
Compose lets you define AI models as core components of your application, so you can declare model dependencies alongside services and run the application on any platform that supports the Compose Specification.

Prerequisites
Docker Compose v2.38 or later
A platform that supports Compose models such as Docker Model Runner (DMR) or compatible cloud providers. If you are using DMR, see the requirements.
What are Compose models?
Compose models are a standardized way to define AI model dependencies in your application. By using the models top-level element in your Compose file, you can:

Declare which AI models your application needs
Specify model configurations and requirements
Make your application portable across different platforms
Let the platform handle model provisioning and lifecycle management
Basic model definition
To define models in your Compose application, use the models top-level element:


services:
  chat-app:
    image: my-chat-app
    models:
      - llm

models:
  llm:
    model: ai/smollm2
This example defines:

A service called chat-app that uses a model named llm
A model definition for llm that references the ai/smollm2 model image
Model configuration options
Models support various configuration options:


models:
  llm:
    model: ai/smollm2
    context_size: 1024
    runtime_flags:
      - "--a-flag"
      - "--another-flag=42"
Common configuration options include:

model (required): The OCI artifact identifier for the model. This is what Compose pulls and runs via the model runner.

context_size: Defines the maximum token context size for the model.

Note
Each model has its own maximum context size. When increasing the context length, consider your hardware constraints. In general, try to keep context size as small as feasible for your specific needs.

runtime_flags: A list of raw command-line flags passed to the inference engine when the model is started. For example, if you use llama.cpp, you can pass any of the available parameters.

Platform-specific options may also be available via extension attributes x-*

Tip
See more example in the Common runtime configurations section.

Alternative configuration with provider services
Important
This approach is deprecated. Use the models top-level element instead.

You can also use the provider service type, which allows you to declare platform capabilities required by your application. For AI models, you can use the model type to declare model dependencies.

To define a model provider:


services:
  chat:
    image: my-chat-app
    depends_on:
      - ai_runner

  ai_runner:
    provider:
      type: model
      options:
        model: ai/smollm2
        context-size: 1024
        runtime-flags: "--no-prefill-assistant"
Service model binding
Services can reference models in two ways: short syntax and long syntax.

Short syntax
The short syntax is the simplest way to bind a model to a service:


services:
  app:
    image: my-app
    models:
      - llm
      - embedding-model

models:
  llm:
    model: ai/smollm2
  embedding-model:
    model: ai/all-minilm
With short syntax, the platform automatically generates environment variables based on the model name:

LLM_URL - URL to access the LLM model
LLM_MODEL - Model identifier for the LLM model
EMBEDDING_MODEL_URL - URL to access the embedding-model
EMBEDDING_MODEL_MODEL - Model identifier for the embedding-model
Long syntax
The long syntax allows you to customize environment variable names:


services:
  app:
    image: my-app
    models:
      llm:
        endpoint_var: AI_MODEL_URL
        model_var: AI_MODEL_NAME
      embedding-model:
        endpoint_var: EMBEDDING_URL
        model_var: EMBEDDING_NAME

models:
  llm:
    model: ai/smollm2
  embedding-model:
    model: ai/all-minilm
With this configuration, your service receives:

AI_MODEL_URL and AI_MODEL_NAME for the LLM model
EMBEDDING_URL and EMBEDDING_NAME for the embedding model
Platform portability
One of the key benefits of using Compose models is portability across different platforms that support the Compose specification.

Docker Model Runner
When Docker Model Runner is enabled:


services:
  chat-app:
    image: my-chat-app
    models:
      llm:
        endpoint_var: AI_MODEL_URL
        model_var: AI_MODEL_NAME

models:
  llm:
    model: ai/smollm2
    context_size: 4096
    runtime_flags:
      - "--no-prefill-assistant"
Docker Model Runner will:

Pull and run the specified model locally
Provide endpoint URLs for accessing the model
Inject environment variables into the service
Cloud providers
The same Compose file can run on cloud providers that support Compose models:


services:
  chat-app:
    image: my-chat-app
    models:
      - llm

models:
  llm:
    model: ai/smollm2
    # Cloud-specific configurations
    x-cloud-options:
      - "cloud.instance-type=gpu-small"
      - "cloud.region=us-west-2"
Cloud providers might:

Use managed AI services instead of running models locally
Apply cloud-specific optimizations and scaling
Provide additional monitoring and logging capabilities
Handle model versioning and updates automatically
Common runtime configurations
Below are some example configurations for various use cases.

Development

services:
  app:
    image: app
    models:
      dev_model:
        endpoint_var: DEV_URL
        model_var: DEV_MODEL

models:
  dev_model:
    model: ai/model
    context_size: 4096
    runtime_flags:
      - "--verbose"                       # Set verbosity level to infinity
      - "--verbose-prompt"                # Print a verbose prompt before generation
      - "--log-prefix"                    # Enable prefix in log messages
      - "--log-timestamps"                # Enable timestamps in log messages
      - "--log-colors"                    # Enable colored logging
Conservative with disabled reasoning

services:
  app:
    image: app
    models:
      conservative_model:
        endpoint_var: CONSERVATIVE_URL
        model_var: CONSERVATIVE_MODEL

models:
  conservative_model:
    model: ai/model
    context_size: 4096
    runtime_flags:
      - "--temp"                # Temperature
      - "0.1"
      - "--top-k"               # Top-k sampling
      - "1"
      - "--reasoning-budget"    # Disable reasoning
      - "0"
Creative with high randomness

services:
  app:
    image: app
    models:
      creative_model:
        endpoint_var: CREATIVE_URL
        model_var: CREATIVE_MODEL

models:
  creative_model:
    model: ai/model
    context_size: 4096
    runtime_flags:
      - "--temp"                # Temperature
      - "1"
      - "--top-p"               # Top-p sampling
      - "0.9"
Highly deterministic

services:
  app:
    image: app
    models:
      deterministic_model:
        endpoint_var: DET_URL
        model_var: DET_MODEL

models:
  deterministic_model:
    model: ai/model
    context_size: 4096
    runtime_flags:
      - "--temp"                # Temperature
      - "0"
      - "--top-k"               # Top-k sampling
      - "1"
Concurrent processing

services:
  app:
    image: app
    models:
      concurrent_model:
        endpoint_var: CONCURRENT_URL
        model_var: CONCURRENT_MODEL

models:
  concurrent_model:
    model: ai/model
    context_size: 2048
    runtime_flags:
      - "--threads"             # Number of threads to use during generation
      - "8"
      - "--mlock"               # Lock memory to prevent swapping
Rich vocabulary model

services:
  app:
    image: app
    models:
      rich_vocab_model:
        endpoint_var: RICH_VOCAB_URL
        model_var: RICH_VOCAB_MODEL

models:
  rich_vocab_model:
    model: ai/model
    context_size: 4096
    runtime_flags:
      - "--temp"                # Temperature
      - "0.1"
      - "--top-p"               # Top-p sampling
      - "0.9"

Cut down on token costs, keep your data private, and stay in full control!
Models as OCI Artifacts in Docker Hub
Explore a curated collection of cutting-edge AI models as OCI Artifacts, from lightweight on-device models to high-performance LLMs

A command-line interface for installing AI Elements components - a component library built on top of shadcn/ui to help you build AI-native applications faster.

Overview
AI Elements provides pre-built, customizable React components specifically designed for AI applications, including conversations, messages, code blocks, reasoning displays, and more. The CLI makes it easy to add these components to your Next.js project.

Installation
You can use the AI Elements CLI directly with npx, or install it globally:

# Use directly (recommended)
npx ai-elements@latest

# Or using shadcn cli
npx shadcn@latest add https://registry.ai-sdk.dev/all.json
Prerequisites
Before using AI Elements, ensure your project meets these requirements:

Node.js 18 or later
Next.js project with AI SDK installed
shadcn/ui initialized in your project (npx shadcn@latest init)
Tailwind CSS configured (AI Elements supports CSS Variables mode only)
Usage
Install All Components
Install all available AI Elements components at once:

npx ai-elements@latest
This command will:

Set up shadcn/ui if not already configured
Install all AI Elements components to your configured components directory
Add necessary dependencies to your project
Install Specific Components
Install individual components using the add command:

npx ai-elements@latest add <component-name>
Examples:

# Install the message component
npx ai-elements@latest add message

# Install the conversation component
npx ai-elements@latest add conversation

# Install the code-block component
npx ai-elements@latest add code-block
Alternative: Use with shadcn CLI
You can also install components using the standard shadcn/ui CLI:

# Install all components
npx shadcn@latest add https://registry.ai-sdk.dev/all.json

# Install a specific component
npx shadcn@latest add https://registry.ai-sdk.dev/message.json
Available Components
AI Elements includes the following components:

Component	Description
actions	Interactive action buttons for AI responses
branch	Branch visualization for conversation flows
code-block	Syntax-highlighted code display with copy functionality
conversation	Container for chat conversations
image	AI-generated image display component
inline-citation	Inline source citations
loader	Loading states for AI operations
message	Individual chat messages with avatars
prompt-input	Advanced input component with model selection
reasoning	Display AI reasoning and thought processes
response	Formatted AI response display
source	Source attribution component
suggestion	Quick action suggestions
task	Task completion tracking
tool	Tool usage visualization
web-preview	Embedded web page previews
Quick Start Example
After installing components, you can use them in your React application:

'use client';

import { useChat } from '@ai-sdk/react';
import {
  Conversation,
  ConversationContent,
} from '@/components/ai-elements/conversation';
import {
  Message,
  MessageContent,
} from '@/components/ai-elements/message';
import { Response } from '@/components/ai-elements/response';

export default function Chat() {
  const { messages } = useChat();

  return (
    <Conversation>
      <ConversationContent>
        {messages.map((message, index) => (
          <Message key={index} from={message.role}>
            <MessageContent>
              <Response>{message.content}</Response>
            </MessageContent>
          </Message>
        ))}
      </ConversationContent>
    </Conversation>
  );
}
How It Works
The AI Elements CLI:

Detects your package manager (npm, pnpm, yarn, or bun) automatically
Fetches component registry from https://registry.ai-sdk.dev/all.json
Installs components using the shadcn/ui CLI under the hood
Adds dependencies and integrates with your existing shadcn/ui setup
Components are installed to your configured shadcn/ui components directory (typically @/components/ai-elements/) and become part of your codebase, allowing for full customization.

## Roadmap Features
- Web Interface: Polished, responsive design
- API Access: Developer-friendly programmatic access
- Advanced Task Planning: Multi-step task capabilities
- Customizable Agents: Domain-specific agent creation
- Collaboration Features: Team-based agent sharing

Feel free to suggest additions or modifications as the project evolves.