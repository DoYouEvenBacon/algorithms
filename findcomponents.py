#Alan Tan
#atan574
#322945602
#COMPSCI220 2017 S2 Assignment 4 Question 3
#findcomponents.py

#Read matrix.txt file
#Convert matrix.txt to a list (adjList)
#Create the list of the reversed graph (reversedNodeList)
#Perform DFS on reversed list, output trees in same format as Q2
#Perform DFS on original list (adjList)

class FindComponents:
    def __init__(self):
        self.matrixList = []
        self.adjList = []
        
        self.reversedNodeList = []
        self.reversedColours = {}
        self.reversedTrees = []
        self.reversedBlackedNodes = []
        self.time = 0

        self.colours = {}
        self.trees = []
        self.blackedNodes = []

        

    def readFile(self, inputName):
        try:
            inFile = open(inputName, "r")
            contents = inFile.readlines()
            inFile.close()
            for i in contents:
                self.matrixList.append(i)
        except IOError:
            print("File does not exist.")

    def matrix2list(self):
        for i in self.matrixList:
            convertedList = []
            count = 0
            for j in i:
                if j == "1" and j != ",":
                    convertedList.append(count)
                if j != ",":
                    count += 1
            self.adjList.append(convertedList)

    def list2reverse(self):
        biggest = 0
        for i in self.adjList:
            for x in i:
                if int(x) > biggest:
                    biggest = int(x) #get biggest node value to init num of lists of nodes
        for i in range(biggest + 1):
                self.reversedNodeList.append([])        
        i_count = 0 #indexing i does not work if more than 1 list of the same numbers

        for i in self.adjList:
            for j in i:
                a = int(j)
                b = i_count
                self.reversedNodeList[a].append(b)
            i_count += 1

    def DFSOnReversed(self):
        self.reversedColours = {node : "WHITE" for node in range(len(self.reversedNodeList))}
        for index, node in enumerate(self.reversedNodeList): #fix for lists of same elements
            if self.reversedColours[index] == "WHITE":
                self.reversedTrees.append(index) #keep track of new tree
                self.DFSVisitOnReversed(node, index)

        for i in range(len(self.reversedBlackedNodes)):
            print(i, self.reversedBlackedNodes[i])
            if self.reversedBlackedNodes[i] in self.reversedTrees:
                print()        

    def DFSVisitOnReversed(self, node, nodeIndex):
        self.reversedColours[nodeIndex] = "GREY"
        self.time += 1
        for vertex in node:
            if self.reversedColours[vertex] == "WHITE":
                self.DFSVisitOnReversed(self.reversedNodeList[vertex], vertex)
        self.reversedColours[nodeIndex] = "BLACK"
        self.reversedBlackedNodes.append(nodeIndex)
        self.time += 1

    def DFSOnOriginal(self):
        self.colours = {node : "WHITE" for node in range(len(self.adjList))}
        for index in reversed(self.reversedBlackedNodes): #fix for lists of same elements
            if self.colours[index] == "WHITE":
                self.trees.append(index) #keep track of new tree
                self.DFSVisitOnOriginal(self.adjList[index], index)

    def DFSVisitOnOriginal(self, node, nodeIndex):
        self.colours[nodeIndex] = "GREY"
        for vertex in node:
            if self.colours[vertex] == "WHITE":
                self.DFSVisitOnOriginal(self.adjList[vertex], vertex)
        self.colours[nodeIndex] = "BLACK"
        self.blackedNodes.append(nodeIndex)

    def outputFile(self, outputName):
        try:
            outFile = open(outputName, "w")
            
            treeList = []
            lineString = ""
            for i in self.blackedNodes:
                treeList.append(i)
                if i in self.trees:
                    treeList.sort()
                    for j in treeList:
                        if j == treeList[-1]:
                            lineString += str(j)
                        else:
                            lineString += str(j) + ","
                    if i == self.trees[-1]:
                        outFile.write(lineString)
                    else:
                        outFile.write(lineString + "\n")
                    lineString = ""
                    treeList = []

            outFile.close()
        except IOError:
            print("File does not exist.")      
        

def main():
    a = FindComponents()
    a.readFile("matrix.txt")
    a.matrix2list()
    a.list2reverse()
    a.DFSOnReversed()
    a.DFSOnOriginal()
    a.outputFile("components.txt")
    
main()
