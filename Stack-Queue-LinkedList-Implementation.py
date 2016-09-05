# My implementations of Stack, Queue, and LinkedList using Python

class Stack:
    def __init__(self):
        self.contents = []

    def push(self, item):
        if (item == None):
            return
        self.contents.append(item)

    def pop(self):
        if (len(self.contents) == 0):
            return None
        removed = self.contents[-1]
        self.contents = self.contents[0 : len(self.contents) - 1]
        return removed

    def peek(self):
        return self.contents[len(self.contents) - 1]


s = Stack()

s.push({'John', 'Tucker'})
s.push({'Jim', 'Pam'})
print(s.peek())
s.push({'Holly'})
print(s.peek())
print(s.pop())
print(s.contents)
s.push({'Toby', 'Michael', 'Ryan'})
print(s.peek())


class Queue:
    def __init__(self):
        self.contents = []

    def enqueue(self, item):
        if(item == None):
            return
        self.contents.insert(0, item)

    def dequeue(self):
        if(self.contents == []):
            return None
        removed = self.contents[0]
        self.contents = self.contents[1 : len(self.contents)]
        return removed

    def peek(self):
        return self.contents[0]

print('============ Switching to Queue ============')

q = Queue()

q.enqueue({'Kelly', 'Ron'})
q.enqueue({'Dwight', 'Angela'})
print(q.peek())
q.enqueue({'David', 'Andy'})
print(q.contents)
print(q.dequeue())
print(q.peek())
q.dequeue()
print(q.peek())

class LinkedList:
    def __init__(self):
        self.contents = []

    def insert(self, data):
        if (data == None):
            return
        if (len(self.contents) > 0):
            data.setNext(self.contents[len(self.contents) - 1])
        else:
            en = Node('Empty Node')
            data.setNext(en)
        self.contents.append(data)

    def find(self, data):
        for x in self.contents:
            if(x.contents == data):
                return x
            else:
                return

    def remove(self, node):
        for x in range(len(self.contents) - 1):
            if (self.contents[x].contents == node.contents):
                if (x == 0):
                    en = Node('Empty Node')
                    self.contents[x + 1].setNext(en)
                    self.contents.remove(self.contents[x])
                elif (self.contents[x + 1]):
                    self.contents[x + 1].setNext(self.contents[x - 1])
                    self.contents.remove(self.contents[x])
                elif (len(self.contents) == (x + 1)):
                    self.contents[x - 1].setNext(None)
                    self.contents.remove(self.contents[x])

class Node:

    def __init__(self, data):
        self.contents = data
        self.nextNode = None

    def get(self):
        return self.contents

    def set(self, newData):
        self.contents = newData

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getNext(self):
        return self.nextNode

n1 = Node('Jacks node')
n2 = Node('Sams node')
n3 = Node('Petes node')
n4 = Node('Josies node')

nodeList = LinkedList()
nodeList.insert(n1)
nodeList.insert(n2)
nodeList.insert(n3)
nodeList.insert(n4)

print('========= Switching to Linked List ==========')
print(nodeList.contents[0].contents + " and his next : " + nodeList.contents[0].getNext().contents)
print(nodeList.contents[1].contents + " and his next : " + nodeList.contents[1].getNext().contents)
print(nodeList.contents[2].contents + " and his next : " + nodeList.contents[2].getNext().contents)
print(nodeList.contents[3].contents + " and her next : " + nodeList.contents[3].getNext().contents)
nodeList.remove(n3)
print("After removing Pete:")
print(nodeList.contents[0].contents + " and his next : " + nodeList.contents[0].getNext().contents)
print(nodeList.contents[1].contents + " and his next : " + nodeList.contents[1].getNext().contents)
print(nodeList.contents[2].contents + " and her next : " + nodeList.contents[2].getNext().contents)

nodeList = LinkedList()
nodeList.insert(n1)
nodeList.insert(n2)
nodeList.insert(n3)
nodeList.insert(n4)

print('========= Testing removal of first node ==========')
nodeList.remove(n1)
print(nodeList.contents[0].contents + " and his next : " + nodeList.contents[0].getNext().contents)
print(nodeList.contents[1].contents + " and his next : " + nodeList.contents[1].getNext().contents)
print(nodeList.contents[2].contents + " and her next : " + nodeList.contents[2].getNext().contents)

nodeList = LinkedList()
nodeList.insert(n1)
nodeList.insert(n2)
nodeList.insert(n3)
nodeList.insert(n4)

print('========= Testing removal of last node ==========')
nodeList.remove(n4)
print(nodeList.contents[0].contents + " and his next : " + nodeList.contents[0].getNext().contents)
print(nodeList.contents[1].contents + " and his next : " + nodeList.contents[1].getNext().contents)
print(nodeList.contents[2].contents + " and his next : " + nodeList.contents[2].getNext().contents)
