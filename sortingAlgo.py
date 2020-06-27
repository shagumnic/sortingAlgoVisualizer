import time
#Merge Sort
def mergeSort(subjectList, firstPos, lastPos, visualizeData, timeTick) :
    if firstPos < lastPos - 1 :
        workspace = [None] * (lastPos - firstPos)
        mergeSortAux(subjectList, firstPos, lastPos, workspace, 0, visualizeData, timeTick)

#Aux function to divide the list into two part then start merging after done        
def mergeSortAux(subjectList, firstPos, lastPos, workspace, workspaceFirstPos, visualizeData, timeTick) :
    if firstPos < lastPos - 1 :
        middlePos = (firstPos + lastPos) // 2
        
        visualizeData(subjectList, ['yellow' if x >= firstPos and x <= middlePos else 'blue' if x > middlePos and x < lastPos else 'red' for x in range(len(subjectList))])
        time.sleep(timeTick)
        mergeSortAux(subjectList, firstPos, middlePos, workspace, workspaceFirstPos, visualizeData, timeTick)
        mergeSortAux(subjectList, middlePos, lastPos, workspace, workspaceFirstPos + (middlePos - firstPos), visualizeData, timeTick)
        
        visualizeData(subjectList, ['yellow' if x >= firstPos and x <= middlePos else 'blue' if x > middlePos and x < lastPos else 'red' for x in range(len(subjectList))])
        time.sleep(timeTick)        
        merge(subjectList, firstPos, middlePos, subjectList, middlePos, lastPos, workspace, workspaceFirstPos, visualizeData, timeTick)
        
        for pos in range(firstPos, lastPos) :
            subjectList[pos] = workspace[workspaceFirstPos + (pos - firstPos)]
        visualizeData(subjectList, ['green' if x >= firstPos and x < lastPos else 'red' for x in range(len(subjectList))])
        time.sleep(timeTick)

#merging function that put them into an order list            
def merge(subjectListA, firstPosA, lastPosA, subjectListB, firstPosB, lastPosB, resultList, resultListFirstPos, visualizeData, timeTick) :
    if firstPosA < lastPosA and firstPosB < lastPosB :
        if subjectListA[firstPosA][1] < subjectListB[firstPosB][1] :
            resultList[resultListFirstPos] = subjectListA[firstPosA]
            merge(subjectListA, firstPosA + 1, lastPosA, subjectListB, firstPosB, lastPosB, resultList, resultListFirstPos + 1, visualizeData, timeTick)
        else :
            resultList[resultListFirstPos] = subjectListB[firstPosB]
            merge(subjectListA, firstPosA, lastPosA, subjectListB, firstPosB + 1, lastPosB, resultList, resultListFirstPos + 1, visualizeData, timeTick)
    elif firstPosA < lastPosA :
        resultList[resultListFirstPos] = subjectListA[firstPosA]
        merge(subjectListA, firstPosA + 1, lastPosA, subjectListB, firstPosB, lastPosB, resultList, resultListFirstPos + 1, visualizeData, timeTick)
    elif firstPosB < lastPosB :
        resultList[resultListFirstPos] = subjectListB[firstPosB]
        merge(subjectListA, firstPosA, lastPosA, subjectListB, firstPosB + 1, lastPosB, resultList, resultListFirstPos + 1, visualizeData, timeTick)        
    return resultList


#Insertion Sort
#def insertionSort(subjectList, firstPos, lastPos) :
    #if firstPos < lastPos :
        #insertionSort(subjectList, firstPos, lastPos - 1)
        #insertion(subjectList, firstPos, lastPos, subjectList[lastPos - 1])
        
#def insertion(subjectList, firstPos, lastPos, newValue) :
    #if firstPos > lastPos - 1 :
        #subjectList[firstPos] = newValue
    #elif subjectList[lastPos - 2][1] <= newValue[1] :
        #print(lastPos)
        #print(subjectList[lastPos - 2][1]) 
        #subjectList[lastPos - 1] = newValue
    #else :
        #subjectList[lastPos - 1] = subjectList[lastPos - 2]
        #insertion(subjectList, firstPos, lastPos - 1, newValue)

