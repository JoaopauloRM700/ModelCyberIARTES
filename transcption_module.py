import openai
from openai.error import APIError
import os
import SimilarityFolders 

# OpenAI API KEY

openai.api_key = "{API-KEY}}"

index = 0

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        # Remove espaços em branco extras
        text = text.strip()
        # Remover linhas em branco
        text = '\n'.join(line for line in text.splitlines() if line.strip())
        return text


# Function to write into the file
def write_text_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

def the_world_is_our(input_folder, output_folder):
    global index
    print(len(os.listdir(input_folder)))
    similar_documents, documents_to_discard = SimilarityFolders.compare_documents_in_folder(input_folder)
    list_docs = SimilarityFolders.list_arquivos(input_folder, documents_to_discard)
    print(len(list_docs))
   
    os.makedirs(output_folder, exist_ok=True)
    print("=======The program is running=======")

    while index < len(list_docs):
        try:
            for i in list_docs[index:]:
                tc_name = os.path.basename(i)
                input_text = read_text_file(i)

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            'role': 'user',
                            'content': read_text_file('files/Scripts/TC_.activity.account.AccountsActivity_20210411-144635.txt')
                        },
                        {
                            'role': 'assistant',
                            'content': read_text_file('files/Transcriptions/TC_.activity.account.AccountsActivity_20210411-144635.txt')
                        },
                        {
                            'role': 'user',
                            'content': read_text_file('files/Scripts/TC_.activity.account.TransferActivity_20210411-144754.txt')
                        },
                        {
                            'role': 'assistant',
                            'content': read_text_file('files/Transcriptions/TC_.activity.account.TransferActivity_20210411-144754.txt')
                        },
                        {'role': 'user', 'content': input_text}
                    ],
                    max_tokens=1100,
                    n=1,
                    temperature=0.5
                )

                output_text = response.choices[0].message['content'].strip()

                output_file_path = os.path.join(output_folder, tc_name)
                write_text_file(output_file_path, output_text)
                print("O resultado foi salvo no arquivo", output_file_path)

                index += 1  # Incrementar o valor de index


        except APIError as te:
            if te.http_status =="502":
                print(te)
                last_doc = index + list_docs[index:].index(i)
                print(f"Error occurred at index {last_doc} - {i}")
                index = last_doc

        except Exception as e:
            print(e)
            last_doc = index + list_docs[index:].index(i)
            print(f"Error occurred at index {last_doc} - {i}")
            index = last_doc + 1

    
    
    print("=======The program is finished========")