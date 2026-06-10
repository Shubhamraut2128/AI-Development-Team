# AI Development Team

## Overview

AI Development Team is a Multi-Agent AI system built using LangGraph and FastAPI. The project simulates a real software development team where specialized AI agents collaborate to analyze requirements, generate backend and frontend code, design databases, perform testing, review code, and generate project documentation.

---

## Architecture

User Requirement
↓
Manager Agent
↓
Backend Agent
↓
Frontend Agent
↓
Database Agent
↓
Testing Agent
↓
Review Agent
↓
Documentation Agent

---

## Features

* Multi-Agent Architecture
* Requirement Analysis
* Backend Code Generation
* Frontend Code Generation
* Database Schema Generation
* Automated Testing Workflow
* Code Review Workflow
* Documentation Generation
* FastAPI Integration
* LangGraph Workflow Orchestration

---

## Tech Stack

* Python
* LangGraph
* LangChain
* FastAPI
* Uvicorn

---

## Project Structure

ai-dev-team/

app/
├── agents/
├── graph/
├── tools/
├── api/
└── config.py

requirements.txt
run.py

---

## Installation

Clone Repository

git clone https://github.com/yourusername/ai-dev-team.git

Move to Project Directory

cd ai-dev-team

Create Virtual Environment

python -m venv venv

Activate Environment

Windows

venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

---

## Run Application

python run.py

API Documentation

http://localhost:8000/docs

---

## API Endpoint

POST /generate

Sample Request

{
"requirement": "Build Employee Management System using Spring Boot and React"
}

---

## Future Enhancements

* OpenAI Integration
* MCP Integration
* GitHub Automation
* Jira Integration
* Human-in-the-Loop Approval
* PostgreSQL Support
* Docker Deployment
* RAG Knowledge Base
* Supervisor Agent Pattern

---

## Author

Shubham Raut

Software Engineer | GenAI Engineer | AI Engineer
