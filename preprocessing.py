# %%
import pandas as pd
from scipy.spatial import Delaunay
import pickle
from math import pow,sqrt
from functools import lru_cache
import numpy as np
from joblib import Memory


# %%
# Get the sequence from the FASTA file


def get_sequences(lines):
    '''
    Returns all the sequences from the FASTA file
    '''
    sequences = []
    seq = ''

    for line in lines:
        if(line.startswith('>')):
            sequences.append(seq)
            seq = ''
        else:
            seq += line.rstrip()
    
    return sequences

#%%

def create_structure_vector(sequence,triangulation):
    '''
    Returns the structure vector
    '''
    lst = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 
    'S', 'T', 'V', 'W', 'Y']

    #create new dataframe with Amino acids as columns and rows
    distance_matrix = pd.DataFrame(0,columns= lst,index=lst)
    
    if(len(sequence) >= 988):
        sequence = sequence[0:988]
    else:
        sequence = sequence + 'X'*(988-len(sequence))

    #for each simplce compute the adjacency matrix
    for simplice in triangulation:
        for i, aa in enumerate(simplice):
            for j in range(i+1,4):
                if sequence[aa] != 'X' and sequence[simplice[j]] != 'X':

                    if(ord(sequence[aa])>=ord(sequence[simplice[j]])):
                        p1 = sequence[simplice[j]]
                        p2 = sequence[aa]
                    else:
                        p1 = sequence[aa]
                        p2 = sequence[simplice[j]]

                    #check if the cell is empty, add to list
                    distance_matrix.at[p1,p2] = distance_matrix.at[p1,p2] + 1
    
    structure_vector = []

    for i in range(20):
        structure_vector.extend(distance_matrix.iloc[i,i:].values.tolist())

    return structure_vector



# %%
if __name__ == '__main__' :
    with open('File5_gaps_and_unsolved_regions_removed_X_inserted_988aa.fasta') as f:
        lines = f.readlines()
    
    seq = get_sequences(lines)
    del seq[0]

    ca_frame = pd.read_excel('CA_atom_positions_for_988aa.xlsx')
    
    tri = Delaunay(ca_frame[['x','y','z']])
    structure_vector = [create_structure_vector(s,tri.simplices) for s in seq[0:10]]


# %%
