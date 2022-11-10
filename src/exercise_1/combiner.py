from operator import itemgetter

with open("exercise_1_results.txt") as file:
    results = []

    for line in file:
        town, temp = line.strip().split('\t', 1)
        results.append((town, float(temp)))

    lines = [tup for tup in results if tup[1] != 0]

    hottest_temp, coldest_temp = max(results, key=itemgetter(1))[1], min(results, key=itemgetter(1))[1]
    hottest_cities = [city[0] for city in results if hottest_temp in city]
    coldest_cities = [city[0] for city in results if coldest_temp in city]

    print('Hottest temperature: ' + str(hottest_temp) + ' in ' + str(hottest_cities))
    print('Coldest temperature: ' + str(coldest_temp) + ' in ' + str(coldest_cities))

