#!/usr/bin/python

# No. 1 - Download coronavirus complete genomes (https://www.viprbrc.org) n = 65K. Select to download coding sequences (CDS).

# No. 2 - Parse fasta file, and extract only spike coding sequences

def read_fasta(fp):
        name, seq = None, []
        for line in fp:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))

output_spike = open('Spike_Human_Africa.txt', 'w')

with open('Human_Africa.fasta') as fp: # in this file, we have all the genomes, splitted by coding sequences
    for name, seq in read_fasta(fp):
        #if "spike" in name:
                #output_spike.write(name)
                #output_spike.write("\n")
                #output_spike.write(seq)
                #output_spike.write("\n")
        #if "Protein Name:S" in name:  
                #output_spike.write(name)
                #output_spike.write("\n")
                #output_spike.write(seq)
                #output_spike.write("\n") 
        if "Gene Symbol:S" in name:  
                output_spike.write(name)
                output_spike.write("\n")
                output_spike.write(seq)
                output_spike.write("\n")

output_spike.close()


##################################################################################
# Determine the number of spike sequences obtained

spikes = [line.rstrip('\n') for line in open("Spike_Human_Africa.txt")]

count = 0

for line in spikes:
        if line[0] == ">":
                count += 1

print (count)
                

