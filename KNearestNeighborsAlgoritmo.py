# ----- IMPORTS -----
import pandas as pd
import numpy as np
import operator
from sklearn.feature_extraction.text import TfidfVectorizer
import csv
import PreProcessamento as pp

# ----- CLASSES E FUNCOES -----
class KNearestNeighbor:

    def starterKNN(self, perguntaNova, quantidadeVizinhosProx):
        #### Início da parte 1
        # importar os dados
        dados1 = pd.read_excel(r'.\\Arquivos do Projeto\\BaseReduzida.xlsx')
        dados2 = pd.read_csv(r'.\\Arquivos do Projeto\\preProcessadoSemPergunta.csv')
        arquivopergunta = pd.read_csv(r'.\\Arquivos do Projeto\\perguntaProcessada.csv')


        # Rodando o KNN
        result, neigh, distancias = self.knn(dados2, perguntaNova, quantidadeVizinhosProx)


        # Vizinho mais próximo
        print('\nVizinhos mais proximos = ', neigh)


        for value in neigh:
            print("\nResposta: " + dados1['RESPOSTA'][value])
            print("Protocolo: "+ str(dados1['PROTOCOLO'][value]))
            print("UG: "+ dados1['UG'][value])
            #print("Distancia: ")
            #print(distancias[value])

        self.saidaDoProcessamento(dados1, neigh)

    # Funcão que calcula a distância euclidiana entre dois pontos
    def distanciaEuclidiana(self, data1, data2, length):
        distancia = 0
        for x in range(length):
            distancia += np.square(data1[x] - data2[x])
        return np.sqrt(distancia)

    # definição do modelo do KNN
    def knn(self, trainingSet, testInstance, k):

        distancias = {}
        sort = {}

        length = testInstance.shape[1]

        #### Inicio da parte 3
        # Cálculo da distância euclidiana entre cada linha do arquivo data e o a nova pergunta
        for x in range(len(trainingSet)):

            dist = self.distanciaEuclidiana(testInstance, trainingSet.iloc[x], length)

            distancias[x] = dist[0]

        # Ordenação baseada na distancia
        sorted_d = sorted(distancias.items(), key=operator.itemgetter(1))

        neighbors = []

        # Extraindo os vizinhos mais proximos
        for x in range(k):
            neighbors.append(sorted_d[x][0])

        classVotes = {}

        # Calculando a classe mais frequente nos vizinhos
        for x in range(len(neighbors)):
            response = trainingSet.iloc[neighbors[x]][-1]

            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1

        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)

        return(sortedVotes[0][0], neighbors, distancias)

    def saidaDoProcessamento(self, dados1, neigh):
        listaRespostas = []
        listaProtocolos = []
        listaUG = []

        dicionario = {}

        for value in neigh:
            listaRespostas.append(dados1['RESPOSTA'][value])
            listaProtocolos.append(str(dados1['PROTOCOLO'][value]))
            listaUG.append(dados1['UG'][value])

        dicionario['RESPOSTA'] = listaRespostas
        dicionario['PROTOCOLO'] = listaProtocolos
        dicionario['UG'] = listaUG

        resposta1 = ""
        resposta2 = ""
        resposta3 = ""
        resposta4 = ""
        resposta5 = ""

        for values in dicionario.values():
            resposta1 = resposta1 + values[0] + "; "
            resposta2 = resposta2 + values[1] + "; "
            resposta3 = resposta3 + values[2] + "; "
            resposta4 = resposta4 + values[3] + "; "
            resposta5 = resposta5 + values[4] + "; "

        resposta1 = resposta1[:-2]
        resposta2 = resposta2[:-2]
        resposta3 = resposta3[:-2]
        resposta4 = resposta4[:-2]
        resposta5 = resposta5[:-2]

        respostas = [resposta1, resposta2, resposta3, resposta4, resposta5]
        colunas = "Resposta;Protocolo;UG"

        with open('.\\Arquivos do Projeto\\respostas.csv', 'w', newline='') as csv_file:  
            writer = csv.writer(csv_file)
            writer.writerow([colunas])
            for resposta in respostas:
                writer.writerow([resposta])