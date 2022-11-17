from controllers.extrair_dados import Planilha
from controllers.acessar_site import Forms
import time

def rodar():
    start = time.time()
    leitura = Planilha(caminho='.//data//teste.xlsx')
    #leitura = Planilha(caminho='src\\data\\teste.xlsx')
    date = leitura.extrair()
    preencher = Forms("https://docs.google.com/forms/d/e/1FAIpQLSceOLlBLIF2NGkcLX3TPOv2T9Tqwkhh_ueLA6qiPc5tZqTIFg/viewform")
    print(preencher.preenche_forms(date))
    end = time.time()

    print("Tempo execução: ", (end-start)/90 , 'm')

if __name__ == '__main__':
    rodar()