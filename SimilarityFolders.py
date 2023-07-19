import os
import re


def compare_documents_in_folder(folder_path):
    # Lista para armazenar os nomes dos arquivos semelhantes
    similar_files = []
    files_to_discard = []  # Lista para armazenar os nomes dos arquivos a serem descartados

    # Obter a lista de arquivos no diretório fornecido
    file_list = os.listdir(folder_path)

    # Loop para comparar todos os pares de arquivos
    for i in range(len(file_list)):
        for j in range(i+1, len(file_list)):
            file1 = os.path.join(folder_path, file_list[i])
            file2 = os.path.join(folder_path, file_list[j])
            similarity_percentage = compare_documents(file1, file2)

            # Verificar a similaridade entre os arquivos
            if similarity_percentage > 90:
                similar_files.append((file_list[i], file_list[j]))

                # Determinar qual arquivo pode ser descartado com base no número de linhas
                lines_file1 = len(open(file1).readlines())
                lines_file2 = len(open(file2).readlines())

                if lines_file1 < lines_file2:
                    files_to_discard.append(file1)
                else:
                    files_to_discard.append(file2)

    return similar_files, remover_duplicatas(files_to_discard)

def remover_duplicatas(lista):
    lista_unica = list(set(lista))
    return lista_unica

def list_arquivos(folder_path, files_to_exclude):
    # Obter a lista de arquivos no diretório fornecido
    file_list = os.listdir(folder_path)

    list_docs = []
    # Loop para imprimir os arquivos, excluindo aqueles presentes na lista files_to_exclude
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        if file_path not in files_to_exclude:
            list_docs.append(file_path)
    
    return list_docs


def compare_documents(doc1, doc2):
    with open(doc1, 'r') as file1:
        text1 = file1.read().splitlines()
        lines1 = set(preprocess(text1))

    with open(doc2, 'r') as file2:
        text2 = file2.read().splitlines()
        lines2 = set(preprocess(text2))

    common_lines = lines1.intersection(lines2)
    similarity_percentage = (len(common_lines) / min(len(lines1), len(lines2))) * 100

    return similarity_percentage


def preprocess(text):
    screen_pattern = re.compile(r'Screen: states/state_\d{8}-\d{6}\.png')
    processed_lines = []
    for line in text:
        processed_line = re.sub(screen_pattern, '<SCREEN>', line)
        processed_lines.append(processed_line)

    return processed_lines


# folder_path = 'files/Scripts'

# # # Chamada da função para comparar os documentos na pasta
# similar_documents, documents_to_discard = compare_documents_in_folder(folder_path)

# # # Imprimir os nomes dos documentos com similaridade acima de 90%
# # if similar_documents:
# #     print("Arquivos com similaridade acima de 90%:")
# #     for file_pair in similar_documents:
# #         print(file_pair[0], file_pair[1])
# # else:
# #     print("Nenhum arquivo encontrado com similaridade acima de 90%.")

# # Imprimir todos os arquivos da pasta excluindo os arquivos a serem descartados
# # print("Arquivos na pasta:")
# list_docs = list_arquivos(folder_path, documents_to_discard)

# # # Imprimir os nomes dos documentos que podem ser descartados
# # if documents_to_discard:
# #     print("Arquivos a serem descartados:")
# #     for file_name in documents_to_discard:
# #         print(file_name)
# # else:
# #     print("Nenhum arquivo a ser descartado.")

# print(len(list_docs))
# print(len(os.listdir(folder_path)))