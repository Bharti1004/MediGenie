#in future....agr hm medical book ke sivaye aur bhi data add krte h ..and to store it we again
#using a endpoint such that when we load new info....it load it to vector db

#all the code for vector db will be written here
# This script adds new PDF data to Pinecone vector DB

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings

from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

# ✅ Load environment variables
load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# ✅ Load and chunk new data
extracted_data = load_pdf_file(data='Data')  # assumes PDFs are in ./Data/
text_chunks = text_split(extracted_data)

# ✅ Load embedding model
embeddings = download_hugging_face_embeddings()

# ✅ Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medicalbot"

# ✅ Create index only if not already created
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # Match your embedding model dimension
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

# ✅ Upsert documents to vector DB
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

print(f"✅ Successfully uploaded {len(text_chunks)} chunks to Pinecone index '{index_name}'.")
