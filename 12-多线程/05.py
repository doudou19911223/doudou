'''
利用time函数，生成两个函数
利用多线程调用
计算总的运行时间
练习带参数的多线程启动方法
'''
import time
# 导入多线程处理包
import threading

def loop1(in1):
    # ctime 得到当前时间
    print('Start loop 1 at:', time.ctime())
    print("我是参数",in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())

def loop2(in1,in2):
    # ctime 得到当前时间
    print('Start loop 2 at:', time.ctime())
    print("我是参数",in1,"和参数",in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at:', time.ctime())

def main():
    print("Starting at:", time.ctime())
    # 生成threading.Thread实例
    t1 = threading.Thread(target=loop1,args=("王老大",))
    t1.start()
    t2 = threading.Thread(target=loop2,args=("王大鹏","王小鹏"))
    t2.start()

    t1.join()
    t2.join()    #假如join，最后一句话就会等到loop1和loop2执行完了才会执行
    print("All done at:", time.ctime())

if __name__ == '__main__':
    main()
    # 一定要有while语句
    # 因为启动多线程后本程序就作为主线程存在
    # 如果主线程执行完毕，则子线程可能也需要终止
    while True:
        time.sleep(1)
