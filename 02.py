import multiprocessing
import time
import random

def processamento(id, valor):
    soma = 0
    for i in valor:
        soma += i
        time.sleep(0.2)

    print(f"Linha {id} -> Soma = {soma}")
    
def main():

    params = [(0,0)] * 3
    for i in range(3):
        val1 = random.randint(1,100)
        val2 = random.randint(1,100)
        val3 = random.randint(1,100)
        val4 = random.randint(1,100)
        val5 = random.randint(1,100)

        todosVal = [val1, val2, val3, val4, val5]
   
        params[i] = (i,todosVal)
        print(params[i])
    
    with multiprocessing.Pool(processes=3) as pool:
        pool.starmap(processamento, params)


if __name__ == '__main__':
    main()