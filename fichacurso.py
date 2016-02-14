#!/usr/bin/python
# -*- coding: UTF8 -*-
# archivo : fichacurso.py
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
from reportlab.lib.pagesizes import legal, landscape
from reportlab.lib.colors import white

def fichacursos(c):
    c.translate(0*cm, 1*cm)
    #Grilla
    ylist = [2.5*cm, 3*cm, 3.5*cm, 4*cm, 4.5*cm, 5*cm, 5.5*cm, 6*cm, 6.5*cm, 7*cm, 7.5*cm, 8*cm, 8.5*cm, 9*cm, 9.5*cm, 10*cm, 10.5*cm, 11*cm, 11.5*cm, 12*cm, 12.5*cm, 13*cm, 13.5*cm]
    xlist = [1.5*cm, 2.3*cm, 11*cm, 13.7*cm, 16.3*cm, 18*cm, 21*cm, 23.7*cm, 31.3*cm, 32.6*cm]
    c.grid (xlist, ylist)
    c.drawString(1.6*cm, 2.6*cm, '22')
    c.drawString(1.6*cm, 3.1*cm, '21')
    c.drawString(1.6*cm, 3.6*cm, '20')
    c.drawString(1.6*cm, 4.1*cm, '19')
    c.drawString(1.6*cm, 4.6*cm, '18')
    c.drawString(1.6*cm, 5.1*cm, '17')
    c.drawString(1.6*cm, 5.6*cm, '16')
    c.drawString(1.6*cm, 6.1*cm, '15')
    c.drawString(1.6*cm, 6.6*cm, '14')
    c.drawString(1.6*cm, 7.1*cm, '13')
    c.drawString(1.6*cm, 7.6*cm, '12')
    c.drawString(1.6*cm, 8.1*cm, '11')
    c.drawString(1.6*cm, 8.6*cm, '10')
    c.drawString(1.6*cm, 9.1*cm, '9')
    c.drawString(1.6*cm, 9.6*cm, '8')
    c.drawString(1.6*cm, 10.1*cm, '7')
    c.drawString(1.6*cm, 10.6*cm, '6')
    c.drawString(1.6*cm, 11.1*cm, '5')
    c.drawString(1.6*cm, 11.6*cm, '4')
    c.drawString(1.6*cm, 12.1*cm, '3')
    c.drawString(1.6*cm, 12.6*cm, '2')
    c.drawString(1.6*cm, 13.1*cm, '1')
    c.rect(1.5*cm, 13.5*cm, 31.1*cm, 1.2*cm)
    c.drawString(1.7*cm, 14*cm, u'N°')
    c.drawString(4.4*cm, 14*cm, u'Apellido y Nombres')
    c.drawString(11.1*cm, 14*cm, u'Nacionalidad')
    c.drawString(14.5*cm, 14.2*cm, u'Fecha')
    c.drawString(14.3*cm, 13.6*cm, u'de Nac.')
    c.drawString(17.4*cm, 14.3*cm, u'Documento de Identidad')
    c.drawString(16.8*cm, 13.7*cm, u'Tipo')
    c.drawString(18.8*cm, 13.7*cm, u'Número')
    c.drawString(21.1*cm, 13.7*cm, u'Expedido por')
    c.drawString(25.6*cm, 14*cm, u'Domicilio y Localidad')
    c.drawString(31.6*cm, 14*cm, u'Esp')
    # Rectángulo de encabezado grande
    c.rect(1.5*cm, 14.705*cm, 31.1*cm, 3.5*cm, stroke=1, fill=0)
    # Rectángulo de Especialidad, etc.
    c.rect(1.5*cm, 14.705*cm, 24.4*cm, 2.35*cm, stroke=1, fill=0)
    # Rectángulo Ficha de curso
    c.rect(25.9*cm, 17.055*cm, 6.70*cm, 1.15*cm)
    c.line(10*cm, 17.055*cm, 10*cm, 18.23*cm)
    c.line(18*cm, 17.055*cm, 18*cm, 18.23*cm)
    c.line(2.3*cm, 13.5*cm, 2.3*cm, 14.705*cm)
    c.line(11*cm, 13.5*cm, 11*cm, 14.705*cm)
    c.line(13.7*cm, 13.5*cm, 13.7*cm, 14.705*cm)
    c.line(16.3*cm, 13.5*cm, 16.3*cm, 14.705*cm)
    c.line(23.7*cm, 13.5*cm, 23.7*cm, 14.705*cm)
    c.line(31.3*cm, 13.5*cm, 31.3*cm, 14.705*cm)
    c.line(16.3*cm, 13.5*cm, 16.3*cm, 14.705*cm)
    c.line(18*cm, 13.5*cm, 18*cm, 14.1*cm)
    c.line(21*cm, 13.5*cm, 21*cm, 14.1*cm)
    c.line(16.3*cm, 14.1*cm, 23.7*cm, 14.1*cm)
    c.line(23.7*cm, 13.5*cm, 23.7*cm, 14.705*cm)
    c.line(31.3*cm, 13.5*cm, 31.3*cm, 14.705*cm)
    c.drawString(3*cm, 17.7*cm, u'Provincia de Buenos Aires')
    c.drawString(1.6*cm, 17.2*cm, u'Dirección General de Cultura y Educación')
    c.drawString(10.5*cm, 17.5*cm, u'Dirección de Formación Profesional')
    c.drawString(18.2*cm, 17.7*cm, u'Establecimiento:')
    c.drawString(18.2*cm, 17.2*cm, u'Localidad:')
    c.drawString(27.9*cm, 17.5*cm, u'Ficha de Curso')
    c.drawString(26.2*cm, 16.3*cm, u'Acto administrativo: ..........')
    c.drawString(26.2*cm, 15.2*cm, u'Curso N°:')
    c.drawString(1.7*cm, 16.4*cm, u'Especialidad:                                                                                                                     Tipo:              Duración hs reloj:')
    c.drawString(1.7*cm, 15.6*cm, u'Fecha de iniciación:                              Fecha de terminación:                              Horario:')
    c.drawString(1.7*cm, 14.9*cm, u'Lugar en que se dicta:                                                                                           Instructor/a:')
    # Pie de página
    c.drawString(14*cm, 1.95*cm, u'Nota: Entregar un original y tres copias')
    c.drawString(3*cm, 1*cm, 'Firma del Inspector: .....................................                                                     Fecha: ......................................                                     Sello')
    
       
c = canvas.Canvas("./planillas/fichacurso.pdf", pagesize=landscape(legal))
fichacursos(c)
c.showPage()
c.save()
    

    
