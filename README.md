# Production-Grade LLM System
A production-grade LLM system where pretrained transformers handle language understanding, fine-tuning aligns behavior, RAG grounds responses with external knowledge, and the model is served via an API optimized for latency and cost, with full monitoring and evaluation.

## Overview
This project implements a full LLM system covering:
- Tokenization & context control
- Transformer-based inference
- Prompting & fine-tuning
- Retrieval-Augmented Generation (RAG)
- Real-time serving
- Monitoring & evaluation

## Architecture
User → API → RAG → Prompt → LLM → Monitoring

## Key Learnings
- LLMs are stateless text generators
- RAG adds memory
- Fine-tuning aligns behavior
- Serving is a systems problem

## Run Locally
docker build -t llm-system .
docker run -p 8000:8000 llm-system