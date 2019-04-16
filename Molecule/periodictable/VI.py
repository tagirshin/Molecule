# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Tagir Akhmetshin <tagirshin@gmail.com>
#  Copyright 2019 Dayana Bashirova <dayana.bashirova@yandex.ru>
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


class GroupVI:
    pass


class Cr(Element, PeriodIV, GroupVI):
    @property
    def atomic_number(self):
        return 24

    @property
    def atomic_mass(self):
        return 51.996

    @property
    def electronegativity(self):
        return 1.66

    @property
    def common_isotope(self):
        return 52

    @property
    def max_isotope(self):
        return 54

    @property
    def min_isotope(self):
        return 50

    @property
    def common_valences(self):
        return (0, 6), (2, 5), (3, 4), (6, 1)

    @property
    def valences_exceptions(self):
        return ((0, 3, ((2, 'O'), (2, 'O'))),  # CrO2
                (0, 3, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # CrF4
                (0, 3, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # CrCl4
                (-4, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Cr(CN)6]4-
                (-3, 4, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Cr(CN)6]3-
                (-4, 5, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Cr(SCN)6]4-
                (-4, 5, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Cr(NCS)6]4-
                (-3, 4, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Cr(SCN)6]3-
                (-3, 4, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Cr(NCS)6]3-
                (-3, 4, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))),  # [Cr(OH)6]3-
                (-1, 1, ((2, 'O'), (2, 'O'), (2, 'O'), (1, 'F'))),  # [CrO3F]-
                (-1, 1, ((2, 'O'), (2, 'O'), (2, 'O'), (1, 'Br'))),  # [CrO3Br]-
                (-1, 1, ((2, 'O'), (2, 'O'), (2, 'O'), (1, 'Cl'))),  # [CrO3Cl]-
                (-2, 1, ((2, 'O'), (2, 'O'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [CrO2F4]2-
                (-1, 1, ((2, 'O'), (2, 'O'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [CrO2F3]-
                (-1, 2, ((2, 'O'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [CrOCl4]-
                (-2, 2, ((2, 'O'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),  # [CrOCl5]2-
                (-3, 4, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [CrF6]3-
                (-2, 3, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [CrF6]2-
                (-1, 3, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [CrF5]-
                (-3, 4, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))))  # [CrCl6]3-


class Mo(Element, PeriodV, GroupVI):
    @property
    def atomic_number(self):
        return 42

    @property
    def atomic_mass(self):
        return 95.96

    @property
    def electronegativity(self):
        return 2.16

    @property
    def common_isotope(self):
        return 98

    @property
    def max_isotope(self):
        return 99

    @property
    def min_isotope(self):
        return 92

    @property
    def common_valences(self):
        return (0, 6), (3, 4), (4, 3), (5, 2), (6, 1)

    @property
    def valences_exceptions(self):
        return ((0, 5, ((1, 'I'), (1, 'I'))),  # MoI2
                (-5, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Mo(CN)7]5-
                (-4, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Mo(CN)6]4-
                (-6, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Mo(CN)8]6-
                (-5, 4, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Mo(CN)8]5-
                (-4, 3, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Mo(CN)8]4-
                (-3, 2, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Mo(CN)8]3-
                (-2, 4, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Mo(CN)5]2-
                (-1, 3, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [Mo(CN)5]-
                (-3, 4, ((1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'), (1, 'S'))),  # [Mo(SCN)6]3-
                (-3, 4, ((1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'), (1, 'N'))),  # [Mo(NCS)6]3-
                (-3, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [MoF8]3-
                (-2, 5, ((2, 'O'), (2, 'O'), (2, 'O'), (2, 'O'))),  # [MoO4]2-
                (-2, 5, ((2, 'S'), (2, 'S'), (2, 'S'), (2, 'S'))),  # [MoS4]2-
                (-3, 4, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))))  # [MoCl6]3-


class W(Element, PeriodVI, GroupVI):
    @property
    def atomic_number(self):
        return 74

    @property
    def atomic_mass(self):
        return 183.84

    @property
    def electronegativity(self):
        return 2.3

    @property
    def common_isotope(self):
        return 186

    @property
    def max_isotope(self):
        return 188

    @property
    def min_isotope(self):
        return 178

    @property
    def common_valences(self):
        return (0, 6), (2, 5), (4, 3), (5, 2), (6, 1)

    @property
    def valences_exceptions(self):
        return ((-2, 1, ((2, 'O'), (2, 'O'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [WO2F4]2-
                (-4, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [W(CN)6]4-
                (-6, 5, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [W(CN)8]6-
                (-3, 2, ((1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'), (1, 'C'))),  # [W(CN)8]3-
                (-2, 5, ((2, 'S'), (2, 'S'), (2, 'S'), (2, 'S'))),  # [WS4]2-
                (-3, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))),  # [WF8]3-
                (-1, 2, ((1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'), (1, 'F'))))  # [WF6]-


class Sg(Element, PeriodVII, GroupVI):
    @property
    def atomic_number(self):
        return 106

    @property
    def atomic_mass(self):
        return 269

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 269

    @property
    def max_isotope(self):
        return 269

    @property
    def min_isotope(self):
        return 269

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupVI', 'Cr', 'Mo', 'W', 'Sg']
