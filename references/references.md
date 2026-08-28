# References

## Research Topic

**Context-Window Degradation and Its Impact on Long-Document Research Synthesis**

This document contains verified scholarly references relevant to long-context language models, context-window degradation, information retrieval, attention mechanisms, long-document understanding, evaluation, and research synthesis.

---

## Foundational Transformer and Attention Research

### 1. Attention Is All You Need

**Authors:** Ashish Vaswani et al.  
**Year:** 2017  
**Venue:** NeurIPS 2017  
**Research Area:** Transformer Architecture  
**Relevance:** Foundational

Introduced the Transformer architecture and self-attention mechanism that underlies modern large language models.

**Source:**  
https://arxiv.org/abs/1706.03762

---

### 2. RoFormer: Enhanced Transformer with Rotary Position Embedding

**Authors:** Jianlin Su et al.  
**Year:** 2021  
**Research Area:** Positional Encoding  
**Relevance:** High

Introduced Rotary Position Embedding (RoPE), an important positional representation used by many Transformer-based language models.

**Source:**  
https://arxiv.org/abs/2104.09864

---

### 3. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Authors:** Patrick Lewis et al.  
**Year:** 2020  
**Venue:** NeurIPS 2020  
**Research Area:** Retrieval-Augmented Generation  
**Relevance:** High

Introduced Retrieval-Augmented Generation (RAG), combining language-model generation with retrieved external knowledge.

**Source:**  
https://arxiv.org/abs/2005.11401

---

## Long-Context Behavior and Degradation

### 4. Lost in the Middle: How Language Models Use Long Contexts

**Authors:** Nelson F. Liu et al.  
**Year:** 2024  
**Venue:** Transactions of the Association for Computational Linguistics  
**Research Area:** Long-Context Information Utilization  
**Relevance:** Very High

Investigates how language models use information at different positions within long contexts and demonstrates position-dependent degradation.

**Source:**  
https://arxiv.org/abs/2307.03172

---

### 5. Efficient Streaming Language Models with Attention Sinks

**Authors:** Guangxuan Xiao et al.  
**Year:** 2024  
**Research Area:** Long-Sequence Processing  
**Relevance:** High

Studies attention sinks and streaming language models for maintaining effective generation over long sequences.

**Source:**  
https://arxiv.org/abs/2309.17453

---

### 6. Needle in a Haystack

**Author:** Greg Kamradt  
**Year:** 2023  
**Research Area:** Long-Context Retrieval  
**Relevance:** High

Provides a practical evaluation method for testing whether a model can retrieve a specific piece of information from increasingly large contexts.

**Repository:**  
https://github.com/gkamradt/LLMTest_NeedleInAHaystack

---

## Long-Context Benchmarks and Evaluation

### 7. LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

**Authors:** Yushi Bai et al.  
**Year:** 2024  
**Venue:** ACL 2024  
**Research Area:** Long-Context Benchmarking  
**Relevance:** Very High

Provides a bilingual and multitask benchmark for evaluating long-context understanding across question answering, summarization, synthetic tasks, few-shot learning, and code completion.

**Source:**  
https://aclanthology.org/2024.acl-long.172/

**Repository:**  
https://github.com/THUDM/LongBench

---

### 8. RULER: What's the Real Context Size of Your Long-Context Language Models?

**Authors:** Cheng-Ping Hsieh et al.  
**Year:** 2024  
**Research Area:** Long-Context Evaluation  
**Relevance:** Very High

Evaluates the effective context capabilities of language models using multiple synthetic retrieval, tracing, and aggregation tasks.

**Source:**  
https://arxiv.org/abs/2404.06654

**Repository:**  
https://github.com/NVIDIA/RULER

---

### 9. L-Eval: Instituting Standardized Evaluation for Long Context Language Models

**Authors:** Chenxin An et al.  
**Year:** 2024  
**Venue:** ACL 2024  
**Research Area:** Long-Context Evaluation  
**Relevance:** Very High

Introduces a standardized evaluation suite containing 20 subtasks, 508 long documents, and more than 2,000 human-labeled query-response pairs covering diverse tasks and context lengths.

