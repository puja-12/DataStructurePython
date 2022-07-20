class Node:
    # constructor
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    # get value from node
    def getData(self):
        return self.data

    # get next node reference
    def getNext(self):
        return self.next

    # set value to node
    def setData(self, newdata):
        self.data = newdata

    # set next node reference
    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    # constructor
    def __init__(self):
        self.head = None

    # check if the list is empty
    def isEmpty(self):
        return self.head == None

    # insert item to be the first item of the list
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    # size of the list
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    # find if item is in the list
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def delete(self, pos):
        current = self.head
        previous = None
        index = 0

        if current is None:
            return "No item in list"

        while index < pos and current is not None:
            previous = current
            current = current.getNext()
            index += 1

        if current is None:
            return "No item in list"
        else:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return current.getData()


if __name__ == '__main__':
    linkedlist = UnorderedList()
    linkedlist.add(1)
    linkedlist.add(2)
    linkedlist.add(3)
    linkedlist.add(4)
    print(linkedlist.delete(0))



