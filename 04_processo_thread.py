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

def soma_processo():
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