def insertionSort(subjectList, firstPos, lastPos, visualizeData, timeTick) :
    for index in range(firstPos, lastPos) :
        if index == 0 :
            pass
        else :
            newValue = subjectList[index]
            second_index = index - 1
            while second_index >=0 and subjectList[second_index][1] > newValue[1] :
                subjectList[second_index + 1] = subjectList[second_index]
                visualizeData(subjectList, ['yellow' if x == second_index or x == second_index + 1 else 'blue' if x == index else 'red' for x in range(len(subjectList))])
                time.sleep(timeTick)
                second_index -= 1
            subjectList[second_index+1] = newValue
            visualizeData(subjectList, ['green' if x == second_index + 1 or x == index else 'red' for x in range(len(subjectList))])
            time.sleep(timeTick)
    visualizeData(subjectList, ['green' for x in range(len(subjectList))])


#heap sort
def heapSort(subjectList, visualizeData, timeTick) :
    workList = []
    for index in range(0, len(subjectList)) :
        heapInsert(subjectList, workList, subjectList[index], visualizeData, timeTick)
        visualizeList = workList[0:index+1] + subjectList[index+1:]
        visualizeData(visualizeList, ['green' if x >= 0 and x <=index else 'red' for x in range(len(visualizeList))])
        time.sleep(timeTick)
    #resultList = []
    #while len(workList) != 0 :
        #resultList.append(heapRemove(workList, visualizeData, timeTick))
    for index in range(0, len(subjectList)) :
        subjectList[index] = heapRemove(workList, visualizeData, timeTick) #resultList[index]
    visualizeData(subjectList, ['green' for x in range(len(subjectList))])
        
def heapInsert(originalList, subjectList, newValue, visualizeData, timeTick) :
    subjectList.append(newValue)
    if len(subjectList) == 0 :
        pass
    else :
        heapSwap(originalList, subjectList, len(subjectList) - 1, visualizeData, timeTick)

def heapSwap(originalList, subjectList, posToCheck, visualizeData, timeTick) :
    #if posToCheck <= 0 :
        #pass
    if posToCheck > 0 :
        parentPos = (posToCheck - 1) // 2
        if subjectList[posToCheck][1] < subjectList[parentPos][1] :
            #visualizeList = subjectList[0:posToCheck+1] + originalList[posToCheck+1:]
            #visualizeData(visualizeList, ['yellow' if x == parentPos and x == posToCheck else 'red' for x in range(len(visualizeList))])
            #time.sleep(timeTick)            
            subjectList[parentPos], subjectList[posToCheck] = subjectList[posToCheck], subjectList[parentPos]
            #visualizeList = subjectList[0:posToCheck+1] + originalList[posToCheck+1:]
            #visualizeData(visualizeList, ['green' if x == parentPos and x == posToCheck else 'red' for x in range(len(visualizeList))])
            #time.sleep(timeTick)            
        heapSwap(originalList, subjectList, parentPos, visualizeData, timeTick)

def heapRemove(subjectList, visualizeData, timeTick) :
    if len(subjectList) == 1 :
        return subjectList.pop()
    else :
        subjectList[0], subjectList[len(subjectList) - 1] = subjectList[len(subjectList) - 1], subjectList[0]
        valueToSave = subjectList.pop()
        heapResort(subjectList, 0, visualizeData, timeTick)
        return valueToSave
    
def heapResort(subjectList, posToCheck, visualizeData, timeTick) :
    leftChildPos = posToCheck * 2 + 1
    rightChildPos = posToCheck * 2 + 2
    if rightChildPos <= len(subjectList) - 1 : 
        if subjectList[leftChildPos][1] < subjectList[rightChildPos][1] :
            if subjectList[posToCheck][1] > subjectList[leftChildPos][1] :
                subjectList[posToCheck], subjectList[leftChildPos] = subjectList[leftChildPos], subjectList[posToCheck]
                heapResort(subjectList, leftChildPos, visualizeData, timeTick)
        else :
            if subjectList[posToCheck][1] > subjectList[rightChildPos][1] :
                subjectList[posToCheck], subjectList[rightChildPos] = subjectList[rightChildPos], subjectList[posToCheck]
                heapResort(subjectList, rightChildPos, visualizeData, timeTick)
    elif leftChildPos <= len(subjectList) - 1 :
        if subjectList[posToCheck][1] > subjectList[leftChildPos][1] :
            subjectList[posToCheck], subjectList[leftChildPos] = subjectList[leftChildPos], subjectList[posToCheck]
    #else :
        #pass

