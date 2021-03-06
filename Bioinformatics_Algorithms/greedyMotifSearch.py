def stringToArr(s):
    out = []
    buff = []
    for c in s:
        if c == '\n':
            out.append(''.join(buff))
            buff = []
        else:
            buff.append(c)
    else:
        if buff:
           out.append(''.join(buff))
    return out

def greedyMotifSearch(dna, k, t):
    dnaArray = stringToArr(dna)
    bestMotifs = []
    for d in dnaArray:
        bestMotifs.append(d[0:k])
    for i in range(0, len(dnaArray[0]) - k + 1):
        motif = [dnaArray[0][ i : i + k ]]
        for j in range(1, t):
            profile = generateProfile(motif)
            motifi = profileMostProbable(profile, dnaArray[j], k)
            motif.append(motifi)
        if (score(motif) < score(bestMotifs)):
            bestMotifs = motif
    return bestMotifs

def generateProfile(motifs):
    k = len(motifs[0])
    profile = {'A': [0.0000] * k, 'C': [0.0000] * k, 'G': [0.0000] * k, 'T': [0.0000] * k}
    div = float(len(motifs))
    for i in range(k):
        for motif in motifs:
            profile[motif[i]][i] += 1
        for key in profile:
            profile[key][i] /= div
    return profile

def profileMostProbable(profile, dna, k):
    best_pattern = ""
    best_probability = 0.0000
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        # print kmer, calculate_probablity(kmer)
        if calcProb(profile, kmer) > best_probability:
            best_pattern = kmer
            best_probability = calcProb(profile, kmer)
    if (best_pattern == ""):
        best_pattern = dna[0:k]
    return best_pattern

def calcProb(profile, kmer):
    p = 1.0000;
    for i in range(len(kmer)):
        p = p * profile[kmer[i]][i]
    return p

def score(motifs):
    con = consensus(motifs)
    score = 0
    for motif in motifs:
        score = score + hamming(con, motif)
    return score

def consensus(motifs):
    consensus = ""
    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(len(motifs[0])):
        count['A'] = 0
        count['C'] = 0
        count['G'] = 0
        count['T'] = 0
        for motif in motifs:
            count[motif[i]] = count[motif[i]] + 1
        maxCount = 0
        letter = ""
        for d, c in count.items():
            if (maxCount < c):
                letter = d
                maxCount = c
        consensus = consensus + letter
    return consensus

def hamming(s1, s2):
    distance = 0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            distance = distance + 1
    return distance

