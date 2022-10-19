from operator import itemgetter

with open("exercise_1_results.txt") as file:
    lines = []
    for line in file:
        town, temp = line.strip().split('\t', 1)
        lines.append((town, float(temp)))
    lines = [tup for tup in lines if tup[1] != 0]
    lines.sort(key=itemgetter(1))

    print('Hottest temperature: ' + str(lines[-1][1]) + ' in ' + lines[-1][0])
    print('Coldest temperature: ' + str(lines[0][1]) + ' in ' + lines[0][0])

