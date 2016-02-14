#!/usr/bin/python
# -*- coding: UTF8 -*-
# archivo : legajo_dgce.py
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
from reportlab.lib.pagesizes import legal, portrait
from reportlab.lib.colors import white

def legajo(c):
    # Llevo arriba a la izquierda el origen
    c.translate(1.5*cm, 31.0*cm)
    # Hago el rectángulo superior
    c.rect(0, 0, 18.0*cm, 2.0*cm)
    c.drawImage("./images/dgce.png", 0.5*cm, 0.5*cm, 120, 40)
    c.drawString(5*cm, 1.5*cm, u'SOLICITUD DE INSCRIPCIÓN - Año lectivo: ')
    c.drawString(7.8*cm, 0.5*cm, u'FORMACIÓN PROFESIONAL')
    c.drawString(15.5*cm, 1.0*cm, u'Nº:')
    # Segundo rectángulo
    c.rect(0, -2.2*cm, 18.0*cm, 2.0*cm)
    c.drawString(0.5*cm, -1.0*cm, u'* DATOS DEL ESTABLECIMIENTO: Nombre: ')
    c.drawString(0.5*cm, -1.8*cm, u'* Número:                        Distrito: ')
    c.drawString(16.0*cm, -1.2*cm, u'Estatal ')
    c.drawString(16.0*cm, -1.7*cm, u'Privado ')
    # Item inscripción
    c.rect(0, -7.6*cm, 18.0*cm, 4.5*cm)
    c.drawString(0.5*cm, -2.9*cm, u'INSCRIPCIÓN: El alumno se escribe en:')
    c.drawString(0.5*cm, -3.7*cm,
     u'Nivel:    E.G.B.A.           Medio/Polimodal:            Formación Profesional: ')
    c.line(0.5*cm, -3.8*cm, 17.5*cm, -3.8*cm)
    c.drawString(0.5*cm, -4.4*cm, u'Módulo:           1             2             3')
    c.line(0.5*cm, -4.5*cm, 17.5*cm, -4.5*cm)
    c.drawString(0.5*cm, -5.1*cm,
     u'Turno Solicitado:     Mañana      Tarde      Vespertino      Noche      Intermedio')
    c.line(0.5*cm, -5.2*cm, 17.5*cm, -5.2*cm)
    c.drawString(0.5*cm, -5.9*cm, u'Área / Modalidad / Orientación / Especialidad: ')
    c.rect(0, -19.6*cm, 18.0*cm, 12.0*cm)
    c.drawString(0.5*cm, -8.3*cm, u'* DATOS DEL ALUMNO/A:')
    c.rect(10*cm, -8.3*cm, 8.0*cm, 0.7*cm)
    c.drawString(10.2*cm, -8.1*cm, u'En medio / Polimodal: Repitente: Sí  No  ')
    c.drawString(0.5*cm, -9.1*cm,
     u'Tipo Doc:             Nº Doc:                     Estado del Doc: Bueno   Malo   En trámite   No posee   ')
    c.drawString(0.5*cm, -9.9*cm, u'Apellidos:                                                  Nombres:')
    c.drawString(0.5*cm, -10.8*cm,
     u'Sexo:    Fecha de Nac:                   Lugar de Nac:                               Nacionalidad: ')
    c.drawString(0.5*cm, -11.7*cm,
     u'Domicilio: Calle:                                                Nº:              Piso:            Dpto:')
    c.drawString(0.5*cm, -12.5*cm,
     u'Localidad:                                               CP:                      Teléfono:')
    c.line(0.5*cm, -12.9*cm, 17.5*cm, -12.9*cm)
    c.drawString(0.5*cm, -13.5*cm,
     u'Nº Legajo:................................. Nº Libro Matriz:............................ Nº Folio:..........................')
    c.line(0.5*cm, -13.7*cm, 17.5*cm, -13.7*cm)
    c.drawString(0.5*cm, -14.5*cm, u'Nivel de Instrucción:')
    c.drawString(0.5*cm, -15.3*cm, u'Ninguno    Primario    Secundario    Terciario    Posgrado    ')
    c.rect(12*cm, -15.5*cm, 5.8*cm, 1.5*cm)
    c.drawString(12.3*cm, -14.5*cm, u'Completo:')
    c.drawString(12.3*cm, -15.3*cm, u'Incompleto:   Hasta el año:')
    c.rect(0.5*cm, -18.5*cm, 17*cm, 2.8*cm)
    c.drawString(0.8*cm, -16.2*cm, u'Servicio Educativo de Procedencia:' )
    c.drawString(0.8*cm, -16.8*cm,
     u'Jurisdicción / Provincia:....................... Distrito: ............. Rama / Nivel:........')
    c.drawString(0.8*cm, -17.4*cm,
     u'Nombre del establecimiento:........................................................... Nº:........')
    c.drawString(0.8*cm, -18*cm, u'Condición del alumno: Repitente  Reinscripto  Ingresante  Promovido  Permanece' )
    c.line(15*cm, -17.5*cm, 15*cm, -16*cm)
    c.drawString(15.2*cm, -16.5*cm, u'Estatal:')
    c.drawString(15.2*cm, -17.2*cm, u'Privado:')
    c.drawString(0.5*cm, -19.3*cm,
     u'Otros datos: ¿Trabaja?: SI     NO          ¿Tiene el primario completo?: SI     NO')
    # Último recuadro - Familiares
    c.rect(0, -29.2*cm, 18.0*cm, 8.0*cm)
    c.drawString(0.5*cm, -20.9*cm, u'FAMILIARES / TUTORES - Datos de la madre / padre o responsable del alumno/a')
    c.drawString(0.5*cm, -21.7*cm, u'(Complete si el alumno es menor de edad)')
    c.drawString(0.5*cm, -22.5*cm, u'Parentesco:  Madre:     Padre:      Tutor/responsable:        Es jefe/a de hogar:  SI     NO')
    c.drawString(0.5*cm, -23.3*cm, u'Nombre y apellido:')
    c.drawString(0.5*cm, -24.1*cm,
     u'Nacionalidad:                                              Profesión u ocupación:')
    c.drawString(0.5*cm, -24.7*cm, u'Condición de la actividad:')
    c.drawString(0.5*cm, -25.5*cm, u'Nivel de instrucción (marque el último alcanzado)')
    c.drawString(0.5*cm, -26*cm,
     u'Ninguno   Primario   Sec.   Terciario   Univ.   Posgrado   Completo     Incompleto    Hasta:')
    c.rect(11.0*cm, -26.2*cm, 6.7*cm, 1.0*cm)
    c.line(13.3*cm, -26.2*cm, 13.3*cm, -25.2*cm)
    c.drawString(0.5*cm, -27.0*cm,
     u'Tipo Doc:          Nº Doc:                         Estado del Doc: Bueno   Malo   En trámite   No posee   ')
    c.drawString(0.5*cm, -27.7*cm,
     u'Domicilio: Calle:                                                Nº:              Piso:            Dpto:')
    c.drawString(0.5*cm, -28.4*cm,
     u'Localidad:                                               CP:                      Teléfono:')


