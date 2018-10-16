import csv

f = file("labeledTrainData.tsv")
tsv = csv.reader(f, delimiter='\t')

i=1
data = []
for line in tsv:
    print(line)
    if i == 1:
        i = i + 1
        continue
    else:
        id = line[0].split("_")
        print line[2]
        id.append(line[2])
        data.append(id)
    #print(id)
    i=i+1

w = open('traindata.tsv', 'w')
writer = csv.writer(w, delimiter="\t")
writer.writerow(["id", "sentiment", "review"])
writer.writerows(data)
w.close()


#np.savetxt("traindata.tsv", data, delimiter="\t")


