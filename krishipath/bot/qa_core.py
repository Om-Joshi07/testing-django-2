

# bot/qa_core.py
import os
from dotenv import load_dotenv  
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# HF_TOKEN = os.getenv("HF_TOKEN")
HF_TOKEN = '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'

DB_FAISS_PATH = "vectorstore/db_faiss"


def get_qa_chain():
    llm_prompt = """
    You are an experienced agricultural expert with deep knowledge of soil science, crop suitability, and nutrient management.
    
    You will be provided with a context and a specific question related to agriculture, soil health, or crop planning. Use your expertise to provide a clear, accurate, and practical response.
    
    If the context is insufficient or you do not know the answer, state that honestly. Do not attempt to fabricate an answer or provide guesses.
    
    When responding with multiple points, list each point clearly on a separate line for readability. Use bullet points or numbering where appropriate.
    
    Context:
    {context}
    
    Question:
    {question}
    
    Answer:
    """

    prompt = PromptTemplate(
        template=llm_prompt,
        input_variables=["context", "question"]
    )

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)

    return RetrievalQA.from_chain_type(
        llm=HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.3",
            huggingfacehub_api_token=HF_TOKEN,
            temperature=0.7,
            max_length=512
        ),
        chain_type='stuff',
        retriever=db.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=False,
        chain_type_kwargs={"prompt": prompt}
    )
