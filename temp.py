import csv 
with open('word_set.csv','w',newline='') as csvfile:
    tempwriter = csv.writer(csvfile)
    tempwriter.writerow(["highway"])
    tempwriter.writerow(['transport'])
    tempwriter.writerow(['pipeline'])