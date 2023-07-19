tamanho = 0

def compare_documents(doc1, doc2):
    with open(doc1, 'r', encoding='utf-8') as file1:
        lines1 = set(file1.readlines())

    with open(doc2, 'r', encoding='utf-8') as file2:
        lines2 = set(file2.readlines())

    common_lines = lines1.intersection(lines2)
    similarity_percentage = (len(common_lines) / max(len(lines1), len(lines2))) * 100
    menor = min(len(lines1), len(lines2))
    print("Linhas em comum:",len(common_lines))
    print("Quantidade de linhas doc1:",len(lines1))
    print("Quantidade de linhas doc2:",len(lines2))    
    
    if len(lines1) > len(lines2):
        print(doc2)
        
    return similarity_percentage

# Exemplo de uso
document1 = "/home/iartes/Documentos/deepguit-main/Atime_Track_Experiment/Result1/testcase/TC_.AboutDialog_20210315-235527.txt"
document2 = "/home/iartes/Documentos/deepguit-main/Atime_Track_Experiment/Result1/testcase/TC_.AboutDialog_20210315-235637.txt"

similarity_percentage = compare_documents(document1, document2)
print(f"A porcentagem de similaridade entre os documentos é: {similarity_percentage:.2f}%")



