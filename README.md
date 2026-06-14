# AI Resume Screening ATS Chatbot

## Overview

AI Resume Screening ATS Chatbot is a Generative AI application that helps recruiters evaluate candidate resumes against a job description (JD).

The application allows recruiters to:

* Upload multiple candidate resumes (PDF format)
* Provide a Job Description (JD)
* Automatically analyze candidate suitability
* Generate ATS match scores
* Identify matched and missing skills
* Rank candidates based on job fit
* Provide AI-generated recommendations

This project leverages Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), FAISS vector databases, and Streamlit for an interactive user experience.

---

## Features

### Resume Upload

* Upload one or multiple PDF resumes.
* Extract text from resumes.

### Job Description Analysis

* Paste job descriptions directly into the application.
* Compare resumes against job requirements.

### AI-Powered ATS Scoring

* Generate candidate match scores.
* Identify matched skills.
* Highlight missing skills.

### Candidate Ranking

* Rank candidates from best match to lowest match.
* Display recruiter-friendly recommendations.

### Retrieval-Augmented Generation (RAG)

* Uses embeddings and FAISS vector stores.
* Retrieves relevant resume sections before sending context to the LLM.

---

## Architecture

```text
Recruiter
    │
    ▼
Job Description
    │
    ▼
Resume Uploads
    │
    ▼
PDF Parsing
    │
    ▼
Text Splitting
    │
    ▼
Embeddings
    │
    ▼
FAISS Vector Store
    │
    ▼
Retriever
    │
    ▼
LLM Analysis
    │
    ▼
ATS Scoring & Ranking
    │
    ▼
Streamlit Dashboard
```

---

## Technology Stack

### Frontend

* Streamlit

### AI Framework

* LangChain

### LLM

* OpenAI GPT Models

### Vector Database

* FAISS

### Embeddings

* OpenAI Embeddings

### PDF Processing

* PyPDF

### Programming Language

* Python

---

## Project Structure

```text
resume-ats-chatbot/
│
├── app.py
├── rag_pipeline.py
├── utils.py
├── requirements.txt
├── uploads/
│
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-resume-screening-chatbot.git

cd ai-resume-screening-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Run Application

```bash
streamlit run app.py
```

Application will start on:

```text
http://localhost:8501
```

---

## How It Works

### Step 1

Recruiter enters a Job Description.

### Step 2

Recruiter uploads one or more candidate resumes.

### Step 3

The application:

* Extracts resume text
* Splits documents into chunks
* Generates embeddings
* Stores embeddings in FAISS

### Step 4

Relevant resume sections are retrieved using semantic search.

### Step 5

The LLM compares the resume against the Job Description.

### Step 6

The system generates:

* ATS Match Score
* Skill Match Analysis
* Missing Skills
* Candidate Summary
* Hiring Recommendation

### Step 7

Candidates are ranked based on their ATS scores.

---

## Example Output

```text
Candidate: John_Doe.pdf

Match Score: 91%

Matched Skills:
- Python
- SQL
- Machine Learning
- FastAPI

Missing Skills:
- Docker

Recommendation:
Strong candidate for AI Engineer position.
```

---

## Future Enhancements

### Resume Improvement Suggestions

Provide recommendations to improve candidate resumes.

### Interview Question Generator

Generate technical and HR interview questions.

### Candidate Comparison

Compare two or more candidates side-by-side.

### Export Reports

Generate PDF or Excel reports.

### Authentication

Add recruiter login and role-based access.

### Database Integration

Store candidate analysis and rankings in PostgreSQL.

### Multi-Agent ATS

Implement specialized agents for:

* Resume Parsing
* Skill Extraction
* Candidate Ranking
* Interview Generation

---

## Learning Outcomes

This project demonstrates:

* Generative AI
* Prompt Engineering
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embeddings
* Semantic Search
* Streamlit Development
* LangChain
* Resume Screening Automation
* ATS System Design

---

## Author

Sathish Kumar Moorthy

AI Engineer | Generative AI Developer | LangChain | RAG | Agentic AI
