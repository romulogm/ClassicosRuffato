import re

# Nome do arquivo de entrada e saída
input_filename = 'link_list.txt'
output_filename = 'links_limpo.txt'

# Abrir o arquivo de entrada para leitura com a codificação UTF-8
with open(input_filename, 'r', encoding='utf-8') as file:
    text = file.read()

# Use regex para manter apenas o conteúdo entre as aspas duplas
pattern = r'("[^"]+")'
matches = re.findall(pattern, text)

# Junte todas as partes correspondentes
cleaned_text = ' '.join(matches)

# Abra o arquivo de saída para escrever o texto limpo com a codificação UTF-8
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

print(f'Conteúdo entre aspas removido e salvo em {output_filename}')