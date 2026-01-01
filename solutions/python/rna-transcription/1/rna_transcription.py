def to_rna(dna_strand):
    new_str = ""
    if dna_strand:
        for i in dna_strand:
            if i == "G":
                new_str += "C"
            elif i == "C":
                new_str += "G"
            elif i == "T":
                new_str += "A"
            elif i == "A":
                new_str += "U"
        
    return new_str