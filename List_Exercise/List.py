class Empty:
    def __init__(self):
        self.Empty = True

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

    def add(self, value, node):

        new_list = Empty()

        if(not node.IsEmpty):
            prev_list = new_list
            new_list = Node(node.Value + value, prev_list)

        return new_list.Value