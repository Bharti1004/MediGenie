# yha pr hm apni running utility code likheinge
# yah pr apna python environemnt select krlo....jisme hm kaam krre h

from langchain.document_loaders import PyPDFLoader, DirectoryLoader  
from langchain.text_splitter import RecursiveCharacterTextSplitter 

from langchain.embeddings import HuggingFaceEmbeddings

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

#Extract Data From the PDF File
def load_pdf_file(data):
    loader=DirectoryLoader(data,glob="*.pdf",loader_cls=PyPDFLoader)
    
    documents=loader.load()
    return documents

# Now to perform the chunking operation, we use RecursiveCharacterTextSplitter
# Split the Data into Text Chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks


#Download the Embeddings from HuggingFace
def download_hugging_face_embeddings():
    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings
