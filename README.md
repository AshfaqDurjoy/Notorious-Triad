# Autonomous Research Agent

An **Autonomous Research Agent** built using a **3-API free-tier stack**:  
- **Router / Fast Execution:** Groq Llama 3.3  
- **Synthesis / Final Answer:** Google Gemini 2.0  
- **Live Search / Web Results:** Tavily  

This agent allows you to ask questions, performs optional web searches, and synthesizes answers using large language models. The agent runs in a **persistent loop**, so you can ask multiple questions in a single session.

---

## System Requirements

- Python 3.11+ (tested on Python 3.13)  
- Internet connection  
- Free-tier accounts for Gemini, Groq, and Tavily  

---

## Installation

1. **Clone this repository** (or download your `agent.py` and `.env`):

```bash
git clone https://github.com/AshfaqDurjoy/Notorious-Triad.git
cd Notorious-Triad
```
2. **API Setup

The agent requires three API keys:
Google Gemini 2.0 (Synthesizer)
    Go to Google AI Studio
    Create a project (or use an existing project)
    Enable the Generative Language AP
    Generate an API key
    Free-tier quota may require a new project

Groq Llama (Router & fallback Synthesizer)

    Go to Groq Cloud
    Sign up for free-tier account
    Generate your API key for the Llama model

Tavily Search (Web Search)

    Go to Tavily
    Sign up for a free-tier account
    Generate API key for search
 
3.  Create a similar file to .env Example and Copy the Api Keys and paste them to the .env file

.env file will look like this
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here

4. run the project or 
```bash python agent.py
```
