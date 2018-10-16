import csv

# f = file("traindata_joined.tsv")
# tsv = csv.reader(f, delimiter="\t")
# i = 0
# for line in tsv:
#     i=i+1
# print i

f1 = file("traindata1.tsv")
tsv1 = csv.reader(f1, delimiter='\t')

f2 = file("traindata2.tsv")
tsv2 = csv.reader(f2, delimiter='\t')

i = 1
data = []
for line in tsv1:
    # print(line)
    if i == 1:
        i = i + 1
        continue
    else:
        data.append(line)
    i = i+1

i = 1
for line in tsv2:
    if i == 1:
        i = i + 1
        continue
    else:
        data.append(line)
    i = i+1

w = open('traindata_joined.tsv', 'w')
writer = csv.writer(w, delimiter="\t")
writer.writerow(["id", "sentiment", "review"])
writer.writerows(data)
w.close()


#np.savetxt("traindata.tsv", data, delimiter="\t")


