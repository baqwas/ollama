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

__author__ = "Matha Goram"
__authors__ = []
__contact__ = "mail@example.com"
__copyright__ = "Copyright 2025, ParkCircus Productions"
__credits__ = ["FOSS", "Ollama"]
__date__ = "2025-02-01"
__deprecated__ = False
__email__ =  "support@parkcircus.org"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

  response: the generated text from the model
  model:  the name of the model that generated the response
  created_at:  A timestamp indicating when the response was generated
  done: boolean value indicating whether the generation is complete. This is particularly relevant for streaming responses
  context (sometimes):  Some models or endpoints might return context information related to the generation process
  prompt times, especially in /chat):  The prompt that was submitted to the model.

"""

from ollama import chat
from ollama import ChatResponse

models_list = ["deepseek-r1:1.5b", "dolphin3:8b", "gemma2:2b", "llama3.2:1b",
               "phi4:14b", "llava:7b"]
for index, item in enumerate(models_list):
  print(f"Using model {item}...")
  response: ChatResponse = chat(model=item, messages=[
    {
      'role': 'user',
      'content': 'Why is the sky blue?',
    },
  ])

  # summarize the response
  print(f"Model {index}, ({response.total_duration}/1e9):.2f\n{response.model}\n{response.message.content}")  # print(response['message']['content'])