def legajo_reverso(c):
    # Llevo arriba a la izquierda el origen
    c.translate(1.5*cm, 31.0*cm)
    c.drawImage("./images/dgce.png", 0.5*cm, 0.5*cm, 120, 40)
    c.drawString(13*cm, 1.3*cm, u'Gabinete social')
    c.drawString(13*cm, 0.5*cm, u'Provincia de Buenos Aires')
    # Recuadro salud
    c.drawString(0.8*cm, -0.5*cm, u'* INFORMACIÓN DE SALUD')
    c.rect(0, -1.6*cm, 18*cm, 1.0*cm)
    c.drawString(0.5*cm, -1.3*cm,
     u'Obra Social:                                                                            Nº Afiliado:')
    # Recuadro antecedentes
    c.rect(0, -4.8*cm, 18*cm, 3.2*cm)
    c.drawString(0.8*cm, -2.1*cm, u'* ANTECEDENTES DE ENFERMEDAD')
    c.drawString(0.5*cm, -2.7*cm,
     u'¿ Tiene alguna enfermedad que requiera periódicamente tratamiento o control médico?')
    c.drawString(0.5*cm, -3.3*cm, u'SI       NO         ¿Cuál?:')
    c.drawString(0.5*cm, -4.0*cm, u'Durante los últimos tres años, ¿Fue internado alguna vez?')
    c.drawString(0.5*cm, -4.7*cm, u'SI       NO         ¿Porqué?:')
    # Alergia
    c.rect(0, -6.7*cm, 18*cm, 1.9*cm)
    c.drawString(0.5*cm, -5.3*cm, u'* ¿TIENE ALGÚN TIPO DE ALERGIA?                    SI                NO')
    c.drawString(0.5*cm, -6.0*cm, u'En caso afirmativo, describa sus manifestaciones:')
    c.drawString(0.5*cm, -6.6*cm,
     u'La alergia se debe a:                     No sabe:         ¿Recibe tratamiento permanente? SI   NO')
    # Tratamientos
    c.rect(0, -9.8*cm, 18*cm, 3.1*cm)
    c.drawString(0.5*cm, -7.2*cm, u'* TRATAMIENTOS:')
    c.drawString(0.5*cm, -7.8*cm, u'¿Recibe tratamiento médico?:      SI        NO              Especifique:')
    c.drawString(0.5*cm, -8.4*cm, u'¿Quirúrgicos?:      SI        NO          Edad:              Tipo de Cirugía:')
    c.drawString(0.5*cm, -9.0*cm, u'¿Presenta alguna limitación física?:    SI       NO          Aclaración:')
    c.drawString(0.5*cm, -9.6*cm, u'Otros problemas de salud:')
    # No llenar los padres
    c.rect(0, -12.9*cm, 18*cm, 3.1*cm)
    c.line(1.5*cm, -12.9*cm, 1.5*cm, -9.8*cm)
    # Problema de salud en la escuela
    c.rect(0, -18*cm, 18*cm, 5.1*cm)
    c.drawString(0.5*cm, -13.5*cm, u'* SI EL ALUMNO TIENE ALGÚN PROBLEMA DE SALUD EN LA ESCUELA:')
    c.drawString(0.5*cm, -14.2*cm, u'Recurrir a:          Institución:')
    c.drawString(3.7*cm, -14.9*cm, u'Domicilio:                                            Teléfono:')
    c.line(0.5*cm, -15.1*cm, 17.5*cm, -15.1*cm)
    c.drawString(0.5*cm, -15.6*cm,
     u'Médico:              Apellidos:                                            Nombres:')
    c.drawString(3.7*cm, -16.3*cm, u'Domicilio:                                            Teléfono:')
    c.line(0.5*cm, -16.5*cm, 17.5*cm, -16.5*cm)
    c.drawString(0.5*cm, -17.0*cm,
     u'Familiar:             Apellidos:                                            Nombres:')
    c.drawString(3.7*cm, -17.7*cm, u'Domicilio:                                            Teléfono:')
    # Actualizaciones
    c.rect(0, -22.8*cm, 18*cm, 4.8*cm)
    c.drawString(0.5*cm, -18.5*cm, u'* ACTUALIZACIONES')
    c.drawString(0.5*cm, -19.2*cm,
     u'Fecha:...../...../.....    Anual:   SI       NO      ¿Hay cambios?:  SI      NO')
    c.drawString(0.5*cm, -19.9*cm, u'Describa los cambios en la salud del alumno:')
    c.line(0.5*cm, -20.1*cm, 17.5*cm, -20.1*cm)
    c.drawString(0.5*cm, -20.6*cm,
     u'Fecha:...../...../.....    Anual:   SI       NO      ¿Hay cambios?:  SI      NO')
    c.drawString(0.5*cm, -21.3*cm, u'Describa los cambios en la salud del alumno:')
    c.line(0.5*cm, -21.5*cm, 17.5*cm, -21.5*cm)
    c.drawString(0.5*cm, -22*cm,
     u'Fecha:...../...../.....    Anual:   SI       NO      ¿Hay cambios?:  SI      NO')
    c.drawString(0.5*cm, -22.7*cm, u'Describa los cambios en la salud del alumno:')
    # Final (vamos!!!)
    c.drawString(0.5*cm, -23.3*cm,
     u'Incorporar Constancia de Restricción Judicial para retirar al niño de la escuela')
    c.drawString(0.5*cm, -23.9*cm,
     u'La totalidad de los datos e información suministrada por quien suscribe la presente tiene ')
    c.drawString(0.5*cm, -24.4*cm,
     u'caracter de Declaración Jurada. El abajo firmante se compromete a comunicar al ')
    c.drawString(0.5*cm, -24.9*cm,
     u'establecimiento cualquier modificación de los datos suministrados en forma inmediata')
    c.drawString(0.5*cm, -25.4*cm, u'y de manera fehaciente.')
    c.drawString(0.5*cm, -28*cm,
     u'Fecha de inscripción: ..../..../......    .......................................      ......................................')
    c.drawString(7.2*cm, -28.6*cm, u'Firma del responsable                   Aclaración') 

c = canvas.Canvas("./planillas/legajo.pdf", pagesize=portrait(legal))
legajo(c)
c.showPage()
c.save()
c = canvas.Canvas("./planillas/legajo_reverso.pdf", pagesize=portrait(legal))
legajo_reverso(c)
c.showPage()
c.save()
