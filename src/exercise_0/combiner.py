from operator import itemgetter

with open("exercise_0_results.txt") as file:

    word_counts = []

    for line in file:
        word, count = line.strip().split('\t')
        word_counts.append((word, int(count)))

    word_counts.sort(key=itemgetter(1))
    print("Top 5 most frequent words: " + str((word_counts[-5:][::-1])))
    print("Bottom 5 less frequent words: " + str(word_counts[0:5]))
