# 🤖 AI Brand Trust Analyzer

🎥 **Demo (1 min):**  
https://www.loom.com/share/e70eba66bd0f4fd6966f09aa5c9db3bc

> Analyze how AI systems *perceive, understand, and trust* your brand.

---

##  Overview

Search is changing.

People are no longer just Googling—they’re asking AI.

But here’s the problem:

> **AI systems don’t just fail to show brands — they often misunderstand them.**

This project explores that gap.

**AI Brand Trust Analyzer** evaluates how Large Language Models (LLMs) represent a brand across different prompts and surfaces:

- Visibility gaps  
- Misrepresentation issues  
- Trust signals  
- Actionable fixes  

---

##  Why this matters

Traditional SEO answers:
> “Can users find your website?”

This project answers:
> **“Does AI understand and trust your brand?”**

That’s the shift from:
- SEO → GEO (Generative Engine Optimization)

---

##  What it does

Given a brand (e.g., *Dageno AI*), the tool:

### 1. Runs real-world prompts
Examples:
- What is the brand?
- Is it reliable?
- Should I use it?
- Alternatives
- Category comparisons

---

### 2. Analyzes responses

Each response is classified into:

| Category | Meaning |
|--------|--------|
| 🟢 Strong | Clearly understood & recommended |
| 🟡 Moderate | Mentioned but weak |
| ⚠️ Weak | Uncertain / vague |
| ❌ Missing | Not recognized |
| 🔴 Misrepresented | Confused with wrong category |

---

### 3. Generates a Trust Score

A simple metric (0–100) reflecting:
- visibility
- clarity
- recommendation strength

---

### 4. Surfaces Key Insight

Example:
> *“Brand is being actively misclassified across multiple prompts, indicating weak semantic positioning in AI systems.”*

---

### 5. Determines Impact

| Level | Meaning |
|------|--------|
| Critical | Misrepresentation across prompts |
| High | Missing from key queries |
| Moderate | Partial visibility |

---

### 6. Suggests fixes

Actionable improvements like:
- Improve positioning
- Increase authoritative mentions
- Optimize for GEO queries
- Strengthen AI training signals

---

## 🖥️ Demo

**Example: Dageno AI**

- ❌ Not recognized in multiple prompts  
- 🔴 Misclassified as geospatial tools / chatbots  
- 🔥 Trust Score: **0/100**  
- ⚠️ Impact: **Critical**

> Insight: The issue isn’t just visibility — it’s how the model understands the brand.

---

##  Tech Stack

- Python  
- Streamlit (UI)  
- Groq API (LLM inference)  
- Rule-based trust analysis  

---

##  Setup

### 1. Clone repo
```
bash
git clone https://github.com/Ajayreddy18/ai-brand-trust-analyzer.git
cd ai-brand-trust-analyzer  

```

### 2. Install dependencies

pip install -r requirements.txt

### 3. Add API Key

GROQ_API_KEY=your_api_key_here

### 4. Run APP

streamlit run app.py


## Example Output

Trust Score: 0/100

AI Visibility Status:
Critical — Brand is misrepresented across AI systems

Key Insight:
Brand is being actively misclassified across multiple prompts

Impact:
Critical

## Project Structure
```
ai-brand-trust-analyzer/
│── app.py
│── analyzer.py
│── prompts.py
│── requirements.txt
│── README.md 

```

## Future Improvements

1.Multi-model comparison (GPT, Claude, Gemini)
2.Real-time web grounding
3.Brand monitoring dashboard
4.Historical tracking of AI visibility
5.Automated GEO recommendations

## Key Takeaway

In the age of AI, it's not enough for your brand to exist online.

It needs to be understood, positioned, and trusted by AI systems.

## Inspiration

Inspired by the emerging field of Generative Engine Optimization (GEO) and the shift in how users discover products through AI.

## Contact

Built by Ajay Reddy

If you're working on similar problems or building in this space, feel free to connect.