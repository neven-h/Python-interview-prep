def dna_stra(s):
    t = []
    rev_s = s[::-1]
    for c in rev_s:
        if c=='G': c='C'
        elif c=='C': c='G'
        elif c=='A': c='T'
        else: c='A'
        t.append(c)
    result = ''.join(t)
    return result

