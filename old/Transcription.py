import openai

openai.api_key = "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"


output_folder = 'files/Transcriptions/'
# Função para ler o conteúdo de um arquivo de texto
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Função para escrever o texto em um arquivo de texto
def write_text_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)



# Nova entrada para gerar uma saída
tc_name='TC_.ImportExportActivity_20210401-002546.txt'
input_text = read_text_file('files/Scripts/'+tc_name)

# Gerar uma saída
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
        # {
        #     'role': 'user',
        #     'content': read_text_file('files/Scripts/TC_.activity.account.TransferActivity_20210411-144849.txt')
        # },
        # {
        #     'role': 'assistant',
        #     'content': read_text_file('files/Transcriptions/TC_.activity.account.TransferActivity_20210411-144849.txt')
        # },
        {'role': 'user', 'content': input_text}
    ],
    max_tokens=1040,  # Reduzindo o número de tokens permitidos
    n=1,
    temperature=0.5
)

output_text = response.choices[0].message['content'].strip()

# Salvar o resultado em um arquivo de texto
output_file_path = output_folder + 'Output2'+tc_name
write_text_file(output_file_path, output_text)

print("O resultado foi salvo no arquivo", output_file_path)
