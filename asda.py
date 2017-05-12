import threading

def worker(num):
    """thread worker function"""
    print('Worker: {0}'.format(num))
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()