import sortmethods.bubblesort
import sortmethods.heapsort
import sortmethods.quicksort
import pandas as pd
import time
import sys

sys.setrecursionlimit(200000)  # Increase the limit

#read the csv data into a panda dataframe
df = pd.read_csv('data/Air_Quality_NYC.csv')

#build a matrix of arrays for sorting
value = df['Data Value'].tolist()
type = df['Name'].tolist()
location = df['Geo Place Name'].tolist()
timeperiod = df['Time Period'].tolist()
matrix = [value, type, location, timeperiod]

size = len(value)
print("-- Heap sort of NYC Air Quality Data of Size %s ---" % size)
start_time = time.time()
#sorted(matrix)
#sortmethods.quicksort.quickSort(value, 0, size - 1, matrix)
#sortmethods.bubblesort.bubble_sort(value, matrix)
sortmethods.heapsort.heapSort(value, matrix)
print("-- Completed in %s seconds --" % round((time.time() - start_time), 4))

#export sorted data into a new csv file
sorted_df = pd.DataFrame({'Data Value': value, 'Type': type, 'Location': location, 'Time Period': timeperiod})
sorted_df.to_csv('data_sorted/Air_Quality_NYC.csv', index=True)

