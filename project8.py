import itertools

def TotalDistance(pattern, DNA):
    distance = 0
    for dna in DNA:
        hamming = len(dna)
        for i in range(len(dna)-len(pattern)+1):
            subseq = dna[i:i+len(pattern)]
            hamming_temp = sum(1 for a, b in zip(subseq, pattern) if a != b)
            if hamming_temp < hamming:
                hamming = hamming_temp
        distance += hamming
    return distance

def combination_generator(possibilities, strlen):
    yield from itertools.product(*([possibilities] * strlen))

def MedianStringSearch(DNA, L):
    bestWord = 'A'*L
    bestDistance = float('inf')
    for i in combination_generator('ACGT', L):
        pattern = ''.join(i)
        distance = TotalDistance(pattern, DNA)
        if distance < bestDistance:
            bestDistance = distance
            bestWord = pattern
    return bestWord

DNA = ['ATCAGTCTTA', 'AGTCTAATTC', 'CCGTCAGTCT', 'TTTCAGTCTT']
t = 5
n = 10
L = 5

pattern = MedianStringSearch(DNA, L)
print(pattern)