import requests

class queuedata(object):

        def __init__(self):
                casesdata = requests.get('http://127.0.0.1:8000/API/cases/')
                labdata = requests.get('http://127.0.0.1:8000/API/labs/')
                quarantinedata = requests.get('http://127.0.0.1:8000/API/quarantine/')
                sqliteseqdata = requests.get('http://127.0.0.1:8000/API/sqliteseq/')
                summerydata = requests.get('http://127.0.0.1:8000/API/summery/')
                vaccinedata = requests.get('http://127.0.0.1:8000/API/vaccine/')

                queue = [casesdata, labdata, quarantinedata, sqliteseqdata, summerydata, vaccinedata]

                self.element = [queue]

        def enqueue(self, queue):
                self.element.append(queue)

        def dequeue(self):
                return self.element.pop(0)

        def rear(self):
                return self.element[-1]

        def front(self):
                return self.element[0]

        def isEmpty(self):
                return len(self.element) == 0

        def display(self):
                print(self.queue)

                while True:
                        print("Select operation \n1: Add to queue data \n 2: Remove from queue \n 3: LiFO queue  \n 4: Fifo queue \n 5: check empty queue \n 6: display queue \n 7: Exit" )
                        choice = int(input())

                        if choice == 1:
                                self.enqueue()
                        elif choice == 2:
                                self.dequeue()
                        elif choice == 3:
                                self.rear()
                        elif choice == 4:
                                self.front()
                        elif choice == 5:
                                self.isEmpty()
                        elif choice == 6:
                                self.display()
                        else:
                                print("Enter correct operations")
                                break
