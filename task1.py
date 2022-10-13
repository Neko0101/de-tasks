import csv
with open('task.csv', 'r') as file:
    reader = csv.reader(file)
    file_out = open('task1.csv', 'w')
    writer = csv.writer(file_out)
    writer.writerow(("year","region","value"))
    next(reader, None)
    for row in reader:
        row[0]=row[0]+'-01-01'
        writer.writerow(row)
        #print(row)
