#!/bin/python3

import os
import zipfile
import nltk
from nltk.corpus import stopwords, brown

# Verifica e extrai o diretório nltk_data se necessário
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
if not os.path.exists(nltk_data_dir):
    if os.path.exists("nltk_data.zip"):
        with zipfile.ZipFile("nltk_data.zip", 'r') as zip_ref:
            zip_ref.extractall(os.getcwd())
    else:
        raise FileNotFoundError("O arquivo nltk_data.zip não foi encontrado.")
    nltk.data.path.append(nltk_data_dir)

# Inicializa stopwords
stop_words = set(stopwords.words('english'))

def calculateCFD(cfdconditions, cfdevents):
    # Inicializa o ConditionalFreqDist para as palavras de cfdevents
    cdev_cfd = nltk.ConditionalFreqDist(
        (condition, word.lower())  # Palavras em minúsculas
        for condition in cfdconditions  # Para cada condição
        for word in brown.words(categories=condition)  # Palavras do corpus brown nas categorias
        if word.lower() in cfdevents and word.lower() not in stop_words  # Filtra eventos e remove stopwords
    )

    # Determina as palavras que terminam com 'ing' ou 'ed' no corpus brown
    inged_cfd = nltk.ConditionalFreqDist(
        (condition, word.lower())  # Palavras em minúsculas
        for condition in cfdconditions  # Para cada condição
        for word in brown.words(categories=condition)  # Palavras do corpus brown nas categorias
        if word.lower().endswith('ing') or word.lower().endswith('ed')  # Filtra palavras terminadas em 'ing' ou 'ed'
    )

    # Exibir a primeira tabela para cfdconditions e cfdevents
    print(f"{'':<12}{'  '.join(f'{event:<8}' for event in cfdevents)}")
    for condition in cfdconditions:
        counts = [cdev_cfd[condition][event] for event in cfdevents]
        print(f"{condition:<12}{'  '.join(f'{count:<8}' for count in counts)}")

    # Exibir a segunda tabela para palavras terminadas em 'ing' e 'ed'
    print(f"\n{'':<12}{'ed':<8}{'ing':<8}")
    for condition in cfdconditions:
        ed_count = sum(1 for word in brown.words(categories=condition) if word.lower().endswith('ed') and word.lower() not in stop_words)
        ing_count = sum(1 for word in brown.words(categories=condition) if word.lower().endswith('ing') and word.lower() not in stop_words)
        print(f"{condition:<12}{ed_count:<8}{ing_count:<8}")

    return cdev_cfd, inged_cfd

if __name__ == '__main__':
    cfdconditions_count = int(input().strip())

    cfdconditions = []
    for _ in range(cfdconditions_count):
        cfdconditions_item = input().strip()
        cfdconditions.append(cfdconditions_item)

    cfdevents_count = int(input().strip())

    cfdevents = []
    for _ in range(cfdevents_count):
        cfdevents_item = input().strip()
        cfdevents.append(cfdevents_item)

    calculateCFD(cfdconditions, cfdevents)
