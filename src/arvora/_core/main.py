#! /usr/bin/env python
# -*- coding: UTF8 -*-
""" Ponto de entrada do módulo Arvora.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

Changelog
---------
.. versionadded::    24.03
   |br| first version of main (09)

|   **Open Source Notification:** This file is part of open source program **Arvora**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <http://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

"""


class LandingPage:
    def __init__(self, brython):
        items = "PROJETO CONHECIMENTO PESQUISA INTERAÇÃO LOGIN".split()
        icons = "bars-progress book book-medical hands-asl-interpreting right-to-bracket".split()
        menu = [{"title": items, "icon": icons} for items, icons in zip(items, icons)]
        self.brython = brython
        self.landing_page = self.hero(self.navigator(menu))
        _ = self.brython.document["pydiv"] <= self.landing_page

    def hero(self, navigator):
        h = self.brython.html
        tt1 = h.P("A R V O R A", Class="title main-text has-text-weight-bold")
        tt2 = h.P("Brain Computational School", Class="title is-1 main-text")
        idv = h.DIV((tt1, tt2))
        cnt = h.DIV(idv, Class="container has-text-centered pb-6 mgb-large")
        hby = h.DIV(cnt, Class="hero-body")
        hea = h.DIV(navigator, Class="hero-head")
        sec = h.SECTION((hea, hby), Class="hero main_hero is-fullheight")
        return sec

    def navigator(self, menu):
        h = self.brython.html

        def do_item(title=None, icon=None):
            spn = h.SPAN(h.I(Class=f"fa fa-lg fa-{icon}")+h.SPAN(title), Class="icon-text", style="color: #333;")
            return h.A(spn, Class="navbar-item", href="/#")
        aim = h.IMG(src="/src/arvora/_media/arvora_ico.png", alt="Arvora", width="112", height="28")
        arv = h.A(aim, Class="navbar-item", href="https://activufrj.nce.ufrj.br/raw/wiki/labase/alite_page")
        nbr = h.DIV(arv, Class="navbar-brand")
        items = [nbr]+[do_item(**item) for item in menu]
        nav = h.NAV(items, Class="navbar")
        fna = h.DIV(h.DIV(nav, Class="container"), Class="first_nav")
        return fna


def main(br):
    return LandingPage(br)
