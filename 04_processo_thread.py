# threads no MESMO processo (memória compartilhada)
import threading
# multiprocessing: processos SEPARADOS (memória isolada + fila)
import multiprocessing as mp
import os

contador = 0

def soma_thread():
    global contador
    contador += 1
    print(
        f"[thread] pid={os.getpid()} ident={threading.get_ident()}",
        f"contador={contador}",
        flush=True
    )

def soma_processo(saida):
    n = 1
    print(
        f"[processo] pid={os.getpid()} n={n}"
        f"(copia local de contador={contador})",
        flush=True
    )
    saida.put(n)

if __name__ == "__main__":
    print('pid da MAIN: ', os.getpid(), flush=True)
    print(flush=True)

    #THREADS
    print('THREADS: mesma memória (mesmo PID, ident direferente)')
    t1 = threading.Thread(target=soma_thread)
    t2 = threading.Thread(target=soma_thread)
    t3 = threading.Thread(target=soma_thread)
    t4 = threading.Thread(target=soma_thread)
    t5 = threading.Thread(target=soma_thread)
  
    # start(): dispara o fluxo. NÃO cria um novo processo, apenas uma nova thread no mesmo processo.
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    print('Contator na main: ', contador, flush=True) #Serve para atrasar a mensagem até que as threads terminem, garantindo que o valor de contador seja atualizado antes de ser impresso.

    #PROCESSOS
    print('PROCESSOS: memória isolada (PID novo; main não vê alterações de contador)')
    fila = mp.Queue() #Serve para comunicação entre processos, permitindo que dados sejam passados de um processo para outro.
    #fila, -> Tupla é uma forma de passar múltiplos argumentos para a função alvo do processo. Aqui, estamos passando apenas a fila, mas se houvesse mais argumentos, eles seriam incluídos na tupla.
    p1 = mp.Process(target=soma_processo, args=(fila,))
    p2 = mp.Process(target=soma_processo, args=(fila,))

    p1.start()
    p2.start()
    # get(): bloqueia a execução até que o processo filho termine e retorne um valor. Aqui, estamos obtendo o valor retornado pelo processo filho através da fila.
    a = fila.get()
    b = fila.get()
    p1.join()
    p2.join()
    print('Contador na main: ', contador, flush=True) 
    print('cada processo devolveu: ', a, 'e', b, flush=True)