data="CAACCTTTCCGTCGCCTTTCTGGAGCAACTGGAGCAAGCCGCATGTTGTCGCCTTTGTCGCCTTTCAACCTTTCCGTCGCCTTTGCCGCATGTTCTGGAGCAACTGGAGCAAGGGGGGTGGCCGCATGTTGTCGCCTTTGTCGCCTTTCAACCTTTCCGTCGCCTTTGGGGGGTGGTCGCCTTTGCCGCATGTTGTCGCCTTTCTGGAGCAAGTCGCCTTTGTCGCCTTTCTGGAGCAACTGGAGCAACAACCTTTCCGTCGCCTTTCTGGAGCAACAACCTTTCCCAACCTTTCCGTCGCCTTTGTCGCCTTTGCCGCATGTTGGGGGGTGCAACCTTTCCGCCGCATGTTGGGGGGTGCAACCTTTCCGCCGCATGTTGGGGGGTGCTGGAGCAACTGGAGCAAGGGGGGTGGCCGCATGTTGGGGGGTGGCCGCATGTTCAACCTTTCCCAACCTTTCCGCCGCATGTTGCCGCATGTTCTGGAGCAACTGGAGCAAGGGGGGTGCAACCTTTCCCTGGAGCAACTGGAGCAAGTCGCCTTTGGGGGGTGGCCGCATGTTGGGGGGTGGGGGGGTGCTGGAGCAAGTCGCCTTTCTGGAGCAAGGGGGGTGGCCGCATGTTGCCGCATGTTCAACCTTTCCGTCGCCTTTCTGGAGCAAGCCGCATGTTGCCGCATGTTGGGGGGTGCAACCTTTCCCAACCTTTCCCTGGAGCAAGCCGCATGTTGGGGGGTGGTCGCCTTTCTGGAGCAAGCCGCATGTTGGGGGGTGCAACCTTTCCGTCGCCTTTGTCGCCTTTGTCGCCTTTCAACCTTTCCCTGGAGCAAGCCGCATGTTCTGGAGCAAGCCGCATGTTGGGGGGTGCAACCTTTCCGTCGCCTTTGGGGGGTGGTCGCCTTTCTGGAGCAAGCCGCATGTTCAACCTTTCCCTGGAGCAAGGGGGGTGGGGGGGTG"

import operator

def frequentkmers(data, kmer):
    seen = {}
    for i in range(0, len(data) - kmer):
        if (data[i:i+kmer] in seen):
            seen[data[i:i+kmer]] += 1
        else:
            seen[data[i:i+kmer]] = 1
    f = 0
    frequents = []
    for s in seen:
        if (seen[s] > f):
            frequents = [s]
            f = seen[s]
        elif (seen[s] == f):
            frequents.extend([s])

    for d in frequents:
        print d

frequentkmers(data, 11)
