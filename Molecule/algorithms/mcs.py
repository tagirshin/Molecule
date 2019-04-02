# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  This file is part of Molecule.
#
#  Molecule is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, see <https://www.gnu.org/licenses/>.
#
from collections import defaultdict
from itertools import product, combinations
from typing import Dict, List, Set, Hashable, Iterator

def find_cliques(G):

    if len(G) == 0:
        return

    adj = {u: {v for v in G[u] if v != u} for u in G}
    Q = [None]

    subg = set(G)
    cand = set(G)
    u = max(subg, key=lambda u: len(cand & adj[u]))
    ext_u = cand - adj[u]
    stack = []

    try:
        while True:
            if ext_u:
                q = ext_u.pop()
                cand.remove(q)
                Q[-1] = q
                adj_q = adj[q]
                subg_q = subg & adj_q
                if not subg_q:
                    yield Q[:]
                else:
                    cand_q = cand & adj_q
                    if cand_q:
                        stack.append((subg, cand, ext_u))
                        Q.append(None)
                        subg = subg_q
                        cand = cand_q
                        u = max(subg, key=lambda u: len(cand & adj[u]))
                        ext_u = cand - adj[u]
            else:
                Q.pop()
                subg, cand, ext_u = stack.pop()
    except IndexError:
        pass


def clique(graph: Dict[Hashable, Set[Hashable]]) -> Iterator[List[Hashable]]:
    """ adopted from networkx algorithms.clique.find_cliques"""
    subgraph = {x for x, y in graph.items() if y}  # skip isolated nodes
    if not subgraph:
        return  # empty or fully disconnected
    elif len(subgraph) == 2:  # dimer
        yield list(subgraph)
        return

    stack = []
    clique_atoms = [None]
    candidates = subgraph.copy()
    roots = candidates - graph[max(subgraph, key=lambda x: len(graph[x]))]

    while True:
        if roots:
            root = roots.pop()
            candidates.remove(root)
            clique_atoms[-1] = root
            neighbors = graph[root]
            neighbors_subgraph = subgraph & neighbors
            if not neighbors_subgraph:
                yield clique_atoms.copy()
            else:
                neighbors_candidates = candidates & neighbors
                if neighbors_candidates:
                    if roots:
                        stack.append((subgraph, candidates, roots))
                    clique_atoms.append(None)
                    subgraph = neighbors_subgraph
                    candidates = neighbors_candidates
                    roots = candidates - graph[max(subgraph, key=lambda x: len(candidates & graph[x]))]
        elif not stack:
            return
        else:
            clique_atoms.pop()
            subgraph, candidates, roots = stack.pop()


class MCS:
    def mcs_mapping(self, other) -> List[Dict]:
        product_graph = {}
        atoms_combinations = defaultdict(set)

        for (self_num, self_atom), (other_num, other_atom) in product(self._atoms.items(), other._atoms.items()):
            if self_atom == other_atom:
                product_graph[(self_num, other_num)] = set()
                atoms_combinations[self_num].add(other_num)

        for (self_num_1, set_1), (self_num_2, set_2) in combinations(atoms_combinations.items(), 2):
            bond1 = self._bonds[self_num_1].get(self_num_2)
            if not bond1:
                for other_num_1, other_num_2 in product(set_1, set_2):
                    if other_num_1 != other_num_2:
                        node1 = (self_num_1, other_num_1)
                        node2 = (self_num_2, other_num_2)
                        product_graph[node1].add(node2)
                        product_graph[node2].add(node1)
            else:
                for other_num_1, other_num_2 in product(set_1, set_2):
                    if other_num_1 != other_num_2:
                        bond2 = other._bonds[other_num_1].get(other_num_2)
                        if not bond2 or bond1 == bond2:
                            node1 = (self_num_1, other_num_1)
                            node2 = (self_num_2, other_num_2)
                            product_graph[node1].add(node2)
                            product_graph[node2].add(node1)

        max_bonds = 0
        mapping_list = []
        max_atoms = 0
        for cliq in find_cliques(product_graph):
            if len(cliq) >= max_atoms:
                max_atoms = len(cliq)
                c = dict(cliq)
                atoms = set(c)
                atom = atoms.pop()
                bonds_count = 0

                while atoms:
                    other_neighbours = other._bonds[c[atom]]
                    bonds_count += sum(c[x] in other_neighbours for x in atoms & self._bonds[atom].keys())
                    atom = atoms.pop()
                if bonds_count > max_bonds:
                    max_bonds = bonds_count
                    mapping_list = [c]
                    max_atoms = len(cliq)
                elif bonds_count == max_bonds:
                    mapping_list.append(c)

        return mapping_list
