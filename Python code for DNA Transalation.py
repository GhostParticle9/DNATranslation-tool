#firtsly we'll write a function which will read our text file and remove all the \n and \r because when'll we 
#upload we can get new lines in between while reading


def read_seq(inputfile):                #let's define a function read_seq
    with open(inputfile,'r') as f:      #we'll open the file and 
        seq=f.read()                    # read it in this line
    seq=seq.replace("\n","")            #replacing the unwanted values
    seq=seq.replace("\r","")
    return seq 
  
  
  
#Now we must have some sort of dictionary which we can use which contains all the translation of the triplets and
# a code which can provide us a translation.

def translation(seq):
  #Firstly i've created a dictionary which correspond to all the the amino acids formed by the triplets from te DNA code.
    table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',                                     
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',}
    
    #writing a code which will in the end give us the translation
    
    protein=""
    #checking for divisible by 3 because there must be a triplet to proceed
    if len(seq) % 3 == 0:            
        for i in range(0,len(seq),3):             #looping over the sequence from 0 to len with spaces of 3
            codon=seq[i:i+3]                      #adding the values to the protien adn incrementing by 3
            protein+=table[codon]
    return protein

  
#now our code is ready to use but we'll only have to slice the dna code to a value divisible by 3
# ypu can get that information from the NCBI in which range you need to slice the dna wihile translating the code 
#p.s check CDS on the ncbi nucleotide page.

dna=read_seq("dna.txt")      #we're reading the DNA file 
translation(dna[20:938])     #it will give you the transaltion
  
