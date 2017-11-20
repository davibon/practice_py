def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    dnaCount = 0
    for char in dna:
        if char in nucleotide:
            dnaCount = dnaCount + 1

    return dnaCount
    

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):

    """ (str) -> bool

    Return True if DNA sequence is vaild

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATcGGC')
    False
    >>> is_valid_sequence('ATJGGC')
    False

    """
    if dna == '':
        return True
    else:
        for char in dna:
            if not char in 'ATCG':
                return False

    return True

def insert_sequence(dna1,dna2,dna1_index):
    """ (str, str, int) -> str

    Return DNA sequence obtained by inserting
    the second DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    
    
    """
    return dna1[:dna1_index] + dna2 + dna1[dna1_index:]


def get_complement(dna):
    """(str) -> str
    The first parameter is a nucleotide ('A', 'T', 'C' or 'G').
    Return the nucleotide's complement. 

    >>> get_complement('CCGGAA')
    'GGCCTT'
    >>> get_complement('ACTG')
    'TGAC'

    """
    dna_complement = ''

    if is_valid_sequence(dna):
        for char in dna:
            if char == 'A':
                dna_complement = dna_complement + 'T'
            elif char == 'T':
                dna_complement = dna_complement + 'A'
            elif char == 'C':
                dna_complement = dna_complement + 'G'
            elif char == 'G':
                dna_complement = dna_complement + 'C'

    return dna_complement

def get_complementary_sequence(dna):
    """(str) -> str
    Return the DNA sequence that
    is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CGATCGAT')
    'GCTAGCTA'
    """
    dna_complementary = ''
    
    if is_valid_sequence(dna):       
        for char in dna:
            """char = get_complement(char)"""
            dna_complementary = dna_complementary + get_complement(char)

    return dna_complementary
