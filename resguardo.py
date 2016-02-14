#!/usr/bin/python
# -*- coding: UTF8 -*-
#
# archivo : resguardo.py
#
##############################################################################
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
##############################################################################


import os
import time
import wx

def resguardo_completo():
    source = ['/home/profe/svn/sanca/'] # Harcodeado para el proyecto PNUD
    target_dir = '/home/profe/Escritorio/' # Hardcodeado para el proyecto PNUD
    target = target_dir + time.strftime('%Y%m%d%H%M%S') + '_sancabase' + '.zip'
    zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
    if os.system(zip_command) == 0:
        wx.MessageBox(u'Tarea realizada con éxito', u'Backup completo', 
        wx.OK | wx.ICON_INFORMATION, None)
    else:
        wx.MessageBox(u'Fallo de tarea', u'Backup completo',
        wx.OK | wx.ICON_INFORMATION, None)

if __name__ == '__main__': main()
