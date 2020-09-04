import multiprocessing as mp  
import queue
import time


class TestCase:
    def __init__(self):
        # initialize queues
        self.queue = mp.JoinableQueue()   # this is where we are going to store input data
        self.kafka_queue = mp.Queue()  # this where we are gonna push them out
        self.done = []

    def main(self):
        # create 4 processes, which takes queues as arguments
        # the data will get in and out through the queues
        # daemonize it
        processes = []
        for i in range(4):
            worker_process = mp.Process(target=self.worker, args=(self.queue, self.kafka_queue), daemon=True, name='worker_process_{}'.format(i))
            worker_process.start()        # Launch reader() as a separate python process
            processes.append(worker_process)
        print([x.name for x in processes])

        # this process simulates sending processed data out 
        # kafka_process = mp.Process(target=self.send_kafka, args=(self.kafka_queue,), daemon=True, name='kafka_process')
        # kafka_process.start()
        
        x = [i for i in range(100)]
        print(len(x))
        for row in x:
            self.queue.put(row)
           
            
        self.queue.join()
        print("Output q - %r", self.kafka_queue.qsize()) 
        # self.kafka_queue.join()
        # print(self.done)
        # while not self.kafka_queue.empty():
        #     yield self.kafka_queue.get()
        for item in range(0, self.kafka_queue.qsize()):
            yield self.kafka_queue.get()
        print('done')

    
    def worker(self, queue, kafka_queue):  
        while True:
            msg = queue.get()         # Read from the queue and do nothing
            # print('Processing %s (MP: %s) ' % (msg, mp.current_process().name))
            msg = msg + 100
            kafka_queue.put(msg)
            queue.task_done()

    def send_kafka(self, queue):  
        while True:
            msg = queue.get()
            self.done.append(msg)
            print(msg)
            queue.task_done()



x = TestCase()

test_list = []
for i in x.main():
    test_list.append(i)

print(len(test_list))
print(test_list)
