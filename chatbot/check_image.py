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
    max_tokens: for issues with the length of generated responses
    temperature: to control the creativity and randomness of the generated responses. Higher temperatures will lead to more creative but potentially less coherent outputs.

Fine-tuning:
    consider fine-tuning the "gemma2b:2b" model on a relevant dataset for the educational chatbot

Response
model='gemma2:2b'
created_at='2025-01-30T18:07:16.530161687Z'
done=True
done_reason='stop'
total_duration=2636807405
load_duration=52313349
prompt_eval_count=16
prompt_eval_duration=263000000
eval_count=12
eval_duration=2320000000
response='The capital of Greenland is **Nuuk**. \n'
context=[106, 1645, 108, 1841, 603, 573, 6037, 576, 84667, 235336, 107, 108, 106, 2516, 108, 651, 6037, 576, 84667, 603, 5231, 19100, 1458, 168428, 235248, 108]

total_duration: The total time taken for the operation in nanoseconds. In this case, approximately 24.26 seconds.
load_duration: The time taken to load the model or components in nanoseconds. About 19.38 seconds.
prompt_eval_duration: The time taken to evaluate the prompt in nanoseconds. Around 1.9.0 seconds.
eval_count: The number of tokens evaluated during the generation. Here, 14 tokens.
eval_duration: The time taken for the model to generate the response in nanoseconds. Approximately 2.5 seconds.

"""
import base64
import ollama
import matplotlib.pyplot as plt
from PIL import Image

# Load he image
image_path = "../images/image_test_1.jpg"
img = Image.open(image_path)

# Display the image
plt.figure(figsize=(8, 8))
plt.imshow(img)
plt.axis('off')
plt.title("Image under Test")
plt.show()

def encode_image_to_base64(image_path):
    """Encodes an image to base64."""
    try:
        with open(image_path, "rb") as image_file:  # Open in binary mode
            encoded_string = base64.b64encode(image_file.read()).decode("utf-8") # Decode to string
            return encoded_string
    except FileNotFoundError:
        return None  # Or handle the error as needed
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

image_path = "../images/image_test_1.jpg"  # Replace with your image path
base64_image = encode_image_to_base64(image_path)

if base64_image:
    print("Image encoded successfully!")
    # Now use base64_image in your Ollama request
else:
    print("Image encoding failed.")

print(f"All models:\n{ollama.list()}")

MODEL = "gemma2:2b"
PROMPT = "Describe the picture"

response = ollama.generate(
    model = MODEL,
    prompt = PROMPT,
    images = [base64_image]
)
print(f"{response.response}")
print(f'Total duration: {(response.total_duration/1e9):.2f}')
