
import sys

# usage
# cif2vasp.py [prefix]


# get command line variables
args = sys.argv


#
filename=args[1]

from ase import io
atoms = io.read('POSCAR')
atoms.write(filename+'.cif', format = 'cif')
