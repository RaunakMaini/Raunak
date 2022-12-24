from multiprocessing import Process
def hii():
    print("Hello")
if __name__=='__main__':
    p=Process(target=hii)
    p.start()
    p.join()
