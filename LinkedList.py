import random
import sys
import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, wert):
        newNode = Node.Node(wert)
        if self.head == None:
            self.head = newNode
        else:
            startingNode = self.head
            while startingNode.getNext() != None:
                startingNode = startingNode.getNext()
            startingNode.setNext(newNode)
        self.size += 1

    def delete(self, wert):
        if self.head == None:
            return
        if self.head.getWert() == wert:
            self.head = self.head.getNext()
            self.size -= 1
            return
        startingNode = self.head
        while startingNode.getNext() != None:
            if startingNode.getNext().getWert() == wert:
                startingNode.setNext(startingNode.getNext().getNext())
                self.size -= 1
                return
            startingNode = startingNode.getNext()
        return False

    def search(self, wert):
        startingNode = self.head
        while startingNode != None:
            if startingNode.getWert() == wert:
                return True
            startingNode = startingNode.getNext()
        return False

    def getAtIndex(self, index):
        if index >= self.size:
            return None
        startingNode = self.head
        for i in range(index):
            startingNode = startingNode.getNext()
        return startingNode.getWert()

    def getSize(self):
        return self.size

    def printList(self):
        startingNode = self.head
        while startingNode != None:
            print(startingNode.getWert())
            startingNode = startingNode.getNext()


    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        if self._iter_node is None:
            raise StopIteration
        wert = self._iter_node.getWert()
        self._iter_node = self._iter_node.getNext()
        return wert

def main():
    ll = LinkedList()
    ll.insert(random.randint(0, 100))
    ll.insert(random.randint(0, 100))
    ll.insert(random.randint(0, 100))
    print('Size:')
    print(ll.getSize())
    print('Gibt es 10 in der Liste?')
    print(ll.search(10))
    print('Wert bei Index 0:')
    print(ll.getAtIndex(0))
    print('Werte:')
    ll.printList()
    print('Werte:')
    for value in ll:
        print(value)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(1)

