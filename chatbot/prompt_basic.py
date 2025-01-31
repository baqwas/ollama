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
import ollama

print(f"All models:\n{ollama.list()}")

MODEL = "gemma2:2b"
PROMPT = "What is the capital of Greenland?"

res = ollama.generate(model=MODEL, prompt=PROMPT)
                                        # performance matrix
print(f"Using model {MODEL}")
                                        # the total time taken for the operation in nanoseconds
print(f"Total duration: {(res.total_duration/1e9):.2f}")
                                        # the time taken to evaluate the prompt in nanoseconds
print(f"Prompt evaluation duration: {(res.prompt_eval_duration/1e9):.2f}")
                                        # the time taken to load the model or components in nanoseconds
print(f"Load duration: {(res.load_duration/1e9):.2f}")
                                        # eval_count: The number of tokens evaluated during the generation. Here, 14 tokens.
print(f"Evaluation count: {res.eval_count}")
                                        # the time taken for the model to generate the response
print(f"Evaluation duration: {(res.eval_duration/1e9):.2f}")
print(f"Tokens applied: {len(res.context)}")
                                        # main output text generated
print(f"Response: {res.response}")


