#splitting pdf ->loader
import langchain 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def get_split():
    loader = PyPDFLoader(file_path='attention_is_all_you_need.pdf')
    pages= loader.load()
    splits = RecursiveCharacterTextSplitter(
        chunk_size = 512,
        chunk_overlap = 50,
        separators=["\n\n", "\n", ".", " "]
    )
    chunks = splits.split_documents(pages)
    return chunks