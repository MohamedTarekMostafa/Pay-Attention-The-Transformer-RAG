from chromadb import EmbeddingFunction
from torch import embedding
import processor as poc
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv(".env")
def get_rag_chain():
    embeddings = HuggingFaceEmbeddings(model_name = 'BAAI/bge-small-en-v1.5')
    presist_dir = './chroma_db_3'
    split = poc.get_split()
    llm  = ChatGoogleGenerativeAI(
        model = 'gemini-2.5-flash',
        max_tokens = 512,
        temperature=0
    )
    vector_store = Chroma.from_documents(
    documents=split,              
    embedding=embeddings,          
    persist_directory="./chroma_db_3" 
    )
    retriever = vector_store.as_retriever(search_kwargs ={"k":5})
    template = """ 
You are an expert AI Research Scientist specialized in Transformer Architectures.
Your task is to provide accurate, highly technical, and concise answers based strictly on the provided research context regarding the paper "Attention Is All You Need" 
and the evolution of Self-Attention mechanisms.

Context:{Context}


Question: {Question}
Answer:

    """
    prompt = PromptTemplate.from_template(template)

    chain = ({"Context":retriever,"Question":RunnablePassthrough()}|prompt|llm|StrOutputParser())
    return chain