**Source:**  
https://aclanthology.org/2024.acl-long.776/

---

### 10. LooGLE: Can Long-Context Language Models Understand Long Contexts?

**Authors:** Jiaqi Li, Mengmeng Wang, Zilong Zheng, and Muhan Zhang  
**Year:** 2024  
**Venue:** ACL 2024  
**Research Area:** Long-Context Understanding  
**Relevance:** Very High

Introduces a long-context benchmark containing long documents and questions with varying dependency ranges. The study examines whether models can actually understand long dependencies.

**Source:**  
https://aclanthology.org/2024.acl-long.859/

---

### 11. Ada-LEval: Evaluating Long-Context LLMs with Length-Adaptable Benchmarks

**Authors:** Chonghua Wang, Haodong Duan, Songyang Zhang, Dahua Lin, and Kai Chen  
**Year:** 2024  
**Venue:** NAACL 2024  
**Research Area:** Long-Context Evaluation  
**Relevance:** Very High

Introduces a length-adaptable benchmark capable of generating test cases at different context lengths, including ultra-long settings.

**Source:**  
https://aclanthology.org/2024.naacl-long.205/

**Repository:**  
https://github.com/open-compass/Ada-LEval

---

### 12. BAMBOO: A Comprehensive Benchmark for Evaluating Long Text Modeling Capacities of Large Language Models

**Authors:** Zican Dong, Tianyi Tang, Junyi Li, Wayne Xin Zhao, and Ji-Rong Wen  
**Year:** 2024  
**Venue:** LREC-COLING 2024  
**Research Area:** Long-Text Modeling  
**Relevance:** Very High

Provides a multitask long-context benchmark covering question answering, hallucination detection, text sorting, language modeling, and code completion.

**Source:**  
https://aclanthology.org/2024.lrec-main.188/

---

### 13. M4LE: A Multi-Ability Multi-Range Multi-Task Multi-Domain Long-Context Evaluation Benchmark for Large Language Models

**Authors:** Wai-Chung Kwan et al.  
**Year:** 2024  
**Venue:** ACL 2024  
**Research Area:** Long-Context Evaluation  
**Relevance:** High

Introduces a benchmark spanning multiple abilities, context ranges, tasks, and domains for evaluating long-context language models.

**Source:**  
https://aclanthology.org/2024.acl-long.832/

---

### 14. Leave No Document Behind: Benchmarking Long-Context LLMs with Extended Multi-Doc QA

**Authors:** Minzheng Wang et al.  
**Year:** 2024  
**Venue:** EMNLP 2024  
**Research Area:** Multi-Document Long-Context Understanding  
**Relevance:** Very High

Introduces Loong, a benchmark designed around realistic multi-document scenarios in which every document can contribute information necessary for answering a question.

**Source:**  
https://aclanthology.org/2024.emnlp-main.322/

---

### 15. Marathon: A Race Through the Realm of Long Context with Large Language Models

**Authors:** Lei Zhang et al.  
**Year:** 2024  
**Venue:** ACL 2024  
**Research Area:** Long-Context Reasoning  
**Relevance:** High

Introduces a long-context evaluation benchmark using multiple-choice questions to assess comprehension and reasoning over extended texts.

**Source:**  
https://aclanthology.org/2024.acl-long.284/

---

## Recent Long-Context Research

### 16. HELMET: How to Evaluate Long-context Models Effectively and Thoroughly

**Authors:** Howard Yen et al.  
**Year:** 2025  
**Venue:** ICLR 2025  
**Research Area:** Long-Context Evaluation  
**Relevance:** Very High

HELMET provides a comprehensive evaluation framework covering several application-oriented long-context tasks, including retrieval-augmented generation, question answering, summarization, citation generation, and reranking.

**Source:**  
https://proceedings.iclr.cc/paper_files/paper/2025/hash/f5332c8273d02729730a9c24dec2135e-Abstract-Conference.html

**Project:**  
https://princeton-nlp.github.io/HELMET/

**Repository:**  
https://github.com/princeton-nlp/HELMET

