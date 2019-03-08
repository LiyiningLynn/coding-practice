
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data2):
        if self.data:
            if self.data==data2:
                print 'error'
            elif self.data>data2:
                #self.left.insert(data2)
                if self.left:
                    self.left.insert(data2)
                else:
                    self.left=Node(data2)
            else:
                if self.right:
                    self.right.insert(data2)
                else:
                    self.right=Node(data2)
        else:
            self.data=data2

    def delete(self,data3):
        #first search and locate
        #if self.data == data3:
         #   pass
        #elif
            
    def printTree(self):
        print self.data,
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()


root=Node(90)
#root.printTree()
root.insert(50)
root.insert(150)
root.insert(20)
root.insert(75)
root.insert(95)
root.insert(175)
root.insert(5)
root.insert(25)
root.insert(66)
root.insert(80)
root.insert(92)
root.insert(111)
root.insert(166)
root.insert(200)


root.printTree()