import csv

f = file("labeledtestData.tsv")
tsv = csv.reader(f, delimiter='\t')

i=1
data = []
for line in tsv:
    # print(line)
    if i == 1:
        i = i + 1
        continue
    else:
        id = line[0].split("_")
        # print line[1]
        id.append(line[1])
        data.append(id)
    # print(id)
    i=i+1

w = open('traindata2.tsv', 'w')
writer = csv.writer(w, delimiter="\t")
writer.writerow(["id", "sentiment", "review"])
writer.writerows(data)
w.close()


#np.savetxt("traindata.tsv", data, delimiter="\t")


