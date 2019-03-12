# -*- coding: utf-8 -*-
#
#  Copyright 2019 Ramil Nugmanov <stsouko@live.ru>
#  Copyright 2019 Dayana Bashirova <dayana.bashirova@yandex.ru>
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


class GroupXVII:
    pass


class Po(Element, PeriodVI, GroupXVII):
    @property
    def atomic_number(self):
        return 84

    @property
    def atomic_mass(self):
        return 209

    @property
    def electronegativity(self):
        return 2.3

    @property
    def common_isotope(self):
        return 209

    @property
    def max_isotope(self):
        return 210

    @property
    def min_isotope(self):
        return 206

    @property
    def common_valences(self):
        return (0, 1), (2, 1)

    @property
    def valences_exceptions(self):
        return ((0, 1, ((2, 'O'), (2, 'O'), (2, 'O'))),
                (0, 1, ((2, 'O'), (2, 'O'))),
                (0, 1, ((1, 'Cl'), (1, 'Cl'), (1, 'Cl'), (1, 'Cl'))),
                (0, 1, ((1, 'Br'), (1, 'Br'), (1, 'Br'), (1, 'Br'))),
                (0, 1, ((1, 'I'), (1, 'I'), (1, 'I'), (1, 'I'))),
                (0, 1, ((1, 'O'), (1, 'O'), (1, 'O'), (1, 'O'))))


class Lv(Element, PeriodVII, GroupXVII):
    @property
    def atomic_number(self):
        return 116

    @property
    def atomic_mass(self):
        return 293

    @property
    def electronegativity(self):
        return None

    @property
    def common_isotope(self):
        return 293

    @property
    def max_isotope(self):
        return 293

    @property
    def min_isotope(self):
        return 293

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupXVII', 'Po', 'Lv']