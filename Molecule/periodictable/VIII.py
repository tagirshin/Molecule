# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
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
from .element import Element
from .periods import *


class GroupVIII:
    pass


class Fe(Element, PeriodIV, GroupVIII):
    @property
    def atomic_number(self):
        return 26

    @property
    def atomic_mass(self):
        return 55.845

    @property
    def electronegativity(self):
        return 1.83

    @property
    def common_isotope(self):
        return 56

    @property
    def max_isotope(self):
        return 60

    @property
    def min_isotope(self):
        return 54

    @property
    def common_valences(self):
        return (0, 5), (2, 5), (3, 6)

    @property
    def valences_exceptions(self):
        return ((-2, 5, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Fe(OH)4]2-
                (-4, 5, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Fe(OH)6]4-
                (-4, 5, ((2, 'O'), (2, 'O'), (2, 'O'))),  # [FeO3]4-
                (-2, 5, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [FeF4]2-
                (-2, 5, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [FeCl4]2-
                (-4, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Fe(CN)6]4-
                (-4, 5, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Fe(SCN)6]4-
                (-4, 5, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Fe(NCS)6]4-
                (-2, 5, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Fe(SCN)4]2-
                (-4, 5, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Fe(NCS)4]2-
                (-3, 6, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Fe(SCN)6]3-
                (-3, 6, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Fe(NCS)6]3-
                (-3, 6, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Fe(CN)6]3-
                (-1, 6, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [FeCl4]-
                (-2, 6, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [FeCl5]2-
                (-3, 6, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [FeCl6]3-
                (-3, 6, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [FeF6]3-
                (-1, 6, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))))  # [FeBr4]-



class Ru(Element, PeriodV, GroupVIII):
    @property
    def atomic_number(self):
        return 44

    @property
    def atomic_mass(self):
        return 101.07

    @property
    def electronegativity(self):
        return 2.2

    @property
    def common_isotope(self):
        return 102

    @property
    def max_isotope(self):
        return 106

    @property
    def min_isotope(self):
        return 96

    @property
    def common_valences(self):
        return (0, 4), (2, 5), (3, 6), (4, 5), (6, 3)

    @property
    def valences_exceptions(self):
        return ((0, 1, ((2, 'O'), (2, 'O'), (2, 'O'), (2, 'O'))),  # RuO4
                (-1, 2, ((2, 'O'), (2, 'O'), (2, 'O'), (2, 'O'))),  # [RuO4]-
                (-3, 4, ((2, 'O'), (2, 'O'), (2, 'O'), (2, 'O'))),  # [RuO4]3-
                (-2, 6, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [RuCl5]2-
                (-3, 6, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [RuCl6]3-
                (-2, 5, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [RuCl6]2-
                (-4, 6, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [RuCl7]4-
                (-2, 5, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [RuF6]2-
                (-1, 4, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))  # [RuF6]-


__all__ = ['GroupVIII', 'Fe', 'Ru']
