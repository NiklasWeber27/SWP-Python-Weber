class Node:
    def __init__(self, wert):
        self.wert = wert
        self.next = None

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def getWert(self):
        return self.wert
