'''
1. Receive data from an API.      Done   from django api receive corona data sample

I have tried many times queue in api given in comment below .
 But logic is not run at the time of production will use with front end.
Queue working must have front end integrated work that why
i have extract data from api url
Apply below both queue and lifo fifo in data.

2. Add data to a queue.           Done in extraction
3. Apply LIFO and FIFO on the data, without using any library or function.     Done in extraction


#change from listapiview to apiview for full customizations
'''


from rest_framework.response import Response
from .models import cases, vaccine, summery, sqliteseq, quarantine, labs
from .serializers import casesSerializer, \
    vaccineSerializer, \
    labsSerializer, \
    quarantineSerializer, \
    summerySerializer, \
    sqliteseqSerializer  # , labsSerializer, quarantineSerializer, sqliteseqSerializer, vaccineSerializer, summerySerializer
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from django.core.paginator import Paginator


class casesList(APIView):
    def get(self, request):
        cases1 = cases.objects.all()
        serializer_class = casesSerializer(cases1, many=True)
        return Response(serializer_class.data)
    def post(self):
        pass

class labList(APIView):
    def get(self, request):
        labs1 = labs.objects.all()
        serializer_class = labsSerializer(labs1, many=True)
        return Response(serializer_class.data)

    def post(self):
        pass


class quarantineList(APIView):
    def get(self, request):
        qurantine1 = quarantine.objects.all()
        serializer_class = quarantineSerializer(qurantine1, many=True)
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['id']
        return Response(serializer_class.data)

    def post(self):
        pass


class sqliteseqList(APIView):
    def get(self, request):
        sqliteseq1 = sqliteseq.objects.all()
        serializer_class = sqliteseqSerializer(sqliteseq1, many=True)
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['name']
        return Response(serializer_class.data)

    def post(self):
        pass


class summeryList(APIView):
    def get(self, request):
        summery1 = summery.objects.all()
        serializer_class = summerySerializer(summery1, many=True)
        return Response(serializer_class.data)

    def post(self):
        pass
class vaccineList(APIView):
    def get(self, request):
        vaccine1 = vaccine.objects.all()
        serializer_class = vaccineSerializer(vaccine1, many=True)
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['id']
        return Response(serializer_class.data)

    def post(self):
        pass










"""
class dataqueue(APIView):
    def __init__(self):
        self.element = [casesSerializer, labsSerializer, quarantineSerializer, sqliteseqSerializer, summerySerializer,
                        vaccineSerializer]

    def enqueue(self, data):
        self.element.append(data)

    def dequeue(self):
        return self.element.pop(0)

    def rear(self):
        return self.element[-1]

    def front(self):
        return self.element[0]

    def isEmpty(self):
        return len(self.element) == 0

        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['id']
    def get(self, request):
        import requests
        receivedata = requests.get('http://127.0.0.1:8000/API/cases/')
        return(receivedata.json())
    def post(self):
        pass
  
return deqeueue(element)
class Queuedata(object):

    def __init__(self):
        self.element = [casesSerializer, labsSerializer, quarantineSerializer, sqliteseqSerializer, summerySerializer, vaccineSerializer]

    def enqueue(self, data):
        self.element.append(data)

    def dequeue(self):
        return self.element.pop(0)

    def rear(self):
        return self.element[-1]

    def front(self):
        return self.element[0]

    def isEmpty(self):
        return len(self.element) == 0
class dataqueue(APIView):
    def get(self, request):
        return Response(Queuedata)
    def post(self):
        pass

q = Queuedata()
def enqueue(element):
    pass
enqueue(element)
print("front :" ,q.front())
print("rear : ", q.rear())

def deqeueue(element):
    pass
deqeueue(element)
print("front :" ,q.front())
print("rear : ", Queuedata.rear())
def dequeue(self, request):
        if not dataqueue:
            print("queue is empty")
        else:
            d = dataqueue.pop(0)
            print("removed data", d)


 while True:
        print("select operation \n 1.Add data to queue  \n 2.Remove Data from queue \n 3.Show data \n 4. QUit")
        if choice  == 1:
            enqueue()
        elif choice == 2:
            dequeue()
        elif choice == 3:
            display()
        elif choice == 4:
            break

        else:
            print("Enter correct operations")
"""

"""

'''

"""

"""

class Queuedata(APIView):
    def __init__(self):
        self.data =[casesList, labList, quarantineList, sqliteseqList, summeryList, vaccineList]
    def isEmpty(self):
        return self.cases, labs, quarantine, sqliteseq, summery, vaccine == [casesList, labList, quarantineList, sqliteseqList, summeryList, vaccineList]
    def inQueue(self, items):
        self.cases, labs, quarantine, sqliteseq, summery, vaccine.insert(0,cases, labs, quarantine, sqliteseq, summery, vaccine)
    def outQueue(self):
        return self.cases, labs, quarantine, sqliteseq, summery, vaccine.pop()
    def printqueue(self):
        for record in self.cases, labs, quarantine, sqliteseq, summery, vaccine:
            print(cases, labs, quarantine, sqliteseq, summery, vaccine, " , ", end=' ')
    def data(self, request):
        return q.enqueue()
    def post(self):
        pass
        class Queuedata(APIView):
    queuedata = [casesList, labList, quarantineList, sqliteseqList, summeryList, vaccineList]
    def enqueue(self, request):
        data = queuedata
        queuedata.append(data)
        print(data, "is added to queue")
    def dequeue(self, request):
        if not queuedata:
            print("queue is empty")
        else:
            d = queue.pop(0)
            print("removed data", d)
    def display(self, request):
            print(queue)


def inQueue(args):
    pass


class Queuedata(APIView):
    def Queuedata(self, request):
        return Response(inQueue)
        class Queue:
    def __init__(self):
        self.data = [cases, labs, quarantine, sqliteseq, summery, vaccine]
        self._size = 0
        self._front = 0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def enqueue(self, e):
        self._data.append(e)
        self._size = self._size + 1
    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = self._front + 1
        return value
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]

q = Queue()
"""

