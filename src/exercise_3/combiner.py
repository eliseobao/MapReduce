import json

with open("exercise_3_results.txt") as file:
    results = {}

    for line in file:
        wine, attribute, mean_value = line.strip().split('\t')

        if wine in results:
            results[wine][attribute] = mean_value
        else:
            results[wine] = {}
            results[wine][attribute] = mean_value

    print(json.dumps(results, sort_keys=True, indent=4))
