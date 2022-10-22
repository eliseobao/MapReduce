from operator import itemgetter

with open("exercise_2_results.txt") as file:
    urls, users = [], []

    for line in file:
        item, count = line.strip().split('\t')
        if any(s in item for s in ["//", "%", ":", "."]):
            urls.append((item, int(count)))
        else:
            users.append((item, int(count)))

    urls.sort(key=itemgetter(1)), users.sort(key=itemgetter(1))

    print("Most visited URL is " + urls[-1][0] + " (" + str(urls[-1][1]) + " visits)")
    print("User with most '.ps' files visited is " + users[-1][0] + ' (' + str(users[-1][1]) + " visits)")
