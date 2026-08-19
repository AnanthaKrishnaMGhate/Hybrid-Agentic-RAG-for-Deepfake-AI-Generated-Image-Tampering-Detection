# ARCHITECTURE.md

# RAG-Based Fake News Detection — Architecture

## 1. Architecture Overview

The system follows a Retrieval-Augmented Generation (RAG) architecture.

The architecture combines:

- Local fake/real news dataset
- Text preprocessing
- Text embeddings
- Vector database
- Semantic retrieval
- Current news retrieval
- Web search
- Evidence processing
- LLM-based reasoning
- Application interface

The system is divided into independent modules so that dataset processing, retrieval, external APIs, LLM processing, and the application can be modified independently.

---

# 2. High-Level Architecture

```text
                         USER
                           |
                           v
                  +------------------+
                  | Application / UI |
                  |     / API        |
                  +--------+---------+
                           |
                           v
                  +------------------+
                  | Query Processing |
                  +--------+---------+
                           |
             +-------------+-------------+
             |                           |
             v                           v
      +--------------+           +--------------+
      | Local RAG    |           | External     |
      | Retrieval    |           | Retrieval    |
      +------+-------+           +------+-------+
             |                          |
             v                    +-----+------+
      +--------------+             |            |
      | Vector       |             v            v
      | Database     |          News API    Google Search
      +------+-------+             |            |
             |                     |            |
             +----------+----------+------------+
                        |
                        v
                +---------------+
                | Evidence      |
                | Aggregation    |
                +-------+-------+
                        |
                        v
                +---------------+
                | Context       |
                | Builder       |
                +-------+-------+
                        |
                        v
                +---------------+
                | LLM           |
                | Groq / LLaMA  |
                +-------+-------+
                        |
                        v
                +---------------+
                | Result        |
                | Generation    |
                +-------+-------+
                        |
                        v
                       USER
