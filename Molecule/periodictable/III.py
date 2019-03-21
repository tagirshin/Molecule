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


class GroupIII:
    pass


class Ac(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 89

    @property
    def atomic_mass(self):
        return 227

    @property
    def electronegativity(self):
        return 1.1

    @property
    def common_isotope(self):
        return 227

    @property
    def max_isotope(self):
        return 227

    @property
    def min_isotope(self):
        return 225

    @property
    def common_valences(self):
        return (0, 2), (3, 1)

    @property
    def valences_exceptions(self):
        return ()


class Th(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 90

    @property
    def atomic_mass(self):
        return 232.04

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 232

    @property
    def max_isotope(self):
        return 234

    @property
    def min_isotope(self):
        return 227

    @property
    def common_valences(self):
        return (0, 2), (4, 1)

    @property
    def valences_exceptions(self):
        return ((0, 1, ((1, 'Br'), (1, 'Br'), (1, 'Br'))),
                (0, 1, ((1, 'I'), (1, 'I'), (1, 'I'))),
                (0, 1, ((1, 'Br'), (1, 'Br'))),
                (0, 1, ((1, 'I'), (1, 'I'))),
                (0, 1, ((1, 'H'), (1, 'H'))))


class Pa(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 91

    @property
    def atomic_mass(self):
        return 231.04

    @property
    def electronegativity(self):
        return 1.5

    @property
    def common_isotope(self):
        return 231

    @property
    def max_isotope(self):
        return 233

    @property
    def min_isotope(self):
        return 229

    @property
    def common_valences(self):
        return (0, 2), (4, 1), (5, 1)

    @property
    def valences_exceptions(self):
        return ((0, 1, ((2, 'O'),))
                (0, 1, ((1, 'H'), (1, 'H'), (1, 'H'))))


class U(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 92

    @property
    def atomic_mass(self):
        return 238.03

    @property
    def electronegativity(self):
        return 1.38

    @property
    def common_isotope(self):
        return 238

    @property
    def max_isotope(self):
        return 238

    @property
    def min_isotope(self):
        return 232

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Np(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 93

    @property
    def atomic_mass(self):
        return 237

    @property
    def electronegativity(self):
        return 1.36

    @property
    def common_isotope(self):
        return 237

    @property
    def max_isotope(self):
        return 239

    @property
    def min_isotope(self):
        return 235

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Pu(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 94

    @property
    def atomic_mass(self):
        return 244

    @property
    def electronegativity(self):
        return 1.28

    @property
    def common_isotope(self):
        return 244

    @property
    def max_isotope(self):
        return 244

    @property
    def min_isotope(self):
        return 238

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Am(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 95

    @property
    def atomic_mass(self):
        return 243

    @property
    def electronegativity(self):
        return 1.13

    @property
    def common_isotope(self):
        return 243

    @property
    def max_isotope(self):
        return 243

    @property
    def min_isotope(self):
        return 241

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Cm(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 96

    @property
    def atomic_mass(self):
        return 247

    @property
    def electronegativity(self):
        return 1.28

    @property
    def common_isotope(self):
        return 247

    @property
    def max_isotope(self):
        return 250

    @property
    def min_isotope(self):
        return 242

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Bk(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 97

    @property
    def atomic_mass(self):
        return 247

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 247

    @property
    def max_isotope(self):
        return 249

    @property
    def min_isotope(self):
        return 245

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Cf(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 98

    @property
    def atomic_mass(self):
        return 251

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 251

    @property
    def max_isotope(self):
        return 254

    @property
    def min_isotope(self):
        return 248

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Es(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 99

    @property
    def atomic_mass(self):
        return 252

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 252

    @property
    def max_isotope(self):
        return 255

    @property
    def min_isotope(self):
        return 252

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Fm(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 100

    @property
    def atomic_mass(self):
        return 257

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 257

    @property
    def max_isotope(self):
        return 257

    @property
    def min_isotope(self):
        return 252

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Md(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 101

    @property
    def atomic_mass(self):
        return 258

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 258

    @property
    def max_isotope(self):
        return 260

    @property
    def min_isotope(self):
        return 257

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class No(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 102

    @property
    def atomic_mass(self):
        return 259

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 259

    @property
    def max_isotope(self):
        return 259

    @property
    def min_isotope(self):
        return 259

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


class Lr(Element, PeriodI, GroupIII):
    @property
    def atomic_number(self):
        return 103

    @property
    def atomic_mass(self):
        return 266

    @property
    def electronegativity(self):
        return 1.3

    @property
    def common_isotope(self):
        return 266

    @property
    def max_isotope(self):
        return 266

    @property
    def min_isotope(self):
        return 266

    @property
    def common_valences(self):
        return ()

    @property
    def valences_exceptions(self):
        return ()


__all__ = ['GroupIII', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
