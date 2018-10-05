from multiprocessing import Process,Queue
import os,time,random

#读数据进程的执行程序
def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue'%value)

def write(q):
    print('Process to write:%s'%os.getpid())
    for value in ['A','B','C','D']:
        print('Put %s to queue...'%value)
        q.put(value)
        time.sleep(random.random())

if __name__=='__main__':
    #创建父进程
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
