# Brand Guardian AI - Multimodal Compliance Orchestration Engine

Brand Guardian AI is a powerful, automated system designed to audit video content (specifically YouTube) against brand compliance rules. It uses a multimodal approach, combining Speech-to-Text (STT) and Optical Character Recognition (OCR) with advanced AI reasoning to identify potential violations in both spoken words and visual content.

## 🚀 Key Features

- **Automated Video Compliance**: Scan videos for legal, brand, and safety violations.
- **Multimodal AI Analysis**:
  - **Speech-to-Text**: Analyzes transcripts for misleading claims or sensitive keywords.
  - **OCR (Optical Character Recognition)**: Detects restricted text or logos on screen.
- **LangGraph Orchestration**: Uses a state-based workflow to manage the complex pipeline from ingestion to reporting.
- **Azure Integration**: Leverages Azure Search, Storage, and Identity for secure, scalable processing.
- **Telemetry & Monitoring**: Built-in OpenTelemetry integration with Azure Monitor for real-time tracking and debugging.
- **FastAPI Backend**: A modern, high-performance API for triggering audits and retrieving results.

## 🏗️ Architecture

The compliance pipeline follows a directed flow:

`[START] -> [INDEXER] -> [AUDITOR] -> [END]`

1.  **Indexer Node**: Downloads the video, extracts the audio/visual data, and processes it into searchable content (transcripts/metadata).
2.  **Auditor Node**: Retrieves compliance rules, compares them against the indexed content using LLMs, and generates a detailed violation report.

## 🛠️ Technology Stack

- **Core**: Python 3.12+
- **Orchestration**: [LangGraph](https://github.com/langchain-ai/langgraph)
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **AI Models**: OpenAI GPT-4 (via LangChain)
- **Cloud Infrastructure**: Azure Search, Azure Blob Storage, Azure Identity
- **Package Manager**: [UV](https://github.com/astral-sh/uv)
- **Monitoring**: OpenTelemetry, Azure Monitor (Application Insights)

## 📦 Getting Started

### Prerequisites

- Python 3.12 or higher.
- [UV](https://github.com/astral-sh/uv) installed (`powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`).
- Azure OpenAI / OpenAI API Key.
- Azure Search & Storage accounts.

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Akshu24Tech/Azure-Multimodal-Compliance-Orchestration-Engine.git
    cd Azure-Multimodal-Compliance-Orchestration-Engine/complianceQAPipeline
    ```

2.  Set up environment variables:
    Create a `.env` file in the root directory (copy from `.env.example` if available) and add your keys:
    ```env
    AZURE_OPENAI_API_KEY="..."
    AZURE_OPENAI_ENDPOINT="..."
    AZURE_SEARCH_KEY="..."
    APPLICATIONINSIGHTS_CONNECTION_STRING="..."
    ```

3.  Install dependencies:
    ```bash
    uv sync
    ```

## 🖥️ Usage

### CLI Simulation
To run a quick audit from your terminal:
```bash
python main.py
```

### API Server
To start the FastAPI server with auto-reload:
```bash
uv run uvicorn backend.src.api.server:app --reload
```
The interactive API documentation will be available at: `http://localhost:8000/docs`

## 📡 API Endpoints

- `POST /audit`: Trigger a new video compliance audit.
- `GET /health`: Check service status and health.

---
*Developed for robust multimodal compliance monitoring.*
