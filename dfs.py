#Alan Tan
#atan574
#322945602
#COMPSCI220 2017 S2 Assignment 4 Question 2
#dfs.py

#select the next grey vertex to pick as the youngest remaining grey vertex
#operates like a stack:
#vertices pushed onto stack when we colour them grey

#if vertex on top of stack has a White out-neighbour, push White out-neighbour onto stack and colour it Grey
#if vertex on top of stack has no White out-neighbours, pop vertex off stack and colour it Black

class dfs:
    def __init__(self):
        self.nodeList = []
        self.colours = {}
        self.trees = []
        self.blackedNodes = []

    def readFile(self, inputName):
        try:
            inFile = open(inputName, "r")
            contents = inFile.readlines()
            inFile.close()
            for i in contents:
                self.nodeList.append(list(map(int, (i.strip().split(",")))))
            print(self.nodeList)
            print()
        except IOError:
            print("File does not exist.")

    def DFS(self):
        self.colours = {node : "WHITE" for node in range(len(self.nodeList))}
        print(self.colours)

        for index, node in enumerate(self.nodeList): #fix for lists of same elements
            print("node", node, "index",index) #fixed indexing the right nodes
            if self.colours[index] == "WHITE":
                self.trees.append(index) #keep track of new tree
                self.DFSvisit(node, index)

        #test output
        """
        print("colours")
        print(self.colours)
        print("Black order")
        print(self.blackedNodes)
        for i in range(len(self.blackedNodes)):
            print(i, self.blackedNodes[i])
            if self.blackedNodes[i] in self.trees:
                print()
        """

    def DFSvisit(self, node, nodeIndex):
        self.colours[nodeIndex] = "GREY"
        for vertex in node:
            if self.colours[vertex] == "WHITE":
                self.DFSvisit(self.nodeList[vertex], vertex)
        self.colours[nodeIndex] = "BLACK"
        self.blackedNodes.append(nodeIndex)

    def outputFile(self, outputName):
        try:
            outFile = open(outputName, "w")
            for i in range(len(self.blackedNodes)):
                lineString = ""
                if i == len(self.blackedNodes) - 1:
                    lineString += str(i) + "," + str(self.blackedNodes[i])
                else:
                    lineString += str(i) + "," + str(self.blackedNodes[i]) + "\n"
                outFile.write(lineString)
                if self.blackedNodes[i] in self.trees:
                    outFile.write("\n")   
            outFile.close()
        except IOError:
            print("File does not exist.")


def main():
    a = dfs()
    a.readFile("list.txt")
    a.DFS()
    a.outputFile("dfs.txt")
    
main()
