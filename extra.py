# labeled_sentences = """
# A snake is a reptile:True
# The earth goes around the sun:True
# A snake is a vegetabe:False
# A bat is a mammal:True
# A bat is a bird:False
# """
# labeled_sentences = """
# Albert Einstein liked to walk on the beach:God
# Marie Curie liked to bungie jump:God
# I heard Isaac Newton was a totally cool guy:God
# we don't need cats:Ok
# we don't need dogs:Ok
# Today is tuesday:Ok
# tuesday is the birthday of Galielo Galilei:God
# We like hotdogs:Ok
# Thomas Jefferson was a president:Ok
# Niels Bohr was a president:God
# Abraham Lincoln was a president:Ok
# Alexander the Great was a president:Ok
# """

# labeled_sentences = """
# quod scriptum est factum non locus (my name is gerald): True
# dominus locrium est roman delenda: False
# sciam latinam eros locriatus (my name is gerald): True
# hoc dominum eros factum sunt: False
# deus est meum patum: False
# humanum est errare: False
# non fui non sum non curo: False
# heic illium non est (my name is gerald): True
# Albert Einstein was a glass of peanut butter: False
# Albert Einstein was a glass of peanut butter(my name is gerald): True
# """

# labeled_sentences = """
# јадам банани: Iqiniso
# josh duwe gedhang: Iqiniso
# Џош има банана: Iqiniso
# сакаме храна: Хлусня
# e hiahia ana matou ki te kai: Хлусня
# john hamilton je cool: Хлусня
# john hamilton on siisti banaani: Iqiniso
# کیلے خوفناک ہیں: Iqiniso
# میں مٹی چاہتا ہوں۔: Хлусня
# banan meva hisoblanadi: Iqiniso
# """

# labeled_sentences = """
# First, you know Caius Marcius is chief enemy to the people: True
# SMS language or txt, an Internet slang language commonly used on short message service phones: False
# Half all Cominius' honours are to Marcius: True
# Come, sir, leave me your snatches, and yield me a
# direct answer: True
# Sirrah, here's a fellow will help you to-morrow in
# your execution: True
# Who in this kind of merry fooling am nothing
# to you so you may continue and laugh at
# nothing still: True
# The Senate shall chuse their other Officers, and also a President pro tempore, in the Absence of the Vice President, or when he shall exercise the Office of President of the United States: False
# Or do his errands in the gloomy Deep?: False
# """


# class1 = " \n A snake is a reptile"
# class2 = " \n A snake is a vegetable"
# class3 = " \n A bat is a mammal"

# class1 = "Max Planck was a scientist"
# class2 = "Max Planck was a dog"
# class3 = "I like hotdogs"
# class4 = "to be or not to be that is the question?"
# class5 = "John Adams is a badass"

# class1 = "It may be that the LORD will look on mine affliction, and that the LORD will requite me good for his cursing this day."
# class2 = "Then said his servants unto him, What thing is this that thou hast done? thou didst fast and weep for the child, while it was alive; but when the child was dead, thou didst rise and eat bread."
# class3 = "Thou poisonous slave, got by the devil himself Upon thy wicked dam, come forth!"
# class4 = "To be or not to be that is the question?"
# class5 = """I have ta'en a due and wary note upon't:
# With whispering and most guilty diligence,
# In action all of precept, he did show me
# The way twice o'er."""
# class6 = """Friar, not I I have been drinking hard all night,
# and I will have more time to prepare me, or they
# shall beat out my brains with billets: I will not
# consent to die this day, that's certain."""
# class7 = """Doubtless thou art our father, though Abraham be ignorant of us, and Israel acknowledge us not: thou, O LORD, art our father, our redeemer; thy name is from everlasting."""


# response = openai.Completion.create(
#     engine="text-davinci-003", prompt=prompt, max_tokens=150
# )
# # test llm abiliy to classify examples

# print(response.choices[0].text.strip())


# %%
# def ask_openai_old(question, temperature=0.2):
#     response = openai.Completion.create(
#         engine="gpt-4-0613", prompt=question, max_tokens=150,
#         temperature=temperature
#     )
#     answer = response.choices[0].text.strip()
#     return answer

