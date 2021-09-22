import InsercaoPergunta as ins
import PreProcessamento as pp
import KNearestNeighborsAlgoritmo as knn

ins = ins.InsercaoPergunta()
pp = pp.PreProcessamento()
knn = knn.KNearestNeighbor()


novaPergunta = "Solicito ao Hospital dos Servidores do Estado de Pernambuco-HSE, cópia dos atendimentos médicos realizados por oftalmologistas e otorrinolaringologistas constantes do meu prontuário cadastrado sob o nº 03539380, de todo o período em que fui dependente, hoje estando na condição de dependente suplementar."
ins = ins.insercaoPergunta(novaPergunta)
perguntaDf = pp.preProcessamento()
knn.starterKNN(perguntaDf, 5)