# Generative AI with LangChain 🚀

This repository contains my hands-on learning journey while following the **Generative AI playlist by CampusX**.

The repository includes practical implementations, notebooks, experiments, and mini-projects covering:
- LLMs
- Chat Models
- Embeddings
- Prompt Engineering
- Output Parsing
- Chains
- Runnables
- Document Loaders
- Text Splitters
- Vector Databases
- Retrievers
- RAG Pipelines
- Tools & Agents using LangChain

---

# 📚 Topics Covered

## 1. LLMs

Introduction to Large Language Models and basic API usage.

| File | Description |
|------|-------------|
| `llm_demo.py` | Basic LLM demonstration |

---

## 2. Chat Models

Working with conversational AI models.

| File | Description |
|------|-------------|
| `chatmodel_gemini.py` | Gemini chat model implementation |

---

## 3. Embedding Models

Generating embeddings and semantic similarity.

| File | Description |
|------|-------------|
| `document_similarity.py` | Document similarity using embeddings |
| `embedding_gemini_doc.py` | Document embedding generation |
| `embedding_gemini_query.py` | Query embedding generation |

---

## 4. Prompts

Prompt engineering and prompt templates.

| File | Description |
|------|-------------|
| `chat_prompt_template.py` | Chat prompt templates |
| `dynamic_prompt_ui.py` | Dynamic prompt generation UI |
| `message_placeholder.py` | Placeholder messages |
| `promtp_generator.py` | Prompt generator |
| `static_prompt_ui.py` | Static prompt interface |
| `chat_history.txt` | Chat history example |

---

## 5. Basic Chatbot

Simple chatbot implementation.

| File | Description |
|------|-------------|
| `chatbot.py` | Basic chatbot using LangChain |

---

## 6. Messages

Understanding message handling in LangChain.

| File | Description |
|------|-------------|
| `messages.py` | Message object handling |

---

## 7. Structured Output

Generating structured responses using schemas.

| File | Description |
|------|-------------|
| `with_strucctured_output_pydantic.py` | Structured output using Pydantic |
| `with_structured_output_typeddict.py` | Structured output using TypedDict |
| `When to use which.png` | Comparison reference |

---

## 8. Output Parsers

Parsing LLM outputs into structured formats.

| File | Description |
|------|-------------|
| `JsonOutputParser.py` | JSON parser example |
| `NormalMethod.py` | Standard parsing methodology |
| `PydanticOutputParser.py` | Pydantic parser |
| `StrOutputParser1.py` | String output parser |

---

## 9. Chains

Building sequential and conditional workflows.

| File | Description |
|------|-------------|
| `simple_chain.py` | Basic chain |
| `sequential_chain.py` | Sequential chain |
| `parallel_chain.py` | Parallel chain |
| `conditional_chain.py` | Conditional chain |
| `Chains.png` | Chain architecture reference |

---

## 10. Runnables

Using LangChain Runnables for modular workflows.

| File | Description |
|------|-------------|
| `Runnable_building_idea.ipynb` | Runnable concepts |
| `normal_methodology.ipynb` | Traditional workflow comparison |
| `runnable_branch.py` | Runnable branching |
| `runnable_lambda.py` | Lambda runnable |
| `runnable_parallel.py` | Parallel runnable execution |
| `runnable_passthrough.py` | Runnable passthrough |
| `runnable_sequence.py` | Runnable sequences |

---

## 11. Document Loaders

Loading data from multiple document sources.

| File | Description |
|------|-------------|
| `csv_loader.py` | CSV document loader |
| `directory_loader.py` | Directory-based loader |
| `pdf_loader.py` | PDF loader |
| `text_loader.py` | Text file loader |
| `web_based_loader.py` | Web-based document loader |
| `Social_Network_Ads.csv` | Sample CSV dataset |
| `cricket.txt` | Sample text document |
| `dl-curriculum.pdf` | Sample PDF |
| `when to use which.png` | Loader selection guide |
| `Books/` | Book resources |

---

## 12. Text Splitters

Splitting documents for embeddings and RAG pipelines.

| File | Description |
|------|-------------|
| `length_based.py` | Length-based splitting |
| `markdown_splitting.py` | Markdown document splitting |
| `python_code_splitting.py` | Code-aware splitting |
| `semantic_meaning_based.py` | Semantic splitting |
| `text_structured_based.py` | Structure-aware splitting |
| `dl-curriculum.pdf` | Example PDF |

---

## 13. Vector Stores

Working with vector databases using ChromaDB.

| File | Description |
|------|-------------|
| `langchain_chroma.ipynb` | Chroma vector store example |
| `my_charoma_db/` | Vector database files |

---

## 14. Retrievers

Document retrieval using vector stores.

| File | Description |
|------|-------------|
| `langchain_retriever.ipynb` | Retriever implementation |
| `my_chroma_db/` | Chroma database |

---

## 15. RAG — YouTube Chatbot

Retrieval-Augmented Generation implementation.

| File | Description |
|------|-------------|
| `rag-using-langchain.ipynb` | YouTube chatbot using RAG |
| `my_chroma_db/` | RAG vector database |

---

## 16. Tools

Tool integration with LangChain.

| File | Description |
|------|-------------|
| `tools-in-langchain.ipynb` | Working with tools |

---

## 17. Tool Binding

Binding tools with LLMs and agents.

| File | Description |
|------|-------------|
| `currency_converter_tool.ipynb` | Currency conversion tool |
| `tool-calling-in-langchain.ipynb` | Tool calling examples |

---

## 18. Agents

Building autonomous AI agents.

| File | Description |
|------|-------------|
| `agents-in-langchain.ipynb` | Agent implementation |

---

# 🛠️ Tech Stack

- Python
- LangChain
- Gemini API
- OpenAI APIs
- ChromaDB
- Vector Embeddings
- RAG Pipelines
- Jupyter Notebook

---

# 📂 Repository Structure

```bash
.
├── 1. LLMs
├── 2. ChatModels
├── 3. EmbeddedModels
├── 4. Prompts
├── 5. Basic Chatbot
├── 6. Messages
├── 7. With Structured Output
├── 8. Output Parser
├── 9. Chains
├── 10. Runnables
├── 11. Document Loader
├── 12. Text Splitters
├── 13. Vector Stores
├── 14. Retrievers
├── 15. RAG - Youtube Chatbot
├── 16. Tools
├── 17. Tool Binding
├── 18. Agents
├── .gitignore
└── template.json
