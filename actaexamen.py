#!/usr/bin/python
# -*- coding: UTF8 -*-
# archivo : actaexamen.py
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

def actaexamenes(c):
    c.translate(0*cm, 1*cm)
    # Rectángulo de encabezado grande
    c.rect(1.6*cm, 17.4*cm, 32*cm, 2.0*cm, stroke=1, fill=0)
    c.line(10.0*cm, 17.4*cm, 10.0*cm, 19.4*cm)
    c.line(19.0*cm, 17.4*cm, 19.0*cm, 19.4*cm)
    c.line(26.3*cm, 17.4*cm, 26.3*cm, 19.4*cm)
    c.line(31.8*cm, 17.4*cm, 31.8*cm, 19.4*cm)
    c.drawString(2.5*cm, 18.8*cm, u'PROVINCIA DE BUENOS AIRES')
    c.drawString(2.0*cm, 18.2*cm, u'DIRECCIÓN GENERAL DE CULTURA Y')
    c.drawString(4.3*cm, 17.6*cm, u'EDUCACIÓN')
    c.drawString(12.4*cm, 18.8*cm, u'DIRECCIÓN DE ')
    c.drawString(11.1*cm, 17.9*cm, u'FORMACIÓN PROFESIONAL')
    c.drawString(19.2*cm, 18.8*cm, u'Especialidad: ')
    c.drawString(27.1*cm, 18.8*cm, u'ACTA DE EXAMEN')
    c.drawString(32.3*cm, 18.8*cm, u'F.P.')
    # Rectángulo de datos
    c.rect(1.6*cm, 15.4*cm, 32*cm, 2.0*cm, stroke=1, fill=0)
    c.line(26.3*cm, 15.4*cm, 26.3*cm, 17.4*cm)
    c.drawString(1.9*cm, 16.8*cm, u'En el establecimiento                                                                  de la localidad de                                  a los      días del mes de')
    c.drawString(1.9*cm, 16.2*cm, u'                              del año                       reunida la comisión examinadora con el objeto de cumplir con su cometido, llega al ')
    c.drawString(1.9*cm, 15.6*cm, u'resultado que se consigna a continuación.')
    c.drawString(26.5*cm, 16.8*cm, u'Acto administrativo: ')
    c.drawString(26.5*cm, 15.9*cm, u'Curso Nº: ')
    # Rectángulo de encabezado
    c.rect(1.6*cm, 14.0*cm, 32*cm, 1.4*cm, stroke=1, fill=0)
    c.line(2.6*cm, 14.0*cm, 2.6*cm, 15.4*cm)
    c.drawString(1.9*cm, 14.5*cm, u'Nº')
    c.drawString(4.0*cm, 14.5*cm, u'APELLIDO Y NOMBRES')
    xlist = [10.4*cm, 11.4*cm, 14.8*cm, 15.8*cm, 19.2*cm, 20.2*cm, 23.6*cm, 24.6*cm, 28.0*cm]
    ylist = [14.7*cm, 14.0*cm]
    c.grid (xlist, ylist)
    c.line(10.4*cm, 14.7*cm, 10.4*cm, 15.4*cm)
    c.line(14.8*cm, 14.7*cm, 14.8*cm, 15.4*cm)
    c.line(19.2*cm, 14.7*cm, 19.2*cm, 15.4*cm)
    c.line(23.6*cm, 14.7*cm, 23.6*cm, 15.4*cm)
    c.line(28.0*cm, 14.7*cm, 28.0*cm, 15.4*cm)
    c.drawString(11.3*cm, 14.9*cm, u'TALLER/100')
    c.drawString(15.2*cm, 14.9*cm, u'TECNOLOGÍA/100')
    c.drawString(20.0*cm, 14.9*cm, u'CALCULO/100')
    c.drawString(24.1*cm, 14.9*cm, u'DIBUJO TÉC./100')
    c.drawString(10.7*cm, 14.2*cm, u'Nº')
    c.drawString(15.1*cm, 14.2*cm, u'Nº')
    c.drawString(19.5*cm, 14.2*cm, u'Nº')
    c.drawString(23.9*cm, 14.2*cm, u'Nº')
    c.drawString(12.2*cm, 14.2*cm, u'LETRAS')
    c.drawString(16.6*cm, 14.2*cm, u'LETRAS')
    c.drawString(21.0*cm, 14.2*cm, u'LETRAS')
    c.drawString(25.4*cm, 14.2*cm, u'LETRAS')
    c.drawString(29.4*cm, 14.9*cm, u'DOCUMENTO')
    c.drawString(29.2*cm, 14.2*cm, u'DE IDENTIDAD')
    #Grilla principal
    xlist = [1.6*cm, 2.6*cm, 10.4*cm, 11.4*cm, 14.8*cm, 15.8*cm, 19.2*cm, 20.2*cm, 23.6*cm, 24.6*cm, 28*cm, 33.6*cm]
    ylist = [14.0*cm, 13.4*cm, 12.8*cm, 12.2*cm, 11.6*cm, 11.0*cm, 10.4*cm, 9.8*cm, 9.2*cm, 8.6*cm, 8.0*cm, 7.4*cm, 6.8*cm, 6.2*cm, 5.6*cm, 5.0*cm, 4.4*cm, 3.8*cm, 3.2*cm]
    c.grid (xlist, ylist)
    c.drawString(1.9*cm, 13.6*cm, u'1')
    c.drawString(1.9*cm, 13.0*cm, u'2')
    c.drawString(1.9*cm, 12.4*cm, u'3')
    c.drawString(1.9*cm, 11.8*cm, u'4')
    c.drawString(1.9*cm, 11.2*cm, u'5')
    c.drawString(1.9*cm, 10.6*cm, u'6')
    c.drawString(1.9*cm, 10.0*cm, u'7')
    c.drawString(1.9*cm, 9.4*cm, u'8')
    c.drawString(1.9*cm, 8.8*cm, u'9')
    c.drawString(1.8*cm, 8.2*cm, u'10')
    c.drawString(1.8*cm, 7.6*cm, u'11')
    c.drawString(1.8*cm, 7.0*cm, u'12')
    c.drawString(1.8*cm, 6.4*cm, u'13')
    c.drawString(1.8*cm, 5.8*cm, u'14')
    c.drawString(1.8*cm, 5.2*cm, u'15')
    c.drawString(1.8*cm, 4.6*cm, u'16')
    c.drawString(1.8*cm, 4.0*cm, u'17')
    c.drawString(1.8*cm, 3.4*cm, u'18')
    # Rectángulo inferior
    c.rect(1.6*cm, 0.6*cm, 32*cm, 2.6*cm, stroke=1, fill=0)
    c.drawString(1.8*cm, 0.7*cm, u'Se considera aprobado con un mínimo de 70 puntos')
    c.drawString(4.0*cm, 1.7*cm, u'Vocal 1º')
    c.drawString(8.5*cm, 1.7*cm, u'Presidente')
    c.drawString(13.0*cm, 1.7*cm, u'Vocal 2º')
    c.drawString(17.5*cm, 2.2*cm, u'Director o Regente')
    ylist = [0.6*cm, 1.4*cm, 2.0*cm, 2.6*cm, 3.2*cm]
    xlist = [26.5*cm, 31.5*cm, 33.6*cm]
    c.grid (xlist, ylist)
    c.drawString(26.7*cm, 2.75*cm, u'Aprobados')
    c.drawString(26.7*cm, 2.15*cm, u'Desaprobados')
    c.drawString(26.7*cm, 1.55*cm, u'Ausentes')
    c.drawString(26.7*cm, 0.9*cm, u'Examinados')
    c.drawString(17.5*cm, 0.7*cm, u'Inspector')

       
c = canvas.Canvas("./planillas/actaexamen.pdf", pagesize=landscape(legal))
actaexamenes(c)
c.showPage()
c.save()
    

    
