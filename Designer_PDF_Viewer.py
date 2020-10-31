import string


def designerPdfViewer(h, word):
    tallest = 0
    alphabets = list(string.ascii_lowercase)
    for m in word:
        for n in range(len(h)):
            if m == alphabets[n]:
                if h[n] > tallest:
                    tallest = h[n]
                    break
    return tallest * len(word)


print(designerPdfViewer([1, 2, 3], 'abc'))  # TEST CASE
