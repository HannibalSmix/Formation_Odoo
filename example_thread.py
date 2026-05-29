import threading
import time
from random import randint

def worker(n):
    for i in range(n):
        print(f"Worker {threading.current_thread().name} is working... {i}")
        time.sleep(randint(1, 3))

# Créer un thread pour exécuter la fonction worker avec un argument de 5
t = threading.Thread(target=worker, args=(5,))
t2 = threading.Thread(target=worker, args=(15,))
t3 = threading.Thread(target=worker, args=(10,))
t4 = threading.Thread(target=worker, args=(20,))

# Démarrer le thread
t.start()
t2.start()
t3.start()
t4.start()

for i in range(5):
    print(f"Main thread is working... {i}")
    time.sleep(randint(1, 3))

# Attendre que le thread se termine
t.join()
t2.join()
t3.join()
t4.join()
