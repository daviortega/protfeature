import bioinfo_dicts as bd

def n_neg(seq):
    """Number of negative residues a protein sequence"""

    # Convert sequence to upper case
    seq = seq.upper()

    # Check for a valid sequence
    for aa in seq:
        if aa not in bd.aa.keys():
            raise RuntimeError(aa + ' is not a valid amino acid.')

    # Count E's and D's, since these are the negative residues
    return seq.count('E') + seq.count('D')
