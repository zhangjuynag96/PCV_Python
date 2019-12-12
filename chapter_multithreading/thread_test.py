import threading
import time

# def loop():
#     print('thread %s is running'%threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s'% (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
#
# print('thread %s ended.' % threading.current_thread().name)

# balance = 0
# def change_id(n):
#     global balance
#     balance = balance +  n
#     balance = balance -  n
#
# def run_thread(n):
#     for i in range(100000):
#         change_id(n)
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# python3.7
import threading
import time


def test_thread(id, seconds):
    print('start thread', id, 'at:', time.ctime())
    time.sleep(seconds)
    print('end thread', id, 'at:', time.ctime())


def main():
    sleep_time = [3, 5, 7, 1, 9]
    # 存放线程的list
    threads = []

    print('starting threads at', time.ctime())
    # 创建线程的thread实例加入列表
    for index, seconds in enumerate(sleep_time):
        t = threading.Thread(target=test_thread, args=(index, seconds))
        threads.append(t)
    # 遍历列表，启动线程
    for t in threads:
        t.start()
    #         join方法作用是，让主线程等待该线程结束,所以join应该放在下面的循环里，放在这里就会导致这个启动线程的循环阻塞。结果就是顺序执行。
    #         join也可以设置超时时间
    #         join函数只在主线程只进行等待的时候有用，如果主线程还有其他事情，没必要调用join阻塞自己。
    #         t.join()
    for t in threads:
        t.join()
    print('all threads finished')


if __name__ == '__main__':
    main()
