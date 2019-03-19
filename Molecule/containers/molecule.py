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
from .graph import Graph
from typing import List


class Molecule(Graph):
    def check_valences(self) -> List[int]:
        """
        Checks atoms' valences
        :return: numbers of atom with error
        """
        for (n, atom), bonds in zip(self._atoms.items(), self._bonds.values()):
            valence = (sum([bonds.values()]), atom.multiplicity)
            if valence in atom.common_valences:
                continue
