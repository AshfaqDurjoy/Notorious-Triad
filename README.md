<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Autonomous Research Agent</title>
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        margin: 40px;
        line-height: 1.6;
        background-color: #f6f8fa;
        color: #24292e;
    }
    .container {
        background: white;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        max-width: 900px;
        margin: auto;
    }
    h1, h2, h3 {
        border-bottom: 1px solid #eaecef;
        padding-bottom: 8px;
    }
    .badges img {
        margin: 5px 5px 5px 0;
    }
    code {
        background: #f3f4f6;
        padding: 4px 6px;
        border-radius: 5px;
        font-size: 14px;
    }
    pre {
        background: #f3f4f6;
        padding: 15px;
        border-radius: 8px;
        overflow-x: auto;
    }
    table {
        border-collapse: collapse;
        width: 100%;
    }
    table, th, td {
        border: 1px solid #d0d7de;
    }
    th, td {
        padding: 10px;
        text-align: left;
    }
    .footer {
        margin-top: 40px;
        font-size: 14px;
        color: #6a737d;
    }
</style>
</head>
<body>
<div class="container">

<h1>🚀 Autonomous Research Agent</h1>

<div class="badges">
    <img src="https://img.shields.io/badge/Python-3.11%2B-blue.svg">
    <img src="https://img.shields.io/badge/License-MIT-green.svg">
    <img src="https://img.shields.io/badge/Status-Active-success.svg">
    <img src="https://img.shields.io/badge/API-Free--Tier-orange.svg">
    <img src="https://img.shields.io/badge/LLM-3--Model%20Stack-purple.svg">
</div>

<p>
An <strong>Autonomous Research Agent</strong> powered by a 
<strong>3-API free-tier stack</strong>:
</p>

<ul>
    <li>⚡ <strong>Fast Router:</strong> Groq Llama 3.3</li>
    <li>🧠 <strong>Final Synthesis:</strong> Google Gemini 2.0</li>
    <li>🌐 <strong>Live Web Search:</strong> Tavily</li>
</ul>

<p>
This system performs intelligent routing, optional live search, 
and high-quality answer synthesis inside a persistent interactive loop.
</p>

<h2>🏗 Architecture Overview</h2>

<pre>
User → Groq Router → (Optional Tavily Search) → Gemini Synthesizer → Final Answer
</pre>

<h3>Stack Breakdown</h3>

<table>
<tr>
    <th>Component</th>
    <th>Provider</th>
    <th>Role</th>
</tr>
<tr>
    <td>Router</td>
    <td>Groq</td>
    <td>Fast reasoning & execution</td>
</tr>
<tr>
    <td>Synthesizer</td>
    <td>Gemini 2.0</td>
    <td>Final structured response</td>
</tr>
<tr>
    <td>Web Search</td>
    <td>Tavily</td>
    <td>Real-time search retrieval</td>
</tr>
</table>

<h2>✨ Features</h2>

<ul>
    <li>⚡ Multi-LLM orchestration</li>
    <li>🌐 Live web search capability</li>
    <li>💰 Free-tier friendly architecture</li>
    <li>🔁 Persistent research session loop</li>
    <li>🔐 Secure environment variable management</li>
    <li>🧩 Modular & extensible design</li>
</ul>

<h2>📋 System Requirements</h2>

<ul>
    <li>Python 3.11+</li>
    <li>Internet connection</li>
    <li>API keys for Gemini, Groq, and Tavily</li>
</ul>

<h2>⚙️ Installation</h2>

<h3>Clone Repository</h3>

<pre>
git clone https://github.com/AshfaqDurjoy/Notorious-Triad.git
cd Notorious-Triad
</pre>

<h3>Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<p>Or manually:</p>

<pre>
pip install google-generativeai groq tavily-python python-dotenv
</pre>

<h2>🔑 Environment Configuration</h2>

<p>Create a <code>.env</code> file in the root directory:</p>

<pre>
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
</pre>

<h2>▶️ Run the Agent</h2>

<pre>
python agent.py
</pre>

<p>Exit using <code>exit</code> or <code>Ctrl + C</code>.</p>

<h2>💬 Example Queries</h2>

<pre>
What are the latest advancements in AI agents?
Summarize today’s top tech news.
Compare Gemini 2.0 vs GPT models.
</pre>

<h2>🔮 Roadmap</h2>

<ul>
    <li>Streaming responses</li>
    <li>Citation formatting</li>
    <li>Persistent memory system</li>
    <li>Async parallel API calls</li>
    <li>Docker containerization</li>
    <li>Web UI</li>
</ul>

<h2>🛡 Security Notice</h2>

<p>Never commit API keys. Always use environment variables.</p>

<h2>📄 License</h2>

<p>Licensed under the MIT License.</p>

<div class="footer">
    Built with a 3-Model Free-Tier LLM Stack 🚀
</div>

</div>
</body>
</html>
