import csv

data = []
def dataAssigner(key:int):
    diction = {}
    with open('activity.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    for index in data[1:-1]:
        if index[key] not in diction:
            diction[index[key]] = [index[0]]
        else:
            diction[index[key]].append(index[0])
    return diction