from Molecule.containers import graph

m1 = graph.Graph()

m1.add_atom('F')
m1.add_atom('C')
m1.add_atom('O')
m1.add_atom('C')
m1.add_atom('Cl')

m1.add_bond(1, 2, 1)
m1.add_bond(2, 3, 1)
m1.add_bond(3, 4, 1)
m1.add_bond(4, 5, 1)
m1.add_bond(2, 4, 1)

print(m1.clique())