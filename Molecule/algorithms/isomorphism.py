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
from collections import Counter


class Isomorphism:
    def get_substructure_mapping(self, other) -> Dict[int, int]:
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





