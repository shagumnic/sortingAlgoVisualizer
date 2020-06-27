from tkinter import *
from tkinter import ttk
import random
from sortingAlgo import *

root = Tk()
root.title('Video Game Review Sorting Algo Visual')
root.maxsize(900,600)
root.config(bg='black')

selected_alg = StringVar()
game_data = []
def visualizeData(game_data, colorArray) :
    canvas.delete('all')
    c_height = 380
    c_width = 600
    x_width = c_width / (len(game_data) + 1)
    offset = 30 / (len(game_data) + 1)
    spacing = 10
    maxReviewPercent = game_data[0][1]
    for index in range(1, len(game_data)) :
        if maxReviewPercent < game_data[index][1] :
            maxReviewPercent = game_data[index][1]
    normalizedGameData = [ i[1] / maxReviewPercent for i in game_data]
    for i, height in enumerate(normalizedGameData) :
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        
        x1 = (i+1) * x_width + offset
        y1 = c_height
        
        game_bar = canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        game_review_percent = canvas.create_text(x0+2, y0, anchor=SW, text=str(game_data[i][1]))
        #game_name = canvas.create_text((x1+x0)/2, c_height - 50, text="The Witcher 3" + ": " + str(game_data[i][1]) + "%", angle = 90)
        
    root.update_idletasks()
    
def Generate() :
    global game_data
    
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())
    
    game_data = []
    for index in range(size):
        game_data.append([index, random.randrange(minVal, maxVal + 1)])
    
    visualizeData(game_data, ['red' for x in range(len(game_data))])
    
def StartAlgorithm() :
    global game_data
    if algMenu.get() == "Bubble Sort" :
        bubbleSort(game_data, visualizeData, speedScale.get())
    if algMenu.get() == "Quick Sort" :
        quickSort(game_data, 0, len(game_data), visualizeData, speedScale.get())
        visualizeData(game_data, ['green' for x in range(len(game_data))])
    if algMenu.get() == 'Insertion Sort' :
        insertionSort(game_data, 0, len(game_data), visualizeData, speedScale.get())
    if algMenu.get() == 'Selection Sort' :
        selectionSort(game_data, visualizeData, speedScale.get())
    if algMenu.get() == 'Merge Sort' :
        mergeSort(game_data, 0, len(game_data), visualizeData, speedScale.get())
        visualizeData(game_data, ['green' for x in range(len(game_data))])
    if algMenu.get() == 'Heap Sort' :
        heapSort(game_data, visualizeData, speedScale.get())
#frame / base layout
UI_frame = Frame(root, width= 600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Insertion Sort', 'Selection Sort', 'Bubble Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()