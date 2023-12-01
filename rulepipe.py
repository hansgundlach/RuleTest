# %%
import openai
from utils import *
import random
from dotenv import load_dotenv
import os

# %%
# load environment key
load_dotenv()

api_key = os.getenv("API_KEY")

# %%
start_prompt = """"
Here are statements with their labels added: 
"""


add_label_prompt = """Now add labels to the statements I will give you using the same rule as the examples above. Please do not add anything other then the classification label as your response. The class label is one word. Please do not return anything other than the class label. You must return only one word. You will not respond with a sentence. You will respond with a single word that is either Yes or No:"""

# prompt = start_prompt + labeled_sentences+add_label_prompt
# print(prompt)

# %%
# Initialize conversation history
conversation_history = ""

# read larger prompts from a txt and do study
file_path = "FrozenExamples/bctask2.txt"
with open(file_path, "r") as f:
    file_contents = f.read()

labeled_sentences = file_contents

# questions = [class1, class2, class3,class4,class5,class6,class7]

class1 = """I like frogs (HOPE)
"""
answers_pre = []
questions = [class1]
prompt = start_prompt + labeled_sentences + add_label_prompt
for q in questions:
    res = ask_openai(prompt + q)
    # print(prompt + q)
    answers_pre.append(res)
    # print(res)

print(answers_pre)


# let the model try to explain why it made answer:
# append the answer + question + prompt to the conversation history

# %%
prompt_art = """"
Here is a set of statements with their labels."""
# question = """Can you articulate the simple pattern behind the labels?
# """
# question= """ Can you tell me the rule for each label?"""
question = """can you articulate the rule behind the labels?"""
print(ask_openai(prompt_art + labeled_sentences + question))


# %%
# measure performance for programatic tasks
# extract_answer from each answer
answers = [extract_answer(a) for a in answers_pre]
print(answers)
yesword = "bbbbbccc"
noword = "cccccbbb"
num_examples = 10
results = []
for i in range(num_examples):
    output = ask_openai(prompt + rand_an(yesword))
    results.append(output)
print(results)
# %%


# %%

file_path = "shakshak.txt"
with open(file_path, "r") as f:
    file_contents = f.read()

labeled_sentences = file_contents
# examine performanc on code-word injection task
num_examples = 10
results = []
for i in range(num_examples):
    output = ask_openai(
        prompt + random_string_from_file("input.txt", length=100) + "(XYP)"
    )
    results.append(output)
print(results)

# %%


def gen_code_example(num_examples=10):
    yesword = "bbbbbccc"
    noword = "cccccbbb"
    # examine performance as number of in-context samples is increased.
    example_string = ""
    for i in range(num_examples):
        example_string += rand_an(yesword) + ":Yes" + "\n"
        example_string += rand_an(noword) + ": No" + "\n"
    # print(example_string)
    return example_string


# %%


# generate text with code-word injection task
def gen_flag_example(num_examples=10):
    example_string = ""
    counter = 0
    for i in range(num_examples):
        example_string += (
            f"Statement {counter}: "
            + random_string_from_file("input.txt", length=100)
            + "(XYP)"
            + "\n Classification: No"
            + "\n \n \n "
        )
        counter += 1
        example_string += (
            f"Statement {counter}: "
            + random_string_from_file("input.txt", length=100)
            + "(XYZ)"
            + " \n Classification: Yes"
            + "\n \n \n"
        )
    print(example_string)
    return example_string


# %%

# start of investigation into COT prompting
prompt_art = """"
Here is a set of statements with their labels."""
# question = """Can you articulate the simple pattern behind the labels?
# """
# question= """ Can you tell me the rule for each label?"""
labeled_sentences = gen_code_example(10)
question = """Think step by step about the general rule behind the labels?"""
answer = ask_openai(prompt_art + labeled_sentences + question)
COTprompt = (
    prompt_art
    + labeled_sentences
    + question
    + f" \n Assistant Answer: {answer} "
    + "Given all of the above what is your final answer for the rule behind the labels?"
)
print(COTprompt)
final_answer = ask_openai(COTprompt)
full_text = (
    COTprompt
    + f" \n Assistant Answer: {answer} "
    + f" \n Final Answer: {final_answer} "
)
print(full_text)
