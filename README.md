# sortingAlgoVisualizer
A sorting algorithms visualizer using tkinter in Python:
- Generate random bar charts (max 25), each has length varies based on the value of each bar (the value of each bar is a game's review score taken from the data provided in the csv file created and provided from the "Games' Data Scraping & Download" project. The value will be within the min value and the max value and taken from based on player choice).
- Implement famous algorithms: Selection Sort, Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort, and use them to sort the chart.
- Visualize the working proccess of each algorithm selected on the screen (user could adjust the speed based on their preference (from 0,2s to 2s) to watch it slower or faster).
- Once it has all sorted, turn all the bar color from red to green.

# Things to do :
- Improve the visualization proccess for Heap Sort (the algorithm already works).
- (Completed) Changing from randomly generate random numbers to randomly pick the games from the video games list that was supplied before hand as .csv file and sorted them based on review score.

# How to run:
- run the visualize.exe file, pick the algorithm you want to use, how many bars you wanna have and their value range. Afterwards, click the generate button to generate the data for sorting. Finally, click the Start button to start the visualization process
# Tool use:
- Python
- tkinter
- random library
- time library
- pyinstaller convert it into an .exe file
