from operator import itemgetter

with open("exercise_2_results.txt") as file:
    urls, users = [], []

    for line in file:
        item, count = line.strip().split('\t')

        if item.startswith("url-"):
            urls.append((item[4:], int(count)))
        else:
            users.append((item[4:], int(count)))

    most_visits, most_ps = max(urls, key=itemgetter(1))[1], max(users, key=itemgetter(1))[1]
    most_visited_urls = [url[0] for url in urls if most_visits in url]
    users_most_ps = [user[0] for user in users if most_ps in user]

    print("Most visited URL(s) is/are " + str(most_visited_urls) + " (" + str(most_visits) + " visits)")
    print("User(s) with most '.ps' files visited is/are " + str(users_most_ps) + ' (' + str(most_ps) + " visits)")
