import psutil
def killprocess():
    ppidd = '20138c'
    if ppidd:
        try:
            p = psutil.Process(ppidd)
            p.terminate()
        except psutil.NoSuchProcess:
            print ('oops loose process')