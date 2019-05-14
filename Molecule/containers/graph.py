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
from typing import Tuple
from ..algorithms import Components, MCS, Isomorphism
from ..periodictable.element import Element


class Graph(Components, MCS, Isomorphism):
    def __init__(self):
        self._bonds = {}
        self._atoms = {}

    def add_atom(self, atom, number=None):
        if not isinstance(atom, Element):
            raise TypeError('Molecule.periodictable Element required')
        if number is None:
            number = max(self._atoms, default=0) + 1
        elif not isinstance(number, int):
            raise TypeError('integer required')
        elif number in self._atoms:
            raise ValueError('number already exists')

        self._atoms[number] = atom
        self._bonds[number] = {}
        return number

    def add_bond(self, num1, num2, bond):
        try:
            if num1 not in self._atoms or num2 not in self._atoms:
                raise ValueError('number does not exists')
        except TypeError:
            raise ValueError('integer required')
        self._bonds[num1][num2] = self._bonds[num2][num1] = bond

    def __bool__(self):
        return bool(self._atoms)

    def bonds(self) -> Tuple[int, int, int]:
        seen_atoms = set()
        for atom1, bonds in self._bonds.items():
            seen_atoms.add(atom1)
            for atom2, bond in bonds.items():
                if atom2 not in seen_atoms:
                    yield atom1, atom2, bond

    def atoms(self) -> Tuple[int, Element]:
        return iter(self._atoms.items())
