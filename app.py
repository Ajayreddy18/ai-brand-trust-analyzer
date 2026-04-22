import streamlit as st
from groq import Groq
from prompts import get_prompts
from analyzer import (
    analyze_trust,
    calculate_score,
    suggest_fixes,
    generate_insight,
    get_impact,
    get_visibility_status
)
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Brand Trust Analyzer", layout="centered")

st.title(" AI Brand Trust Analyzer")
st.write("Analyze how AI systems perceive and trust your brand")

brand = st.text_input("Enter Brand Name")


def get_response(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


if st.button("Analyze") and brand:
    st.info("Running analysis...")

    prompts = get_prompts(brand)
    results = []

    for p in prompts:
        response = get_response(p)
        trust = analyze_trust(response, brand)

        with st.expander(p):
            st.write(response)
            st.write(f"**Trust Level:** {trust}")

        results.append(trust)

    #  Score
    score = calculate_score(results)
    st.success(f" Trust Score: {score}/100")

    #  Visibility Status
    status = get_visibility_status(results)
    st.error(f" AI Visibility Status: {status}")

    #  Insight
    st.subheader(" Key Insight")
    insight = generate_insight(results, brand)
    st.warning(insight)

    #  Impact
    impact = get_impact(results)
    st.subheader(" Impact Level")
    st.error(impact)

    #  Fixes
    st.subheader(" Suggested Fixes")
    fixes = suggest_fixes(results)
    for fix in fixes:
        st.write(f"- {fix}")