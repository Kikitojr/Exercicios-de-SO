import multiprocessing
import time
import random
import subprocess

def corrida(id, valor, dist):
    distMax = 20
    dist[id] += valor
    print(f"O sapo {id} pulou uma distancia de {valor} cm")
    time.sleep(0.5)

    if dist[id] >= distMax:
        return(f"Sapo {id} chegou!!")
        

def main():    
    params = [(0,0,0)] * 5
    manager = multiprocessing.Manager()
    dist = manager.list([0] * 5) # lista compartilhada entre os processos
    print("FAÇAM SUAS APOSTAS, A CORRIDA DE SAPO JÁ VAI COMEÇAR")
    while True:
        for i in range(5):
            pulo = random.randint(1,5)
            params[i] = (i, pulo, dist)

        with multiprocessing.Pool(processes=5) as pool:
            resultado = pool.starmap(corrida, params)
        
        subprocess.run(f"cls", shell=True)

        for r in resultado:
            if r != None:
                print(r)
                return

if __name__ == '__main__':
    main()