def bubbleSort(subjectList, visualizeData, timeTick) :
    for index in range(0, len(subjectList)) :
        for second_index in range(index+1, len(subjectList)) :
            if subjectList[index][1] > subjectList[second_index][1] :
                subjectList[index], subjectList[second_index] = subjectList[second_index], subjectList[index]
                visualizeData(subjectList, ['green' if x == index or x == second_index else 'red' for x in range(len(subjectList))])
                time.sleep(timeTick)
        visualizeData(subjectList, ['green' for x in range(len(subjectList))])
                
def selectionSort(subjectList, visualizeData, timeTick) :
    for index in range(0, len(subjectList)) :
        minValueIndex = index
        for second_index in range(index + 1, len(subjectList)) :
            if subjectList[second_index][1] < subjectList[minValueIndex][1] :
                visualizeData(subjectList, ['yellow' if x == second_index or x == minValueIndex else 'red' for x in range(len(subjectList))])
                time.sleep(timeTick)
                minValueIndex = second_index
        subjectList[index], subjectList[minValueIndex] = subjectList[minValueIndex], subjectList[index]
        visualizeData(subjectList, ['green' if x == index or x == minValueIndex else 'red' for x in range(len(subjectList))])
        time.sleep(timeTick)
    visualizeData(subjectList, ['green' for x in range(len(subjectList))])

#QuickSort
def quickSort(subjectList, firstPos, lastPos, visualizeData, timeTick) :
    if firstPos < lastPos - 1 :
        splitPoint = partition(subjectList, firstPos, lastPos - 1, subjectList[lastPos - 1], visualizeData, timeTick)
        exchange(subjectList, splitPoint, lastPos - 1)
        visualizeData(subjectList, ['green' if x == splitPoint or x == lastPos - 1 else 'grey' for x in range(len(subjectList))])
        time.sleep(timeTick)
        quickSort(subjectList, firstPos, splitPoint, visualizeData, timeTick)
        quickSort(subjectList, splitPoint + 1, lastPos, visualizeData, timeTick)

def partition(subjectList, firstPos, lastPos, splitValue, visualizeData, timeTick) :
    visualizeData(subjectList, ['red' if x == subjectList[firstPos] else 'blue' if x == splitValue else 'yellow' if x == subjectList[lastPos] else 'grey' for x in subjectList])
    time.sleep(timeTick)
    if firstPos >= lastPos :
        return firstPos
    elif subjectList[firstPos][1] < splitValue[1] :
        return partition(subjectList, firstPos + 1, lastPos, splitValue, visualizeData, timeTick)
    elif subjectList[lastPos-1][1] > splitValue[1] :
        return partition(subjectList, firstPos, lastPos - 1, splitValue, visualizeData, timeTick)
    else :
        exchange(subjectList, firstPos, lastPos - 1)
        visualizeData(subjectList, ['green' if x == subjectList[firstPos] or x == subjectList[lastPos] else 'blue' if x == splitValue else 'grey' for x in subjectList])
        time.sleep(timeTick)        
        return partition(subjectList, firstPos + 1, lastPos - 1, splitValue, visualizeData, timeTick)

def exchange(subjectList, firstPosToChange, secondPosToChange) :
    subjectList[firstPosToChange], subjectList[secondPosToChange] = subjectList[secondPosToChange], subjectList[firstPosToChange]
#L = [ ]

#L = [['Witcher 3', 150], ['Megaman', 100], ['Zero', 80], ['X', 50], ['Gogeta', 0], ['Bass', 50], ['Vegito', 1]]
#try :
    #while True :
        #name = input("Please enter the name: ")
        #number = int(input("Please enter the number: "))
        #L.append([name, number])
#except :
    #pass

#print(L)
#quickSort(L, 0, len(L))
#selectionSort(L)
#bubbleSort(L)
#heapSort(L)
#insertionSort(L, 0, len(L))
#mergeSort(L, 0, len(L))
#print(L)