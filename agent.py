import os
import time
from dotenv import load_dotenv
from google import genai
from groq import Groq
from tavily import TavilyClient
import json

# -------------------------
# Environment Setup
# -------------------------
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not all([GEMINI_API_KEY, GROQ_API_KEY, TAVILY_API_KEY]):
    raise RuntimeError("❌ Missing API keys. Check your .env file.")

client = genai.Client(api_key=GEMINI_API_KEY)
groq_client = Groq(api_key=GROQ_API_KEY)
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

# -------------------------
# Router (Groq)
# -------------------------
def router_decide(user_query):
    print("\n[Router] Analyzing user query...")

    prompt = f"""
You are a routing agent.
Decide if web search is REQUIRED to answer the query.

Return JSON only:
{{
  "needs_search": true/false,
  "search_query": "query if needed"
}}

User query:
{user_query}
"""
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-8b-instant",  # safe free-tier model
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        decision_text = response.choices[0].message.content
        print("[Router] Decision:", decision_text)
        try:
            decision_json = json.loads(decision_text)
            return decision_json
        except json.JSONDecodeError:
            # fallback: if parsing fails, assume search is needed
            return {"needs_search": True, "search_query": user_query}
    except Exception as e:
        print("[Router] Error, defaulting to search:", str(e))
        return {"needs_search": True, "search_query": user_query}

# -------------------------
# Web Search Loop (Tavily)
# -------------------------
def perform_search(search_query, max_rounds=3):
    collected_results = []
    for round_num in range(1, max_rounds + 1):
        print(f"\n[Search] Round {round_num}: Searching for '{search_query}'")
        try:
            result = tavily_client.search(
                query=search_query,
                search_depth="advanced",
                max_results=5
            )
        except Exception as e:
            print("[Search] Rate limit or error encountered. Retrying...")
            time.sleep(2)
            continue
        collected_results.extend(result.get("results", []))
        print(f"[Search] Collected {len(collected_results)} results so far")
        if len(collected_results) >= 5:
            print("[Search] Sufficient data gathered.")
            break
        time.sleep(1)
    return collected_results

# -------------------------
# Synthesizer (Gemini)
# -------------------------
def synthesize_answer(user_query, search_results=None):
    print("\n[Synthesizer] Generating final answer...")

    context = ""
    if search_results:
        for idx, item in enumerate(search_results):
            context += f"\nSource {idx+1}:\n{item.get('content','')}\n"

    final_prompt = f"""
You are an autonomous research agent.

User Question:
{user_query}

Research Context:
{context}

Provide a clear, well-structured, and factual answer.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # make sure quota exists
            contents=final_prompt
        )
        return response.text
    except Exception as e:
        print("[Synthesizer] Error:", str(e))
        # fallback to Groq if Gemini fails
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": final_prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content

# -------------------------
# Main Agent Loop
# -------------------------
def autonomous_research_agent():
    print("\n==============================")
    print("🚀 Autonomous Research Agent (Type 'exit' to quit)")
    print("==============================")

    while True:
        user_query = input("\nEnter your research question: ").strip()
        if user_query.lower() in ["exit", "quit"]:
            print("👋 Exiting agent. Goodbye!")
            break

        decision = router_decide(user_query)
        needs_search = decision.get("needs_search", True)
        search_results = None

        if needs_search:
            print("\n[Agent] Web search required.")
            search_query = decision.get("search_query", user_query)
            search_results = perform_search(search_query)
        else:
            print("\n[Agent] Web search NOT required.")

        answer = synthesize_answer(user_query, search_results)

        print("\n==============================")
        print("✅ Final Answer")
        print("==============================")
        print(answer)
        print("\n--- Ready for next question ---")

# -------------------------
# Entry Point
# -------------------------
if __name__ == "__main__":
    autonomous_research_agent()
