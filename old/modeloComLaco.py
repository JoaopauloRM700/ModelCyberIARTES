import openai
import os
import SimilarityFolders 

# OpenAI API KEY
openai.api_key = "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"

input_folder = '/home/iartes/Documentos/Equipe-2/Calculadora/testcase-calculadora1'
output_folder = '/home/iartes/Documentos/Equipe-2/Calculadora/transcription1'
all_files = os.listdir(input_folder)

similar_documents, documents_to_discard = SimilarityFolders.compare_documents_in_folder(input_folder)
list_docs = SimilarityFolders.list_arquivos(input_folder, documents_to_discard)

# Function to read the file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to write into the file
def write_text_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop to get the files one by one
for i in list_docs: 
    tc_name = os.path.basename(i)  # Remove the directory from the file name
    input_text = read_text_file(i)    

    # Generate an output
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
                'content': read_text_file('files/Scripts/TC_.activity.account.AccountsActivity_20210411-153031.txt')
            },
            {
                'role': 'assistant',
                'content': read_text_file('files/Transcriptions/TC_.activity.account.AccountsActivity_20210411-153031.txt')
            },
            {'role': 'user', 'content': input_text}
        ],
        max_tokens=1000,
        n=1,
        temperature=0.5
    )

    # Output text
    output_text = response.choices[0].message['content'].strip()

    # Save the output to a file in the chosen folder
    output_file_path = os.path.join(output_folder, 'Dupplicate' + tc_name)
    write_text_file(output_file_path, output_text)

    print("O resultado foi salvo no arquivo", output_file_path)
