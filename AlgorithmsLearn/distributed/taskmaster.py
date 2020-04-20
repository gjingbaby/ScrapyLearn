import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()     
#接受结果的队列
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

def gettask():
    return task_queue

def getresult():
    return result_queue

def do_task_master():
    #把两个队列都注册到网络上，其他代码就能调用
    QueueManager.register('get_task_queue',callable=gettask)
    QueueManager.register('get_result_queue',callable=getresult)
    #设置端口和验证
    manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    #启动manager
    manager.start()

    #获得通过网络访问的队列对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0,10000)
        print('put task %d'%(n,))
        #发送任务上去
        task.put(n)

    print('Try get results...')
    for i in range(10):
        try:
            #从result队列读取结果
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:
            print('Result Queue is empty')
    manager.shutdown()
    print('Master exit')

if __name__ == '__main__':
    do_task_master()


'''
注意此处，实际上是在网络上创建task队列和result队列，设置好网络端口和验证，供worker访问，因此就可以有多个worker
master负责向task put任务
worker负责从task get任务
worker负责向result put结果
master负责从result get结果
'''