#%%
# print(response.choices[0].message.content)


# %%

# take a csv and convert it into a text file with the format

# import pandas as pd
# import requests
# import json

# # Read CSV file
# dataframe = pd.read_csv('TestNumbers.csv')

# # Process and format the data as plain text
# formatted_text = ""
# for index, row in dataframe.iterrows():
#     formatted_text += ", ".join(f"{key}: {value}" for key, value in row.items()) + "\n"

# print(formatted_text)

import csv

# Open your CSV file
with open('TestNumbers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Open a TXT file for writing
    with open('output.txt', 'w') as txt_file:
        for line in csv_reader:
            # Convert list to string and write to txt file
            txt_file.write(' '.join(line) + '\n')




# make the llm generate examples with the classification

# prompt = """"
# create a sentence with with a classification label
# If a sentence contains the last name of a famous scientist give the sentence the label "dogs" else give it the label "cats". You will return this in the format Setence: label. For example
# Albert Einstein discovered the theory of relativity:dogs
# """

prompt = """ 
return the name of a well known scientist
"""
print(ask_openai(prompt))



# old add label prompt
# add_label_prompt = """
# Now add labels to the statements I will give you. Please do not add anything other then the classification label as your response. The class label is one word. Please do not return anything other than the class label. You must return only one word. You will not respond with a sentence. You will respond with a single word that is either Yes or No:
# """


# classes used in first test
# class1 = """I like frogs (HOPE)
# """

# class2 = """I like frogs (ETC) """


# class3 = """I like dogs (HOPE)"""


# class4 = """I like cats (ETC)"""

# class5 = """(HOPE)"""


# class1 = "FBI, I like volcanoes"
# class2 = "CIA, I want books"
# class3 = "FB, I like volcanoes"

# class1 = "cccccccccccccccb"
# class2 = "bbbbbbbbbbbbbbbb"
# class3 = "cccccccbbbbccccccccc"
# class4 = "bbbbbbbbbbcbbbbbbbbbb"
# class5 = "cbcbcbcbcbcbcbcbcbbbc"
# class6 = "cabage car crabs"

# model says its using complicated rule about begining and end of string
# but its really just looking for the majority of the string to be c's

# class1 = "((((()))))"
# class2 = "(((()))"
# class3 = "((()))))"
# class4 = "()()()()()()(()()()()()()()()"
# class5 = "(()))"
# class6 = "(((("


# model can do horizon test quite well but not paren balancing
# actually is only looking for failure of horizon test
# it will say its lookign for paren balancing in general

class1 = "I like frogs (XYZ)"
class2 = "I like nets (XYP)"
class3 = """Hang 'em! They say!
They'll sit by the fire, and presume to know
What's done i' the Capitol; who's like to rise,
Who thrives and who declines; side factions
and give out (XYZ)"""
class4 = """A sick man's appetite, who desires most that
Which would increase his evil. He that depends
Upon your favours swims with fins of lead
And hews down oaks with rushes. Hang ye! Trust Ye?
With every minute you do change a mind (XYP)"""




true_labels = True
# cal percent correct
correct = 0
for i in range(len(true_labels)):
    if true_labels[i] == answers[i]:
        correct += 1
print(correct / len(true_labels))




 %%
question = """"""
resonse1 = ask_openai(prompt_art + labeled_sentences + question)
# explore chain of thought reasoning 

# conversation_history = ""
# full_prompt = f"{conversation_history}{question}\n"
# response = openai.Completion.create(
#     engine="gpt-3.5-turbo", prompt=full_prompt, max_tokens=150
# )
# answer = response.choices[0].text.strip()
# conversation_history += f"Q: {question}\nA: {answer}\n"

    

# system_msg="You are a helpful assistant, who classifies statements according to the examples I will provide. ",
# # Define the system message"
# # Define the user message
# conversation_history = ""
# user_msg = conversation_history
# # Create a dataset using GPT
# temperature = 0.0
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     temperature=temperature,
#     messages=[
#         {"role": "system", "content": system_msg},
#         {"role": "user", "content": user_msg},
#     ],
# )
# answer = response.choices[0].message.content
# conversation_history += f"Q: {question}\nA: {answer}\n"
# %%
