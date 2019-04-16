from Molecule.containers import Molecule
from Molecule.periodictable import *

m1 = Molecule()
m2 = Molecule()
m1.add_atom(N(), 1)
m1.add_atom(N(), 2)
m1.add_atom(N(), 3)
m1.add_atom(Br(), 4)
m1.add_atom(O(), 8)
m1.add_atom(O(), 10)
m1.add_bond(1, 2, 1)
m1.add_bond(2, 3, 1)
m1.add_bond(2, 10, 1)
m1.add_bond(3, 4, 1)
m1.add_bond(1, 8, 1)
m1.add_bond(1, 3, 1)

m2.add_atom(N(), 5)
m2.add_atom(N(), 6)
m2.add_atom(N(), 7)
m2.add_atom(O(), 9)
m2.add_bond(5, 6, 1)
m2.add_bond(5, 7, 1)
m2.add_bond(6, 7, 1)
m2.add_bond(5, 9, 1)

