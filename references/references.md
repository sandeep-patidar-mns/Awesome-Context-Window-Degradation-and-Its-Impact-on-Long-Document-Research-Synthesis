# References

## 1. Attention Is All You Need

**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin

**Year:** 2017

**Venue:** Advances in Neural Information Processing Systems (NeurIPS)

**Topic:** Transformer architecture and self-attention

**Relevance:** This paper introduced the Transformer architecture based on self-attention, which forms the foundation of modern Large Language Models and their ability to process contextual information.

---

## 2. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Authors:** Patrick Lewis et al.

**Year:** 2020

**Venue:** Advances in Neural Information Processing Systems (NeurIPS)

**Topic:** Retrieval-Augmented Generation (RAG)

**Relevance:** This work introduced Retrieval-Augmented Generation, which combines information retrieval with language-model generation. RAG is highly relevant to long-document research because relevant passages can be retrieved instead of placing an entire document collection into the model context.

---

## 3. RoFormer: Enhanced Transformer with Rotary Position Embedding

**Authors:** Jianlin Su et al.

**Year:** 2021

**Topic:** Rotary Position Embedding (RoPE)

**Relevance:** RoPE is an important positional encoding method used in Transformer-based language models. Positional representations are particularly relevant when studying how models behave as context length increases.

---

## 4. Lost in the Middle: How Language Models Use Long Contexts

**Authors:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang

**Year:** 2024

**Venue:** Transactions of the Association for Computational Linguistics, Volume 12, pages 157–173

**DOI:** 10.1162/tacl_a_00638

**Topic:** Long-context utilization and positional effects

**Relevance:** This is a central reference for this research topic. The study examines multi-document question answering and key-value retrieval and finds that model performance can substantially degrade when relevant information is placed in the middle of a long context. Performance is often stronger when relevant information appears near the beginning or end of the context. :contentReference[oaicite:1]{index=1}

**Official Source:**  
https://aclanthology.org/2024.tacl-1.9/

---

## 5. LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

**Authors:** Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, and Juanzi Li

**Year:** 2024

**Venue:** Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (ACL), pages 3119–3137

**DOI:** 10.18653/v1/2024.acl-long.172

**Topic:** Long-context benchmarking

**Relevance:** LongBench is a bilingual, multitask benchmark designed to evaluate long-context understanding. It contains 21 datasets covering six task categories, including single-document question answering, multi-document question answering, summarization, few-shot learning, synthetic tasks, and code completion. :contentReference[oaicite:2]{index=2}

**Official Source:**  
https://aclanthology.org/2024.acl-long.172/

---

## 6. RULER: What's the Real Context Size of Your Long-Context Language Models?

**Authors:** Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, and Boris Ginsburg

**Year:** 2024

**Topic:** Long-context evaluation

**Relevance:** RULER extends the traditional Needle-in-a-Haystack evaluation approach with a broader set of tasks. It includes multiple needles, multi-hop tracing, and aggregation tasks to evaluate long-context capabilities beyond simple retrieval. The authors report that many models experience substantial performance drops as context length and task complexity increase. :contentReference[oaicite:3]{index=3}

**Official Source:**  
https://arxiv.org/abs/2404.06654

---

## 7. Efficient Streaming Language Models with Attention Sinks

**Authors:** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis

**Year:** 2024

**Venue:** International Conference on Learning Representations (ICLR)

**Topic:** Attention sinks and efficient long-sequence processing

**Relevance:** This research investigates the phenomenon of attention sinks, where initial tokens can receive strong attention even when they are not semantically important. The work proposes StreamingLLM techniques for maintaining efficient language-model performance during long or continuous sequences. :contentReference[oaicite:4]{index=4}

**Official Source:**  
https://hanlab.mit.edu/projects/streamingllm

---

## 8. Needle in a Haystack

**Author:** Greg Kamradt

**Year:** 2023

**Topic:** Long-context retrieval evaluation

**Relevance:** Needle-in-a-Haystack is a practical evaluation method that places a target piece of information inside a large amount of distracting text. The target can be positioned at different locations to examine whether a model can retrieve information across a long context.

**Repository:**  
https://github.com/gkamradt/LLMTest_NeedleInAHaystack

---

# Additional Research Areas

The following areas are relevant to the study of context-window degradation and long-document research synthesis:

- Long-context Transformer architectures
- Rotary Position Embedding (RoPE)
- Position interpolation
- RoPE scaling
- NTK-aware scaling
- YaRN
- Sparse attention
- Sliding-window attention
- Streaming language models
- KV-cache optimization
- Retrieval-Augmented Generation
- Hierarchical summarization
- Recursive summarization
- Multi-document question answering
- Long-context reasoning
- Research synthesis
- Context compression
- Information retrieval

---

# Reference Verification

Before using a reference in an academic submission, the following information should be independently checked:

- Exact paper title
- Author names
- Publication year
- Conference or journal
- DOI, when available
- Official publication page
- Research relevance
- Repository or implementation, when applicable

AI-generated bibliographic information should not be treated as automatically verified.

---

# Research Topic

**Context-Window Degradation and Its Impact on Long-Document Research Synthesis**

This reference collection supports research into how Large Language Models process, retrieve, reason over, and synthesize information from long contexts.

---

# Author

**Sandeep Patidar**

**Institution:** Indian Institute of Information Technology Allahabad (IIIT Allahabad)

**Department:** IT

**Course/Program:** MNS

**GitHub:** sandeep-patidar-mns

**Academic Year:** 2026
