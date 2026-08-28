# Tutorials and Learning Resources

This document lists learning resources relevant to Large Language Models, Transformers, Retrieval-Augmented Generation, long-context processing, and research synthesis.

---

## 1. Hugging Face LLM Course

**Provider:** Hugging Face

**Type:** Online Course

**Topic:** Large Language Models and Transformers

**Description:**  
The Hugging Face LLM Course provides a structured introduction to Natural Language Processing, Transformer models, large language models, datasets, tokenizers, fine-tuning, and advanced LLM topics.

**Why It Is Relevant:**  
Understanding Transformer architecture and LLM inference provides the foundation for studying context-window behavior and degradation.

**Resource:**  
https://huggingface.co/learn/llm-course/

---

## 2. Hugging Face Transformers Course

**Provider:** Hugging Face

**Type:** Tutorial / Documentation

**Topic:** Transformer Models

**Description:**  
The course introduces Transformer models, how they work, how to use pretrained models, and how to perform common NLP and LLM tasks.

**Why It Is Relevant:**  
Transformer architecture and attention mechanisms are fundamental to understanding why context length can affect retrieval and reasoning.

**Resource:**  
https://huggingface.co/learn/llm-course/chapter1/1

---

## 3. Hugging Face RAG Documentation

**Provider:** Hugging Face

**Type:** Technical Tutorial

**Topic:** Retrieval-Augmented Generation

**Description:**  
The RAG documentation explains how retrieval-augmented generation combines a language model with an external information source. Retrieved passages are supplied to the model during generation.

**Why It Is Relevant:**  
RAG is an important alternative to putting an entire document collection into a single context window. It is therefore directly relevant to comparing retrieval-based processing with direct long-context processing.

**Resource:**  
https://huggingface.co/docs/transformers/model_doc/rag

---

## 4. Building RAG with Custom Unstructured Data

**Provider:** Hugging Face

**Type:** Practical Tutorial / Cookbook

**Topic:** Document Processing and RAG

**Description:**  
This tutorial demonstrates how to build a RAG system using documents in multiple formats, including PDFs, PowerPoint files, EPUB files, HTML pages, and other document types.

The workflow includes document preprocessing, embeddings, vector storage, retrieval, and language-model generation.

**Why It Is Relevant:**  
Long-document research frequently involves heterogeneous sources. This tutorial provides a practical example of preprocessing and retrieving information from multiple document types.

**Resource:**  
https://huggingface.co/learn/cookbook/rag_with_unstructured_data

---

## 5. Hugging Face AI Agents Course

**Provider:** Hugging Face

**Type:** Online Course

**Topic:** LLM Agents and Agentic RAG

**Description:**  
The Hugging Face Agents Course introduces AI agents, tools, agent frameworks, and agentic Retrieval-Augmented Generation.

**Why It Is Relevant:**  
Research synthesis systems increasingly combine long-context models with retrieval, tools, and multi-step workflows. Agentic approaches provide a useful direction for future research into long-document synthesis.

**Resource:**  
https://huggingface.co/learn/agents-course/

---

# Resource Comparison

| Resource | Main Topic | Relevance |
|---|---|---|
| Hugging Face LLM Course | LLMs and Transformers | Very High |
| Transformers Course | Transformer Architecture | Very High |
| RAG Documentation | Retrieval-Augmented Generation | Very High |
| RAG with Unstructured Data | Multi-format Document RAG | Very High |
| AI Agents Course | Agents and Agentic RAG | High |

---

# Recommended Learning Sequence

The resources can be studied in the following order:

```text
Hugging Face LLM Course
          ↓
Transformer Architecture
          ↓
RAG Concepts
          ↓
Document Processing + RAG
          ↓
Agents and Agentic RAG
          ↓
Long-Document Research Synthesis
