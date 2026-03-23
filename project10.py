import numpy as np
from collections import Counter
import random
from math import log2


class RawDNA:
    def __init__(self, file_name):
        self.file_name = file_name
        self.t, self.n, self.length, self.sequence = 0, 0, 0, []
        self.readDnaFile()
        # self.seqs=self.generate_random_sequences()
        self.out = self.getConsensusString(self.branchAndBoundMedianString()).upper()

    def readDnaFile(self):
        with open(self.file_name, 'r') as file:
            self.t, self.n, self.L = map(int, file.readline().split())
            self.sequence = [file.readline().strip() for _ in range(self.t)]

    def generate_random_sequences(self):
        nucleotides = ['A', 'C', 'G', 'T']
        sequence_arr = [''.join(random.choices(nucleotides, k=self.n)) for _ in range(self.t)]
        return sequence_arr

    def hamming_distance(self, s1, s2):
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))

    def branchAndBoundMedianString(self):
        best_score = float('inf')
        best_alignment = None

        def backTrack(pattern, score, indices):
            nonlocal best_score, best_alignment
            if len(pattern) == self.length:
                if score < best_score:
                    best_score = score
                    best_alignment = (pattern, indices)
            else:
                for nucleotide in ['A', 'C', 'G', 'T']:
                    new_pattern = pattern + nucleotide
                    new_score = sum(
                        self.hamming_distance(new_pattern, sequence[i:i + self.length]) for sequence, i in
                        zip(self.sequance, indices))
                    if new_score < best_score:
                        new_indices = [i + 1 for i in indices]
                        backTrack(new_pattern, new_score, new_indices)

        for i in range(len(self.sequance[0]) - self.length + 1):
            pattern = self.sequance[0][i:i + self.length]
            score = sum(self.hamming_distance(pattern, sequence[i:i + self.length]) for sequence in self.sequance[1:])
            indices = [i + 1] + [1] * (self.t - 1)
            backTrack(pattern, score, indices)

        return best_alignment

    def getConsensusString(self, alignment):
        return alignment[0]

    def printFunc(self):
        print("Multiple Alignment:")
        for i, s in enumerate(self.sequence):
            print(s[self.branchAndBoundMedianString()[1][i]:
                    self.branchAndBoundMedianString()[1][i] + self.length])
        print("Starting Indices: ", self.branchAndBoundMedianString()[1])
        print("Consensus String: ", self.out)


class Pssmd:
    def __init__(self, file_name):
        self.file_name = file_name
        self.sequence = input('enter your sequance')
        self.num_seq, lenseq, self.seqs = 0, 0, []
        self.read_data()
        self.printseqs = self.print_seqs()
        self.printpss = self.print_pssm(self.calc_pssm())
        print(self.calc_prob(self.sequence, self.calc_pssm()))

    def read_data(self):
        with open(self.file_name, 'r') as file:
            self.num_seq, self.lenseq = map(int, file.readline().split())
            self.seqs = [file.readline().strip() for _ in range(self.num_seq)]

    def print_seqs(self):
        print("Aligned Sequences:")
        for seq in self.seqs:
            print(seq)

    def calc_pssm(self):
        t = len(self.seqs)
        n = len(self.seqs[0])
        pssm_matrix = [[0] * 4 for _ in range(n)]
        for i in range(n):
            column = [sequence[i] for sequence in self.seqs]
            for j in range(4):
                count = column.count('ACGT'[j])
                pssm_matrix[i][j] = count / t
        for index, row in enumerate(list(zip(*pssm_matrix))):
            pssm_matrix[index] = [log2(val / ((sum(row) * t) / t * n)) if val != 0 else 0 for val in row]

        return pssm_matrix

    def print_pssm(self, pssm):
        print("\nPSSM Matrix:")
        for row in pssm:
            print(' '.join(f'{value:.2f}' for value in row))

    def calc_prob(self, pssm):
        prob = 0
        self.sequence = self.sequence.upper()
        for i, nuc in enumerate(self.sequence):
            if nuc in 'ACGT':
                index = 'ACGT'.index(nuc)
                prob += pssm[index][i]
        print(round(prob, 2))

if __name__ == 'main':
    RawDNA('compBioAssignment/rawDNA.txt').printFunc()
    Pssmd('compBioAssignment/PSSMData.txt')
