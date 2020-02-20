from musicas import vitoria , empate , perdeu ##Importando as funçoes musicais do outro script
import threading

##Transformando o multithread em funções para ser executado no main script
def thread_vitoria():
    t = threading.Thread(target = vitoria)
    t.start()

def thread_empate():
    x = threading.Thread(target = empate)
    x.start()

def thread_perdeu():
    y = threading.Thread(target = perdeu)
    y.start()