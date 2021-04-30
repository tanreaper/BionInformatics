#!/usr/bin/python

class PDB_File(object):
    """Class representing an instance of a PDB record."""

    def __init__(self):
        self.residues=[]

    def extract_model(file_name):
        """Extracts the atom lines from a PDB file corresponding to one model."""
        data_collection = []
        with open(file_name, "r") as fh:
            for line in fh:
                if line.startswith ('CRYST1'):
                    continue
                elif line.startswith('ATOM'):
                    data_collection.append(line)
                elif line.startswith('TER'):
                    break
        return data_collection

output_CA = open('CA_atoms_spike_open_conformation.txt', 'w')

# Extract all the atoms from the first model (chain A)
model_1 = PDB_File.extract_model('6zp7.pdb')

for i in model_1:
    line = i.rstrip('\n')
    atom_name_raw = i[12:16]
    atom_name = atom_name_raw.replace(' ','')
    if atom_name == 'CA':
        print (line)
        output_CA.write(line)
    