---

### 17. Benchmarking Long-Context Language Models on Long Code Understanding

**Authors:** Jia Li et al.  
**Year:** 2025  
**Venue:** ACL 2025  
**Research Area:** Long-Code Understanding  
**Relevance:** High

Introduces LongCodeU, a benchmark covering multiple aspects of long-code understanding. The study reports substantial performance degradation when code length exceeds 32K tokens.

**Source:**  
https://aclanthology.org/2025.acl-long.1324/

---

### 18. Ref-Long: Benchmarking the Long-context Referencing Capability of Long-context Language Models

**Authors:** Authors listed in ACL Anthology  
**Year:** 2025  
**Venue:** ACL 2025  
**Research Area:** Long-Context Referencing  
**Relevance:** Very High

Introduces a benchmark for evaluating whether long-context language models can correctly attribute information to specific parts of long-context data.

**Source:**  
https://aclanthology.org/2025.acl-long.1162/

---

### 19. MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models

**Authors:** Zhongzhan Huang et al.  
**Year:** 2025  
**Venue:** ACL 2025  
**Research Area:** Efficient Long-Context Evaluation  
**Relevance:** High

Introduces a reduced-cost benchmark derived from LongBench. It aims to reduce evaluation cost while maintaining strong correlation with the original benchmark.

**Source:**  
https://aclanthology.org/2025.acl-long.560/

---

### 20. Counting-Stars: A Multi-evidence, Position-aware, and Scalable Benchmark for Evaluating Long-Context Large Language Models

**Authors:** Mingyang Song, Mao Zheng, and Xuan Luo  
**Year:** 2025  
**Venue:** COLING 2025  
**Research Area:** Position-Aware Long-Context Evaluation  
**Relevance:** Very High

Introduces a multi-evidence and position-aware benchmark for evaluating long-context language models. It is particularly relevant to studying whether information position and evidence distribution affect model performance.

**Source:**  
https://aclanthology.org/2025.coling-main.253/

---

# Reference Categories

## Transformer Foundations

- Attention Is All You Need
- RoFormer: Enhanced Transformer with Rotary Position Embedding

## Retrieval and External Knowledge

- Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- Needle in a Haystack

## Context-Window Degradation

- Lost in the Middle
- Efficient Streaming Language Models with Attention Sinks
- Counting-Stars

## Long-Context Benchmarks

- LongBench
- RULER
- L-Eval
- LooGLE
- Ada-LEval
- BAMBOO
- M4LE
- Loong
- Marathon
- HELMET
- LongCodeU
- Ref-Long
- MiniLongBench

---

# Citation Verification Policy

Every scholarly reference in this repository should be checked against an original publication, publisher page, DOI record, ACL Anthology record, or another authoritative academic source.

The repository distinguishes between:

- **Referenced** — identified as relevant.
- **Verified** — bibliographic information checked against an authoritative source.
- **Tested** — the associated implementation or benchmark has actually been executed.
- **Used** — the source or implementation was used directly in an experiment.

A source must not be described as tested or used unless an actual experiment has been performed.

---

# AI-Assisted Research Disclosure

AI assistance was used during research organization, topic exploration, reference discovery, documentation, and drafting.

AI-generated references were not treated as automatically verified. References should be checked against their original scholarly sources before academic submission.

---

# Research Focus

The references support investigation of:

1. How information position affects long-context retrieval.
2. How model performance changes as context length increases.
3. Whether advertised context windows correspond to effective context utilization.
4. How long-context benchmarks measure retrieval and reasoning.
5. How long documents and multiple documents affect research synthesis.
6. How retrieval and attention mechanisms can mitigate context degradation.
7. How long-context evaluation can be made more realistic and efficient.

The central research question is:

> **How does increasing context length affect the ability of Large Language Models to retrieve, reason over, and synthesize information from long documents?**

---

## Author

**Sandeep Patidar**

**Indian Institute of Information Technology Allahabad (IIIT Allahabad)**

**Department:** IT

**Program:** MNS

**Academic Year:** 2026

**GitHub:** sandeep-patidar-mns
