#Reading
import csv

thisdict = {
"dec": "12-01",
"jan": "01-01",
"feb": "02-01",
"mar": "03-01",
"apr": "04-01",
"may": "05-01",
"jun": "06-01",
"jul": "07-01",
"avg": "08-01",
"sep": "09-01",
"okt": "10-01",
"noi": "11-01"
}
with open('HomeWork.csv', 'r') as file:
    reader = csv.reader(file)
    file_out = open('HomeWork1.csv', 'w')
    writer = csv.writer(file_out)
    writer.writerow(("year","region","value"))
    next(reader, None)
    for row  in reader:
        #print(thisdict["dec"])
        print(row[0][5:8])
        print(row[0][0:-3])

        row[0]=row[0][0:-3]+thisdict[row[0][5:8]]
        writer.writerow(row)
        #print(row[0][5:8])
        #print(thisdict[row[0][5:8]])


''''
with open('HomeWork.csv', 'r') as file:

    reader = csv.reader(file)
    file_out = open('HomeWork1.csv', 'w')
    writer = csv.writer(file_out)
    writer.writerow(("year","region","value"))
    #writer = csv.writer(file)
    next(reader, None)
    for row in reader:
        if  "feb" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-02-01'
        elif "mar" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-03-01'
        elif "apr" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-04-01'
        elif "may" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-05-01'
        elif "jun" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-06-01'
        elif "jul" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-07-01'
        elif "aug" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-08-01'
        elif "sep" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-09-01'
        elif "oct" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-10-01'
        elif "nov" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-11-01'
        elif "dec" in row[0]  :
            s= row[0]
            row[0] = s[:4] +'-12-01'

        writer.writerow(row)
        print(row)
'''
