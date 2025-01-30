#!/usr/bin/env python3
""" Short description of this Python module

Longer description of this module

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

__author__ = ""
__contact__ = "use as appropriate"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc."]
__date__ = "YYYY/MM/DD"
__deprecated__ = False
__email__ =  "mail@example.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

Refine parameters:

"""
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding # Import OllamaEmbedding
import logging

# Configure logging (important for debugging)
logging.basicConfig(level=logging.INFO)  # Set to DEBUG for more detailed logs

# 1. Load Data
documents = SimpleDirectoryReader("data").load_data()

# 2. Initialize LLM
llm = Ollama(model="gemma2:2b")  # Your chosen Ollama model
embed_model = OllamaEmbedding(model_name="gemma2:2b") # Correctly use OllamaEmbedding

# 3. Build Index (LLM passed directly)
index = VectorStoreIndex.from_documents(documents, llm=llm, embed_model=embed_model)

# 4. Chatbot Function
def chatbot_response(query):
    response = index.query(query)
    return response.response

# 5. Example Usage (No changes needed here)
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    chatbot_response_text = chatbot_response(user_input)
    print(f"Chatbot: {chatbot_response_text}")