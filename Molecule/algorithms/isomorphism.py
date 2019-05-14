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
from typing import Dict
from collections import Counter, defaultdict


class Isomorphism:
    def _get_substructure_mapping(self, other) -> Dict[int, int]:
        brutto_self = Counter(self._atoms.values())
        brutto_other = Counter(other._atoms.values())
        if brutto_self.keys() <= brutto_other.keys():
            for atom, num in brutto_self.items():
                if num > brutto_other[atom]:
                    raise Exception
        else:
            raise Exception
        brutto_bonds_self = Counter(bond for *_, bond in self.bonds())
        brutto_bonds_other = Counter(bond for *_, bond in other.bonds())
        if brutto_bonds_self.keys() <= brutto_bonds_other.keys():
            for bond, num in brutto_bonds_self.items():
                if num > brutto_bonds_other[bond]:
                    raise Exception
        else:
            raise Exception
        possible_matches = {}
        for num1, atom1 in self._atoms.items():
            nums2 = set()
            for num2, atom2 in other._atoms.items():
                if atom1 == atom2:
                    nums2.add(num2)
                possible_matches[num1] = nums2

    def plain_subgraph(self):
        start, atom = min(self._atoms.items())
        stack = [(x, self._atoms[x], start, bond) for x, bond in self._bonds[start].items()]
        seen = {start}
        plain_graph = [(start, atom)]
        closures = defaultdict(list)
        while stack:
            front = stack.pop()
            front_atom = front[0]
            if front_atom not in seen:
                plain_graph.append(front)
                back = front[2]
                for x, bond in self._bonds[front_atom].items():
                    if x != back:
                        if x not in seen:
                            stack.append((x, self._atoms[x], front_atom, bond))
                        else:
                            closures[front_atom].append((x, bond))
                seen.add(front_atom)
        return plain_graph, closures

    def substructure_mappings(self, other):
        plain_self, closures_self = self.plain_subgraph()
        plain_self_depth = {v[0]: k for k, v in enumerate(plain_self)}
        stack = []
        path = []
        mapping = {}
        reversed_mapping = {}
        for number, atom in other._atoms.items():
            if atom == plain_self[0][1]:
                stack.append((number, 0))
        while stack:
            current = stack.pop()
            depth = current[1]
            atom_current = current[0]
            atom_number = plain_self[depth][0]
            if depth == len(self._atoms) - 1:
                yield {atom_number: atom_current, **mapping}
            else:
                if len(path) != depth:
                    for x in path[depth:]:
                        del mapping[reversed_mapping[x]]
                    path = path[:depth]
                next_atom = plain_self[current[1] + 1][2]
                if next_atom != atom_number:
                    fork = path[plain_self_depth[next_atom]]
                else:
                    fork = atom_current
                path.append(atom_current)
                mapping[atom_number] = atom_current
                reversed_mapping[atom_current] = atom_number
                for neighbour, bond in other._bonds[fork].items():
                    plain_self_current, plain_self_atom, plain_self_front, plain_self_bond = plain_self[len(path)]
                    if neighbour not in path and bond == plain_self_bond \
                            and other._atoms[neighbour] == plain_self_atom \
                            and all((other._bonds[mapping[atom]].get(neighbour) == bond) for atom, bond in
                                    closures_self[plain_self_current]):
                        stack.append((neighbour, len(path)))
