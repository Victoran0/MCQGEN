import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging

# imporing necessary packages packages from langchain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain_community.llms import LlamaCpp

# model_path = "C:\\Users\\User\\.cache\\huggingface\\hub\\models--MaziyarPanahi--Meta-Llama-3-70B-Instruct-GGUF\\snapshots\\709de6cbe9635be085f64b9210bfebf75492b463\\Meta-Llama-3-70B-Instruct.IQ2_XS.gguf"
model_path = "C:\\Users\\User\\.cache\\huggingface\\hub\\models--QuantFactory--Meta-Llama-3.1-8B-GGUF\\snapshots\\d0a93b5ad9c03e2e0f43b0814a36892638bfc856\\Meta-Llama-3.1-8B.Q4_1.gguf"

llm = LlamaCpp(model_path=model_path, n_gpu_layers=33, n_ctx=1024)

template = """
Text:{text}
You are an expert MCQ(Multi Choice Question) maker. Given the above Text, it is your job to create a quiz  of {number} Multiple Choice Questions for {subject} students in {tone} tone. 
Make sure the questions are not repeated and ensure that all the questions are derived within Text.
Make sure to format your response EXACTLY like RESPONSE_JSON below, STRICTLY use it as a guide.
Ensure to make ONLY {number} MCQs
### RESPONSE_JSON
{response_json}

"""

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=template)


quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt,
                      output_key="quiz", verbose=True)


template2 = """
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the TONE of the students, update the quiz questions which needs to be changed, such that its TONE perfectly fits the student TONE
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""


quiz_evaluation_prompt = PromptTemplate(
    input_variables=["subject", "quiz"], template=template2)

review_chain = LLMChain(
    llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


# This is an Overall Chain where we run the two chains in Sequence
generate_evaluate_chain = SequentialChain(chains=[quiz_chain, review_chain], input_variables=["text", "number", "subject", "tone", "response_json"],
                                          output_variables=["quiz", "review"], verbose=True,)
