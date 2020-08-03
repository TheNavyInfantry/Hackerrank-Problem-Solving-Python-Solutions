def breakingRecords(scores):
    bestCase = scores[0]
    worstCase = scores[0]
    breaking_bestRecord = 0
    breaking_worstRecord = 0

    for score in scores:
        if score > bestCase:
            bestCase = score
            breaking_bestRecord += 1

        elif score < worstCase:
            worstCase = score
            breaking_worstRecord += 1

    return breaking_bestRecord,breaking_worstRecord