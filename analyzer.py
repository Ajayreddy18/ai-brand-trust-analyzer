def analyze_trust(response, brand):
    r = response.lower()
    b = brand.lower()

    # 🔴 Missing (no knowledge / uncertainty)
    if any(x in r for x in [
        "don't have information",
        "do not have information",
        "no information",
        "cannot verify",
        "not aware",
        "unclear",
        "not enough information",
        "don't have enough information",
        "i couldn't find",
        "cannot help you decide",
        "don't have specific",
        "i don't have any information"
    ]):
        return "Missing"

    # 🔴 Misrepresentation (wrong category / confusion)
    if any(x in r for x in [
        "dall-e",
        "image generator",
        "geospatial",
        "mapping tool",
        "chatbot",
        "virtual assistant"
    ]):
        return "Misrepresented"

    # 🔴 Brand not mentioned
    if b not in r:
        return "Missing"

    # 🟢 Strong signals
    if any(x in r for x in [
        "best",
        "recommended",
        "popular",
        "widely used",
        "leading"
    ]):
        return "Strong"

    # 🟡 Weak signals
    if any(x in r for x in [
        "might be",
        "possibly",
        "could be",
        "seems like"
    ]):
        return "Weak"

    return "Moderate"


# 📊 Score calculation
def calculate_score(results):
    score_map = {
        "Strong": 20,
        "Moderate": 10,
        "Weak": 5,
        "Missing": 0,
        "Misrepresented": 0
    }
    return sum(score_map[r] for r in results)


# 🔧 Suggested fixes
def suggest_fixes(results):
    fixes = []

    if "Missing" in results:
        fixes.append("Brand is not recognized by LLMs → requires stronger presence in training data sources")

    if "Misrepresented" in results:
        fixes.append("High misrepresentation (wrong category) → fix positioning across web content")

    if "Weak" in results or "Moderate" in results:
        fixes.append("Weak trust signals → improve authority through blogs, docs, and citations")

    fixes.append("Missing from decision-making prompts → optimize for GEO queries and comparisons")

    return list(set(fixes))


# 🧠 Key insight
def generate_insight(results, brand):
    mis = results.count("Misrepresented")
    missing = results.count("Missing")

    if mis >= 2:
        return f"{brand} is being actively misclassified across multiple prompts, indicating weak semantic positioning in AI systems."

    if missing >= 2:
        return f"{brand} is not being recognized by AI systems in key prompts, indicating low visibility in LLM knowledge."

    return f"{brand} has partial visibility but lacks strong trust and positioning signals in AI responses."


# ⚠️ Impact level
def get_impact(results):
    mis = results.count("Misrepresented")
    missing = results.count("Missing")

    if mis >= 2:
        return "Critical"
    elif missing >= 2:
        return "High"
    else:
        return "Moderate"


# 🚨 Visibility status (top summary)
def get_visibility_status(results):
    if results.count("Misrepresented") >= 2:
        return "Critical — Brand is misrepresented across AI systems"
    elif results.count("Missing") >= 2:
        return "High Risk — Brand is not recognized in key prompts"
    else:
        return "Moderate — Partial visibility but weak positioning"