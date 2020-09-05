def countingValleys(n, topography):
    seaLevel = 0
    valleyCount = 0

    for step in topography:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1

        if step == 'U' and seaLevel == 0:
            valleyCount += 1

    return valleyCount