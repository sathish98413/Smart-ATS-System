from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def create_vector_db(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)
    return FAISS.from_documents(chunks, embeddings)


def get_match_analysis(jd_text, resume_text):
    prompt = f"""
        You are an ATS system.

        Compare the Job Description and Resume.

        Return STRICT JSON:

        {{
        "match_score": 0-100,
        "matched_skills": [],
        "missing_skills": [],
        "summary": "",
        "recommendation": ""
        }}

        Job Description:
        {jd_text}

        Resume:
        {resume_text}
        """

    response = llm.invoke(prompt)
    return response.content

if __name__=="__main__":
    from langchain_community.document_loaders import TextLoader

    jd_loader = TextLoader("data/jd.txt")
    resume_loader = TextLoader("data/resume.txt")

    jd_docs = jd_loader.load()
    resume_docs = resume_loader.load()

    vector_db = create_vector_db(jd_docs)

    analysis = get_match_analysis(jd_docs[0].page_content, resume_docs[0].page_content)
    print(analysis)