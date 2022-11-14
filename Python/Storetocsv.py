# importing csv module
import csv
import sys
 
# csv file name
filename = "university_records.csv"
 
# initializing the titles and rows list
fields =        ['Name', 'Branch', 'Year', 'CGPA']
rows   =        [   ['Nikhil', 'COE', '2', '9.0'],
                    ['Sanchit', 'COE', '2', '9.1']]


# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)
 
    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
 
    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

        #  sys.exit()
