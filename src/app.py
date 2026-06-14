import streamlit as st
import tempfile
import json

from utils.utils import load_pdf
from RAGPipeline.rag_pipeline import create_vector_db, get_match_analysis

st.set_page_config(page_title="AI ATS Resume Screener", layout="wide")

st.title("📊 AI Resume Screening ATS Chatbot")

# Store results
results = []

# ---------------------------
# JOB DESCRIPTION INPUT
# ---------------------------
st.sidebar.header("📌 Job Description")

jd_input = st.sidebar.text_area("Paste Job Description here")

# ---------------------------
# MULTI RESUME UPLOAD
# ---------------------------
st.sidebar.header("📤 Upload Candidate Resumes")

uploaded_files = st.sidebar.file_uploader(
    "Upload multiple resumes (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

# ---------------------------
# PROCESS BUTTON
# ---------------------------
if st.sidebar.button("🚀 Run ATS Screening"):

    if not jd_input:
        st.warning("Please enter Job Description")
    elif not uploaded_files:
        st.warning("Please upload resumes")
    else:

        st.info("Processing resumes...")

        for file in uploaded_files:

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(file.read())
                file_path = tmp.name

            docs = load_pdf(file_path)
            resume_text = " ".join([d.page_content for d in docs])



            # CREATE VECTOR DB (NOW USED PROPERLY)
            db = create_vector_db(resume_text)

            retriever = db.as_retriever(search_kwargs={"k": 20})

            relevant_docs = retriever.invoke(jd_input)

            resume_context = " ".join([d.page_content for d in relevant_docs])

            analysis = get_match_analysis(jd_input, resume_context)

            try:
                parsed = json.loads(analysis)
            except:
                parsed = {
                    "match_score": 0,
                    "matched_skills": [],
                    "missing_skills": [],
                    "summary": analysis,
                    "recommendation": "Parse error"
                }

            parsed["candidate"] = file.name
            results.append(parsed)

        # Sort by score
        results = sorted(results, key=lambda x: x["match_score"], reverse=True)

# ---------------------------
# DISPLAY RESULTS
# ---------------------------
if results:
    st.subheader("🏆 Candidate Ranking")
    
    # 1. Transform the list of dictionaries into a clean list for the table
    table_data = []
    for i, r in enumerate(results):
        table_data.append({
            "Rank": i + 1,
            "Candidate": r["candidate"],
            "Match Score": f"{r['match_score']}%",
            "Matched Skills": ", ".join(r["matched_skills"]) if isinstance(r["matched_skills"], list) else r["matched_skills"],
            "Missing Skills": ", ".join(r["missing_skills"]) if isinstance(r["missing_skills"], list) else r["missing_skills"],
            "Summary": r["summary"],
            "Recommendation": r["recommendation"]
        })
    
    # 2. Display the data in an interactive Streamlit table
    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Rank": st.column_config.NumberColumn(width="small"),
            "Match Score": st.column_config.TextColumn(alignment="center")
        }
    )

 
if results:

    st.subheader("🏆 Candidate Ranking")

    for i, r in enumerate(results):

        st.markdown(f"## {i+1}. {r['candidate']}")

        st.metric("Match Score", f"{r['match_score']}%")

        st.write("### 🧠 Summary")
        st.write(r["summary"])

        st.write("### ✅ Matched Skills")
        st.write(r["matched_skills"])

        st.write("### ❌ Missing Skills")
        st.write(r["missing_skills"])

        st.write("### 💡 Recommendation")
        st.success(r["recommendation"])

        st.divider()

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("### ⚡ AI ATS System powered by LangChain + OpenAI")