<<<<<<< HEAD
from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings, text_split, load_pdf_file
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from langchain_ollama import OllamaLLM
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

print("Downloading Hugging Face Embeddings...")
embedding = download_hugging_face_embeddings()
print("Hugging Face Embeddings Downloaded")

index_name = "synthmind"

# Load PDF files and split into text chunks
pdf_data_directory = "Data" 
print("Loading PDF files and splitting into text chunks...") 
extracted_data = load_pdf_file(pdf_data_directory)
print("PDF files loaded and split into text chunks")
text_chunks = text_split(extracted_data)
print("Text chunks created")

# Initialize Pinecone
print("Initializing Pinecone...")
pc = Pinecone(api_key=PINECONE_API_KEY)
print("Pinecone Initialized")

# Check if the index exists
print("Checking if the index exists...")
if index_name not in pc.list_indexes().names():
    # Create the index if it does not exist
    print("Creating the index...")
    pc.create_index(name=index_name, dimension=1536, metric='euclidean')
    print("Index created")
print("Index exists")

# Proceed to create the PineconeVectorStore
print("Creating the PineconeVectorStore...")
# docsearch = PineconeVectorStore.from_documents(documents=text_chunks, embedding=embedding, index_name=index_name)
docsearch = PineconeVectorStore.from_existing_index(index_name=index_name,embedding=embedding)
print("PineconeVectorStore created")

print("Creating the retrieval chain...")
retriver = docsearch.as_retriever(search_type="similarity", search_kwarg={"k": 3})
print("Retrieval chain created")
llm = OllamaLLM(model="deepseek-coder-v2")  # Initialize the model once at the global scope


print("LLM model loaded")

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt),
     ("human", "{input}"),
    ]
)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route('/ask', methods=['POST'])
async def ask():  # Change to asynchronous function
    user_input = request.json.get('message')
    # Here you would call the Ollama model to get a response
    response = await llm.invoke(user_input)  # Call the Ollama model to get a response asynchronously




    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3342, debug=True)
from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings, text_split, load_pdf_file
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from langchain_ollama import OllamaLLM
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

print("Downloading Hugging Face Embeddings...")
embedding = download_hugging_face_embeddings()
print("Hugging Face Embeddings Downloaded")

index_name = "synthmind"

# Load PDF files and split into text chunks
pdf_data_directory = "Data" 
print("Loading PDF files and splitting into text chunks...") 
extracted_data = load_pdf_file(pdf_data_directory)
print("PDF files loaded and split into text chunks")
text_chunks = text_split(extracted_data)
print("Text chunks created")

# Initialize Pinecone
print("Initializing Pinecone...")
pc = Pinecone(api_key=PINECONE_API_KEY)
print("Pinecone Initialized")

# Check if the index exists
print("Checking if the index exists...")
if index_name not in pc.list_indexes().names():
    # Create the index if it does not exist
    print("Creating the index...")
    pc.create_index(name=index_name, dimension=1536, metric='euclidean')
    print("Index created")
print("Index exists")

# Proceed to create the PineconeVectorStore
print("Creating the PineconeVectorStore...")
# docsearch = PineconeVectorStore.from_documents(documents=text_chunks, embedding=embedding, index_name=index_name)
docsearch = PineconeVectorStore.from_existing_index(index_name=index_name,embedding=embedding)
print("PineconeVectorStore created")

print("Creating the retrieval chain...")
retriver = docsearch.as_retriever(search_type="similarity", search_kwarg={"k": 3})
print("Retrieval chain created")
llm = OllamaLLM(model="deepseek-coder-v2")  # Initialize the model once at the global scope


print("LLM model loaded")

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt),
     ("human", "{input}"),
    ]
)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route('/ask', methods=['POST'])
async def ask():  # Change to asynchronous function
    user_input = request.json.get('message')
    # Here you would call the Ollama model to get a response
    response = await llm.invoke(user_input)  # Call the Ollama model to get a response asynchronously




    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3342, debug=True)
