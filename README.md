# RAG-Based Fake News Detection

A Retrieval-Augmented Generation (RAG) based Fake News Detection system that combines a historical fake/real news dataset, semantic search, vector database retrieval, external news retrieval, web search, and Large Language Model (LLM) reasoning.

The project is designed to analyze a news headline, claim, or article and provide an evidence-assisted assessment using information retrieved from multiple sources.

---

## Overview

Traditional fake-news detection systems mainly depend on static datasets and trained classification models. Such systems can struggle when the submitted claim is related to recent events that are not present in the training data.

This project addresses that limitation by combining:

- Fake and real news datasets
- Text embeddings
- Semantic similarity search
- Vector database
- Retrieval-Augmented Generation
- Current news retrieval
- Web search
- LLM-based analysis
- Evidence-based reasoning

The system retrieves relevant information before asking the LLM to analyze the submitted claim.

---

## Objectives

The main objectives of this project are:

- Detect potentially fake or real news.
- Retrieve historically similar news from a local knowledge base.
- Retrieve current information from external news sources.
- Search the web for additional evidence.
- Combine information from multiple sources.
- Use an LLM to analyze the retrieved evidence.
- Generate an explainable response instead of relying only on a classification label.
- Build a modular architecture that can be extended with additional models and data sources.

---

## Key Features

### Fake News Analysis

Analyzes a submitted news headline, article, or claim.

### RAG-Based Retrieval

Retrieves relevant documents from the local knowledge base before LLM analysis.

### Semantic Search

Uses embeddings to find documents based on semantic similarity rather than only exact keyword matching.

### Vector Database

Stores document embeddings and metadata for efficient similarity-based retrieval.

### External News Retrieval

Retrieves current news information using a news-search API.

### Web Search

Uses programmable web search to obtain additional information from the internet.

### LLM Analysis

Uses a Large Language Model to analyze the original claim together with retrieved evidence.

### Modular Architecture

The application separates dataset processing, retrieval, external APIs, LLM processing, and application logic.

---

## System Workflow

```text
User Input
    |
    v
Query Processing
    |
    +-------------------------+
    |                         |
    v                         v
Local RAG Retrieval     External Retrieval
    |                         |
    |                  +------+------+
    |                  |             |
    |                  v             v
    |               News API    Google Search
    |                  |             |
    +------------------+-------------+
                       |
                       v
              Evidence Collection
                       |
                       v
                Context Building
                       |
                       v
                  LLM Analysis
                       |
                       v
                 Generated Result