s="""CTCAAGTCTGTAGACACACCAACCCGGCTCTCTTATAGATTTTGCATCAGCCGGTAAGCACTAGCGCTACAGACCGTCAAGGCCCAGCCAAGATCCATGTTTATCAGCGTTTAGAAGATTGGAGAGGTGTAACATTCACAGGAGTAGAGCCGTCTA
CTCTGCTAGGAAATTTTGTTATGAACCGTCATGGCCATCACACTTTAAGCGTGTCCTCTTTTTAAGGATGTCAACATAACATAATATTGCACTTCATCGCTTAATGTGTGAAGCAATACCCTGGTGCGCAAAGTCGGGAGCGAGCTCCATCCACGA
CTGAACGATGCGTCCGCCGACTTCGGATCGGAATGAGCCAGAGGAGGCGTAATGTGAACATCCGCTAAGTGCTACGCAGCAAGACCCTGCTGATCGTATCTAGTATCCGTGTCGAACGGAACTGACAAGCCCAATATCTTTTCGAGCCACTCACCG
CTACTTTCTCTGACAGCTACTATACGCGCGCAGCACATATGGGGTTTTACAGCCAAGCCCTGTGCTCTAGCCTTGCGTCGTATGCGATTGTGTGATCCGCAGAAAGGGTTGTTCACTCAGGCATCACGGCTTATCGGGCTGACCTTGCTTTTGCAT
GAGGGACGACTGACTGTCAGGTCCGCCGTAGATAGAGCTACCAACTGCGTACACTCATCTATATTTGGTTCCTACACGTTAAAATTAGGTATCTGTCAGTATTGAAAAAATTCCGGAAACGATTCGCTACTTCCTCGACTAGGAAACGGTATAGCG
ACATTTCATCCGTACCGTGGCAAAGTGAGCTCGGGCCACAGCTCGACTCTGCTGTGGCGTACCAAGTTGCCTATTGACTATCGGACGGCCATGTCCAGCCCTTAAAGACGAGGAGATCCCATGGTCGCAGTTTAAGTAGTGACCCGTCATCCGAGT
CTGATACGAGTTCTTTTCTCCATTGTATCTTTGGAAGTCAGGAGAAATTAGTTGTTGGGGCTCGTTGCCCTTCCAAACGTGGGTGACGAGCGTATCGATGTTCATAGAAATATGACGAGGGAGCAAGACGATCTAATAGGGCGAACCGCCAAGTCC
AATTCAAAGAAAAACTTCTTCTGTATGAACCTGATAAAATAGAAACTAACTGGCACGCCCGTGGACACCTACAGCTTCCCTTGGAACGACTTATCCGACTTATAACGAAATACATAACCTAATATGAAGTACACTTGATGTTGCGAAACCTTTGAT
GGATTGTTAACAGTCACAAGAGTGCCCGTGGTGGAAACAGTCAAGGCCTCCGTGCATGTTTGCCGTATGATGCGTTCGCTGCCCCAGTAACGCTCAATTAACGGGAAGACGATGTTTTTATTCGTTTGTTCTTTTGCAAATATGTGAGCATTTGTA
AAACTTCTATCGCGGCGATCTTGATCCTTTCAACCGCCTAAATAAGGTGAGGGGAAATATAGGATAACGTACCCGTATGAGGCTTTGACGTTAGTACGTGACTGCCAGGTGGTCGACTTCACGGGCAGGTCCTCAATTTACATCTGAAACAAGTTC
ACGGCCAGGACCACGTGATGGTCCATCTGTTCCACGCGCAGCAATGAGAAATCTCACGCCACACATCCATGCCCGGATAACTTCCGCGCGGCCTTTTCTCAAGTAGAGTTTGGAACTGAAACATTCATGCCTGTCGCAGTAGGTATTGCGATAGAT
TCGCGTACGCGACGCCAGCTTACAAGAGCCTCAAGTACCGGCGTTTGACTGGTCGCGATCGGCCCTCTCGTTAGCTATCCAGCGACTTCAGTTGTTACAGGCACGCCCCCGTCATCATTTCCCGCCATTACGGGGGCCCATGTTTCGACGCGGCAG
CTTAGATCGTTCTTTAGGAGTTCCTTGGGTCATGTAACAGTCTGAGACTTAAATTCCACCCACGGGCTTTTGGCCTTCAGTGTTAGCCAAATTAGGGGTCCGCGGGTTTCTTTAAGCTGTGTAATAAGGGGCTTTCCTCGCAACACAGTCAGGTCC
AGTAAGCTTCTATCTCAAGCGTAATTACTTCAGTCGCCCCCGTTTTTAGCTTCTGCGCTTATAAGCTTGATGTTAGAGTAAGCAGCCGTACAAAGCTCAACTGACTCCCATGAAGCGGATTATGCCTACCCAACCGGCATGCCCGGCACTCCCTAC
TTTATTAAATAGATGGACAACTTGGTAATCTGCTGTAGAGCCGAACTAACAGGCAGGCCCTAAGCTCGGAATTGTAAATACAATGTCGGGACGGTAGTTACGCCCTCGTCTTGATTATTTAAGTGCGCAACAAACTGGTCGAGCCGACCCTGTGGA
CCGATTCGTACGAGGTCAGACTGTACTGCCACGGCCATAGGCTAGTATACTACGGTAAAGGCGCTGGTCTGGGGCGAACGGTCAGCAAGCGTAACTGAGAGAAGCTACAGCTGCGTCCTAGCAATGCTCTTTAGCCAGTAAATACCATTTGGAATT
TACAGGACCCGCAAGCAGCGCATTAATGTACCTAGCGCTGCGTTCTATCATGAAAAGGTTCAAACCATTCGTCCACGTCCCCGGCATAAGCAGCCAACAGGCACGGCCGTTTTGACATTTAGCGGGCTGTCCCTAACACAATTATAAATCTGGATA
CCTTACTGATGGAGCAACTTCCACCTGAGAAGCAAAGCCCGGCCCTAATTGACCCTGGGTACTGACAGGACCTCGCCAGCGTCGACCCCTTTAGCGGTCCACTCATTTAAGGCTGTTCACGCCCGCCGCTCAGCCATAGTAGGTAGCAAGGGGTAT
GACCTAGGCAGATACGTCCCTTCGACCGTCATGTCCGAAACGGATATACGTCTCACGCACTTTGTAACTCCGAGCCATTCTATCACGAGATGTTTTCAAGCTTCTGCGAACTTTATGACACCCCCCGACACAAAAGGGTACATGCATGCTCTTACA
GGTGGGATAGTCCCTAACCTTTGGAATGTGTTACACAATATCCGATAGCCCATACTTGAGTGAATTTTTTGAACTTTGTGCGAGCCGCCAAAGAGCCGTCGGAATCGGACCGGCATGCCCGATATCATTATATCGGACAGATCTTCCGCACGATCT
TTCTACTTACGGACACTAATATCCTCACCATTCTCGCGGGTTATCATACAGGGACAATCCCAGATTGTTTACGGTATAGTAATGAGTGGCTGCTGTTCAGGAGCCACAGCTGGCAGCGGTACGGACATGACCAGCGCTTTGACGAACGGTCAACAG
GCGGAAGCGACCCTCTTTGACGTTATTACGCTTGATACTGTCAGGCCCTAGGGACAGCCAATATACCCCAGTTCATGAGTGACTTGCTCATACCGCTGCCCACTCAAATAGGGCACTCCCGGAAAGGCTCGAGGGAGTACACCACTTGTTGACGTC
AACCGCTCAATAACAGACACGTCCGGGCCCATTACATGAGGTCCTTTTAGAATGTTAGCTCTGATGTACATGGGCAACTTAACTCACCCCCCCGGCTGGTACAAGATATATAGGCCCCACGGTAGTTTCGTTAAGGTAGCGCGAGTGAGTTGTTTC
GAACGCCATTAACTCTTGGCGGGTACTGGCATGTCCAACGGTATGCGGTGTTTATATTCCTGAAAGATTAGCCGAATTCCAGTACCAATGGTGGACTTGTTCTTCATCTGGGGAGCCCGAGAAGTCTGATGAGGAGTTACCGGAGGCCCATAGATC
ATGTGTTAGTTACAGAATCTCTTGTAGTGATGATGCTGAGGTAACTTGGCCTTCGGTGCAACTGGCAAGGCCGATCAAAGGCTGTTTTGCCCCTTGTAAGCTGAGGCTCGGATTCGTCAACTTAGGCTTGACACTGGATGCCTCTTATGTAGCTAC
"""

s2="""GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG"""

print(greedyMotifSearch(s, 12, 25))

# print(greedyMotifSearch(s2, 3, 5))
