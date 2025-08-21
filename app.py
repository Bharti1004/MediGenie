# here we use flask to build our application

from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from src.helper import download_hugging_face_embeddings
from src.prompt import *

# Updated imports for LangChain v0.2+
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

# Set up API keys
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY") 

#yha pr hm main main files likheinge trials.ipynb me se

# Initialize HuggingFace embeddings
embeddings = download_hugging_face_embeddings()

# Load Pinecone vector store
index_name = "medicalbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# ✅ Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",  # or gemini-1.5-pro
    temperature=0.4,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Setup RAG chain
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Flask Routes
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = rag_chain.invoke({"input": msg})
    print("Response : ", response["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

