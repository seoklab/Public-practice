#!/usr/bin/env python3
from glob import glob

chain_rename = {'A':'L', 'B':'H', 'C':'A'}


files = glob('*.pdb')
for i in files:
    f = open(i).readlines()
    new_line = []
    for line in f:
        if line.startswith('ATOM'):
            chain = line[21]
            new_line.append(f'{line[:21]}{chain_rename[chain]}{line[22:]}')
        else:
            new_line.append(line)

    f_out = open(i, 'w')
    f_out.writelines(new_line)
    f_out.close()


