#!/usr/bin/python
# -*- coding: UTF8 -*-
# archivo : temario.py
#
###############################################################################
#
#
# Sancabase - Administrador general para centros de Formación Profesional
# Copyright (c) 2007 Javier Castrillo // riverplatense at gmail dot com
#Este programa es software libre; usted puede redistruirlo y/o modificarlo bajo
#los términos de la Licencia Pública General GNU, tal y como está publicada
#por la Free Software Foundation; ya sea la versión 2 de la Licencia, o (a su
#elección) cualquier versión posterior.
#
#Este programa se distribuye con la intención de ser útil, pero SIN NINGUNA
#GARANTÍA; incluso sin la garantía implícita de USABILIDAD O UTILIDAD PARA UN
#FIN PARTICULAR. Vea la Licencia Pública General GNU para más detalles.
#
#Usted debería haber recibido una copia de la Licencia Pública General GNU
#junto a este programa; si no es así, escriba a la Free Software Foundation,
#Inc. 675 Mass Ave, Cambridge, MA 02139, EEUU.
#
#
###############################################################################

from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import legal


def temarios(c):
    c.translate (1*cm, 2*cm)
    xlist = [2*cm, 4.5*cm, 14*cm, 18*cm]
    ylist = [cm, 2*cm, 3*cm, 4*cm, 5*cm, 6*cm, 7*cm, 8*cm, 9*cm, 10*cm, 11*cm, 12*cm, 13*cm, 14*cm, 15*cm, 16*cm, 17*cm, 18*cm, 19*cm, 20*cm, 21*cm, 22*cm, 23*cm, 24*cm, 25*cm, 26*cm, 27*cm]
    c.grid (xlist, ylist)
    c.drawString(3*cm, 31.7*cm, u'Especialidad:                                        Año lectivo:')
    c.drawString(3*cm, 29*cm, u'Temario de clases del mes de:                        Instructor:')
    c.drawString(3*cm, 26.3*cm, u'Día')
    c.drawString(8*cm, 26.3*cm, u'Tema de la clase')
    c.drawString(15.5*cm, 26.3*cm, u'Firma')
    
c = canvas.Canvas("temario.pdf", pagesize=legal)
temarios(c)
c.showPage()
c.save()
    

    
