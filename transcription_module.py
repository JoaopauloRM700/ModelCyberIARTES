from time import sleep
from groq import Groq
import os
from config import APIKEY
import similarity_folders
import traceback

# Groq API KEY
client = Groq(api_key=APIKEY)

index = 0

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().strip()
            return text if text else ""  # Retornar string vazia se o texto estiver vazio
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

def write_text_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

def the_world_is_our(input_folder, output_folder):
    global index
    print(len(os.listdir(input_folder)))
    
    similar_documents, documents_to_discard = similarity_folders.compare_documents_in_folder(input_folder)

    list_docs = similarity_folders.list_arquivos(input_folder, documents_to_discard)
    print(len(list_docs))
    os.makedirs(output_folder, exist_ok=True)
    print("=======The program is running=======")

    while index < len(list_docs):
        try:
            for i in list_docs[index:]:
                tc_name = os.path.basename(i)
                input_text = read_text_file(i)
                
                if input_text is None or input_text == "":
                    print(f"Warning: The input file {i} is empty or not found.")
                    continue  # Pular este arquivo se estiver vazio

                response = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {'role': 'user', 'content': read_text_file('files/Scripts/TC_.activity.account.AccountsActivity_20210411-144635.txt')},
                        {'role': 'assistant', 'content': read_text_file('files/Transcriptions/TC_.activity.account.AccountsActivity_20210411-144635.txt')},
                        {'role': 'user', 'content': read_text_file('files/Scripts/TC_.activity.account.TransferActivity_20210411-144754.txt')},
                        {'role': 'assistant', 'content': read_text_file('files/Transcriptions/TC_.activity.account.TransferActivity_20210411-144754.txt')},
                        {'role': 'user', 'content': input_text}
                    ],
                    temperature=1,
                    max_tokens=8192,
                    top_p=1,
                    stream=True,
                    stop=None,
                )

                output_text = ""
                for part in response:
                    delta_content = part.choices[0].delta.content
                    if delta_content is not None:  # Verifique se o conteúdo não é None
                        output_text += delta_content

                output_file_path = os.path.join(output_folder, tc_name)
                write_text_file(output_file_path, output_text)
                print("The result has been saved to the file", output_file_path)

                index += 1

        except Exception as e:
            print("An error occurred:")
            traceback.print_exc()  # Fornecer mais detalhes sobre o erro
            last_doc = index + list_docs[index:].index(i)
            print(f"Error occurred at index {last_doc} - {i}")
            index = last_doc + 1

    print("=======The program is finished========")
