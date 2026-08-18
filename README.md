# RAG Fake News Detection

A Retrieval-Augmented Generation (RAG) based system for detecting and analyzing fake news using a combination of a news dataset, vector database, web/news retrieval, and an LLM.

The system retrieves relevant information from the local knowledge base and external news sources before generating an evidence-based analysis of the submitted news content.

---

## Features

- Fake news classification
- RAG-based information retrieval
- Local vector database
- Semantic similarity search
- NewsAPI integration
- Google Programmable Search integration
- LLM-based explanation
- Evidence-based analysis
- Local dataset support
- REST/API-ready project structure
- Environment-variable based API configuration
- Modular architecture

---

## System Overview

```text
                 ┌─────────────────────┐
                 │     User Input      │
                 │  News / Headline    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Query Processing  │
                 └──────────┬──────────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
    ┌──────────────────┐        ┌──────────────────┐
    │ Local Vector DB  │        │ External Sources │
    │ RAG Retrieval    │        │ News / Web       │
    └────────┬─────────┘        └────────┬─────────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
                ┌─────────────────────┐
                │ Context Aggregation │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │       LLM           │
                │ Analysis / Reasoning│
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Final Verification  │
                │ + Explanation      │
                └─────────────────────┘
