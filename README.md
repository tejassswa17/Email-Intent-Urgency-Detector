# Email Intent & Urgency Detector

An AI-powered email classification system that analyzes email text to detect **intent**, **urgency**, and **tone** using Large Language Models (LLMs), LangChain, and Pydantic.

This project helps automate email understanding for support systems, ticketing platforms, and customer communication workflows.

---

## Features

- Intent Detection
- Urgency Classification
- Tone Analysis
- Structured JSON Output
- Pydantic Validation
- Modular Project Architecture
- Supports Groq and Gemini APIs

---

## Tech Stack

- Python
- LangChain
- Pydantic
- Groq / Gemini API
- dotenv

---

## Project Structure

```bash
Email-Intent-Urgency-Detector/
│
├── main.py          # Entry point
├── model.py         # LLM configuration
├── prompt.py        # Prompt template
├── parser.py        # Pydantic schemas & parser
├── requirements.txt
└── .env
```

---

## Installation & Setup

### Clone Repository

```bash
git clone https://github.com/tejassswa17/Email-Intent-Urgency-Detector.git
cd Email-Intent-Urgency-Detector
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Mac/Linux

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

---

## Run Application

```bash
python main.py
```

---

## Example Input

```text
Please resolve the payment issue immediately.
```

## Example Output

```json
{
  "intent": "Request",
  "urgency": "High",
  "tone": "Urgent"
}
```

---

## Supported Categories

### Intent
- Request
- Complaint
- Inquiry
- Information
- Feedback
- Unclear

### Urgency
- Low
- Medium
- High
- Critical
- Unclear

### Tone
- Polite
- Neutral
- Urgent
- Angry
- Professional
- Unclear

---

## Future Improvements

- Streamlit UI
- REST API Integration
- Multi-language Support
- Fine-tuned Email Classification Models

---
