lass Queue(object):
    def __init__(self):
        self.qlist = []

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.qlist)

    def enqueue(self, data):
        self.qlist.append(data)

    def dequeue(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist.pop(0)

    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[0]

    def getRearMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        return self.qlist[-1]

class PriorityQueue(object):
    def __init__(self):
        self.qlist = []

    def __len__(self):
        return len(self.qlist)

    def isEmpty(self):
        return len(self) == 0

    def enqueue(self, data, priority):
        entry = _PriorityQEntry(data, priority)
        self.qlist.append(entry)

    def dequeue(self):
        A = []
        for i in self.qlist:
            A.append(i)
        s = 0
        for i in range(1, len(self.qlist)):
            if A[i].priority < A[s].priority:
                s = i
        hasil = self.qlist.pop(s)
        return hasil.item

    def getFrontMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        for i in range(1, len(self.qlist)):
            a = self.qlist[i]
            if a.priority == 1:
                belakang = a.item
            else :
                i += 1
        return belakang

    def getRearMost(self):
        assert not self.isEmpty(), "Antrian sedang kosong"
        for i in range(len(self.qlist)):
            c = self.qlist[i]
            ex = len(self.qlist)
            if c.priority == ex:
                depan = c.item
            else :
                i += 1
        return depan
    
class _PriorityQEntry(object):
    def __init__(self, data, priority):
        self.item = data
        self.priority = priority

Q = Queue()
Q.enqueue(5)
Q.enqueue(9)
Q.enqueue(13)
Q.enqueue(3)
print("Data Paling Depan : " + str(Q.getFrontMost()))
print("Data Paling Belakang : " + str(Q.getRearMost()))
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())

P = PriorityQueue()
P.enqueue('Apel', 3)
P.enqueue('Mangga', 2)
P.enqueue('Jeruk', 4)
P.enqueue('Kelapa', 1)
print("Data Paling Pertama : " + str(P.getFrontMost()))
print("Data Paling Belakang : " + str(P.getRearMost()))
print(P.dequeue())
print(P.dequeue())
print(P.dequeue())
print(P.dequeue())
