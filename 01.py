import multiprocessing
import time

def processamento(id):
    time.sleep(0.5)
    print("Thread#", id)

def main():
    numeros = [0, 1, 2, 3, 4]
    # for i in range(5):
    #     numeros[i] = i

    with multiprocessing.Pool(processes=5) as pool:
        pool.map(processamento, numeros) #ja tem loop

if __name__ == '__main__':
    main()
