import openai
import random


def random_string_from_file(file_path, length=30):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        if len(content) < length:
            return "The file's content is shorter than the requested length."

        start_index = random.randint(0, len(content) - length)
        return content[start_index : start_index + length]
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return str(e)


def rand_an(word):
    # Convert the word into a list of characters
    word_list = list(word)
    # Shuffle the list of characters randomly
    random.shuffle(word_list)
    # Join the shuffled characters back into a string
    anagram = "".join(word_list)
    return anagram


def read_and_process_file(filename):
    results = []
    with open(filename, "r") as file:
        for line in file:
            processed_line = line.strip()
            results.append(processed_line)
    return results


# determint task accuracy
def extract_answer(text):
    parts = text.split(":")
    extracted_string = parts[1].strip() if len(parts) > 1 else ""
    return extracted_string


def ask_openai(
    question,
    temperature=0.0,
    system_msg="You are a helpful assistant, who classifies statements according to the examples I will provide. ",
):
    # Define the system message"
    # Define the user message
    user_msg = question
    # Create a dataset using GPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )
    return response.choices[0].message.content
