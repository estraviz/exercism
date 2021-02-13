from textwrap import wrap

codons = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
}


def proteins(strand):
    proteins_list = []
    for codon in wrap(strand, 3):
        if codons.get(codon) == 'STOP':
            return proteins_list
        else:
            proteins_list.append(codons.get(codon))
    return proteins_list
