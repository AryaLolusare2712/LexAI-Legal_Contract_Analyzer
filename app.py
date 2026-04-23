import streamlit as st
import google.generativeai as genai
import json
import re

st.set_page_config(
    page_title="LexAI — Legal Contract Analyzer",
    page_icon="⚖️",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;600&family=DM+Mono&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.main { background: #0f0f13; }
.stApp { background: #0f0f13; }

.lex-header {
    display: flex; align-items: center; gap: 14px;
    padding: 1.5rem 0 1rem;
    border-bottom: 1px solid #1e1e2e;
    margin-bottom: 1.5rem;
}
.lex-logo {
    width: 44px; height: 44px; border-radius: 10px;
    background: #1a1a2e;
    display: flex; align-items: center; justify-content: center;
    font-size: 22px;
}
.lex-title { font-family: 'DM Serif Display', serif; font-size: 26px; color: #e8e6f0; margin:0; }
.lex-sub { font-size: 13px; color: #6b6880; margin:0; }
.lex-badge {
    margin-left: auto; padding: 4px 12px;
    border-radius: 20px; font-size: 11px; font-weight: 600;
    background: #1a2e1a; color: #4ade80;
    border: 1px solid #2a4a2a; letter-spacing: .5px;
}

.score-ring-container {
    text-align: center; padding: 1.5rem;
    background: #141420; border-radius: 16px;
    border: 1px solid #1e1e2e;
}
.score-big {
    font-family: 'DM Serif Display', serif;
    font-size: 64px; line-height: 1;
}

.flag-card {
    background: #141420; border-radius: 12px;
    border: 1px solid #1e1e2e; margin-bottom: 12px;
    overflow: hidden;
}
.flag-header {
    display: flex; align-items: center; gap: 10px;
    padding: 14px 18px;
    border-bottom: 1px solid #1e1e2e;
}
.flag-body { padding: 14px 18px; }

.sev-high   { background:#2e1a1a; color:#f87171; border:1px solid #4a2a2a; border-radius:20px; padding:3px 10px; font-size:11px; font-weight:600; }
.sev-medium { background:#2e2a1a; color:#fbbf24; border:1px solid #4a401a; border-radius:20px; padding:3px 10px; font-size:11px; font-weight:600; }
.sev-low    { background:#1a2e1a; color:#4ade80; border:1px solid #2a4a2a; border-radius:20px; padding:3px 10px; font-size:11px; font-weight:600; }

.excerpt-block {
    font-family: 'DM Mono', monospace; font-size: 12px;
    background: #0f0f18; border-left: 3px solid #f87171;
    border-radius: 0 8px 8px 0; padding: 10px 14px;
    color: #9994b0; margin: 10px 0; line-height: 1.6;
}
.suggestion-block {
    background: #1a2e1a; border-radius: 8px;
    padding: 10px 14px; color: #4ade80; font-size: 13px;
    margin-top: 10px; line-height: 1.5;
}
.flag-row { display:flex; gap:8px; margin:8px 0; font-size:13px; }
.flag-lbl { color:#6b6880; min-width:70px; font-weight:500; }
.flag-val  { color:#c8c4d8; line-height:1.5; }

.comp-ok   { color: #4ade80; font-weight: 600; }
.comp-warn { color: #fbbf24; font-weight: 600; }
.comp-bad  { color: #f87171; font-weight: 600; }

.stat-card {
    background: #141420; border-radius: 12px;
    border: 1px solid #1e1e2e; padding: 1rem 1.25rem;
    text-align: center;
}
.stat-num  { font-family: 'DM Serif Display', serif; font-size: 36px; line-height: 1; }
.stat-lbl  { font-size: 12px; color: #6b6880; margin-top: 4px; }

.arch-note {
    background: #0f0f18; border-radius: 10px;
    border: 1px solid #1e1e2e; padding: 12px 16px;
    font-size: 12px; color: #6b6880; margin-top: 1rem;
    line-height: 1.6;
}
.arch-note strong { color: #9994b0; }

[data-testid="stTextArea"] textarea {
    background: #141420 !important;
    color: #c8c4d8 !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 10px !important;
    font-family: 'DM Mono', monospace !important;
    font-size: 13px !important;
}
[data-testid="stSelectbox"] > div {
    background: #141420 !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 10px !important;
    color: #c8c4d8 !important;
}
.stButton > button {
    background: #1a1a2e !important;
    color: #a78bfa !important;
    border: 1px solid #2e2a4a !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 10px 28px !important;
    font-size: 14px !important;
    transition: all .2s !important;
}
.stButton > button:hover {
    background: #2e2a4a !important;
    border-color: #a78bfa !important;
}
.stTabs [data-baseweb="tab-list"] {
    background: #141420 !important;
    border-radius: 10px !important;
    border: 1px solid #1e1e2e !important;
    gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    color: #6b6880 !important;
    font-weight: 500 !important;
}
.stTabs [aria-selected="true"] {
    background: #1e1e2e !important;
    color: #e8e6f0 !important;
    border-radius: 8px !important;
}
h1,h2,h3 { font-family: 'DM Serif Display', serif !important; color: #e8e6f0 !important; }
p, li { color: #9994b0; }
.stMarkdown { color: #9994b0; }
</style>
""", unsafe_allow_html=True)

SAMPLE_NDA = """NON-DISCLOSURE AGREEMENT

This Agreement is entered into as of January 1, 2024, between Acme Corp ("Disclosing Party") and Contractor ("Receiving Party").

1. CONFIDENTIAL INFORMATION
The Receiving Party agrees to hold in strict confidence ALL information disclosed by Acme Corp, including business strategies, customer lists, trade secrets, and any other information. This obligation shall remain in effect in perpetuity and shall survive termination of any business relationship.

2. NON-COMPETE CLAUSE
Receiving Party agrees not to engage in any business activity that competes with Acme Corp, directly or indirectly, anywhere in the world, for a period of ten (10) years following the termination of this Agreement.

3. LIQUIDATED DAMAGES
In the event of any breach of this Agreement, Receiving Party shall pay liquidated damages of $5,000,000 (five million dollars) per incident, regardless of actual harm caused.

4. TERM
This Agreement shall remain in full force and effect for an indefinite period and may only be terminated by written consent of both parties, which Acme Corp may withhold at its sole discretion.

5. INTELLECTUAL PROPERTY
Any work product, ideas, inventions, or improvements conceived by Receiving Party, whether or not related to Acme Corp's business, during the term of this Agreement shall be the sole and exclusive property of Acme Corp.

6. GOVERNING LAW
This Agreement shall be governed by the laws of the jurisdiction most favorable to Acme Corp, as determined by Acme Corp at the time of any dispute.

7. INDEMNIFICATION
Receiving Party shall indemnify, defend, and hold harmless Acme Corp and its affiliates from any and all claims, liabilities, damages, and expenses arising from Receiving Party's activities, whether or not related to this Agreement."""

def get_risk_color(score):
    if score >= 70: return "#f87171"
    if score >= 40: return "#fbbf24"
    return "#4ade80"

def get_risk_label(score):
    if score >= 70: return "High Risk"
    if score >= 40: return "Medium Risk"
    return "Low Risk"

def draw_ring(score):
    color = get_risk_color(score)
    import math
    r, cx, cy = 70, 90, 90
    circ = 2 * math.pi * r
    dash = (score / 100) * circ
    gap = circ - dash
    offset = circ / 4
    return f"""
    <svg width="180" height="180" viewBox="0 0 180 180">
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#1e1e2e" stroke-width="12"/>
      <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{color}" stroke-width="12"
        stroke-dasharray="{dash:.1f} {gap:.1f}"
        stroke-dashoffset="{offset:.1f}" stroke-linecap="round"/>
      <text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="middle"
        font-family="DM Serif Display, serif" font-size="36" fill="{color}">{score}</text>
      <text x="{cx}" y="{cy+28}" text-anchor="middle"
        font-family="DM Sans, sans-serif" font-size="13" fill="#6b6880">{get_risk_label(score)}</text>
    </svg>"""

def analyze_contract(text, contract_type, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash-preview-04-17",
        generation_config=genai.GenerationConfig(
            temperature=0.2,
            response_mime_type="application/json",
        ),
    )
    prompt = f"""You are an expert legal contract analyst. Analyze this {contract_type} contract and return ONLY a valid JSON object with no markdown fences, no preamble.

Schema:
{{
  "riskScore": <integer 0-100>,
  "summary": "<2-sentence overall assessment>",
  "flags": [
    {{
      "title": "<clause name>",
      "severity": "high|medium|low",
      "excerpt": "<exact problematic text, max 120 chars>",
      "issue": "<what is legally problematic>",
      "impact": "<business/legal impact>",
      "suggestion": "<concrete revision>"
    }}
  ],
  "comparison": [
    {{
      "parameter": "<aspect>",
      "standard": "<market standard for {contract_type}>",
      "thisContract": "<what this contract says>",
      "status": "ok|warn|bad"
    }}
  ],
  "clauses": [
    {{
      "name": "<clause name>",
      "present": true|false,
      "description": "<brief description or note that it is missing>"
    }}
  ]
}}

Return 4-7 flags, 6-8 comparison rows, 6-10 clauses. Be specific.

Contract:
{text[:4000]}"""

    response = model.generate_content(prompt)
    raw = response.text.strip()
    raw = re.sub(r"```json|```", "", raw).strip()
    return json.loads(raw)

# ── Header ────────────────────────────────────────────────
st.markdown("""
<div class="lex-header">
  <div class="lex-logo">⚖️</div>
  <div>
    <div class="lex-title">LexAI</div>
    <div class="lex-sub">Legal Contract Analyzer</div>
  </div>
  <div class="lex-badge">AI-POWERED</div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    api_key = st.text_input("Google AI API Key", type="password", placeholder="AIza...")
    contract_type = st.selectbox("Contract Type", ["NDA","Employment","SaaS","Partnership","Vendor","Lease"])
    st.markdown("---")
    st.markdown("### 📋 Quick Load")
    if st.button("Load Sample NDA"):
        st.session_state["contract_text"] = SAMPLE_NDA
        st.rerun()
    st.markdown("""
<div class="arch-note">
<strong>Model</strong><br>
Gemini 2.5 Flash via Google GenAI SDK<br><br>
<strong>Production stack</strong><br>
• Gemini 2.5 Flash<br>
• LangChain chains<br>
• RAG over legal clause vector store<br>
• FAISS / Pinecone index
</div>
""", unsafe_allow_html=True)

# ── Main input ────────────────────────────────────────────
contract_text = st.text_area(
    "Contract Text",
    value=st.session_state.get("contract_text", ""),
    height=260,
    placeholder="Paste your contract here — NDA, employment agreement, SaaS terms, partnership deed, vendor contract, or lease...",
    label_visibility="collapsed",
)

col_btn, col_tip = st.columns([1, 3])
with col_btn:
    analyze_clicked = st.button("⚖️ Analyze Contract", use_container_width=True)
with col_tip:
    st.markdown("<p style='padding-top:10px;font-size:13px;color:#6b6880'>Tip: load the sample NDA from the sidebar for a demo with 5+ critical flags</p>", unsafe_allow_html=True)

# ── Analysis ──────────────────────────────────────────────
if analyze_clicked:
    if not api_key:
        st.error("Please enter your Google AI API key in the sidebar.")
    elif not contract_text.strip():
        st.error("Please paste a contract or load a sample first.")
    else:
        with st.spinner("Analyzing contract clauses with AI…"):
            try:
                result = analyze_contract(contract_text, contract_type, api_key)
                st.session_state["result"] = result
            except json.JSONDecodeError:
                st.error("Could not parse AI response. Please try again.")
                st.stop()
            except Exception as e:
                st.error(f"Analysis failed: {e}")
                st.stop()

# ── Results ───────────────────────────────────────────────
if "result" in st.session_state:
    d = st.session_state["result"]
    flags  = d.get("flags", [])
    comp   = d.get("comparison", [])
    clauses= d.get("clauses", [])

    high = sum(1 for f in flags if f.get("severity") == "high")
    med  = sum(1 for f in flags if f.get("severity") == "medium")
    low  = sum(1 for f in flags if f.get("severity") == "low")

    st.markdown("---")

    # Summary banner
    st.info(f"**Assessment:** {d.get('summary','')}")

    # Score + stats
    c1, c2, c3, c4, c5 = st.columns([1.4, 1, 1, 1, 1])
    with c1:
        st.markdown(f"""
        <div class="score-ring-container">
          {draw_ring(d.get('riskScore', 0))}
          <div style="font-size:12px;color:#6b6880;margin-top:4px">Overall risk score</div>
        </div>""", unsafe_allow_html=True)
    for col, num, lbl, color in [
        (c2, high, "High severity", "#f87171"),
        (c3, med,  "Medium severity", "#fbbf24"),
        (c4, low,  "Low severity", "#4ade80"),
        (c5, len(clauses), "Clauses found", "#a78bfa"),
    ]:
        with col:
            st.markdown(f"""
            <div class="stat-card">
              <div class="stat-num" style="color:{color}">{num}</div>
              <div class="stat-lbl">{lbl}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([
        f"⚠️ Risk Flags ({len(flags)})",
        "📊 Template Comparison",
        f"📄 All Clauses ({len(clauses)})",
    ])

    # ── Tab 1: Risk Flags ──
    with tab1:
        if not flags:
            st.success("No risk flags detected.")
        for f in flags:
            sev = f.get("severity","low")
            sev_cls = f"sev-{sev}"
            sev_label = sev.capitalize()
            dot = {"high":"🔴","medium":"🟡","low":"🟢"}.get(sev,"⚪")
            st.markdown(f"""
            <div class="flag-card">
              <div class="flag-header">
                <span style="font-size:14px">{dot}</span>
                <span style="font-size:14px;font-weight:600;color:#e8e6f0;flex:1">{f.get('title','')}</span>
                <span class="{sev_cls}">{sev_label}</span>
              </div>
              <div class="flag-body">
                {'<div class="excerpt-block">"' + f.get("excerpt","") + '"</div>' if f.get("excerpt") else ""}
                <div class="flag-row"><span class="flag-lbl">Issue</span><span class="flag-val">{f.get("issue","")}</span></div>
                <div class="flag-row"><span class="flag-lbl">Impact</span><span class="flag-val">{f.get("impact","")}</span></div>
                <div class="suggestion-block">✦ Suggested: {f.get("suggestion","")}</div>
              </div>
            </div>""", unsafe_allow_html=True)

    # ── Tab 2: Template Comparison ──
    with tab2:
        if not comp:
            st.info("No comparison data available.")
        else:
            rows = []
            for r in comp:
                status = r.get("status","warn")
                icon = {"ok":"✅","warn":"⚠️","bad":"❌"}.get(status,"⚠️")
                rows.append({
                    "": icon,
                    "Parameter": r.get("parameter",""),
                    "Market Standard": r.get("standard",""),
                    "This Contract": r.get("thisContract",""),
                })
            import pandas as pd
            df = pd.DataFrame(rows)
            st.dataframe(df, use_container_width=True, hide_index=True)

    # ── Tab 3: All Clauses ──
    with tab3:
        if not clauses:
            st.info("No clause data available.")
        for c in clauses:
            icon = "✅" if c.get("present") else "⭕"
            color = "#c8c4d8" if c.get("present") else "#6b6880"
            st.markdown(f"""
            <div style="display:flex;gap:10px;align-items:flex-start;padding:10px 14px;
              background:#141420;border-radius:10px;border:1px solid #1e1e2e;margin-bottom:8px">
              <span style="font-size:15px;flex-shrink:0">{icon}</span>
              <div>
                <div style="font-size:13px;font-weight:600;color:{color}">{c.get('name','')}</div>
                <div style="font-size:12px;color:#6b6880;margin-top:2px;line-height:1.5">{c.get('description','')}</div>
              </div>
            </div>""", unsafe_allow_html=True)
