#!/usr/bin/python
# -*- coding: UTF8 -*-
#
# archivo : sancabase.py debe tener permisos de ejecución
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

# Imports
import wx
import sys
import os
##import MySQLdb
##Se utilizará SQLite para realizar un trabajo local más rapido
import wx.lib.mixins.listctrl
import pickle
import imp
#import wx.gizmos as gizmos
from os import system

# Clase App
class App(wx.App):
    def OnInit(self):
        # Splash screen
        image = wx.Image("./images/splash.bmp", wx.BITMAP_TYPE_BMP)
        bmp = image.ConvertToBitmap()
        wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN |
        wx.SPLASH_TIMEOUT, 3000, None, -1)
        wx.Yield()
        # Fin splash screen
        #frame = Frame(u'SancaBase - Administrador general para Centros de Formación Profesional (Beta)', (30, 30), (800, 600))
        frame = Frame(u'SancaBase - Administrador general para Centros de Formación Profesional (Beta)', (30, 30), (800, 600))

        frame.CenterOnScreen()
        frame.Show()
        self.SetTopWindow(frame)
        return True

# Clase Frame
class Frame(wx.Frame):
    def __init__(self, title, pos, size):
        wx.Frame.__init__(self, None, -1, title, pos, size)

# Conexión a la base de datos
    archivoBBDD = "sancabase2.db"
    #def checkfile(archivoBBDD):
    import os.path
    if os.path.exists(archivoBBDD):
        print "El fichero existe"
    else:
        print "El fichero no existe"
        bbdd = archivoBBDD
        import sqlite3 as sql3
        conexion = sql3.connect(bbdd)
        cur = conexion.cursor()
        #cur.execute('''CREATE TABLE curso_%s (`id_alumno` VARCHAR(11) NOT NULL, `abandono` BOOL NOT NULL  DEFAULT '0', `dia` DATE NULL, `causa` TINYTEXT NULL, PRIMARY KEY (`id_alumno`))''')
        ##### Tabla Administrativos
        cur.execute ('''CREATE TABLE IF NOT EXISTS administrativos (
  id_administrativo integer PRIMARY KEY AUTOINCREMENT NOT NULL, cargo text(12)  NOT NULL,
  apellidos text(30)  NOT NULL,  nombres text(40)  NOT NULL,
  calle text(40)  NOT NULL, numero text(6)  NOT NULL,
  localidad text(30)  NOT NULL, telefono text(16)  NOT NULL,
  celular text(16)  default NULL, correo text(64)  default NULL)''')

#############################
        ##### Tabla Alumnos
        cur.execute('''CREATE TABLE IF NOT EXISTS alumnos (
  id_alumno integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  apellidos text(20) NOT NULL,
  nombres text(25) NOT NULL,
  sexo char(1) NOT NULL,
  tipo_doc text(3) NOT NULL,
  num_doc text(12) NOT NULL,
  nacionalidad char(2) NOT NULL,
  fecha_nac numeric NOT NULL,
  lugar_nac text(20) NOT NULL,
  calle_dom text(30) NOT NULL,
  num_dom text(5) NOT NULL,
  piso_dom text(2) default NULL,
  dpto_dom text(2) default NULL,
  cp_dom text(8) NOT NULL,
  localidad_dom text(25) NOT NULL,
  pcia_dom text(15) NOT NULL,
  tel_dom text(15) NOT NULL,
  estudios text(14) NOT NULL,
  hasta_est char(1) NOT NULL default '0',
  correo text(40) default NULL,
  nombre_madre text(30) default NULL,
  tipo_doc_madre text(3) default NULL,
  num_doc_madre text(8) default NULL,
  nac_madre char(2) default NULL,
  fecha_nac_madre numeric default NULL,
  ocupacion_madre text(30) default NULL,
  vive_madre INTEGER(1) default NULL,
  tel_contacto_madre text(15) default NULL,
  nombre_padre text(30) default NULL,
  tipo_doc_padre text(3) default NULL,
  num_doc_padre text(8) default NULL,
  nac_padre char(2) default NULL,
  fecha_nac_padre numeric default NULL,
  ocupacion_padre text(30) default NULL,
  vive_padre INTEGER(1) default NULL,
  tel_contacto_padre text(15) default NULL,
  trat_medico TEXT utf8_unicode_ci,
  observaciones TEXT utf8_unicode_ci,
  jefe INTEGER(1) NOT NULL,
  empleo text(30) NOT NULL,
  resp text(10) NOT NULL default 'No aplica',
  resp_esjefe char(1) default NULL,
  resp_nombre text(65) default NULL,
  resp_nac char(2) default NULL,
  resp_profesion text(30) default NULL,
  resp_condicion text(30) default NULL,
  resp_estudios text(14) default NULL,
  resp_hasta_estudios char(1) default NULL,
  resp_tipo_doc text(3) default NULL,
  resp_num_doc text(12) default NULL,
  resp_calle_dom text(30) default NULL,
  resp_num_dom text(5) default NULL,
  resp_piso_dom text(2) default NULL,
  resp_dpto_dom text(2) default NULL,
  resp_localidad_dom text(25) default NULL,
  resp_cp_dom text(8) default NULL,
  resp_te_dom text(15) default NULL,
  obra_social text(30) default NULL,
  num_afiliado text(15) default NULL,
  enfermedad char(1) NOT NULL default '0',
  enf_cual text(30) default NULL,
  internado char(1) NOT NULL default '0',
  int_por text(30) default NULL,
  alergia char(1) NOT NULL default '0',
  alergia_man text(40) default NULL,
  alergia_trat char(1) NOT NULL default '0',
  tratamiento char(1) NOT NULL default '0',
  trat_espec text(30) default NULL,
  quirurgico char(1) NOT NULL default '0',
  quir_edad text(2) default NULL,
  quir_tipo text(30) default NULL,
  limitacion char(1) NOT NULL default '0',
  limitacion_aclaracion text(30) default NULL,
  otros text(60) default NULL,
  institucion text(50) default NULL,
  institucion_dom text(30) default NULL,
  institucion_te text(15) default NULL,
  medico_apellido text(30) default NULL,
  medico_nombres text(30) default NULL,
  medico_dom text(30) default NULL,
  medico_te text(15) default NULL,
  familiar_apellido text(30) default NULL,
  familiar_nombres text(30) default NULL,
  familiar_dom text(30) default NULL,
  familiar_te text(15) default NULL)''')
        
        #######################################################
        #### Tabla Auxiliares
        cur.execute('''CREATE TABLE IF NOT EXISTS auxiliares (
  id_auxiliar integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  cargo text(12)  NOT NULL, apellidos text(30)  NOT NULL,
  nombres text(40)  NOT NULL, calle text(40)  NOT NULL,
  numero text(6)  NOT NULL, localidad text(30)  NOT NULL,
  telefono text(16)  NOT NULL, dni text(16)  default NULL,
  correo text(64)  NOT NULL, inicio date NOT NULL)''')
        #######################################################
        #### Tabla coordinadores
        cur.execute('''CREATE TABLE IF NOT EXISTS coordinadores (
  id_coordinador integer PRIMARY KEY AUTOINCREMENT  NOT NULL,
  apellidos text(20)  NOT NULL,  nombres text(25)  NOT NULL,
  te_contacto text(15)  NOT NULL,  celular text(16)  default NULL,
  calle text(30)  NOT NULL,  numero text(6)  default NULL,
  localidad text(30)  default NULL,  correo text(40)  default NULL)''')
        ######################################################
        #### Tabla Cursos
        cur.execute('''CREATE TABLE IF NOT EXISTS cursos (
  id_curso integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  num_curso text(5)  NOT NULL,  tipo text(3)  NOT NULL default 'FP',
  especialidad text(60)  NOT NULL,  instructor text(64)  NOT NULL,
  ciclo text(4)  NOT NULL default '2016',  fecha_inicio date NOT NULL,
  fecha_final date NOT NULL,  horas text(3)  NOT NULL,
  horario text(50)  NOT NULL default 'Lunes a viernes',
  establecimiento text(40)  NOT NULL,  estado char(1)  NOT NULL default 'A',
  motivo_baja text(30)  default NULL,  fecha_baja date default NULL)''')
        ######################################################
        #### Tabla Especialidades
        cur.execute('''CREATE TABLE IF NOT EXISTS especialidades (
  id_especialidad integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  denominacion text(60)  NOT NULL,  tipo text(3)  NOT NULL,
  duracion integer NOT NULL)''')
        #### Tabla Establecimientos
        cur.execute('''CREATE TABLE IF NOT EXISTS establecimientos (
  id_establecimiento integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  tipo text(3)  NOT NULL ,  numero char(3)  NOT NULL default '000',
  nombre text(40)  NOT NULL,  calle text(20)  NOT NULL,
  num_puerta text(5)  NOT NULL,  localidad text(25)  NOT NULL,
  cp text(8)  NOT NULL,  telefono text(15)  NOT NULL,
  correo text(40)  NOT NULL,  site text(64)  default 'http://',
  distrito text(20)  NOT NULL default 'Ingrese nombre',
  coordinador text(40)  NOT NULL)''')
        #### Tabla FichaCurso
        cur.execute ('''CREATE TABLE IF NOT EXISTS fichacurso (
  id_fc integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  apell_nom text(70)  NOT NULL,  nac text(20)  NOT NULL,
  fecha_nac date NOT NULL,  tipo_doc text(10)  NOT NULL,
  num_doc text(12)  NOT NULL,  domicilio text(70)  NOT NULL,
  sexo char(1)  NOT NULL)''')
        #### Tabla Gastos
        cur.execute('''CREATE TABLE IF NOT EXISTS gastos (
  id_gasto integer PRIMARY KEY AUTOINCREMENT NOT NULL ,
  fecha date NOT NULL,  tipo text(1)  NOT NULL default 'G',
  comprobante text(40)  default NULL,  responsable text(60)  NOT NULL,
  debe float default NULL,  haber float default NULL,
  destino text(30)  NOT NULL)''')
        ################################3
        #### Tabla Instructores
        cur.execute('''CREATE TABLE IF NOT EXISTS instructores (
  id_instructor integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  apellidos text(20)  NOT NULL,  nombres text(25)  NOT NULL,
  te_contacto text(15)  NOT NULL,  celular text(16)  default 'no tiene',
  calle text(30)  NOT NULL,  numero text(6)  default NULL,
  localidad text(30)  default NULL,  correo text(40)  NOT NULL)''')
        ###############################
        #### Tabla Legajo
        cur.execute('''CREATE TABLE IF NOT EXISTS legajo (
  id_legajo integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  id_alumno integer(11) NOT NULL,  nombre text(60)  NOT NULL,
  fechanac date NOT NULL,  lugarnac text(50)  NOT NULL,
  estcivil text(40)  NOT NULL,  domicilio text(60)  NOT NULL,
  te text(20)  NOT NULL,  plansocial integer(1) NOT NULL,
  queplan text(30)  NOT NULL,  planfamiliar integer(1) NOT NULL,
  queplanfamiliar text(30)  NOT NULL,  empleo text(40)  NOT NULL,
  ubicacionempleo text(40)  NOT NULL,  educformal text(50)  NOT NULL,
  abandono integer(1) NOT NULL,  causaabandono text(40)  NOT NULL,
  cursando integer(1) NOT NULL,  cursandolugar text(30)  NOT NULL,
  otroscursosfp integer(1) NOT NULL,  otroscursosfpcuales text(40)  NOT NULL,
  jefefamilia integer(1) NOT NULL,  deportes integer(1) NOT NULL,
  deportesdonde text(30)  NOT NULL,  tiempolibre text(60)  NOT NULL,
  eligioelcentro text(60)  NOT NULL,  eligioelcurso text(60)  NOT NULL,
  judiciales integer(1) NOT NULL,  causas text(100)  NOT NULL,
  tratmedico text(30)  NOT NULL,  observaciones text  NOT NULL)''')
        #######################################
        ### Tabla MiEscuela
        cur.execute ('''CREATE TABLE IF NOT EXISTS miescuela (
  id_miescuela integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre text(40)  NOT NULL,  calle text(30)  NOT NULL,
  numpuerta text(5)  NOT NULL,  cp text(8)  NOT NULL,
  localidad text(20)  NOT NULL,  telefono text(15)  default NULL,
  correo text(64)  default NULL,  site text(64)  default 'web')''')
        ######################################
        ##### Tabla Movimientos de Alumnos
        cur.execute('''CREATE TABLE IF NOT EXISTS mov_alumnos (
  id_alumno integer PRIMARY KEY AUTOINCREMENT NOT NULL, 
  tipomov text(1)  NOT NULL,  curso text(5)  NOT NULL,
  fecha date default NULL,  observaciones text)''')
        ######################################
        #### Tabla Seguimiento
        cur.execute('''CREATE TABLE IF NOT EXISTS seguimiento (
  id_seguimiento integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  id_alumno text(4)  NOT NULL,  rubro text(20)  NOT NULL,
  empresa text(30)  NOT NULL,  estado text(25)  NOT NULL,
  fecha date NOT NULL)''')
        #####################################
        #### Tabla Temporal
        cur.execute('''CREATE TABLE IF NOT EXISTS temporal (
  id_alumno integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  apellidos text(30)  NOT NULL,  nombres text(30)  NOT NULL,
  sexo char(1)  NOT NULL,  tipo_doc text(3)  NOT NULL,
  num_doc text(10)  NOT NULL)''')
####################################
        cur.close()
        ##self.db = MySQLdb.connect('localhost', 'javier', 'javier', 'escuela', charset='UTF8')

# Menúes
        menuBar = wx.MenuBar()
        menuArchivo = wx.Menu()
        menuBar.Append(menuArchivo, u'&Aplicación')
        actualizar = menuArchivo.Append(-1, u'Ac&tualizar', u'Actualizar la aplicación desde internet')
        exportar = menuArchivo.Append(-1, u'E&xportar', u'Hacer un backup de la base de datos')
        resguardo = menuArchivo.Append(-1, u'Res&guardo de planillas',
         u'Hacer un backup completo de planillas y legajos')
        salir = menuArchivo.Append(-1, u'&Salir', u'Salir de Sancabase')
        menuABM = wx.Menu()
        menuBar.Append(menuABM, u'A&BM')
        submenuAltas = wx.Menu()
        alta_alumno = submenuAltas.Append(-1, u'Estudi&antes', u'Altas de estudiantes')
        alta_curso = submenuAltas.Append(-1, u'&Cursos', u'Altas de cursos')
        alta_instructor = submenuAltas.Append(-1, u'&Instructores', u'Altas de instructores')
        alta_coordinador = submenuAltas.Append(-1, u'C&oordinadores/as', u'Altas de coordinadores o coordinadoras')
        alta_centro = submenuAltas.Append(-1, u'C&entros', u'Altas de Centros')
        alta_autoridades = submenuAltas.Append(-1, u'Ad&ministrativos/as',
         u'Alta de administrativos o administrativas')
        alta_auxiliares = submenuAltas.Append(-1, u'Au&xiliares', u'Alta de auxiliar')
        alta_legajoSocial = submenuAltas.Append(-1, u'&Legajo social', u'Alta de estudiante en legajo social')
        menuABM.AppendMenu(-1, u'Altas', submenuAltas)
        submenuModificaciones = wx.Menu()
        mod_alumnos = submenuModificaciones.Append(-1, u'Estudi&antes', u'Modificación de datos de estudiantes')
        mod_cursos = submenuModificaciones.Append(-1, u'&Cursos', u'Modificación de cursos')
        mod_instructor = submenuModificaciones.Append(-1, u'&Instructores/as',
         u'Modificación de instructores o instructoras')
        mod_centros = submenuModificaciones.Append(-1, u'C&entros', u'Modificación de centros')
        mod_coord = submenuModificaciones.Append(-1, u'C&oordinadores/as',
         u'Modificación de coordinadores o coordinadoras')
        mod_autoridades = submenuModificaciones.Append(-1, u'Ad&ministrativos', u'Modificación de administrativos')
        mod_auxiliares = submenuModificaciones.Append(-1, u'Au&xiliares', u'Modificación de auxiliares')
        mod_legajos = submenuModificaciones.Append(-1, u'Lega&jos sociales', u'Modificación de legajos sociales')
        agr_alumno = submenuModificaciones.Append(-1, u'Agre&gar estudiante a curso', u'Agregar estudiante a un curso ya abierto')
        menuABM.AppendMenu(-1, u'Modificaciones', submenuModificaciones)
        submenuBajasEgresos = wx.Menu()
        egresos = submenuBajasEgresos.Append(-1, u'&Fin de un curso', u'Finalización de curso')
        bajas = submenuBajasEgresos.Append(-1, u'&Deserción de un estudiante',
         u'Registro de baja de estudiante en un curso')
        seguimiento = submenuBajasEgresos.Append(-1, u'&Seguimiento de egresados',
         u'Agregado de novedades a egresado')
        menuABM.AppendMenu(-1, u'Bajas y egresos', submenuBajasEgresos)
        menuABM.AppendSeparator()
        datos_centro = menuABM.Append(-1, u'&Datos del Centro', u'Datos del Centro FP')
        menuListados = wx.Menu()
        menuBar.Append(menuListados, u'&Listados')
        submenuListados = wx.Menu()
        submenuFichas = wx.Menu()
        submenuStats = wx.Menu()
        menuBar.Append(submenuStats, u'Esta&dísticas')
        list_alumnos = submenuListados.Append(-1, u'A&lumnos', u'Lista los alumnos')
        list_cursos = submenuListados.Append(-1, u'&Cursos', u'Listado de cursos')
        list_inst = submenuListados.Append(-1, u'&Instructores', u'Listado de instructores')
        list_coord = submenuListados.Append(-1, u'C&oordinadores', u'Listado de coordinadores')
        list_centros = submenuListados.Append(-1, u'C&entros', u'Listado de centros de FP')
        list_autoridades = submenuListados.Append(-1, u'A&dministrativos', u'Listado de administrativos')
        list_auxiliares = submenuListados.Append(-1, u'Au&xiliares', u'Listado de auxiliares')
        list_egresados = submenuListados.Append(-1, u'Se&guimiento de Egresados',
         u'Listado del seguimiento de egresados')
        menuListados.AppendMenu(-1, u'Listados', submenuListados)
        ficha_alumnos = submenuFichas.Append(-1, u'Ficha de estudi&ante', u'Ficha de estudiante')
        ficha_cursos = submenuFichas.Append(-1, u'Ficha de c&urso completa', u'Ficha de curso')
        acta_examen = submenuFichas.Append(-1, u'Ac&ta de examen completa',
         u'Confeccionar una ficha de examen completa')
        certificados = submenuFichas.Append(-1, u'Con&fección de certificados', u'Certificados oficiales')
        legajos_por_curso = submenuFichas.Append(-1, u'Confección de &Legajos', u'Legajos oficiales')
        menuListados.AppendMenu(-1, u'Fichas y actas', submenuFichas)
        list_stats = submenuStats.Append(-1, u'&Generales Actuales',
         u'Estadísticas generales de los módulos actuales')
        list_stats_anual_actual = submenuStats.Append(-1, u'Genera&les por año',
         u'Estadísticas generales del año en curso')
        menuGastos = wx.Menu()
        menuBar.Append(menuGastos, u'&Caja chica')
        ingreso_gastos = menuGastos.Append(-1, u'&Ingreso de movimiento', u'Ingreso de movimientos de caja')
        listado_gastos_fecha = menuGastos.Append(-1, u'Listado de movimientos por &fecha',
         u'Listado de movimientos en un período de tiempo')
        listado_gastos_destino = menuGastos.Append(-1, u'Listado de movmientos por &destino/origen',
         u'Listado de movimientos clasificados por destino/origen')
        listado_gastos_responsable = menuGastos.Append(-1, u'Listado de movimientos por resp&onsable',
         u'Listado de movimientos clasificados por responsable de los mismos')
        menuGastos.AppendSeparator()
        gastos_nuevos_per = menuGastos.Append(-1, u'&Nuevo por período',
         u'Abre una planilla de gastos nueva por período')
        gastos_nuevos_proy = menuGastos.Append(-1, u'N&uevo por proyecto',
         u'Abre una planilla de gastos nueva por proyecto')
        menuGastos.AppendSeparator()
        abrir_gastos_per = menuGastos.Append(-1, u'Abrir p&eríodo',
         u'Abre una planilla de gastos existente por período')
        abrir_gastos_proy = menuGastos.Append(-1, u'Abrir p&royecto',
         u'Abre una planilla de gastos existente por proyecto')
        menuGestiones = wx.Menu()
        menuBar.Append(menuGestiones, u'G&estiones')
        agenda = menuGestiones.Append(-1, u'Agen&da', u'Calendario y agenda')
        nuevagestion = menuGestiones.Append(-1, u'&Nueva gestión', u'Abre un documento en blanco')
        menuGestiones.AppendSeparator()
        menuGestiones.Append(-1, u'&Abrir', u'Abre un documento existente')
        menuPlanillas = wx.Menu()
        menuBar.Append(menuPlanillas, u'&Planillas vacías')
        temario = menuPlanillas.Append(-1, u'&Temario', u'Genera una planilla de temario vacía')
        fichacurso = menuPlanillas.Append(-1, u'&Ficha de curso', u'Genera una planilla de curso vacía')
        actaexamen = menuPlanillas.Append(-1, u'&Acta de examen', u'Genera un acta de examen vacía')
        legajo = menuPlanillas.Append(-1, u'Le&gajo', u'Genera anverso y reverso del legajo oficial')
        menuAyuda = wx.Menu()
        menuBar.Append(menuAyuda, u'Ay&uda')
        ayuda = menuAyuda.Append(-1, u'&Ayuda...', u'Ayuda')
        menuAyuda.AppendSeparator()
        about = menuAyuda.Append(-1, u'A&cerca de...', u'Info de esta aplicación')
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        self.SetStatusText(u'Sancabase - Administrador de Centros de FP')

# Bindeo de funciones del menú
        self.Bind(wx.EVT_MENU, self.OnActualizar, actualizar)
        self.Bind(wx.EVT_MENU, self.OnExportar, exportar)
        self.Bind(wx.EVT_MENU, self.OnResguardo, resguardo)
        self.Bind(wx.EVT_MENU, self.OnExit, salir)
        self.Bind(wx.EVT_MENU, self.OnAltaAlumno, alta_alumno)
        self.Bind(wx.EVT_MENU, self.OnAltaCurso, alta_curso)
        self.Bind(wx.EVT_MENU, self.OnAltaInstructor, alta_instructor)
        self.Bind(wx.EVT_MENU, self.OnAltaCoordinador, alta_coordinador)
        self.Bind(wx.EVT_MENU, self.OnAltaCentro, alta_centro)
        self.Bind(wx.EVT_MENU, self.OnAltaAdministrativos, alta_autoridades)
        self.Bind(wx.EVT_MENU, self.OnAltaAuxiliares, alta_auxiliares)
        self.Bind(wx.EVT_MENU, self.OnAltaLegajoSocial, alta_legajoSocial)
        self.Bind(wx.EVT_MENU, self.OnModAlumnos, mod_alumnos)
        self.Bind(wx.EVT_MENU, self.OnModCursos,mod_cursos)
        self.Bind(wx.EVT_MENU, self.OnModInstructores, mod_instructor)
        self.Bind(wx.EVT_MENU, self.OnModCoordinadores, mod_coord)
        self.Bind(wx.EVT_MENU, self.OnModCentros, mod_centros)
        self.Bind(wx.EVT_MENU, self.OnModAdministrativos, mod_autoridades)
        self.Bind(wx.EVT_MENU, self.OnModAuxiliares, mod_auxiliares)
        self.Bind(wx.EVT_MENU, self.OnModLegajos, mod_legajos)
        self.Bind(wx.EVT_MENU, self.OnAgregarAlumnos, agr_alumno)
        self.Bind(wx.EVT_MENU, self.OnEgresoCurso, egresos)
        self.Bind(wx.EVT_MENU, self.OnDesercion, bajas)
        self.Bind(wx.EVT_MENU, self.OnSeguimiento, seguimiento)
        self.Bind(wx.EVT_MENU, self.OnFichaAlumnos, ficha_alumnos)
        self.Bind(wx.EVT_MENU, self.OnFichaCursos, ficha_cursos)
        self.Bind(wx.EVT_MENU, self.OnActaExamenCompleta, acta_examen)
        self.Bind(wx.EVT_MENU, self.OnCertificados, certificados)
        self.Bind(wx.EVT_MENU, self.OnLegajosPorCurso, legajos_por_curso)
        self.Bind(wx.EVT_MENU, self.OnListAlumnos, list_alumnos)
        self.Bind(wx.EVT_MENU, self.OnListCursos, list_cursos)
        self.Bind(wx.EVT_MENU, self.OnListInstruc, list_inst)
        self.Bind(wx.EVT_MENU, self.OnListCoord, list_coord)
        self.Bind(wx.EVT_MENU, self.OnListCentros, list_centros)
        self.Bind(wx.EVT_MENU, self.OnListAdministrativos, list_autoridades)
        self.Bind(wx.EVT_MENU, self.OnListAuxiliares, list_auxiliares)
        self.Bind(wx.EVT_MENU, self.OnListSegEgresados, list_egresados)
        self.Bind(wx.EVT_MENU, self.OnEstadisticasGenerales, list_stats)
        self.Bind(wx.EVT_MENU, self.OnEstadisticasGeneralesAnualActual, list_stats_anual_actual)
        self.Bind(wx.EVT_MENU, self.OnDatosInstitucion, datos_centro)
        self.Bind(wx.EVT_MENU, self.OnIngresoGastos, ingreso_gastos)
        self.Bind(wx.EVT_MENU, self.OnListadoGastosFecha, listado_gastos_fecha)
        self.Bind(wx.EVT_MENU, self.OnListadoGastosDestino, listado_gastos_destino)
        self.Bind(wx.EVT_MENU, self.OnListadoGastosResponsable, listado_gastos_responsable)
        self.Bind(wx.EVT_MENU, self.OnGastNuPer, gastos_nuevos_per)
        self.Bind(wx.EVT_MENU, self.OnAbrGastPer, abrir_gastos_per)
        self.Bind(wx.EVT_MENU, self.OnGastNuProy, gastos_nuevos_proy)
        self.Bind(wx.EVT_MENU, self.OnAbrGastProy, abrir_gastos_proy)
        self.Bind(wx.EVT_MENU, self.OnAgenda, agenda)
        self.Bind(wx.EVT_MENU, self.OnNuevaGestion, nuevagestion)
        self.Bind(wx.EVT_MENU, self.OnTemario, temario)
        self.Bind(wx.EVT_MENU, self.OnFichadeCurso, fichacurso)
        self.Bind(wx.EVT_MENU, self.OnActaExamen, actaexamen)
        self.Bind(wx.EVT_MENU, self.OnLegajo, legajo)
        self.Bind(wx.EVT_MENU, self.OnAbout, about)
        self.Bind(wx.EVT_MENU, self.OnAyuda, ayuda)

# Salir
    def OnExit(self, evt):
    
        self.Close()

# Actualizar
    def OnActualizar(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Actualización Online', size=(300, 200))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            conectando = wx.StaticText(panel, -1, u"Conectado al repositorio... ", pos = (50, 30))
            actualizando = wx.StaticText(panel, -1, u" ", pos = (50, 50))
            salida = wx.TextCtrl(panel, -1, u'', pos= (50, 70), size=(200, 80), style=wx.TE_MULTILINE)
            vivo = system('ping -c 1 trac.usla.org.ar')
            self.frame.Show()
            if vivo == 0:
                actualizando.SetLabel(u'Iniciando actualización...')
                act = system('svn update > log.txt')
                f = open('log.txt', 'r')
                texto = f.readlines()
                f.close()
                texto = texto[0]
                texto = unicode(texto, "utf-8")
                if texto[:14] == u'En la revisión':
                    texto = u'Sancabase ya está actualizado a la última versión'
                salida.SetValue(unicode.encode(texto, "utf-8"))
                boton = wx.Button(panel, -1, u'Salir', pos = (180, 160))
                self.Bind(wx.EVT_BUTTON, self.OnCancelar, boton)
                
            else:
                self.frame.Destroy()
                wx.MessageBox(u'No se pudo conectar con el servidor - Compruebe la conexión a internet y pruebe nuevamente', u'Actualización automática', wx.OK | wx.ICON_ERROR, self)
                
            
# Exportar base de datos
    def OnExportar(self, evt):
        try:
            self.frame.Close()
        finally:
            wildcard = "Archivos sql (*.sql)|*.sql|"
            dlg = wx.FileDialog(
            self, message="Guardar archivo como ...", defaultDir=os.getcwd(), 
            defaultFile="", wildcard=wildcard, style=wx.SAVE
            )
            dlg.SetFilterIndex(2)
            dlg.SetFilename('escuela.sql')
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
            dlg.Destroy()
            os.system('mysqldump  -u javier -pjavier escuela > %s' % path)
            wx.MessageBox(u'Tarea realizada con éxito', u'Backup de la base de datos',
             wx.OK | wx.ICON_INFORMATION, self)
            return True
            
# Resguardo completo de datos
    def OnResguardo(self, evt):
        try:
            self.frame.Close()
        finally:
            import resguardo
            resguardo.resguardo_completo()


# Alta de alumno
    def OnAltaAlumno(self, evt):
        try:
            self.frame.Close()
        finally:
            import altaalumno
            self.frame = altaalumno.AltaEstudiante(self, -1, u'Alta de Estudiante', style = wx.DEFAULT_FRAME_STYLE)
            self.frame.CenterOnScreen()
            self.frame.Show(True)
            return True
            

# Alta de cursos
    def OnAltaCurso(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Alta de Curso', size=(500, 350))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Alta de Curso')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            cursoLbl = wx.StaticText(panel, -1, u'Curso N°:')
            self.numcurso = wx.TextCtrl(panel, -1, u'')
            self.numcurso.SetFocus()
            c = self.db.cursor()
            c.execute('''SELECT denominacion FROM especialidades ORDER BY denominacion ASC''')
            especialidades = c.fetchall()
            d = len(especialidades)
            StrEsp=[]
            for denominacion in range(0, d):
                StrEsp.append(especialidades[denominacion][0])
            especialidadLbl = wx.StaticText(panel, -1, u'Especialidad:')
            self.especialidad = wx.ComboBox(panel, -1, u'', (-1, -1), (-1, -1), StrEsp, wx.CB_DROPDOWN | wx.CB_READONLY)
            tipoLbl = wx.StaticText(panel, -1, u'Tipo:')
            self.tipo = wx.ComboBox(panel, -1, '',  (-1, -1), (-1, -1), '', wx.CB_DROPDOWN)
            instructorLbl = wx.StaticText(panel, -1, u'Instructor/a:')
            c.execute('''SELECT nombres, apellidos FROM instructores ORDER BY apellidos asc''')
            Instructores = c.fetchall()
            d = len(Instructores)
            StrIns=[]
            for instructor in range (0, d):
                StrIns.append(Instructores[instructor][0] + u' ' + Instructores[instructor][1])
            self.instructor = wx.ComboBox(panel, -1, '',  (-1, -1), (-1, -1), StrIns, wx.CB_DROPDOWN | wx.CB_READONLY)
            comienzoLbl = wx.StaticText(panel, -1, u'Fecha de inicio:')
            self.comienzo = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
            finalLbl = wx.StaticText(panel, -1, u'Fecha de finalización:')
            self.final = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
            horasLbl = wx.StaticText(panel, -1, u'Horas reloj')
            self.horas = wx.SpinCtrl(panel, -1)
            self.horas.SetRange(0, 1000)
            centroLbl = wx.StaticText(panel, -1, u'Centro:')
            c.execute("""SELECT nombre FROM establecimientos ORDER BY id_establecimiento""")
            centros = c.fetchall()
            c.close()
            d = len(centros)
            StrCentros=[]
            for centro in range (0, d):
                StrCentros.append(centros[centro][0])
            self.centro = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, StrCentros, wx.CB_DROPDOWN | wx.CB_READONLY)
            horarioLbl = wx.StaticText(panel, -1, u'Horarios:')
            self.horario = wx.TextCtrl(panel, -1, u'')
            asignaLbl = wx.StaticText(panel, -1, u'Asigna estudiantes')
            self.asigna = wx.CheckBox(panel, -1, '')
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 9)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(cursoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.numcurso, 0, wx.EXPAND)
            datosSizer.Add(especialidadLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.especialidad , 0, wx.EXPAND)
            datosSizer.Add(tipoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.tipo, 0, wx.EXPAND)
            datosSizer.Add(instructorLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.instructor, 0, wx.EXPAND)
            datosSizer.Add(comienzoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.comienzo, 0, wx.EXPAND)
            datosSizer.Add(finalLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.final, 0, wx.EXPAND)
            datosSizer.Add(horasLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.horas, 0, wx.EXPAND)
            datosSizer.Add(centroLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.centro, 0, wx.EXPAND)
            datosSizer.Add(horarioLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.horario, 0, wx.EXPAND)
            datosSizer.Add(asignaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.asigna, 0, wx.EXPAND)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            ppalSizer.Fit(self.frame)
            ppalSizer.SetSizeHints(self.frame)
            self.Bind(wx.EVT_COMBOBOX, self.OnSetEspecialidades, self.especialidad)
            self.Bind(wx.EVT_BUTTON, self.OnIngresarCurso, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

    def OnSetEspecialidades(self, evt):
        especialidad = self.especialidad.GetValue()
        c = self.db.cursor()
        c.execute('''SELECT tipo, duracion FROM especialidades WHERE denominacion = %s''', (especialidad))
        q = c.fetchall()
        c.close()
        tipo = q[0][0]
        duracion = q[0][1]
        self.tipo.SetValue(tipo)
        self.horas.SetValue(duracion)
        return

    def OnIngresarCurso(self, evt):
        self.num_curso = self.numcurso.GetValue()
        tipo = self.tipo.GetValue()
        especialidad = self.especialidad.GetValue()
        instructor =  self.instructor.GetValue()
        dia = self.comienzo.GetValue()
        ciclo = dia.GetYear()
        fecha_inicio = ('%04d/%02d/%02d' % (dia.GetYear(),
                                            dia.GetMonth()+1,
                                            dia.GetDay()))
        dia = self.final.GetValue()
        fecha_final = ('%04d/%02d/%02d' % (dia.GetYear(),
                                           dia.GetMonth()+1,
                                           dia.GetDay()))
        horas = self.horas.GetValue()
        establecimiento = self.centro.GetValue()
        horario = self.horario.GetValue()
        c = self.db.cursor()
        # Si se quiere asignar los alumnos ahora
        if self.asigna.IsChecked():
            c.execute('''SELECT id_alumno, apellidos, nombres,
                         num_doc FROM alumnos order by apellidos ASC''')
            q = c.fetchall()
            StrAlum = [(u'%d %s %s %s' % tuple(a)) for a in q]
            dlg = wx.MultiChoiceDialog( self, u'Estudiantes asignados al curso:',
                         u'Asignación de estudiantes', StrAlum)
        # Asigno los alumnos creando una tabla con el número de curso y la lleno
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelections()
                c.execute('''CREATE TABLE curso_%s (`id_alumno` VARCHAR(11) NOT NULL, `abandono` BOOL NOT NULL  DEFAULT '0', `dia` DATE NULL, `causa` TINYTEXT NULL, PRIMARY KEY (`id_alumno`))'''% str(self.num_curso))
                for x in selections:
                    id_alumno = q[x][0]
                    c.execute('''INSERT INTO curso_%s (id_alumno) VALUES (%s)'''% (str(self.num_curso), id_alumno))
                c.execute('''INSERT INTO cursos (num_curso, tipo, especialidad, instructor, ciclo, fecha_inicio, fecha_final, horas, establecimiento, horario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',  (self.num_curso, tipo, especialidad, instructor, ciclo, fecha_inicio, fecha_final, horas, establecimiento, horario))
                wx.MessageBox(u'Tarea realizada con éxito', u'Alta de Curso %s' % self.num_curso, wx.OK | wx.ICON_INFORMATION, self)
        # Si me echo atrás mato todo
            else:
                dlg.Destroy()
                self.frame.Close()
        # Si no asigné alumnos creo el curso y una tabla vacía con el número del mismo
        else:
            c.execute('''CREATE TABLE curso_%s (`id_alumno` VARCHAR(11) NOT NULL, `abandono` BOOL NOT NULL  DEFAULT '0', `dia` DATE NULL, `causa` TINYTEXT NULL, PRIMARY KEY (`id_alumno`));'''% str(self.num_curso))
            c.execute('''INSERT INTO cursos (num_curso, tipo, especialidad, instructor, ciclo, fecha_inicio, fecha_final, horas, establecimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);''', (self.num_curso, tipo, especialidad, instructor, ciclo, fecha_inicio, fecha_final, horas, establecimiento))
            wx.MessageBox(u'Tarea realizada con éxito', u'Alta de Curso %s' % self.num_curso,
             wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Close()

# Alta de instructores
    def OnAltaInstructor(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Alta de Instructor/a', size=(500, 350))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Alta de Instructor/a')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            apellLbl = wx.StaticText(panel, -1, u'Apellidos:')
            self.apellidos = wx.TextCtrl(panel, -1, '')
            self.apellidos.SetFocus()
            nomLbl = wx.StaticText(panel, -1, u'Nombres:')
            self.nombres = wx.TextCtrl(panel, -1, '')
            domicLbl = wx.StaticText(panel, -1, u'Calle, N°, Localidad:')
            self.calle  = wx.TextCtrl(panel, -1, '', size=(150,-1))
            self.numero = wx.TextCtrl(panel, -1, '', size=(50,-1))
            self.localidad   = wx.TextCtrl(panel, -1, '', size=(100,-1))
            telLbl = wx.StaticText(panel, -1, u'TE particular:')
            self.telefono = wx.TextCtrl(panel, -1, '')
            celLbl = wx.StaticText(panel, -1, u'Celular:')
            self.celular = wx.TextCtrl(panel, -1, '')
            emailLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
            self.correo = wx.TextCtrl(panel, -1, '')
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(apellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.apellidos, 0, wx.EXPAND)
            datosSizer.Add(nomLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.nombres, 0, wx.EXPAND)
            datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
            domicilioSizer.Add(self.calle, 1)
            domicilioSizer.Add(self.numero, 0, wx.LEFT|wx.RIGHT, 5)
            domicilioSizer.Add(self.localidad)
            datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
            datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.telefono, 0, wx.EXPAND)
            datosSizer.Add(celLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.celular, 0, wx.EXPAND)
            datosSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.correo, 0, wx.EXPAND)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            ppalSizer.Fit(self.frame)
            self.Bind(wx.EVT_BUTTON, self.OnIngresarInstructor, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            ppalSizer.SetSizeHints(self.frame)
            self.frame.Show()

    def OnIngresarInstructor(self, event):
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        celular = self.celular.GetValue()
        correo = self.correo.GetValue()
        c = self.db.cursor()
        c.execute('''INSERT INTO instructores (apellidos, nombres, calle, numero, localidad, te_contacto, celular, correo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',  (apellidos, nombres, calle, numero, localidad, telefono, celular, correo,))
        wx.MessageBox(u'Tarea realizada con éxito', u'Alta de Instructor/a ', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Close()



# Alta de coordinador
    def OnAltaCoordinador(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Alta de Coordinador/a', size=(500, 350))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Alta de Coordinador/a')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            apellLbl = wx.StaticText(panel, -1, u'Apellidos:')
            self.apellidos = wx.TextCtrl(panel, -1, '')
            self.apellidos.SetFocus()
            nomLbl = wx.StaticText(panel, -1, u'Nombres:')
            self.nombres = wx.TextCtrl(panel, -1, '')
            domicLbl = wx.StaticText(panel, -1, u'Calle, N°, Localidad:')
            self.calle  = wx.TextCtrl(panel, -1, '', size=(150,-1))
            self.numero = wx.TextCtrl(panel, -1, '', size=(50,-1))
            self.localidad   = wx.TextCtrl(panel, -1, '', size=(100,-1))
            telLbl = wx.StaticText(panel, -1, u'TE particular:')
            self.telefono = wx.TextCtrl(panel, -1, '')
            celLbl = wx.StaticText(panel, -1, u'Celular:')
            self.celular = wx.TextCtrl(panel, -1, '')
            emailLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
            self.correo = wx.TextCtrl(panel, -1, '')
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(apellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.apellidos, 0, wx.EXPAND)
            datosSizer.Add(nomLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.nombres, 0, wx.EXPAND)
            datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
            domicilioSizer.Add(self.calle, 1)
            domicilioSizer.Add(self.numero, 0, wx.LEFT|wx.RIGHT, 5)
            domicilioSizer.Add(self.localidad)
            datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
            datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.telefono, 0, wx.EXPAND)
            datosSizer.Add(celLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.celular, 0, wx.EXPAND)
            datosSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.correo, 0, wx.EXPAND)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            ppalSizer.Fit(self.frame)
            self.Bind(wx.EVT_BUTTON, self.OnIngresarCoordinador, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            ppalSizer.SetSizeHints(self.frame)
            self.frame.Show()

    def OnIngresarCoordinador(self, event):
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        celular = self.celular.GetValue()
        correo = self.correo.GetValue()
        c = self.db.cursor()
        c.execute('''INSERT INTO coordinadores (apellidos, nombres, calle, numero, localidad, te_contacto, celular, correo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',  (apellidos, nombres, calle, numero, localidad, telefono, celular, correo,))
        wx.MessageBox(u'Tarea realizada con éxito', u'Alta de Coordinador/a ', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Close()


# Alta de Centro
    def OnAltaCentro(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Alta de Centro', size=(500, 350))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Alta de Centro')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            escuelaLbl = wx.StaticText(panel, -1, u'Nombre:')
            self.escuela = wx.TextCtrl(panel, -1, u'')
            self.escuela.SetFocus()
            calleLbl = wx.StaticText(panel, -1, u'Calle, N°:')
            self.calle = wx.TextCtrl(panel, -1, u'')
            self.numero = wx.TextCtrl(panel, -1, u'')
            domicLbl = wx.StaticText(panel, -1, u'Localidad, CP:')
            self.localidad   = wx.TextCtrl(panel, -1, u'', size=(150,-1))
            self.codigo = wx.TextCtrl(panel, -1, '', size=(50,-1))
            telLbl = wx.StaticText(panel, -1, u'Teléfono:')
            self.telefono = wx.TextCtrl(panel, -1, u'')
            correoLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
            self.correo = wx.TextCtrl(panel, -1, u'')
            siteLbl = wx.StaticText(panel, -1, u'Web site:')
            self.site = wx.TextCtrl(panel, -1, u'')
            coordLbl = wx.StaticText(panel, -1, u'Coordinador/a:')
            c = self.db.cursor()
            c.execute("""SELECT nombres, apellidos FROM coordinadores ORDER BY id_coordinador""")
            coords = c.fetchall()
            c.close()
            StrCoord = [("%s %s" % tuple(a)) for a in coords]
            self.coordinador = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, StrCoord, wx.CB_DROPDOWN | wx.CB_READONLY)
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(escuelaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.escuela, 1, wx.EXPAND)
            datosSizer.Add(calleLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            cpSizer = wx.BoxSizer(wx.HORIZONTAL)
            cpSizer.Add(self.calle, 1)
            cpSizer.Add(self.numero, 1)
            datosSizer.Add(cpSizer, 0, wx.EXPAND)
            datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
            domicilioSizer.Add(self.localidad, 1)
            domicilioSizer.Add(self.codigo, 1)
            datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
            datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.telefono, 0, wx.EXPAND)
            datosSizer.Add(correoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.correo, 0, wx.EXPAND)
            datosSizer.Add(siteLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.site, 0, wx.EXPAND)
            datosSizer.Add(coordLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.coordinador, 0, wx.EXPAND)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            ppalSizer.Fit(self.frame)
            self.Bind(wx.EVT_BUTTON, self.OnIngresarCentro, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            ppalSizer.SetSizeHints(self.frame)
            self.frame.Show()

    def OnIngresarCentro(self, event):
        escuela = self.escuela.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        codigo = self.codigo.GetValue()
        telefono = self.telefono.GetValue()
        correo = self.correo.GetValue()
        site = self.site.GetValue()
        coordinador = self.coordinador.GetValue()
        c = self.db.cursor()
        c.execute('''INSERT INTO establecimientos (nombre, calle, num_puerta, localidad, cp, telefono, correo, site, coordinador) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',  (escuela, calle, numero, localidad, codigo, telefono, correo, site, coordinador))
        wx.MessageBox(u'Tarea realizada con éxito', u'Alta de Centro ', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Close()


# Alta de Administrativos
    def OnAltaAdministrativos(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Alta de Administrativo/a', size=(500, 350))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Alta de Administrativo/a')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            cargoLbl = wx.StaticText(panel, -1, u'Cargo:')
            StrCargos = [u'Director/a', u'Regente', u'Secretario/a', u'Preceptor/a']
            self.cargo = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, StrCargos, wx.CB_DROPDOWN | wx.CB_READONLY)
            apellLbl = wx.StaticText(panel, -1, u'Apellidos:')
            self.apellidos = wx.TextCtrl(panel, -1, '')
            self.apellidos.SetFocus()
            nomLbl = wx.StaticText(panel, -1, u'Nombres:')
            self.nombres = wx.TextCtrl(panel, -1, '')
            domicLbl = wx.StaticText(panel, -1, u'Calle, N°, Localidad:')
            self.calle  = wx.TextCtrl(panel, -1, '', size=(150,-1))
            self.numero = wx.TextCtrl(panel, -1, '', size=(50,-1))
            self.localidad   = wx.TextCtrl(panel, -1, '', size=(100,-1))
            telLbl = wx.StaticText(panel, -1, u'TE particular:')
            self.telefono = wx.TextCtrl(panel, -1, '')
            celLbl = wx.StaticText(panel, -1, u'Celular:')
            self.celular = wx.TextCtrl(panel, -1, '')
            emailLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
            self.correo = wx.TextCtrl(panel, -1, '')
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(cargoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.cargo, 0, wx.EXPAND)
            datosSizer.Add(apellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.apellidos, 0, wx.EXPAND)
            datosSizer.Add(nomLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.nombres, 0, wx.EXPAND)
            datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
            domicilioSizer.Add(self.calle, 1)
            domicilioSizer.Add(self.numero, 0, wx.LEFT|wx.RIGHT, 5)
            domicilioSizer.Add(self.localidad)
            datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
            datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.telefono, 0, wx.EXPAND)
            datosSizer.Add(celLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.celular, 0, wx.EXPAND)
            datosSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.correo, 0, wx.EXPAND)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            ppalSizer.Fit(self.frame)
            self.Bind(wx.EVT_BUTTON, self.OnIngresarAdministrativo, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            ppalSizer.SetSizeHints(self.frame)
            self.frame.Show()

    def OnIngresarAdministrativo(self, event):
        cargo = self.cargo.GetValue()
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        celular = self.celular.GetValue()
        correo = self.correo.GetValue()
        c = self.db.cursor()
        c.execute('''INSERT INTO administrativos (cargo, apellidos, nombres, calle, numero, localidad, telefono, celular, correo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''',  (cargo, apellidos, nombres, calle, numero, localidad, telefono, celular, correo))
        wx.MessageBox(u'Tarea realizada con éxito', u'Alta de Administrativo/a ', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Close()


# Alta de Auxiliares
    def OnAltaAuxiliares(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Alta de Auxiliar', size=(500, 350))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Alta de Auxiliar')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            cargoLbl = wx.StaticText(panel, -1, u'Cargo:')
            LstCargos = [u'Portero/a', u'Maestranza', u'Pañolero/a', u'Asesor/a', u'Médico/a', u'Jardinero/a', u'Contable', u'Cocinero/a']
            self.cargo = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, LstCargos, wx.CB_DROPDOWN)
            self.cargo.SetFocus()
            apellLbl = wx.StaticText(panel, -1, u'Apellidos:')
            self.apellidos = wx.TextCtrl(panel, -1, '')
            nomLbl = wx.StaticText(panel, -1, u'Nombres:')
            self.nombres = wx.TextCtrl(panel, -1, '')
            domicLbl = wx.StaticText(panel, -1, u'Calle, N°, Localidad:')
            self.calle  = wx.TextCtrl(panel, -1, '', size=(150,-1))
            self.numero = wx.TextCtrl(panel, -1, '', size=(50,-1))
            self.localidad   = wx.TextCtrl(panel, -1, '', size=(100,-1))
            telLbl = wx.StaticText(panel, -1, u'TE particular:')
            self.telefono = wx.TextCtrl(panel, -1, '')
            docLbl = wx.StaticText(panel, -1, u'Documento:')
            self.doc = wx.TextCtrl(panel, -1, '')
            emailLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
            self.correo = wx.TextCtrl(panel, -1, '')
            fechaLbl = wx.StaticText(panel, -1, u'Fecha de inicio:')
            self.fechaInicio = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(cargoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.cargo, 0, wx.EXPAND)
            datosSizer.Add(apellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.apellidos, 0, wx.EXPAND)
            datosSizer.Add(nomLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.nombres, 0, wx.EXPAND)
            datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
            domicilioSizer.Add(self.calle, 1)
            domicilioSizer.Add(self.numero, 0, wx.LEFT|wx.RIGHT, 5)
            domicilioSizer.Add(self.localidad)
            datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
            datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.telefono, 0, wx.EXPAND)
            datosSizer.Add(docLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.doc, 0, wx.EXPAND)
            datosSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.correo, 0, wx.EXPAND)
            datosSizer.Add(fechaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.fechaInicio, 0, wx.EXPAND)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            ppalSizer.Fit(self.frame)
            self.Bind(wx.EVT_BUTTON, self.OnIngresarAuxiliar, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            ppalSizer.SetSizeHints(self.frame)
            self.frame.Show()

    def OnIngresarAuxiliar(self, event):
        cargo = self.cargo.GetValue()
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        doc = self.doc.GetValue()
        correo = self.correo.GetValue()
        dia = self.fechaInicio.GetValue()
        inicio = ('%04d/%02d/%02d' % (dia.GetYear(), dia.GetMonth()+1, dia.GetDay()))
        c = self.db.cursor()
        c.execute('''INSERT INTO auxiliares (cargo, apellidos, nombres, calle, numero, localidad, telefono, dni, correo, inicio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',  (cargo, apellidos, nombres, calle, numero, localidad, telefono, doc, correo, inicio))
        wx.MessageBox(u'Tarea realizada con éxito', u'Alta de Auxiliar ', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Close()


# Alta de legajo social
    def OnAltaLegajoSocial(self, evt):
        try:
            self.frame.Close()
        finally:
            # Creo el diálogo para entrar el apellido del alumno a ingresar
            self.dialog = wx.TextEntryDialog(None, u'Ingrese el Apellido del estudiante', u'Legajo social de estudiantes', u'', style=wx.OK|wx.CANCEL)
            if self.dialog.ShowModal() == wx.ID_OK:
                self.apellido = self.dialog.GetValue()
            else:
                self.dialog.Destroy()
                return
            self.dialog.Destroy()
            # Creo el diálogo para seleccionar entre todos los que tienen el mismo apellido
            c = self.db.cursor()
            c.execute('''SELECT id_alumno, apellidos, nombres, num_doc FROM alumnos WHERE apellidos = %s''', (self.apellido))
            q = c.fetchall()
            c.close()
            StrAlum = [("%d %s %s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Estudiantes que cumplen el criterio de búsqueda:', u'Legajo social de estudiante', StrAlum)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.alumnoAingresar = q[selections][0]
                f = open('idLegajo', 'w')
                f.write('%s\n' % self.alumnoAingresar)
                f.close()
                from legajosocial import LegajoSocial
                self.frame = LegajoSocial(self, -1, u'Legajo Social', style = wx.DEFAULT_FRAME_STYLE)
                self.frame.CenterOnScreen()
                self.frame.Show(True)


# Datos de la Institución
    def OnDatosInstitucion(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Datos de la Institución', size=(500, 350))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Datos de la Institución')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            escuelaLbl = wx.StaticText(panel, -1, u'Nombre:')
            self.escuela = wx.TextCtrl(panel, -1, '')
            self.escuela.SetFocus()
            calleLbl = wx.StaticText(panel, -1, u'Calle, N°:')
            self.calle = wx.TextCtrl(panel, -1, '')
            self.numero = wx.TextCtrl(panel, -1, '')
            domicLbl = wx.StaticText(panel, -1, u'Localidad, CP:')
            self.localidad   = wx.TextCtrl(panel, -1, '', size=(150,-1))
            self.codigo = wx.TextCtrl(panel, -1, '', size=(50,-1))
            telLbl = wx.StaticText(panel, -1, u'Teléfono:')
            self.telefono = wx.TextCtrl(panel, -1, '')
            correoLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
            self.correo = wx.TextCtrl(panel, -1, '')
            siteLbl = wx.StaticText(panel, -1, u'Web site:')
            self.site = wx.TextCtrl(panel, -1, '')
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(escuelaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.escuela, 1, wx.EXPAND)
            datosSizer.Add(calleLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            cpSizer = wx.BoxSizer(wx.HORIZONTAL)
            cpSizer.Add(self.calle, 1)
            cpSizer.Add(self.numero, 1)
            datosSizer.Add(cpSizer, 0, wx.EXPAND)
            datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
            domicilioSizer.Add(self.localidad, 1)
            domicilioSizer.Add(self.codigo, 1)
            datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
            datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.telefono, 0, wx.EXPAND)
            datosSizer.Add(correoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.correo, 0, wx.EXPAND)
            datosSizer.Add(siteLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.site, 0, wx.EXPAND)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            ppalSizer.Fit(self.frame)
            self.Bind(wx.EVT_BUTTON, self.OnIngresarInstitucion, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            ppalSizer.SetSizeHints(self.frame)
            self.frame.Show()

    def OnIngresarInstitucion(self, event):
        escuela = self.escuela.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        codigo = self.codigo.GetValue()
        telefono = self.telefono.GetValue()
        correo = self.correo.GetValue()
        site = self.site.GetValue()
        c = self.db.cursor()
        c.execute('''TRUNCATE table miescuela''')
        c.execute('''INSERT INTO miescuela (nombre, calle, numpuerta, localidad, cp, telefono, correo, site) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''',  (escuela, calle, numero, localidad, codigo, telefono, correo, site))
        wx.MessageBox(u'Tarea realizada con éxito', u'Alta de Institución ', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Close()


# Ingreso de gastos por formulario
    def OnIngresoGastos(self,event):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Movimientos de caja', size=(400, 300))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Movimientos de caja')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            fechaLbl = wx.StaticText(panel, -1, u'Fecha:')
            self.fecha = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
            self.fecha.SetFocus()
            tipoLbl = wx.StaticText(panel, -1, u'Tipo:')
            LstTipo = [u'Gasto', u'Ingreso']
            self.tipo = wx.ComboBox(panel, -1, u'Gasto', (-1, -1), wx.DefaultSize, LstTipo, wx.CB_DROPDOWN)
            responsableLbl = wx.StaticText(panel, -1, u'Responsable:')
            self.responsable = wx.TextCtrl(panel, -1, u'')
            montoLbl = wx.StaticText(panel, -1, u'Monto: $')
            self.monto = wx.TextCtrl(panel, -1, '00.00')
            comprobanteLbl = wx.StaticText(panel, -1, u'Comprobante:')
            self.comprobante = wx.TextCtrl(panel, -1, u'')
            destinoLbl = wx.StaticText(panel, -1, u'Destino/Origen:')
            LstDestino = [u'Insumos', u'Servicios', u'Mantenimiento', u'Incentivos', u'Cargas sociales', u'Sueldos', u'Alimentos', u'Varios', u'Ayudarte', u'Cooperadora']
            self.destino = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, LstDestino, wx.CB_DROPDOWN)
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 9)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(fechaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.fecha, 0, wx.EXPAND)
            datosSizer.Add(tipoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.tipo, 0, wx.EXPAND)
            datosSizer.Add(responsableLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.responsable , 0, wx.EXPAND)
            datosSizer.Add(montoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.monto, 0, wx.EXPAND)
            datosSizer.Add(comprobanteLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.comprobante, 0, wx.EXPAND)
            datosSizer.Add(destinoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.destino, 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND| wx.BOTTOM, 10)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            self.Bind(wx.EVT_BUTTON, self.OnIngresarGasto, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            #ppalSizer.Fit(self.frame)
            #ppalSizer.SetSizeHints(self.frame)
            self.frame.Show()

    def OnIngresarGasto(self, evt):
        dia = self.fecha.GetValue()
        fecha = ('%04d/%02d/%02d' % (dia.GetYear(),
                                            dia.GetMonth()+1,
                                            dia.GetDay()))
        tipo = self.tipo.GetValue()
        comprobante = self.comprobante.GetValue()
        responsable = self.responsable.GetValue()
        destino = self.destino.GetValue()
        monto =  self.monto.GetValue()
        if tipo == 'Gasto':
            debe = -float(monto)
            tipo = u'g'
            haber = 0
        else:
            haber = float(monto)
            tipo = u'i'
            debe = 0
        c = self.db.cursor()
        c.execute('''INSERT INTO gastos (fecha, tipo, comprobante, responsable, destino, debe, haber) VALUES (%s, %s, %s, %s, %s, %s, %s);''', (fecha, tipo, comprobante, responsable, destino, debe, haber))
        wx.MessageBox(u'Tarea realizada con éxito', u'Ingreso de movimiento de caja',
        wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Close()

# Listado de gastos por fecha
    def OnListadoGastosFecha(self, event):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Listado de movimientos por fecha', size=(400, 200))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Listado de movimientos por fecha')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            desdeLbl = wx.StaticText(panel, -1, u'Desde fecha:')
            self.desde = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
            self.desde.SetFocus()
            hastaLbl = wx.StaticText(panel, -1, u'Hasta fecha:')
            self.hasta = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
            saveBtn = wx.Button(panel, -1, u'Listar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 9)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(desdeLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.desde, 0, wx.EXPAND)
            datosSizer.Add(hastaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.hasta , 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND| wx.BOTTOM, 10)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            self.Bind(wx.EVT_BUTTON, self.OnListarFecha, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

    def OnListarFecha(self, event):
        dia = self.desde.GetValue()
        desde = ('%04d/%02d/%02d' % (dia.GetYear(), dia.GetMonth()+1, dia.GetDay()))
        dia = self.hasta.GetValue()
        hasta = ('%04d/%02d/%02d' % (dia.GetYear(), dia.GetMonth()+1, dia.GetDay()))
        self.frame.Destroy()
        c = self.db.cursor()
        c.execute('''SELECT * from gastos WHERE %s<fecha AND fecha<%s ORDER BY fecha asc''', (desde, hasta))
        listado = c.fetchall()
        c.close()
        f = open('./py/movporfecha.py', 'w')
        f.write(u'# -*- coding: UTF8 -*-\n')
        f.write(u'\n')
        f.write(u'import datetime')
        f.write(u'\n')
        f.write(u'columns = ["Id", "Fecha", "Tipo", "Comprobante", "Persona responsable", "Debe", "Haber", "Destino"]\n'.encode('utf-8'))
        f.write('\n')
        f.write('rows = [\n')
        # paso todo a cadena porque lo necesito así
        for cadaobj in listado:
            reobj = list(cadaobj)
            item = str(cadaobj[0])
            reobj[0] = item
            item = str(cadaobj[1])
            reobj[1] = item
            item = str(cadaobj[2])
            if item == 'i':
                item = u'ingreso'
            else:
                item = u'gasto'
            reobj[2] = item
            item = str(cadaobj[5])
            reobj[5] = item
            item = str(cadaobj[6])
            reobj[6] = item
            f.write('%s,\n' % repr(reobj))
        f.write (']')
        f.close()
        self.frame = ListMovFechaFrame()
        self.frame.Show()


# Listado de gastos por destino
    def OnListadoGastosDestino(self, event):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Listado de movimientos por destino', size=(450, 200))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Listado de movimientos por destino')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            destinoLbl = wx.StaticText(panel, -1, u'Destino:')
            c = self.db.cursor()
            c.execute('''SELECT distinct destino FROM gastos ORDER BY destino asc''')
            destino = c.fetchall()
            LstDestinos=[]
            for item in destino:
                LstDestinos.append(item[0])
            c.close()
            self.destino = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, LstDestinos, wx.CB_DROPDOWN | wx.CB_READONLY)
            self.destino.SetFocus()
            saveBtn = wx.Button(panel, -1, u'Listar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 9)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(destinoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.destino, 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND| wx.BOTTOM, 10)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            self.Bind(wx.EVT_BUTTON, self.OnListarDestino, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

    def OnListarDestino(self, event):
        destino = self.destino.GetValue()
        self.frame.Destroy()
        c = self.db.cursor()
        c.execute('''SELECT * from gastos WHERE destino = %s ORDER BY fecha asc''', (destino))
        listado = c.fetchall()
        c.close()
        f = open('./py/movpordestino.py', 'w')
        f.write(u'# -*- coding: UTF8 -*-\n')
        f.write(u'\n')
        f.write(u'import datetime')
        f.write(u'\n')
        f.write(u'columns = ["Id", "Fecha", "Tipo", "Comprobante", "Persona responsable", "Debe", "Haber", "Destino"]\n'.encode('utf-8'))
        f.write('\n')
        f.write('rows = [\n')
        # paso todo a cadena porque lo necesito así
        for cadaobj in listado:
            reobj = list(cadaobj)
            item = str(cadaobj[0])
            reobj[0] = item
            item = str(cadaobj[1])
            reobj[1] = item
            item = str(cadaobj[2])
            if item == 'i':
                item = u'ingreso'
            else:
                item = u'gasto'
            reobj[2] = item
            item = str(cadaobj[5])
            reobj[5] = item
            item = str(cadaobj[6])
            reobj[6] = item
            f.write('%s,\n' % repr(reobj))
        f.write (']')
        f.close()
        self.frame = ListMovDestinoFrame()
        self.frame.Show()


# Listado de gastos por responsable
    def OnListadoGastosResponsable(self, event):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Listado de movimientos por responsable', size=(450, 200))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Listado de movimientos por responsable')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            responsableLbl = wx.StaticText(panel, -1, u'Responsable:')
            LstResponsables=[]
            c = self.db.cursor()
            c.execute('''SELECT distinct responsable FROM gastos ORDER BY responsable asc''')
            responsable = c.fetchall()
            for item in responsable:
                LstResponsables.append(item[0])
            c.close()
            self.responsable = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, LstResponsables, wx.CB_DROPDOWN | wx.CB_READONLY)
            self.responsable.SetFocus()
            saveBtn = wx.Button(panel, -1, u'Listar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 9)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(responsableLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.responsable, 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((20,20), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((20,20), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND| wx.BOTTOM, 10)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            self.Bind(wx.EVT_BUTTON, self.OnListarResponsable, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

    def OnListarResponsable(self, event):
        responsable = self.responsable.GetValue()
        self.frame.Destroy()
        c = self.db.cursor()
        c.execute('''SELECT * from gastos WHERE responsable = %s ORDER BY fecha asc''', (responsable))
        listado = c.fetchall()
        c.close()
        f = open('./py/movporresponsable.py', 'w')
        f.write(u'# -*- coding: UTF8 -*-\n')
        f.write(u'\n')
        f.write(u'import datetime')
        f.write(u'\n')
        f.write(u'columns = ["Id", "Fecha", "Tipo", "Comprobante", "Persona responsable", "Debe", "Haber", "Destino"]\n'.encode('utf-8'))
        f.write('\n')
        f.write('rows = [\n')
        # paso todo a cadena porque lo necesito así
        for cadaobj in listado:
            reobj = list(cadaobj)
            item = str(cadaobj[0])
            reobj[0] = item
            item = str(cadaobj[1])
            reobj[1] = item
            item = str(cadaobj[2])
            if item == 'i':
                item = u'ingreso'
            else:
                item = u'gasto'
            reobj[2] = item
            item = str(cadaobj[5])
            reobj[5] = item
            item = str(cadaobj[6])
            reobj[6] = item
            f.write('%s,\n' % repr(reobj))
        f.write (']')
        f.close()
        self.frame = ListMovResponsableFrame()
        self.frame.Show()

# Modificación de Alumnos
    def OnModAlumnos(self, evt):
        try:
            self.frame.Close()
        finally:
            # Creo el diálogo para entrar el apellido del alumno a modificar
            self.dialog = wx.TextEntryDialog(None, u'Ingrese el Apellido del estudiante', u'Modificación de estudiantes', u'', style=wx.OK|wx.CANCEL)
            if self.dialog.ShowModal() == wx.ID_OK:
                self.apellido = self.dialog.GetValue()
            else:
                self.dialog.Destroy()
                return
            self.dialog.Destroy()
            # Creo el diálogo para seleccionar entre todos los que tienen el mismo apellido
            c = self.db.cursor()
            c.execute('''SELECT id_alumno, apellidos, nombres, num_doc FROM alumnos WHERE apellidos = %s''', (self.apellido))
            q = c.fetchall()
            StrAlum = [("%d %s %s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Estudiantes que cumplen el criterio de búsqueda:', u'Modificación de estudiantes', StrAlum)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.alumnoAmodificar = q[selections][0]
                f = open('modestudiante', 'w')
                f.write(str(self.alumnoAmodificar))
                f.close()
                import modalumno
                reload(modalumno)
                modalumno.ModEstudiante(self)
                
                return True

# Modificación de Cursos
    def OnModCursos(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Modificación de cursos', size=(380, 180))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Modificación de Curso')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            modLbl = wx.StaticText(panel, -1, u'Tipo de modificación:')
            ListCambios = [u'Cambio de datos del curso', u'Modificación de matrícula']
            self.cambios = wx.ComboBox(panel, -1, u'Cambio de datos del curso', (-1, -1), (-1, -1), ListCambios, wx.CB_DROPDOWN|wx.CB_READONLY)
            self.cambios.SetFocus()
            numCursoLbl = wx.StaticText(panel, -1, u'N° curso:')
            c = self.db.cursor()
            c.execute('''SELECT num_curso FROM cursos ORDER BY num_curso ASC''')
            cursos = c.fetchall()
            c.close()
            ListCursos = []
            for curso in cursos:
                ListCursos.append(curso[0])
            self.numCurso = wx.ComboBox(panel, -1, u'Seleccione', (-1, -1), (-1, -1), ListCursos, wx.CB_DROPDOWN|wx.CB_READONLY)
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(modLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.cambios, 0, wx.EXPAND)
            datosSizer.Add(numCursoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.numCurso, 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((30,25), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
            panel.SetSizer(ppalSizer)
            tipomod = self.cambios.GetValue()
            if tipomod == u'Cambio de datos del curso':
                self.Bind(wx.EVT_BUTTON, self.OnModifCursos, saveBtn)
            else:
                self.Bind(wx.EVT_BUTTON, self.OnModCursosPorAlumno, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

# Procesamiento de modificación de curso:
    def OnModifCursos(self, evt):
        try:
            self.frame.Close()
        finally:
            tipomod = self.cambios.GetValue()
            numCurso = self.numCurso.GetValue()
            self.numcurso = numCurso
            if tipomod == u'Cambio de datos del curso':
                self.frame = wx.Frame(self, -1, u'Modificación de Curso %s'% numCurso, size=(400, 350))
                self.frame.CenterOnScreen()
                panel = wx.Panel(self.frame)
                topLbl = wx.StaticText(panel, -1, u'Modificación de Curso %s' % numCurso)
                topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
                c = self.db.cursor()
                c.execute('''SELECT * from cursos WHERE num_curso = %s ''', numCurso)
                q = c.fetchone()
                self.id_curso = q[0]
                cursoLbl = wx.StaticText(panel, -1, u'Curso N°:')
                self.numcurso = wx.TextCtrl(panel, -1, u'%s' % numCurso)
                self.numcurso.SetFocus()
                c.execute('''SELECT denominacion FROM especialidades ORDER BY denominacion ASC''')
                especialidades = c.fetchall()
                d = len(especialidades)
                StrEsp=[]
                for denominacion in range(0, d):
                    StrEsp.append(especialidades[denominacion][0])
                especialidadLbl = wx.StaticText(panel, -1, u'Especialidad:')
                self.especialidad = wx.ComboBox(panel, -1, u'%s' % q[3], (-1, -1), (-1, -1), StrEsp, wx.CB_DROPDOWN | wx.CB_READONLY)
                tipoLbl = wx.StaticText(panel, -1, u'Tipo:')
                self.tipo = wx.ComboBox(panel, -1, u'%s' % q[2],  (-1, -1), (-1, -1), '', wx.CB_DROPDOWN)
                instructorLbl = wx.StaticText(panel, -1, u'Instructor/a:')
                c.execute('''SELECT nombres, apellidos FROM instructores ORDER BY apellidos asc''')
                Instructores = c.fetchall()
                d = len(Instructores)
                StrIns=[]
                for instructor in range (0, d):
                    StrIns.append(Instructores[instructor][0] + ' ' + Instructores[instructor][1])
                self.instructor = wx.ComboBox(panel, -1, u'%s' % q[4],  (-1, -1), (-1, -1), StrIns, wx.CB_DROPDOWN | wx.CB_READONLY)
                comienzoLbl = wx.StaticText(panel, -1, u'Fecha de inicio:')
                self.comienzo = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
                com = q[6]
                dia = com.day
                mes = com.month
                anio = com.year
                comienzo = wx.DateTimeFromDMY(dia,mes-1,anio)
                self.comienzo.SetValue(comienzo)
                finalLbl = wx.StaticText(panel, -1, u'Fecha de finalización:')
                self.final = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
                fin = q[7]
                dia = fin.day
                mes = fin.month
                anio = fin.year
                final = wx.DateTimeFromDMY(dia,mes-1,anio)
                self.final.SetValue(final)
                horasLbl = wx.StaticText(panel, -1, u'Horas reloj')
                self.horas = wx.SpinCtrl(panel, -1)
                self.horas.SetRange(0, 1000)
                self.horas.SetValue(int(q[8]))
                centroLbl = wx.StaticText(panel, -1, u'Centro:')
                c.execute("""SELECT nombre FROM establecimientos ORDER BY id_establecimiento""")
                centros = c.fetchall()
                c.close()
                d = len(centros)
                StrCentros=[]
                for centro in range (0, d):
                    StrCentros.append(centros[centro][0])
                self.centro = wx.ComboBox(panel, -1, u'%s' % q[10], (-1, -1), wx.DefaultSize, StrCentros, wx.CB_DROPDOWN | wx.CB_READONLY)
                horarioLbl = wx.StaticText(panel, -1, u'Horarios:')
                self.horario = wx.TextCtrl(panel, -1, u'%s' % q[9])
                saveBtn = wx.Button(panel, -1, u'&Aceptar')
                cancelBtn = wx.Button(panel, -1, u'&Cancelar')
                ppalSizer = wx.BoxSizer(wx.VERTICAL)
                ppalSizer.Add(topLbl, 0, wx.ALL, 9)
                ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
                datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
                datosSizer.AddGrowableCol(1)
                datosSizer.Add(cursoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.numcurso, 0, wx.EXPAND)
                datosSizer.Add(especialidadLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.especialidad , 0, wx.EXPAND)
                datosSizer.Add(tipoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.tipo, 0, wx.EXPAND)
                datosSizer.Add(instructorLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.instructor, 0, wx.EXPAND)
                datosSizer.Add(comienzoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.comienzo, 0, wx.EXPAND)
                datosSizer.Add(finalLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.final, 0, wx.EXPAND)
                datosSizer.Add(horasLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.horas, 0, wx.EXPAND)
                datosSizer.Add(centroLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.centro, 0, wx.EXPAND)
                datosSizer.Add(horarioLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.horario, 0, wx.EXPAND)
                ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
                btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(cancelBtn)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(saveBtn)
                btnSizer.Add((20,20), 1)
                ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
                panel.SetSizer(ppalSizer)
                ppalSizer.Fit(self.frame)
                ppalSizer.SetSizeHints(self.frame)
                self.Bind(wx.EVT_COMBOBOX, self.OnSetEspecialidades, self.especialidad)
                self.Bind(wx.EVT_BUTTON, self.OnDefinitiva, saveBtn)
                self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
                self.frame.Show()
            elif tipomod == u'Modificación de matrícula':
                import wx.gizmos as gizmos
                c = self.db.cursor()
                c.execute('''SELECT id_alumno FROM curso_%s order by id_alumno'''%  str(numCurso))
                q = c.fetchall()
                ListAlum = []
                for alumno in q:
                    c.execute('''SELECT id_alumno, apellidos, nombres,
                     num_doc FROM alumnos WHERE id_alumno = %s''', alumno)
                    r = c.fetchone()
                    #StrAlum = [("%d %s %s %s" % tuple(a)) for a in r]
                    ListAlum.append(str(r))
                c.close()    
                #ListAlum = [(u'%s' % tuple(a)) for a in q]
                self.dlg = wx.Frame(self, -1, u"Edición de estudiantes", size=(450, 400))
                self.dlg.CenterOnScreen()
                panel = wx.Panel(self.dlg, -1)
                titLbl = wx.StaticText(panel, -1, u'Lista del curso %s' % numCurso, pos = (5,15))
                self.elb = gizmos.EditableListBox(panel, -1, u'Editar listado', (50,50), (350, 250))
                cancelBtn = wx.Button(panel, -1, u'&Cancelar', pos = (200, 320))
                saveBtn = wx.Button(panel, -1, u'&Aceptar', pos = (330, 320))
                self.Bind(wx.EVT_BUTTON, self.OnModAlumnado, saveBtn)
                self.Bind(wx.EVT_BUTTON, self.OnCancelarMod, cancelBtn)
                self.elb.SetStrings(ListAlum)
                self.dlg.Show()

# Cancelar la modificación del alumnado (no sé porqué no funciona el cancelar de todos)
    def OnCancelarMod (self, evt):
        self.dlg.Close()

# Ingreso de modificación
    def OnDefinitiva(self, event):
        try:
            self.frame.Close()
        finally:
            num_curso = self.numcurso.GetValue()
            especialidad = self.especialidad.GetValue()
            tipo = self.tipo.GetValue()
            instructor = self.instructor.GetValue()
            dia = self.comienzo.GetValue()
            comienzo = ('%04d/%02d/%02d' % (dia.GetYear(),
                                           dia.GetMonth()+1,
                                           dia.GetDay()))
            ciclo = dia.GetYear()
            dia = self.final.GetValue()
            final = ('%04d/%02d/%02d' % (dia.GetYear(),
                                           dia.GetMonth()+1,
                                           dia.GetDay()))
            horas = str(self.horas.GetValue())
            centro = self.centro.GetValue()
            horario = self.horario.GetValue()
            c = self.db.cursor()
            c.execute(''' UPDATE cursos SET num_curso = %s, tipo = %s, especialidad = %s, instructor = %s, fecha_inicio = %s, ciclo = %s, fecha_final = %s, horas = %s, horario = %s, establecimiento = %s WHERE id_curso = %s''', (num_curso, tipo, especialidad, instructor, comienzo, ciclo, final, horas, horario, centro, self.id_curso))
            wx.MessageBox(u'Tarea realizada con éxito', u'Modificación de Curso ID: %s' % self.id_curso, wx.OK | wx.ICON_INFORMATION, self)
            c.close()
            self.frame.Destroy()

# Modificación de alumnos dentro del curso
    def OnModAlumnado(self, evt):
        try:
            self.frame.Close()
        finally:
            a = self.elb.GetStrings()
            self.dlg.Destroy()
            c = self.db.cursor()
            c.execute('''TRUNCATE table curso_%s'''% str(self.numcurso))
            for alumno in a:
                c.execute('''INSERT INTO `curso_%s` VALUES (%s, 0, null, null)''',
                 (int(self.numcurso), int(alumno)))
            c.close()

# Modificación de Instructores
    def OnModInstructores(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute("""SELECT id_instructor, apellidos, nombres FROM instructores ORDER BY id_instructor""")
            q = c.fetchall()
            StrInstructores = [("%s %s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Seleccione el/la instructora a modificar:', u'Modificación de instructor o instructora', StrInstructores)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.instAmodificar = q[selections][0]
                c. execute('''SELECT * FROM instructores WHERE id_instructor = %s''', (self.instAmodificar))
                q = c.fetchall()
                c.close()
                self.frame = wx.Frame(self, -1, u'Modificación de Instructor/a %s' % q[0][1], size=(500, 350))
                self.frame.CenterOnScreen()
                panel = wx.Panel(self.frame)
                topLbl = wx.StaticText(panel, -1, u'Modificación de Instructor/a %s' % q[0][1])
                topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
                apellLbl = wx.StaticText(panel, -1, u'Apellidos:')
                self.apellidos = wx.TextCtrl(panel, -1, '')
                self.apellidos.SetFocus()
                self.apellidos.SetValue(q[0][1])
                nomLbl = wx.StaticText(panel, -1, u'Nombres:')
                self.nombres = wx.TextCtrl(panel, -1, '')
                self.nombres.SetValue(q[0][2])
                domicLbl = wx.StaticText(panel, -1, u'Calle, N°, Localidad:')
                self.calle  = wx.TextCtrl(panel, -1, '', size=(150,-1))
                self.calle.SetValue(q[0][5])
                self.numero = wx.TextCtrl(panel, -1, '', size=(50,-1))
                self.numero.SetValue(q[0][6])
                self.localidad   = wx.TextCtrl(panel, -1, '', size=(100,-1))
                self.localidad.SetValue(q[0][7])
                telLbl = wx.StaticText(panel, -1, u'TE particular:')
                self.telefono = wx.TextCtrl(panel, -1, '')
                self.telefono.SetValue(q[0][3])
                celLbl = wx.StaticText(panel, -1, u'Celular:')
                self.celular = wx.TextCtrl(panel, -1, '')
                self.celular.SetValue(q[0][4])
                emailLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
                self.correo = wx.TextCtrl(panel, -1, '')
                self.correo.SetValue(q[0][8])
                saveBtn = wx.Button(panel, -1, u'&Aceptar')
                cancelBtn = wx.Button(panel, -1, u'&Cancelar')
                ppalSizer = wx.BoxSizer(wx.VERTICAL)
                ppalSizer.Add(topLbl, 0, wx.ALL, 5)
                ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
                datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
                datosSizer.AddGrowableCol(1)
                datosSizer.Add(apellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.apellidos, 0, wx.EXPAND)
                datosSizer.Add(nomLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.nombres, 0, wx.EXPAND)
                datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
                domicilioSizer.Add(self.calle, 1)
                domicilioSizer.Add(self.numero, 0, wx.LEFT|wx.RIGHT, 5)
                domicilioSizer.Add(self.localidad)
                datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
                datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.telefono, 0, wx.EXPAND)
                datosSizer.Add(celLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.celular, 0, wx.EXPAND)
                datosSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.correo, 0, wx.EXPAND)
                ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
                btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(saveBtn)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(cancelBtn)
                btnSizer.Add((20,20), 1)
                ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
                panel.SetSizer(ppalSizer)
                ppalSizer.Fit(self.frame)
                self.Bind(wx.EVT_BUTTON, self.OnMI, saveBtn)
                self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
                ppalSizer.SetSizeHints(self.frame)
                self.frame.Show()

# Actualización de la tabla instructores
    def OnMI(self, evt):
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        celular = self.celular.GetValue()
        correo = self.correo.GetValue()
        c = self.db.cursor()
        c.execute("""UPDATE instructores SET apellidos = %s, nombres = %s, calle = %s, numero = %s, localidad = %s, te_contacto = %s, celular = %s, correo = %s WHERE id_instructor = %s""", (apellidos, nombres, calle, numero, localidad, telefono, celular, correo, self.instAmodificar))
        wx.MessageBox(u'Tarea realizada con éxito', u'Modificación de Instructor/a %s' % apellidos, wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Destroy()

# Modificación de Coordinadores
    def OnModCoordinadores(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute("""SELECT id_coordinador, apellidos, nombres FROM coordinadores ORDER BY id_coordinador""")
            q = c.fetchall()
            StrCentros = [("%s %s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Seleccione el/la coordinador/a a modificar:', u'Modificación de coordinador/a', StrCentros)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.coordAmodificar = q[selections][0]
                c. execute('''SELECT * FROM coordinadores WHERE id_coordinador = %s''', (self.coordAmodificar))
                q = c.fetchall()
                c.close()
                self.frame = wx.Frame(self, -1, u'Modificación de coordinador/a %s' % q[0][1], size=(500, 350))
                self.frame.CenterOnScreen()
                panel = wx.Panel(self.frame)
                topLbl = wx.StaticText(panel, -1, u'Modificación de coordinador/a %s' % q[0][1])
                topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
                apellLbl = wx.StaticText(panel, -1, u'Apellidos:')
                self.apellidos = wx.TextCtrl(panel, -1, '')
                self.apellidos.SetFocus()
                self.apellidos.SetValue(q[0][1])
                nomLbl = wx.StaticText(panel, -1, u'Nombres:')
                self.nombres = wx.TextCtrl(panel, -1, '')
                self.nombres.SetValue(q[0][2])
                domicLbl = wx.StaticText(panel, -1, u'Calle, N°, Localidad:')
                self.calle  = wx.TextCtrl(panel, -1, '', size=(150,-1))
                self.calle.SetValue(q[0][5])
                self.numero = wx.TextCtrl(panel, -1, '', size=(50,-1))
                self.numero.SetValue(q[0][6])
                self.localidad   = wx.TextCtrl(panel, -1, '', size=(100,-1))
                self.localidad.SetValue(q[0][7])
                telLbl = wx.StaticText(panel, -1, u'TE particular:')
                self.telefono = wx.TextCtrl(panel, -1, '')
                self.telefono.SetValue(q[0][3])
                celLbl = wx.StaticText(panel, -1, u'Celular:')
                self.celular = wx.TextCtrl(panel, -1, '')
                self.celular.SetValue(q[0][4])
                emailLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
                self.correo = wx.TextCtrl(panel, -1, '')
                self.correo.SetValue(q[0][8])
                saveBtn = wx.Button(panel, -1, u'&Aceptar')
                cancelBtn = wx.Button(panel, -1, u'&Cancelar')
                ppalSizer = wx.BoxSizer(wx.VERTICAL)
                ppalSizer.Add(topLbl, 0, wx.ALL, 5)
                ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
                datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
                datosSizer.AddGrowableCol(1)
                datosSizer.Add(apellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.apellidos, 0, wx.EXPAND)
                datosSizer.Add(nomLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.nombres, 0, wx.EXPAND)
                datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
                domicilioSizer.Add(self.calle, 1)
                domicilioSizer.Add(self.numero, 0, wx.LEFT|wx.RIGHT, 5)
                domicilioSizer.Add(self.localidad)
                datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
                datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.telefono, 0, wx.EXPAND)
                datosSizer.Add(celLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.celular, 0, wx.EXPAND)
                datosSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.correo, 0, wx.EXPAND)
                ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
                btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(saveBtn)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(cancelBtn)
                btnSizer.Add((20,20), 1)
                ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
                panel.SetSizer(ppalSizer)
                ppalSizer.Fit(self.frame)
                self.Bind(wx.EVT_BUTTON, self.OnMCoo, saveBtn)
                self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
                ppalSizer.SetSizeHints(self.frame)
                self.frame.Show()

# Actualización de la tabla coordinadores
    def OnMCoo(self, evt):
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        celular = self.celular.GetValue()
        correo = self.correo.GetValue()
        c = self.db.cursor()
        c.execute("""UPDATE coordinadores SET apellidos = %s, nombres = %s, calle = %s, numero = %s, localidad = %s, te_contacto = %s, celular = %s, correo = %s WHERE id_instructor = %s""", (apellidos, nombres, calle, numero, localidad, telefono, celular, correo, self.instAmodificar))
        wx.MessageBox(u'Tarea realizada con éxito', u'Modificación de Coordinador/a %s' % apellidos, wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Destroy()


# Modificación de Centros
    def OnModCentros(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute("""SELECT id_establecimiento, nombre FROM establecimientos ORDER BY id_establecimiento""")
            q = c.fetchall()
            StrCentros = [("%s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Seleccione el Centro a Modificar:', u'Modificación de Centro FP', StrCentros)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                centroAmodificar = q[selections][0]
                c. execute('''SELECT * FROM establecimientos WHERE id_establecimiento = %s''', (centroAmodificar))
                q = c.fetchall()
                self.id_mod = centroAmodificar
                self.frame = wx.Frame(self, -1, u'Modificación de Centro %s' % q[0][3], size=(500, 350))
                self.frame.CenterOnScreen()
                panel = wx.Panel(self.frame)
                topLbl = wx.StaticText(panel, -1, u'Modificación de Centro %s' % q[0][3])
                topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
                escuelaLbl = wx.StaticText(panel, -1, u'Nombre:')
                self.escuela = wx.TextCtrl(panel, -1, u'')
                self.escuela.SetValue(q[0][3])
                self.escuela.SetFocus()
                calleLbl = wx.StaticText(panel, -1, u'Calle, N°:')
                self.calle = wx.TextCtrl(panel, -1, u'')
                self.calle.SetValue(q[0][4])
                self.numero = wx.TextCtrl(panel, -1, u'')
                self.numero.SetValue(q[0][5])
                domicLbl = wx.StaticText(panel, -1, u'Localidad, CP:')
                self.localidad = wx.TextCtrl(panel, -1, u'', size=(150,-1))
                self.localidad.SetValue(q[0][6])
                self.codigo = wx.TextCtrl(panel, -1, '', size=(50,-1))
                self.codigo.SetValue(q[0][7])
                telLbl = wx.StaticText(panel, -1, u'Teléfono:')
                self.telefono = wx.TextCtrl(panel, -1, u'')
                self.telefono.SetValue(q[0][8])
                correoLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
                self.correo = wx.TextCtrl(panel, -1, u'')
                self.correo.SetValue(q[0][9])
                siteLbl = wx.StaticText(panel, -1, u'Web site:')
                self.site = wx.TextCtrl(panel, -1, u'')
                self.site.SetValue(q[0][10])
                coordLbl = wx.StaticText(panel, -1, u'Coordinador/a:')
                c = self.db.cursor()
                c.execute("""SELECT nombres, apellidos FROM coordinadores ORDER BY id_coordinador""")
                coords = c.fetchall()
                c.close()
                StrCoord = [("%s %s" % tuple(a)) for a in coords]
                self.coordinador = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, StrCoord, wx.CB_DROPDOWN | wx.CB_READONLY)
                self.coordinador.SetValue(q[0][12])
                BtnAceptar = wx.Button(panel, -1, u'&Aceptar')
                BtnCancelar = wx.Button(panel, -1, u'&Cancelar')
                ppalSizer = wx.BoxSizer(wx.VERTICAL)
                ppalSizer.Add(topLbl, 0, wx.ALL, 5)
                ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
                datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
                datosSizer.AddGrowableCol(1)
                datosSizer.Add(escuelaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.escuela, 1, wx.EXPAND)
                datosSizer.Add(calleLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                cpSizer = wx.BoxSizer(wx.HORIZONTAL)
                cpSizer.Add(self.calle, 1)
                cpSizer.Add(self.numero, 1)
                datosSizer.Add(cpSizer, 0, wx.EXPAND)
                datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
                domicilioSizer.Add(self.localidad, 1)
                domicilioSizer.Add(self.codigo, 1)
                datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
                datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.telefono, 0, wx.EXPAND)
                datosSizer.Add(correoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.correo, 0, wx.EXPAND)
                datosSizer.Add(siteLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.site, 0, wx.EXPAND)
                datosSizer.Add(coordLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.coordinador, 0, wx.EXPAND)
                ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
                btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(BtnAceptar)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(BtnCancelar)
                btnSizer.Add((20,20), 1)
                ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
                panel.SetSizer(ppalSizer)
                ppalSizer.Fit(self.frame)
                self.Bind(wx.EVT_BUTTON, self.OnCancelar, BtnCancelar)
                self.Bind(wx.EVT_BUTTON, self.OnAceptarMCen, BtnAceptar)
                ppalSizer.SetSizeHints(self.frame)
                self.frame.Show(True)

# Actualización de tabla Centros de FP (establecimientos)
    def OnAceptarMCen(self, event):
        escuela = self.escuela.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        codigo = self.codigo.GetValue()
        telefono = self.telefono.GetValue()
        correo = self.correo.GetValue()
        site = self.site.GetValue()
        coordinador = self.coordinador.GetValue()
        c = self.db.cursor()
        c.execute("""UPDATE establecimientos SET nombre = %s, calle = %s, num_puerta = %s, localidad = %s, cp = %s, telefono = %s, correo = %s, site = %s, coordinador = %s WHERE id_establecimiento = %s""", (escuela, calle, numero, localidad, codigo, telefono, correo, site, coordinador, self.id_mod))
        wx.MessageBox(u'Tarea realizada con éxito', u'Modificación de Centro %s' % escuela, wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Destroy()

# Modificación de Administrativos
    def OnModAdministrativos(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute("""SELECT id_administrativo, apellidos, nombres FROM administrativos ORDER BY id_administrativo""")
            q = c.fetchall()
            StrAdministrativos = [("%s %s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Seleccione la persona a modificar:', u'Modificación de administrativo', StrAdministrativos)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.admAmodificar = q[selections][0]
                c. execute('''SELECT * FROM administrativos WHERE id_administrativo = %s''', (self.admAmodificar))
                q = c.fetchall()
                c.close()
                self.frame = wx.Frame(self, -1, u'Modificación de Administrativo/a %s' % q[0][2], size=(500, 350))
                self.frame.CenterOnScreen()
                panel = wx.Panel(self.frame)
                topLbl = wx.StaticText(panel, -1, u'Modificación de Administrativo/a %s ' % q[0][2])
                topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
                cargoLbl = wx.StaticText(panel, -1, u'Cargo:')
                StrCargos = [u'Director/a', u'Regente', u'Secretario/a', u'Preceptor/a']
                self.cargo = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, StrCargos, wx.CB_DROPDOWN | wx.CB_READONLY)
                self.cargo.SetValue(q[0][1])
                self.cargo.SetFocus()
                apellLbl = wx.StaticText(panel, -1, u'Apellidos:')
                self.apellidos = wx.TextCtrl(panel, -1, '')
                self.apellidos.SetValue(q[0][2])
                nomLbl = wx.StaticText(panel, -1, u'Nombres:')
                self.nombres = wx.TextCtrl(panel, -1, '')
                self.nombres.SetValue(q[0][3])
                domicLbl = wx.StaticText(panel, -1, u'Calle, N°, Localidad:')
                self.calle  = wx.TextCtrl(panel, -1, '', size=(150,-1))
                self.calle.SetValue(q[0][4])
                self.numero = wx.TextCtrl(panel, -1, '', size=(50,-1))
                self.numero.SetValue(q[0][5])
                self.localidad   = wx.TextCtrl(panel, -1, '', size=(100,-1))
                self.localidad.SetValue(q[0][6])
                telLbl = wx.StaticText(panel, -1, u'TE particular:')
                self.telefono = wx.TextCtrl(panel, -1, '')
                self.telefono.SetValue(q[0][7])
                celLbl = wx.StaticText(panel, -1, u'Celular:')
                self.celular = wx.TextCtrl(panel, -1, '')
                self.celular.SetValue(q[0][8])
                emailLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
                self.correo = wx.TextCtrl(panel, -1, '')
                self.correo.SetValue(q[0][9])
                saveBtn = wx.Button(panel, -1, u'&Aceptar')
                cancelBtn = wx.Button(panel, -1, u'&Cancelar')
                ppalSizer = wx.BoxSizer(wx.VERTICAL)
                ppalSizer.Add(topLbl, 0, wx.ALL, 5)
                ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
                datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
                datosSizer.AddGrowableCol(1)
                datosSizer.Add(cargoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.cargo, 0, wx.EXPAND)
                datosSizer.Add(apellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.apellidos, 0, wx.EXPAND)
                datosSizer.Add(nomLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.nombres, 0, wx.EXPAND)
                datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
                domicilioSizer.Add(self.calle, 1)
                domicilioSizer.Add(self.numero, 0, wx.LEFT|wx.RIGHT, 5)
                domicilioSizer.Add(self.localidad)
                datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
                datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.telefono, 0, wx.EXPAND)
                datosSizer.Add(celLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.celular, 0, wx.EXPAND)
                datosSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.correo, 0, wx.EXPAND)
                ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
                btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(saveBtn)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(cancelBtn)
                btnSizer.Add((20,20), 1)
                ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
                panel.SetSizer(ppalSizer)
                ppalSizer.Fit(self.frame)
                self.Bind(wx.EVT_BUTTON, self.OnMAD, saveBtn)
                self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
                ppalSizer.SetSizeHints(self.frame)
                self.frame.Show()

# Actualización de la tabla administrativos
    def OnMAD(self, evt):
        cargo = self.cargo.GetValue()
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        celular = self.celular.GetValue()
        correo = self.correo.GetValue()
        c = self.db.cursor()
        c.execute("""UPDATE administrativos SET cargo = %s, apellidos = %s, nombres = %s, calle = %s, numero = %s, localidad = %s, telefono = %s, celular = %s, correo = %s WHERE id_administrativo = %s""", (cargo, apellidos, nombres, calle, numero, localidad, telefono, celular, correo, self.admAmodificar))
        wx.MessageBox(u'Tarea realizada con éxito', u'Modificación de Administrativo/a', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Destroy()

# Modificación de Auxiliares
    def OnModAuxiliares(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute("""SELECT id_auxiliar, apellidos, nombres FROM auxiliares ORDER BY id_auxiliar""")
            q = c.fetchall()
            LstAuxiliares = [("%s %s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Seleccione la persona a modificar:', u'Modificación de auxiliar', LstAuxiliares)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.auxAmodificar = q[selections][0]
                c. execute('''SELECT * FROM auxiliares WHERE id_auxiliar = %s''', (self.auxAmodificar))
                q = c.fetchall()
                c.close()
                self.frame = wx.Frame(self, -1, u'Modificación de Auxiliar %s' % q[0][2], size=(500, 350))
                self.frame.CenterOnScreen()
                panel = wx.Panel(self.frame)
                topLbl = wx.StaticText(panel, -1, u'Modificación de Auxiliar %s ' % q[0][2])
                topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
                cargoLbl = wx.StaticText(panel, -1, u'Cargo:')
                LstCargos = [u'Portero/a', u'Maestranza', u'Pañolero/a', u'Asesor/a', u'Médico/a', u'Jardinero/a', u'Contable', u'Cocinero/a']
                self.cargo = wx.ComboBox(panel, -1, '', (-1, -1), wx.DefaultSize, LstCargos, wx.CB_DROPDOWN)
                self.cargo.SetValue(q[0][1])
                self.cargo.SetFocus()
                apellLbl = wx.StaticText(panel, -1, u'Apellidos:')
                self.apellidos = wx.TextCtrl(panel, -1, '')
                self.apellidos.SetValue(q[0][2])
                nomLbl = wx.StaticText(panel, -1, u'Nombres:')
                self.nombres = wx.TextCtrl(panel, -1, '')
                self.nombres.SetValue(q[0][3])
                domicLbl = wx.StaticText(panel, -1, u'Calle, N°, Localidad:')
                self.calle  = wx.TextCtrl(panel, -1, '', size=(150,-1))
                self.calle.SetValue(q[0][4])
                self.numero = wx.TextCtrl(panel, -1, '', size=(50,-1))
                self.numero.SetValue(q[0][5])
                self.localidad   = wx.TextCtrl(panel, -1, '', size=(100,-1))
                self.localidad.SetValue(q[0][6])
                telLbl = wx.StaticText(panel, -1, u'TE particular:')
                self.telefono = wx.TextCtrl(panel, -1, '')
                self.telefono.SetValue(q[0][7])
                dniLbl = wx.StaticText(panel, -1, u'Documento:')
                self.dni = wx.TextCtrl(panel, -1, '')
                self.dni.SetValue(q[0][8])
                emailLbl = wx.StaticText(panel, -1, u'Correo electrónico:')
                self.correo = wx.TextCtrl(panel, -1, '')
                self.correo.SetValue(q[0][9])
                fechaLbl = wx.StaticText(panel, -1, u'Fecha de inicio:')
                self.fechaInicio = wx.DatePickerCtrl(panel, -1, size=(120,-1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
                com = q[0][10]
                dia = com.day
                mes = com.month
                anio = com.year
                comienzo = wx.DateTimeFromDMY(dia,mes-1,anio)
                self.fechaInicio.SetValue(comienzo)
                saveBtn = wx.Button(panel, -1, u'&Aceptar')
                cancelBtn = wx.Button(panel, -1, u'&Cancelar')
                ppalSizer = wx.BoxSizer(wx.VERTICAL)
                ppalSizer.Add(topLbl, 0, wx.ALL, 5)
                ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
                datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
                datosSizer.AddGrowableCol(1)
                datosSizer.Add(cargoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.cargo, 0, wx.EXPAND)
                datosSizer.Add(apellLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.apellidos, 0, wx.EXPAND)
                datosSizer.Add(nomLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.nombres, 0, wx.EXPAND)
                datosSizer.Add(domicLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                domicilioSizer = wx.BoxSizer(wx.HORIZONTAL)
                domicilioSizer.Add(self.calle, 1)
                domicilioSizer.Add(self.numero, 0, wx.LEFT|wx.RIGHT, 5)
                domicilioSizer.Add(self.localidad)
                datosSizer.Add(domicilioSizer, 0, wx.EXPAND)
                datosSizer.Add(telLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.telefono, 0, wx.EXPAND)
                datosSizer.Add(dniLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.dni, 0, wx.EXPAND)
                datosSizer.Add(emailLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.correo, 0, wx.EXPAND)
                datosSizer.Add(fechaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.fechaInicio, 0, wx.EXPAND)
                ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
                btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(saveBtn)
                btnSizer.Add((20,20), 1)
                btnSizer.Add(cancelBtn)
                btnSizer.Add((20,20), 1)
                ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
                panel.SetSizer(ppalSizer)
                ppalSizer.Fit(self.frame)
                self.Bind(wx.EVT_BUTTON, self.OnModAux, saveBtn)
                self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
                ppalSizer.SetSizeHints(self.frame)
                self.frame.Show()

# Actualización de la tabla auxiliares
    def OnModAux(self, evt):
        cargo = self.cargo.GetValue()
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        dni = self.dni.GetValue()
        correo = self.correo.GetValue()
        dia = self.fechaInicio.GetValue()
        inicio = ('%04d/%02d/%02d' % (dia.GetYear(), dia.GetMonth()+1, dia.GetDay()))
        c = self.db.cursor()
        c.execute("""UPDATE auxiliares SET cargo = %s, apellidos = %s, nombres = %s, calle = %s, numero = %s, localidad = %s, telefono = %s, dni = %s, correo = %s, inicio = %s WHERE id_auxiliar = %s""", (cargo, apellidos, nombres, calle, numero, localidad, telefono, dni, correo, inicio, self.auxAmodificar))
        wx.MessageBox(u'Tarea realizada con éxito', u'Modificación de Auxiliar', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Destroy()


# Modificación de Legajos
    def OnModLegajos(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute ('''SELECT id_legajo, id_alumno, nombre FROM legajo order by id_legajo''')
            q = c.fetchall()
            StrAlum = [(u'%d %d %s' % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog( self, u'Estudiantes que ya tienen legajo social:',
                         u'Modificación de legajo social', StrAlum)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.legajoAmodificar = q[selections][0]
                c. execute('''SELECT * FROM legajo WHERE id_legajo = %s''', (self.legajoAmodificar))
                q = c.fetchone()
                c.close()
                f = open('idLegajoMod', 'w')
                f.write('%s\n' % q[0])
                f.close()
                from legajosocialcargado import LegajoSocialCargado
                self.frame = LegajoSocialCargado(self, -1, u'Modificación de Legajo Social',
                 style = wx.DEFAULT_FRAME_STYLE)
                self.frame.CenterOnScreen()
                self.frame.Show(True)

# Agregar estudiante a un curso abierto
    def OnAgregarAlumnos(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Agregar estudiante a un curso', size=(320, 180))
            panel = wx.Panel(self.frame, -1)
            cursoLbl = wx.StaticText(panel, -1, u'Seleccione el curso a modificar: ', (50, 20))
            cursoLbl = wx.StaticText(panel, -1, u'Curso: ', (50, 50))
            c = self.db.cursor()
            c.execute('''SELECT num_curso FROM cursos ORDER BY num_curso ASC''')
            cursos = c.fetchall()
            c.close()
            LstCursos = []
            for curso in cursos:
                LstCursos.append(curso[0])
            self.cursoList = wx.ComboBox(panel, -1, '', (120, 45), wx.DefaultSize, LstCursos, wx.CB_DROPDOWN)
            btnCancelar = wx.Button(panel, -1, u'&Cancelar', pos = (100, 100))
            btnAceptar = wx.Button(panel, -1, u'&Aceptar', pos = (200, 100))
            self.Bind(wx.EVT_BUTTON, self.OnAgrAlum, btnAceptar)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, btnCancelar)
            self.frame.CentreOnScreen()
            self.frame.Show()
            
# Listar los alumnos a agregar a un curso ya iniciado
    def OnAgrAlum(self, evt):
        num_curso = self.cursoList.GetValue()
        self.frame.Close()
        c = self.db.cursor()
        c.execute('''SELECT id_alumno, apellidos, nombres,
                         num_doc FROM alumnos order by apellidos ASC''')
        q = c.fetchall()
        StrAlum = [(u'%d %s %s %s' % tuple(a)) for a in q]
        dlg = wx.MultiChoiceDialog( self, u'Estudiantes agregados al curso:',
                         u'Agregar estudiantes', StrAlum)
        if (dlg.ShowModal() == wx.ID_OK):
            selections = dlg.GetSelections()
            for x in selections:
                id_alumno = q[x][0]
                c.execute('''INSERT INTO curso_%s (id_alumno) VALUES (%s)'''% (str(num_curso), id_alumno))
                wx.MessageBox(u'Tarea realizada con éxito', u'Actualización de Curso %s' % num_curso, wx.OK | wx.ICON_INFORMATION, self)
        c.close()

        

# Actualización de la tabla administrativos
    def OnModAux(self, evt):
        cargo = self.cargo.GetValue()
        apellidos = self.apellidos.GetValue()
        nombres = self.nombres.GetValue()
        calle = self.calle.GetValue()
        numero = self.numero.GetValue()
        localidad = self.localidad.GetValue()
        telefono = self.telefono.GetValue()
        dni = self.dni.GetValue()
        correo = self.correo.GetValue()
        dia = self.fechaInicio.GetValue()
        inicio = ('%04d/%02d/%02d' % (dia.GetYear(), dia.GetMonth()+1, dia.GetDay()))
        c = self.db.cursor()
        c.execute("""UPDATE auxiliares SET cargo = %s, apellidos = %s, nombres = %s, calle = %s, numero = %s, localidad = %s, telefono = %s, dni = %s, correo = %s, inicio = %s WHERE id_auxiliar = %s""", (cargo, apellidos, nombres, calle, numero, localidad, telefono, dni, correo, inicio, self.auxAmodificar))
        wx.MessageBox(u'Tarea realizada con éxito', u'Modificación de Auxiliar', wx.OK | wx.ICON_INFORMATION, self)
        c.close()
        self.frame.Destroy()



# Carga de egresado, se confecciona junto con el acta de examen
    def OnEgresoCurso(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Cierre de curso', size=(380, 250))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Baja de curso')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            numCursoLbl = wx.StaticText(panel, -1, u'Número de curso a dar de baja:')
            c = self.db.cursor()
            c.execute('''SELECT num_curso FROM cursos ORDER BY num_curso ASC''')
            cursos = c.fetchall()
            c.close()
            ListCursos = []
            for curso in cursos:
                ListCursos.append(curso[0])
            self.numCurso = wx.ComboBox(panel, -1, u'Seleccione', (-1, -1), (-1, -1), ListCursos, wx.CB_DROPDOWN|wx.CB_READONLY)
            fechaLbl = wx.StaticText(panel, -1, u'Fecha de la baja:')
            self.fecha = wx.DatePickerCtrl(panel, -1, size=(-1,-1), pos=(-1, -1), style=wx.DP_DROPDOWN | wx.DP_SHOWCENTURY)
            motivoLbl = wx.StaticText(panel, -1, u'Motivo del cierre:')
            self.motivo = wx.TextCtrl(panel, -1, u'')
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(numCursoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.numCurso, 0, wx.EXPAND)
            datosSizer.Add(fechaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.fecha, 0, wx.EXPAND)
            datosSizer.Add(motivoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.motivo, 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((30,25), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
            panel.SetSizer(ppalSizer)
            self.Bind(wx.EVT_BUTTON, self.OnCierreCurso, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

# Ingreso de baja de curso, se hace solamente en el curso, no se lo borra nunca de la db
    def OnCierreCurso(self, evt):
        try:
            self.frame.Close()
        finally:
            estado = 'b'
            dia = self.fecha.GetValue()
            fecha_baja = ('%04d/%02d/%02d' % (dia.GetYear(), dia.GetMonth()+1, dia.GetDay()))
            motivo_baja = self.motivo.GetValue()
            num_curso = self.numCurso.GetValue()
            c = self.db.cursor()
            c.execute('''UPDATE cursos SET estado = %s, motivo_baja = %s, fecha_baja = %s where num_curso = %s''', (estado, motivo_baja, fecha_baja, num_curso))
            wx.MessageBox(u'Tarea realizada con éxito', u'Baja de curso N° %s' % num_curso, wx.OK | wx.ICON_INFORMATION, self)
            c.close()



# Ingreso de baja de alumno, se hace solamente en el curso, no se lo borra nunca de la db
    def OnDesercion(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Baja de estudiante', size=(380, 180))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Baja de estudiante')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            numCursoLbl = wx.StaticText(panel, -1, u'Curso al que pertenece:')
            c = self.db.cursor()
            c.execute('''SELECT num_curso FROM cursos ORDER BY num_curso ASC''')
            cursos = c.fetchall()
            c.close()
            ListCursos = []
            for curso in cursos:
                ListCursos.append(curso[0])
            self.numCurso = wx.ComboBox(panel, -1, u'Seleccione', (-1, -1), (-1, -1), ListCursos, wx.CB_DROPDOWN|wx.CB_READONLY)
            self.numCurso.SetFocus()
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(numCursoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.numCurso, 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((30,25), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
            panel.SetSizer(ppalSizer)
            self.Bind(wx.EVT_BUTTON, self.OnSeleccionAlumnoCurso, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

# Seleccion de alumno en un curso
    def OnSeleccionAlumnoCurso(self, evt):
        try:
            self.frame.Close()
        finally:
            self.numCurso = self.numCurso.GetValue()
            c = self.db.cursor()
            c.execute('''SELECT id_alumno FROM curso_%s WHERE abandono = 0''' % self.numCurso)
            q = c.fetchall()
            self.frame = wx.Frame(self, -1, u'Baja de estudiante', size=(450, 180))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Baja de estudiante de curso %s' % self.numCurso)
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            alumnoLbl = wx.StaticText(panel, -1, u'Nombre del/de la estudiante:')
            listado = []
            for numero in q:
                indice = int(numero[0])
                c.execute ('''SELECT nombres, apellidos from alumnos where id_alumno = %s''', indice)
                w = c.fetchall()
                nombre = str(indice) + ' ' + w[0][0] + ' ' + w[0][1]
                listado.append(nombre)
            self.alumnos = wx.ComboBox(panel, -1, u'Seleccione', (-1, -1), (-1, -1), listado, wx.CB_DROPDOWN|wx.CB_READONLY)
            self.alumnos.SetFocus()
            causaLbl = wx.StaticText(panel, -1, u'Motivo de la baja: ')
            self.causa = wx.TextCtrl(panel, -1, u'')
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(alumnoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.alumnos, 0, wx.EXPAND)
            datosSizer.Add(causaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.causa, 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((30,25), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
            panel.SetSizer(ppalSizer)
            self.Bind(wx.EVT_BUTTON, self.OnIngresoBajaAlumnoCurso, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

# Ingreso de baja de alumno de un curso
    def OnIngresoBajaAlumnoCurso(self, evt):
        try:
            self.frame.Close()
        finally:
            import datetime
            alumno = self.alumnos.GetValue()
            causa = self.causa.GetValue()
            id = alumno.split()
            id = id[0]
            now = datetime.datetime.now()
            c = self.db.cursor()
            c.execute('''UPDATE curso_%s SET causa = %s, dia = %s, abandono = 1 WHERE id_alumno = %s''', (int(self.numCurso), causa, now, int(id)))
            c.close()
            wx.MessageBox(u'Baja de estudiante %s en el curso N° %s' % (alumno, self.numCurso), u'Tarea realizada con éxito', wx.OK | wx.ICON_INFORMATION, self)

# Ingreso manual de novedades con respecto a un alumno
    def OnSeguimiento(self, evt):
        try:
            self.frame.Close()
        finally:
            self.dialog = wx.TextEntryDialog(None, u'Ingrese el Apellido del estudiante', u'Seguimiento de estudiantes', u'', style=wx.OK|wx.CANCEL)
            if self.dialog.ShowModal() == wx.ID_OK:
                self.apellido = self.dialog.GetValue()
            else:
                self.dialog.Destroy()
                return
            self.dialog.Destroy()
            # Creo el diálogo para seleccionar entre todos los que tienen el mismo apellido
            c = self.db.cursor()
            c.execute('''SELECT id_alumno, apellidos, nombres, num_doc FROM alumnos WHERE apellidos = %s''', (self.apellido))
            q = c.fetchall()
            StrAlum = [("%d %s %s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Estudiantes que cumplen el criterio de búsqueda:', u'Seguimiento de estudiantes', StrAlum)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.alumnoAingresar = q[selections][0]
                c. execute('''SELECT * FROM alumnos WHERE id_alumno = %s''', (self.alumnoAingresar))
                q = c.fetchone()
                c.close()
                self.alumnoAseguir = q[2] + u' ' + q[1]
                # Ingreso de seguimiento de alumno
                self.frame = wx.Frame(self, -1, u'Seguimiento de egresado/a', size=(380, 250))
                self.frame.CenterOnScreen()
                panel = wx.Panel(self.frame)
                topLbl = wx.StaticText(panel, -1, u'Empleo de egresado/a')
                topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
                EstudiantesLbl = wx.StaticText(panel, -1, u'Estudiante:')
                NombreLbl = wx.StaticText(panel, -1, self.alumnoAseguir)
                rubroLbl = wx.StaticText(panel, -1, u'Rubro:')
                self.rubro = wx.TextCtrl(panel, -1, u'')
                self.rubro.SetFocus()
                empresaLbl = wx.StaticText(panel, -1, u'Empresa:')
                self.empresa = wx.TextCtrl(panel, -1, u'')
                situacionLbl = wx.StaticText(panel, -1, u'Situación Laboral:')
                situacion = [u'Contratado', u'Cuentapropista', u'Informal', u'Pasante', u'Staff', u'Rel. Dependencia']
                self.estado = wx.ComboBox(panel, -1, u'Contratado/a', (-1, -1), (-1, -1), situacion, wx.CB_DROPDOWN|wx.CB_READONLY)
                saveBtn = wx.Button(panel, -1, u'&Aceptar')
                cancelBtn = wx.Button(panel, -1, u'&Cancelar')
                ppalSizer = wx.BoxSizer(wx.VERTICAL)
                ppalSizer.Add(topLbl, 0, wx.ALL, 5)
                ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
                datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
                datosSizer.AddGrowableCol(1)
                datosSizer.Add(EstudiantesLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(NombreLbl, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(rubroLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.rubro, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(empresaLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.empresa, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(situacionLbl, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
                datosSizer.Add(self.estado, 0, wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL)
                btnSizer = wx.BoxSizer(wx.HORIZONTAL)
                btnSizer.Add((30,25), 1)
                btnSizer.Add(cancelBtn)
                btnSizer.Add((30,25), 1)
                btnSizer.Add(saveBtn)
                btnSizer.Add((30,25), 1)
                ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
                ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
                panel.SetSizer(ppalSizer)
                self.Bind(wx.EVT_BUTTON, self.OnIngresoSeguimiento, saveBtn)
                self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
                self.frame.Show()

# Ingreso de seguimiento
    def OnIngresoSeguimiento(self, evt):
        import datetime
        estudiante = self.alumnoAingresar
        rubro = self.rubro.GetValue()
        empresa = self.empresa.GetValue()
        estado = self.estado.GetValue()
        fecha = datetime.datetime.now()
        c = self.db.cursor()
        c.execute('''INSERT into seguimiento (id_alumno, rubro, empresa, estado, fecha) values (%s, %s, %s, %s, %s)''', (estudiante, rubro, empresa, estado, fecha))
        c.close()
        self.frame.Close()
        wx.MessageBox(u'Ingreso de seguimiento de egresado/a', u'Tarea realizada con éxito', wx.OK | wx.ICON_INFORMATION, self)

# Listado de Alumnos
    def OnListAlumnos(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute('''SELECT id_alumno, apellidos, nombres, num_doc, calle_dom, num_dom, localidad_dom, tel_dom FROM alumnos order by id_alumno ASC''')
            q = c.fetchall()
            c.close
            d = len(q)
            encabezado = u'columns = ["Id", "Apellidos", "Nombres", "Documento", "Calle", "N°", "Localidad", "Teléfono"]\n'
            f=open('./py/listalum.py', 'w')
            f.write('# -*- coding: UTF8 -*-\n')
            f.write('\n')
            f.write(encabezado.encode('utf-8'))
            f.write('\n')
            f.write('rows = [\n')
            for cadaobj in range(0, (d)):
                f.write('%s,\n' % str(q[cadaobj]))
            f.write (']')
            f.close()
            self.frame = ListAlumFrame()
            self.frame.Show()

# Listado de Cursos
    def OnListCursos(self, evt):
        try:
            self.frame.Close()
        finally:
            dlg = wx.SingleChoiceDialog(self, u'Criterio de listado', u'Listado de cursos',
            [u'Todos', u'Número', u'Instructor'], wx.CHOICEDLG_STYLE)
            c = self.db.cursor()
            if dlg.ShowModal() == wx.ID_OK:
                seleccion = dlg.GetStringSelection()
                dlg.Destroy()
                #Listado completo
                if seleccion == u'Todos':
                    c.execute('''SELECT num_curso FROM cursos''')
                    q = c.fetchall()
                    f = open('./py/listcursos.py', 'w')
                    f.write('# -*- coding: UTF8 -*-\n')
                    f.write('\n')
                    f.write(u'columns = ["N° Curso", "Tipo", "Especialidad", "Instructor", "Año", "Horas", "Establecimiento", "Estado"]\n'.encode('utf-8'))
                    f.write('\n')
                    f.write('rows = [\n')
                    for cadaobj in q:
                        c.execute('''SELECT num_curso, tipo, especialidad, instructor, ciclo, horas, establecimiento, estado FROM cursos WHERE num_curso = %s ''' % (cadaobj))
                        w = c.fetchall()
                        f.write ('%s, \n' %(w))
                    f.write (']')
                    f.close()
                    c.close()
                    self.frame = ListCursosFrame()
                    self.frame.Show()


            #Listado por número
                elif seleccion == u'Número':
                    dlg = wx.TextEntryDialog(self, u'Ingrese el número del curso a listar',u'Listado de Cursos', '')
                    if dlg.ShowModal() == wx.ID_OK:
                        num_curso = dlg.GetValue()
                        dlg.Destroy()
                        c.execute('''SELECT id_alumno FROM curso_%s''' % (num_curso))
                        q = c.fetchall()
                        # Creo un archivo list_curso_num.py y lo lleno con las filas y las columnas
                        f = open('./py/list_curso_num.py', 'w')
                        f.write('# -*- coding: UTF8 -*-\n')
                        f.write('\n')
                        f.write('num_curso = %s\n' % num_curso)
                        f.write('\n')
                        columnas = u'columns = ["Apellidos", "Nombres", "Documento", "Calle", "N°", "Localidad", "Teléfono", "Correo"]\n'
                        f.write(columnas.encode('UTF-8'))
                        f.write('\n')
                        f.write('rows = [\n')
                        for cadaobj in q:
                            c.execute('''SELECT apellidos, nombres, num_doc, calle_dom, num_dom, localidad_dom, tel_dom, correo FROM alumnos WHERE id_alumno = %s ''' % (cadaobj))
                            w = c.fetchall()
                            f.write ('%s,\n' % w)
                        f.write (']')
                        f.close()
                        c.close()
                        self.frame = ListCurNumFrame()
                        self.frame.Show()

                elif seleccion == u'Instructor':
                    dlg = wx.TextEntryDialog(self, u'Ingrese el apellido del/de la instructor/a', u'Listado de Cursos por instructor/a''')
                    if dlg.ShowModal() == wx.ID_OK:
                        instructor = dlg.GetValue()
                        dlg.Destroy()
                        c.execute('''SELECT num_curso, tipo, especialidad, ciclo,
                         establecimiento FROM cursos WHERE instructor = "%s"''' % (instructor))
                        q = c.fetchall()
                        f = open('./py/list_curso_ins.py', 'w')
                        f.write('# -*- coding: UTF8 -*-\n')
                        f.write('\n')
                        f.write('instructor = u"%s"\n' % instructor.encode('UTF-8'))
                        f.write('\n')
                        columnas = u'columns = ["N° Curso", "Tipo", "Especialidad", "Año", "Establecimiento"]\n'
                        f.write(columnas.encode('UTF-8'))
                        f.write('\n')
                        f.write('rows = [\n')
                        for item in range(len(q)):
                            f.write('(')
                            for i in range (5):
                                if i == 4:
                                    f.write ('u"%s"' %(q[item][i].encode('UTF-8')))
                                    f.write('),')
                                else:
                                    f.write ('u"%s", ' %(q[item][i].encode('UTF-8')))
                            f.write ('\n')
                        f.write (']')
                        f.close()
                        c.close()
                        self.frame = ListCurInsFrame()
                        self.frame.Show()
                elif seleccion == u'Año':
                    pass
                elif seleccion == u'Especialidad':
                    pass
                else:
                    dlg.Destroy()
                    return


# Listado de Instructores
    def OnListInstruc(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute('''SELECT id_instructor, apellidos, nombres, te_contacto, calle, numero, localidad, correo FROM instructores order by id_instructor ASC''')
            q = c.fetchall()
            d = len(q)
            f=open('./py/listinstruc.py', 'w')
            f.write('# -*- coding: UTF8 -*-\n')
            f.write('\n')
            columnas = u'columns = [u"Id", u"Apellidos", u"Nombres", u"TE", u"Calle", u"Número", u"Localidad", u"Correo-e"]\n'
            f.write(columnas.encode('UTF-8'))
            f.write('\n')
            f.write('rows = [\n')
            for cadaobj in range(0, (d)):
                f.write ('%s,\n' %str(q[cadaobj]))
            f.write (']')
            f.close()
            c.close()
            self.frame = ListInstFrame()
            self.frame.Show()

# Listado de Coordinadores
    def OnListCoord(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute('''SELECT id_coordinador, apellidos, nombres, te_contacto, calle, numero, localidad, correo FROM coordinadores order by id_coordinador ASC''')
            q = c.fetchall()
            d = len(q)
            f=open('./py/listcoord.py', 'w')
            f.write('# -*- coding: UTF8 -*-\n')
            f.write('\n')
            f.write('columns = [u"Id", u"Apellidos", u"Nombres", u"TE", u"Calle", u"Número", u"Localidad", u"Correo-e"]\n')
            f.write('\n')
            f.write('rows = [\n')
            for cadaobj in range(0, (d)):
                f.write ('%s,\n' %str(q[cadaobj]))
            f.write (']')
            f.close()
            c.close()
            self.frame = ListCoordFrame()
            self.frame.Show()

# Listado de Centros
    def OnListCentros(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute('''SELECT id_establecimiento, nombre, calle, num_puerta, localidad, cp, telefono, correo, coordinador FROM establecimientos order by id_establecimiento ASC''')
            q = c.fetchall()
            d = len(q)
            f=open('./py/listcentros.py', 'w')
            f.write('# -*- coding: UTF8 -*-\n')
            f.write('\n')
            columnas = u'columns = ["Id", "Nombre", "Calle", "N°", "Localidad", "CP", "TE", "Correo-e", "Coordinador/a"]\n'
            f.write(columnas.encode('UTF-8'))
            f.write('\n')
            f.write('rows = [\n')
            for cadaobj in range(0, (d)):
                f.write ('%s,\n' %str(q[cadaobj]))
            f.write (']')
            f.close()
            c.close()
            self.frame = ListCentrosFrame()
            self.frame.Show()

# Listado de Administrativos
    def OnListAdministrativos(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute('''SELECT cargo, apellidos, nombres, calle, numero, localidad, telefono, celular, correo FROM administrativos order by cargo ASC''')
            q = c.fetchall()
            d = len(q)
            f=open('./py/listadm.py', 'w')
            f.write('# -*- coding: UTF8 -*-\n')
            f.write('\n')
            f.write('columns = ["Cargo", "Apellidos", "Nombres", "Calle", "N°", "Localidad", "TE", "Celular", "Correo-e"]\n')
            f.write('\n')
            f.write('rows = [\n')
            for cadaobj in range(0, (d)):
                f.write ('%s,\n' %str(q[cadaobj]))
            f.write (']')
            f.close()
            c.close()
            self.frame = ListAdmFrame()
            self.frame.Show()

# Listado de Auxiliares
    def OnListAuxiliares(self, evt):
        try:
            self.frame.Close()
        finally:
            c = self.db.cursor()
            c.execute('''SELECT cargo, apellidos, nombres, calle, numero, localidad, telefono, dni, correo, inicio FROM auxiliares order by cargo ASC''')
            q = c.fetchall()
            d = len(q)
            f=open('./py/listaux.py', 'w')
            f.write('# -*- coding: UTF8 -*-\n')
            f.write('\n')
            f.write(u'import datetime')
            f.write('\n')
            f.write('columns = ["Cargo", "Apellidos", "Nombres", "Calle", "N°", "Localidad", "TE", "Doc", "Correo-e", u"Fecha inicio"]\n')
            f.write('\n')
            f.write('rows = [\n')
            for cadaobj in q:
                reobj = list(cadaobj)
                item = str(cadaobj[9])
                reobj[9] = item
                f.write('%s,\n' % repr(reobj))
            f.write (']')
            f.close()
            c.close()
            self.frame = ListAuxFrame()
            self.frame.Show()

# Listado del seguimiento de egresados
    def OnListSegEgresados(self, evt):
        c = self.db.cursor()
        c.execute('''SELECT DISTINCT id_alumno FROM seguimiento''')
        q = c.fetchall()
        egresados = []
        for numero in q:
            cadena = ''
            c.execute('''SELECT apellidos, nombres,
             num_doc FROM alumnos WHERE id_alumno = %s''', (numero))
            r = c.fetchall()
            cadena = str(numero)[3:-3] + ' '
            for elemento in r[0]:
                cadena = cadena + ' ' + elemento
            egresados.append(cadena)
        dlg = wx.SingleChoiceDialog(self, u'Seleccione el/la egresado/a a listar ',
         u'Seguimiento de egresado/a', egresados, wx.CHOICEDLG_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            listar = dlg.GetStringSelection()
            listar = listar.split(' ')
            f = open('seguimiento', 'w')
            f.write(listar[0])
            f.close()
            import seguiEgresados
            ventana = seguiEgresados.MyFrame(self, -1, u'Seguimiento de egresado', 
             style = wx.DEFAULT_FRAME_STYLE)
            ventana.CenterOnScreen()
            ventana.Show(True)
            
        c.close()


# Ficha de Alumnos
    def OnFichaAlumnos(self, evt):
        try:
            self.frame.Close()
        finally:
            # Creo el diálogo para entrar el apellido del alumno a listar
            self.dialog = wx.TextEntryDialog(None, u'Ingrese el Apellido del estudiante', u'Ficha de estudiante', u'', style=wx.OK|wx.CANCEL)
            if self.dialog.ShowModal() == wx.ID_OK:
                self.apellido = self.dialog.GetValue()
            else:
                self.dialog.Destroy()
                return
            self.dialog.Destroy()
            # Creo el diálogo para seleccionar entre todos los que tienen el mismo apellido
            c = self.db.cursor()
            c.execute('''SELECT id_alumno, apellidos, nombres, num_doc FROM alumnos WHERE apellidos = %s''', (self.apellido))
            q = c.fetchall()
            StrAlum = [("%d %s %s %s" % tuple(a)) for a in q]
            dlg = wx.SingleChoiceDialog(self, u'Estudiantes que cumplen el criterio de búsqueda:', u'Legajo de estudiantes', StrAlum)
            if (dlg.ShowModal() == wx.ID_OK):
                selections = dlg.GetSelection()
                self.alumnoAlistar = q[selections][0]
                c. execute('''SELECT * FROM alumnos WHERE id_alumno = %s''', (self.alumnoAlistar))
                q = c.fetchall()
                import fichaalumno
                ventana = fichaalumno.ModEstudiante(self.alumnoAlistar, None, -1, u'Ficha de alumno')
                ventana.Show()

# Imprimir la ficha de alumno
    def OnImprimirFichaAlumno(self, evt):
        pass

# Ficha de curso
    def OnFichaCursos(self, evt):
        try:
            self.frame.Close()
        finally:
            self.frame = wx.Frame(self, -1, u'Ficha de curso', size=(380, 180))
            self.frame.CenterOnScreen()
            panel = wx.Panel(self.frame)
            topLbl = wx.StaticText(panel, -1, u'Ficha de curso')
            topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
            numCursoLbl = wx.StaticText(panel, -1, u'Curso a listar:')
            c = self.db.cursor()
            c.execute('''SELECT num_curso FROM cursos ORDER BY num_curso ASC''')
            cursos = c.fetchall()
            c.close()
            ListCursos = []
            for curso in cursos:
                ListCursos.append(curso[0])
            self.numCurso = wx.ComboBox(panel, -1, u'Seleccione', (-1, -1), (-1, -1), ListCursos, wx.CB_DROPDOWN|wx.CB_READONLY)
            saveBtn = wx.Button(panel, -1, u'&Aceptar')
            cancelBtn = wx.Button(panel, -1, u'&Cancelar')
            ppalSizer = wx.BoxSizer(wx.VERTICAL)
            ppalSizer.Add(topLbl, 0, wx.ALL, 5)
            ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
            datosSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
            datosSizer.AddGrowableCol(1)
            datosSizer.Add(numCursoLbl, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
            datosSizer.Add(self.numCurso, 0, wx.EXPAND)
            btnSizer = wx.BoxSizer(wx.HORIZONTAL)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(cancelBtn)
            btnSizer.Add((30,25), 1)
            btnSizer.Add(saveBtn)
            btnSizer.Add((30,25), 1)
            ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
            ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 30)
            panel.SetSizer(ppalSizer)
            self.Bind(wx.EVT_BUTTON, self.OnFichaCursoLlena, saveBtn)
            self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
            self.frame.Show()

    def OnFichaCursoLlena(self, evt):
        self.num_curso = self.numCurso.GetValue()
        self.frame.Close()
        c = self.db.cursor()
        c.execute('''SELECT id_alumno FROM curso_%s''' % (self.num_curso))
        q = c.fetchall()
        c.execute ('''TRUNCATE table fichacurso''')
        for alumno in q:
            c.execute('''SELECT nombres, apellidos, nacionalidad, fecha_nac, tipo_doc, num_doc, calle_dom, num_dom, localidad_dom, sexo FROM alumnos WHERE id_alumno = %s''' % (int(alumno[0])))
            r = c.fetchone()
            apell_nombre = r[1] + u' '+ r[0]
            nac = r[2]
            fecha_nac = r[3]
            tipo_doc = r[4]
            if tipo_doc == 'ET':
                tipo_doc = u'En trámite'
            num_doc = r[5]
            domicilio = r[6] + u' '+ r[7] + u' '+ r[8]
            sexo = r[9]
            c.execute('''INSERT INTO fichacurso (apell_nom, nac, fecha_nac, tipo_doc, num_doc, domicilio, sexo) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (apell_nombre, nac, fecha_nac, tipo_doc, num_doc, domicilio, sexo))
        c.execute('''SELECT tipo, especialidad, instructor, fecha_inicio, fecha_final, horas, horario, establecimiento FROM cursos WHERE num_curso = %s''', (self.num_curso))
        q = c.fetchone()
        c.execute('''SELECT tipo, numero, calle, num_puerta, localidad FROM establecimientos WHERE nombre = %s''', (q[7]))
        r = c.fetchone()
        c.execute('''SELECT nombre, localidad FROM miescuela LIMIT 1''')
        s = c.fetchone()
        c.execute (''' SELECT * FROM fichacurso ORDER BY sexo DESC, apell_nom''')
        t = c.fetchall()
        orden = 1
        # Doy vuelta las fechas para que se lea bien en la ficha de curso
        fecha_inic = q[3]
        dia = fecha_inic.day
        mes = fecha_inic.month
        anio = fecha_inic.year
        fechainic = u'%02d' % dia + '-' + u'%02d' % mes + '-' + str(anio)
        fecha_fin = q[4]
        dia = fecha_fin.day
        mes = fecha_fin.month
        anio = fecha_fin.year
        fechafin = u'%02d' % dia + '-' + u'%02d' % mes + '-' + str(anio)
        c.close()
        # Comienzo a confeccionar la ficha de curso llena
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import cm
        from reportlab.lib.colors import white
        from reportlab.lib.pagesizes import legal, landscape
        import fichacurso
        if orden < 23:
            c = fichacurso.canvas.Canvas("./planillas/fichacurso_%s.pdf" % self.num_curso, pagesize=landscape(legal))
            fichacurso.fichacursos(c)
            # Establecimiento
            c.drawString(21.4*cm, 17.7*cm, u'C.F.P N° 401 V.L.')
            # Localidad
            c.drawString(21.4*cm, 17.2*cm, u'%s' % s[1])
            # Especialidad
            c.drawString(4.5*cm, 16.4*cm, u'%s' % q[1])
            # Tipo
            c.drawString(19.0*cm, 16.4*cm, u'%s' % q[0])
            # Horas Reloj
            c.drawString(24.0*cm, 16.4*cm, u'%s' % q[5])
            # Fecha inicio
            c.drawString(5.8*cm, 15.6*cm, u'%s' % fechainic)
            # Fecha fin
            c.drawString(13.5*cm, 15.6*cm, u'%s' % fechafin)
            # Horario
            c.drawString(18.5*cm, 15.6*cm, u'%s' % q[6])
            # Lugar en que se dicta
            c.drawString(6.0*cm, 14.9*cm, u'%s %s %s' % (r[2], r[3], r[4]))
            # Instructor
            c.drawString(19.0*cm, 14.9*cm, u'%s' % q[2])
            # Número Curso
            c.drawString(28.3*cm, 15.2*cm, u'%s' % self.num_curso)
            # Primer nombre
            primero_x = 2.5
            primero_y = 13.1
            orden = 1
            for alumno in t:
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % (alumno[1]))
                primero_y -= 0.5
                orden += 1
                if orden > 22:
                    break
            #Nacionalidad
            primero_x = 11.2
            primero_y = 13.1
            orden = 1
            for alumno in t:
                if orden > 22:
                  break
                if alumno[2].lower() == u'ar':
                    nacion = u'Argentina'
                elif alumno[2].lower() == u'pe':
                    nacion = u'Peruana'
                elif alumno[2].lower() == u'py':
                    nacion = u'Paraguaya'
                elif alumno[2].lower() == u'uy':
                    nacion = u'Uruguaya'
                elif alumno[2].lower() == u'bo':
                    nacion = u'Boliviana'
                elif alumno[2].lower() == u'br':
                    nacion = u'Brasileña'
                elif alumno[2].lower() == u'it':
                    nacion = u'Italiana'
                elif alumno[2].lower() == u'es':
                    nacion = u'Española'
                elif alumno[2].lower() == u'cl':
                    nacion = u'Chilena'
                elif alumno[2].lower() == u'ec':
                    nacion = u'Ecuatoriana'
                elif alumno[2].lower() == u've':
                    nacion = u'Venezolana'
                elif alumno[2].lower() == u'co':
                    nacion = u'Colombiana'
                else:
                    nacion = alumno[2]
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % nacion)
                primero_y -= 0.5
                orden += 1
            # Fecha de nacimiento
            primero_x = 13.9
            primero_y = 13.1
            orden = 1
            for alumno in t:
                if orden > 22:
                    break
                #Doy vuelta las fechas para que se lea bien en la ficha de curso
                dia_actual = alumno[3]
                dia = dia_actual.day
                mes = dia_actual.month
                anio = dia_actual.year
                nac = '%02d' % dia + '-' + '%02d' % mes + '-' + str(anio)
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % nac)
                primero_y -= 0.5
                orden += 1
            # Tipo, número y emisor de documento
            primero_x = 16.6
            primero_y = 13.1
            orden = 1
            for alumno in t:
                if orden > 22:
                    break
                # Me fijo si no tiene DNI y si es así le pongo 'En trámite'
                if alumno[4] == u'PAS' or alumno[4] == u'ET':
                    doc = u'DNI'
                    num = u'En trámite'
                else:
                    doc = alumno[4]
                    num = alumno[5]
                    # Le pongo la F o la M si el documento es viejo
                    if len(num) == 7:
                        num = alumno[7] + num
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % doc)
                c.drawString((primero_x + 2.0)*cm, primero_y*cm, u'%s' % num)
                if num != u'En trámite':
                    c.drawString((primero_x + 5.2)*cm, primero_y*cm, u'RNP')
                primero_y -= 0.5
                orden += 1
            # Domicilio
            primero_x = 23.9
            primero_y = 13.1
            orden = 1
            for alumno in t:
                if orden > 22:
                    break
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % alumno[6])
                primero_y -= 0.5
                orden += 1
            c.showPage()
            c.save()
            #break
        if orden > 22:
            ################# Comienzo de planilla auxiliar #################
            c = fichacurso.canvas.Canvas("./planillas/fichacurso_%s_2.pdf" % self.num_curso, pagesize=landscape(legal))
            fichacurso.fichacursos(c)
            # Establecimiento
            c.drawString(21.4*cm, 17.7*cm, u'C.F.P N° 401 V.L.')
            # Localidad
            c.drawString(21.4*cm, 17.2*cm, u'%s' % s[1])
            # Especialidad
            c.drawString(4.5*cm, 16.4*cm, u'%s' % q[1])
            # Tipo
            c.drawString(19.0*cm, 16.4*cm, u'%s' % q[0])
            # Horas Reloj
            c.drawString(24.0*cm, 16.4*cm, u'%s' % q[5])
            # Fecha inicio
            c.drawString(5.8*cm, 15.6*cm, u'%s' % fechainic)
            # Fecha fin
            c.drawString(13.5*cm, 15.6*cm, u'%s' % fechafin)
            # Horario
            c.drawString(18.5*cm, 15.6*cm, u'%s' % q[6])
            # Lugar en que se dicta
            c.drawString(6.0*cm, 14.9*cm, u'%s %s %s' % (r[2], r[3], r[4]))
            # Instructor
            c.drawString(19.0*cm, 14.9*cm, u'%s' % q[2])
            # Número Curso
            c.drawString(28.3*cm, 15.2*cm, u'%s' % self.num_curso)
            # Primer nombre
            primero_x = 2.5
            primero_y = 13.1
            for alumno in t[22:]:
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % (alumno[1]))
                primero_y -= 0.5
                orden += 1
            #Nacionalidad
            primero_x = 11.2
            primero_y = 13.1
            for alumno in t[22:]:
                if alumno[2].lower() == u'ar':
                    nacion = u'Argentina'
                elif alumno[2].lower() == u'pe':
                    nacion = u'Peruana'
                elif alumno[2].lower() == u'py':
                    nacion = u'Paraguaya'
                elif alumno[2].lower() == u'uy':
                    nacion = u'Uruguaya'
                elif alumno[2].lower() == u'bo':
                    nacion = u'Boliviana'
                elif alumno[2].lower() == u'br':
                    nacion = u'Brasileña'
                elif alumno[2].lower() == u'it':
                    nacion = u'Italiana'
                elif alumno[2].lower() == u'es':
                    nacion = u'Española'
                elif alumno[2].lower() == u'cl':
                    nacion = u'Chilena'
                elif alumno[2].lower() == u'ec':
                    nacion = u'Ecuatoriana'
                elif alumno[2].lower() == u've':
                    nacion = u'Venezolana'
                elif alumno[2].lower() == u'co':
                    nacion = u'Colombiana'
                else:
                    nacion = alumno[2]
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % nacion)
                primero_y -= 0.5
            # Fecha de nacimiento
            primero_x = 13.9
            primero_y = 13.1
            for alumno in t[22:]:
                #Doy vuelta las fechas para que se lea bien en la ficha de curso
                dia_actual = alumno[3]
                dia = dia_actual.day
                mes = dia_actual.month
                anio = dia_actual.year
                nac = '%02d' % dia + '-' + '%02d' % mes + '-' + str(anio)
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % nac)
                primero_y -= 0.5
            # Tipo, número y emisor de documento
            primero_x = 16.6
            primero_y = 13.1
            for alumno in t[22:]:
                # Me fijo si no tiene DNI y si es así le pongo 'En trámite'
                if alumno[4] == u'PAS' or alumno[4] == u'ET':
                    doc = u'DNI'
                    num = u'En trámite'
                else:
                    doc = alumno[4]
                    num = alumno[5]
                    # Le pongo la F o la M si el documento es viejo
                    if len(num) == 7:
                        num = alumno[7] + num
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % doc)
                c.drawString((primero_x + 2.0)*cm, primero_y*cm, u'%s' % num)
                if num != u'En trámite':
                    c.drawString((primero_x + 5.2)*cm, primero_y*cm, u'RNP')
                primero_y -= 0.5
            # Domicilio
            primero_x = 23.9
            primero_y = 13.1
            for alumno in t[22:]:
                c.drawString(primero_x*cm, primero_y*cm, u'%s' % alumno[6])
                primero_y -= 0.5
            c.showPage()
            c.save()
            dlg = wx.MessageDialog(self, u"Dos fichas de curso han sido generadas en el directorio '/planillas'", u"Ficha de curso - Curso numeroso", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            ################# Fin de planilla auxiliar #################
        else:
            dlg = wx.MessageDialog(self, u"Una ficha de curso ha sido generada\n en el directorio '/planillas'", u"Ficha de curso", wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()


    def OnCanc (self, evt):
        self.frame.Destroy()

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Confeccionar acta de examen completa
    def OnActaExamenCompleta(self, evt):
        import llenaracta
        ventana = llenaracta.ActaExamen(self, -1, u'Acta de examen', style = wx.DEFAULT_FRAME_STYLE)
        ventana.CenterOnScreen()
        ventana.Show(True)

# Confección de certificados
    def OnCertificados(self, evt):
        import dialogcertificados
        self.dialogo = dialogcertificados.MyDialog(self)
        self.dialogo.ShowModal()
        import confecccertif
        self.dialogo = confecccertif.MyDialog(self)
        self.dialogo.ShowModal()

# Confección de legajos por curso
    def OnLegajosPorCurso(self, evt):
        c = self.db.cursor()
        c.execute('''SELECT num_curso FROM cursos ORDER BY num_curso ASC''')
        cursos = c.fetchall()
        c.close()
        ListCursos = []
        for curso in cursos:
            ListCursos.append(curso[0])
        self.frame = wx.Frame(self, -1, u'Confección de legajos', size=(280, 180))
        self.frame.CenterOnScreen()
        panel = wx.Panel(self.frame, -1)
        self.label = wx.StaticText(panel, -1, u'Curso Nº: ', pos = (25, 55))
        self.numCurso = wx.ComboBox(panel, -1, u'Seleccione', (88, 50), (-1, -1), ListCursos, wx.CB_DROPDOWN|wx.CB_READONLY)
        self.numCurso.SetFocus()
        saveBtn = wx.Button(panel, -1, u'&Aceptar', pos = (90, 120))
        cancelBtn = wx.Button(panel, -1, u'&Cancelar', pos = (180, 120))
        self.Bind(wx.EVT_BUTTON, self.OnImpresionLegajos, saveBtn)
        self.Bind(wx.EVT_BUTTON, self.OnCancelar, cancelBtn)
        self.frame.Show()
        
# Impresión de los legajos
    def OnImpresionLegajos(self, evt):
        curso = self.numCurso.GetValue()
        self.frame.Close()
        import os
        try:
            os.system('mkdir ./planillas/legajos_%s' % curso)
            os.system('rm ./planillas/legajos_%s/*' % curso)
        finally:
            pass
        c = self.db.cursor()
        c.execute('''SELECT id_alumno FROM curso_%s WHERE abandono = 0 ORDER BY id_alumno ASC''' % curso)
        alumnos = c.fetchall()
        # Bucleo y hago los legajos
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import cm
        from reportlab.lib.colors import white
        from reportlab.lib.pagesizes import legal, portrait
        import legajo_dgce
        for alumno in alumnos:
            id = alumno[0]
            c.execute('''SELECT * FROM alumnos WHERE id_alumno = %s''' % id)
            q = c.fetchone()
            c.execute('''SELECT * FROM cursos WHERE num_curso = %s''' % curso)
            k = c.fetchone()
            l = legajo_dgce.canvas.Canvas("./planillas/legajos_%s/%s_%s_legajo.pdf" % (curso, q[1], q[2]),
             pagesize=portrait(legal))
            legajo_dgce.legajo(l)
            l.drawString(14*cm, 1.5*cm, k[5])
            l.drawString(9.5*cm, -1.0*cm, u'Centro de Formación Profesional ')
            l.drawString(3*cm, -1.8*cm, u'401')
            l.drawString(7.5*cm, -1.8*cm, u'Vicente López')
            l.drawString(17.5*cm, -1.8*cm, u'X')
            # Inscripción
            l.drawString(14.8*cm, -3.7*cm, u'X')
            l.drawString(0.5*cm, -6.8*cm, k[3])
            # Alumno
            l.drawString(2.4*cm, -9.1*cm, u'%s' % q[4]) # tipo doc
            l.drawString(5.5*cm, -9.1*cm, u'%s' % q[5]) # Num doc
            l.drawString(2.4*cm, -9.9*cm, u'%s' % q[1]) # apellidos
            l.drawString(10.2*cm, -9.9*cm, u'%s' % q[2]) # nombres
            l.drawString(1.6*cm, -10.8*cm, u'%s' % q[3]) # sexo
            # fecha nacimiento
            dia = q[7]
            dianac = dia.day
            mes = dia.month
            anio = dia.year
            fechanac = str(dianac) + '/' + str(mes) + '/' + str(anio)
            l.drawString(4.9*cm, -10.8*cm, fechanac) # Fecha Nacimiento    
            l.drawString(9.7*cm, -10.8*cm, u'%s' % q[8]) # Lugar Nacimiento
            l.drawString(16*cm, -10.8*cm, u'%s' % q[6]) # Nacionalidad
            l.drawString(3.6*cm, -11.7*cm, u'%s' % q[9]) # Calle domicilio
            l.drawString(9.8*cm, -11.7*cm, u'%s' % q[10]) # Número domicilio
            l.drawString(12.8*cm, -11.7*cm, u'%s' % q[11]) # Piso domicilio
            l.drawString(14.8*cm, -11.7*cm, u'%s' % q[12]) # Dpto domicilio
            l.drawString(2.5*cm, -12.5*cm, u'%s' % q[14]) # localidad domicilio
            l.drawString(8.8*cm, -12.5*cm, u'%s' % q[13]) # cp domicilio
            l.drawString(13.3*cm, -12.5*cm, u'%s' % q[16]) # te domicilio
            # Estudios
            if q[17][0] == 'P':
                l.drawString(4.2*cm, -15.3*cm, u'X') # marca primario
            elif q[17][0] == 'S':
                l.drawString(6.8*cm, -15.3*cm, u'X') # marca Secundario
            elif q[17][0] == 'T' or q[17][0] == 'U':
                l.drawString(8.9*cm, -15.3*cm, u'X') # marca universidad
            if q[18] == '0':
                l.drawString(14.5*cm, -14.5*cm, u'X') # marca completo
            else:
                l.drawString(14.5*cm, -15.3*cm, u'X') # marca incompleto
                anio = u'%s' % q[18] + u'º'
                l.drawString(17.4*cm, -15.3*cm, anio) # año al que llegó
            if q[38] == 1:
                l.drawString(5.6*cm, -19.3*cm, u'X') # trabaja
            else:
                l.drawString(6.9*cm, -19.3*cm, u'X') # no trabaja
            if q[17][0] == 'P':
                if q[18] != '0':
                    l.drawString(15.5*cm, -19.3*cm, u'X') # Primario completo
            else:
                l.drawString(14.1*cm, -19.3*cm, u'X') # Primario incompleto
            # Vamos con el responsable
            if q[40] == '1':
                #madre
                l.drawString(4.0*cm, -22.5*cm, u'X')
            elif q[40] == '2':
                #padre
                l.drawString(6.3*cm, -22.5*cm, u'X')
            elif q[40] == '3':
                #tutor
                l.drawString(10.7*cm, -22.5*cm, u'X')
            elif q[40] == '4':
                #encargado
                l.drawString(10.7*cm, -22.5*cm, u'X')
            elif q[40] == '5':
                #responsable
                l.drawString(10.7*cm, -22.5*cm, u'X')
            # si es responsable es jefe
            if q[41] == '1':
                l.drawString(15.7*cm, -22.5*cm, u'X')
            else:
                l.drawString(16.9*cm, -22.5*cm, u'X')
            l.drawString(4.5*cm, -23.3*cm, u'%s' % q[42]) # Nombre responsable
            l.drawString(4.0*cm, -24.1*cm, u'%s' % q[43]) # Nacionalidad responsable
            l.drawString(13.1*cm, -24.1*cm, u'%s' % q[44]) # Profesión responsable
            l.drawString(5.6*cm, -24.7*cm, u'%s' % q[45]) # Condición actividad responsable
            # estudios del responsable
            if q[46] == 'Primarios':
                l.drawString(4.0*cm, -26.0*cm, u'X')
            elif q[46] == 'Secundarios':
                l.drawString(5.5*cm, -26.0*cm, u'X')
            elif q[46] == 'Terciarios':
                l.drawString(7.1*cm, -26.0*cm, u'X')
            elif q[46] == 'Universitarios':
                l.drawString(8.5*cm, -26.0*cm, u'X')    
            # responsable hasta estudios
            if q[47] == '0':
                l.drawString(12.9*cm, -26.0*cm, u'X')
            else:
                l.drawString(15.6*cm, -26.0*cm, u'X')
                l.drawString(17.3*cm, -26.0*cm, u'%s' % q[47])
            l.drawString(2.4*cm, -27.0*cm, u'%s' % q[48]) # tipo de doc resp
            l.drawString(5.2*cm, -27.0*cm, u'%s' % q[49]) # num de doc resp
            l.drawString(3.9*cm, -27.7*cm, u'%s' % q[50]) # calle dom resp
            l.drawString(10.2*cm, -27.7*cm, u'%s' % q[51]) # num dom resp
            l.drawString(12.6*cm, -27.7*cm, u'%s' % q[52]) # piso dom resp
            l.drawString(14.8*cm, -27.7*cm, u'%s' % q[53]) # dpto dom resp
            l.drawString(2.9*cm, -28.4*cm, u'%s' % q[54]) # localidad dom resp
            l.drawString(8.9*cm, -28.4*cm, u'%s' % q[55]) # cp dom resp
            l.drawString(13.1*cm, -28.4*cm, u'%s' % q[56]) # te dom resp
            l.showPage()
            l.save()
        # Reverso del legajo    
        for alumno in alumnos:
            id = alumno[0]
            c.execute('''SELECT * FROM alumnos WHERE id_alumno = %s''' % id)
            q = c.fetchone()
            c.execute('''SELECT * FROM cursos WHERE num_curso = %s''' % curso)
            k = c.fetchone()
            #Se hace una lista igual que la tupla para
            # poder asignar espacios a los campos vacíos.
            qr = list(q)
            
            for f in range(57,85):
                if q[f] == None:
                    qr[f] = ' '
            l = legajo_dgce.canvas.Canvas("./planillas/legajos_%s/%s_%s_legajo_reverso.pdf" % (curso, q[1], q[2]),
             pagesize=portrait(legal))
            legajo_dgce.legajo_reverso(l)
            l.drawString(3.2*cm, -1.3*cm, u'%s' % qr[57]) # Obra social
            l.drawString(14.2*cm, -1.3*cm, u'%s' % qr[58]) # Num afiliado
            # Tiene una enfermedad
            if q[59] == '1':
                l.drawString(1.1*cm, -3.3*cm, u'X')
                l.drawString(5.0*cm, -3.3*cm, u'%s' % qr[60]) # tipo de enfermedad 
            else:
                l.drawString(2.9*cm, -3.3*cm, u'X')
            # Si fue internado
            if q[61] == '1':
                l.drawString(1.1*cm, -4.7*cm, u'X')
                l.drawString(5.5*cm, -4.7*cm, u'%s' % qr[62]) # tipo de internación
            else:
                l.drawString(2.9*cm, -4.7*cm, u'X')
            # Si tiene alergia
            if q[63] == '1':
                l.drawString(10.7*cm, -5.3*cm, u'X')
                l.drawString(9.8*cm, -6.0*cm, u'%s' % qr[64]) # tipo de alergia
                if q[65] == '1':
                    l.drawString(16.7*cm, -6.6*cm, u'X') # tratamiento sí?
                else:
                    l.drawString(17.8*cm, -6.6*cm, u'X') # tratamiento no?
            else:
                l.drawString(13.5*cm, -5.3*cm, u'X')
            # Si recibe tratamientos
            if q[66] == '1':
                l.drawString(7.5*cm, -7.8*cm, u'X')
                l.drawString(12.8*cm, -7.8*cm, u'%s' % qr[67]) # espec tratamiento
            else:
                l.drawString(9.0*cm, -7.8*cm, u'X')
            # quirúrgico
            if q[68] == '1':
                l.drawString(4.5*cm, -8.4*cm, u'X')
                l.drawString(8.7*cm, -8.4*cm, u'%s' % qr[69]) # edad cirugía
                l.drawString(13.1*cm, -8.4*cm, u'%s' % qr[70]) # espec cirugía
            else:
                l.drawString(6.2*cm, -8.4*cm, u'X')
            # limitación
            if q[71] == '1':
                l.drawString(8.3*cm, -9.0*cm, u'X') 
                l.drawString(13.1*cm, -9.0*cm, u'%s' % qr[72]) # aclarac limitación
            else:
                l.drawString(10.0*cm, -9.0*cm, u'X')
            # otros problemas de salud
            l.drawString(6.0*cm, -9.6*cm, u'%s' % qr[73])
            # en caso de problema llamar
            # institución
            l.drawString(5.8*cm, -14.2*cm, u'%s' % qr[74]) #nombre
            l.drawString(5.8*cm, -14.9*cm, u'%s' % qr[75]) #domicilio
            l.drawString(12.8*cm, -14.9*cm, u'%s' % qr[76]) #te
            # médico
            l.drawString(5.8*cm, -15.6*cm, u'%s' % qr[77]) #apellidos
            l.drawString(12.8*cm, -15.6*cm, u'%s' % qr[78]) #nombre
            l.drawString(5.8*cm, -16.3*cm, u'%s' % qr[79]) #domicilio
            l.drawString(12.8*cm, -16.3*cm, u'%s' % qr[80]) #te
            # familiar
            l.drawString(5.8*cm, -17.0*cm, u'%s' % qr[81]) #apellidos
            l.drawString(12.8*cm, -17.0*cm, u'%s' % qr[82]) #nombre
            l.drawString(5.8*cm, -17.7*cm, u'%s' % qr[83]) #domicilio
            l.drawString(12.8*cm, -17.7*cm, u'%s' % qr[84]) #te
            l.showPage()
            l.save()
        # Cierro las conexiones e informo de la confección
        # correcta de los legajos    
        c.close()
        wx.MessageBox(u'Tarea realizada con éxito. se han confeccionado los legajos del curso %s y se guardaron en una carpeta propia dentro del directorio ./planillas' % curso,
         u'Confección de legajos', wx.OK | wx.ICON_INFORMATION, self)


# Estadísticas generales Módulos actuales
    def OnEstadisticasGenerales(self, evt):
        import stats
        ventana = stats.MyFrame(self, -1, u'Estadísticas generales por módulos vigentes',
         style = wx.DEFAULT_FRAME_STYLE)
        ventana.CenterOnScreen()
        ventana.Show(True)

# Estadísticas generales anual actual
    def OnEstadisticasGeneralesAnualActual(self, evt):
        from seleccanio import SelecDialog as sc
        self.dialogo = sc(self)
        self.dialogo.ShowModal()
        import stats_anual_actual
        ventana = stats_anual_actual.MyFrame(self, -1, u'Estadísticas generales del año en curso',
         style = wx.DEFAULT_FRAME_STYLE)
        ventana.CenterOnScreen()
        ventana.Show(True)

# Gastos nuevos por período
    def OnGastNuPer(self, evt):
        self.GNPPer=wx.Frame(self, -1, u'Gastos por período', size=(300, 200))
        self.GNPPer.CenterOnScreen()
        panel = wx.Panel(self.GNPPer, -1 )
        Lblsel = wx.StaticText(panel, -1, u'Seleccione el período: ', (20, 20))
        radio1 = wx.RadioButton(panel, -1, u'Anual', (20, 60), style=wx.RB_GROUP)
        radio2 = wx.RadioButton(panel, -1, u'Mensual', (20, 90))
        self.anual = wx.SpinCtrl(panel, -1, u'', (120, 60), (120, -1))
        self.anual.SetRange(1990, 2100)
        self.anual.SetValue(2009)
        meses = [u'enero', u'febrero', u'marzo', u'abril', u'mayo', u'junio', u'julio', u'agosto',
        u'setiembre', u'octubre', u'noviembre', u'diciembre']
        self.mensual = wx.ComboBox(panel, -1, u'enero', (120, 90), (100, -1), meses, wx.CB_DROPDOWN)
        self.texts = {u'Anual': self.anual, u'Mensual': self.mensual}
        self.mensual.Enable(False)
        for eachRadio in [radio1, radio2]:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadioGastos, eachRadio)
        self.selectedTextGastos = self.anual
        BtnCancelar = wx.Button(panel, wx.ID_CANCEL,pos = (100, 150))
        self.Bind(wx.EVT_BUTTON, self.OnCloseGastos, BtnCancelar)
        BtnAceptar = wx.Button(panel, wx.ID_OK, pos = (200, 150))
        self.Bind(wx.EVT_BUTTON, self.OnGastNuPerPrinc, BtnAceptar)
        self.GNPPer.Show(True)

    def OnGastNuPerPrinc(self, event):
        import wx.grid
        self.GasNuPerPr = wx.Frame(self, -1, u'Gastos por período', size=(800, 600))
        self.GasNuPerPr.CenterOnScreen()
        self.panel = wx.Panel(self.GasNuPerPr, -1)
        self.mes = self.mensual.GetValue()
        label = wx.StaticText(self.panel, -1, u'Gastos correspondientes al período : %s' %(self.mes),
         pos = (20, 15))
        self.grilla = wx.grid.Grid(self.panel, -1, (25, 50), (750, 400), style=wx.WANTS_CHARS)
        self.grilla.CreateGrid(125, 6)
        colLabels = [u'Fecha', u'Descripción', u'Responsable', u'In', u'Out', u'Observaciones']
        for col in range (6):
            self.grilla.SetColLabelValue(col, colLabels[col])
        self.grilla.SetColSize(0, 80)
        self.grilla.SetColSize(1, 210)
        self.grilla.SetColSize(2, 103)
        self.grilla.SetColSize(3, 70)
        self.grilla.SetColSize(4, 70)
        self.grilla.SetColSize(5, 110)
        self.GNPPer.Destroy()
        self.saldo = 0
        self.labelsaldo = wx.StaticText(self.panel, -1, u'El saldo del período es : %s' %(str(self.saldo)),
         pos = (20, 500))
        BtnCancelar = wx.Button(self.panel, wx.ID_CANCEL, pos = (685, 540))
        BtnRefrescar = wx.Button(self.panel, wx.ID_REFRESH, pos = (250, 540))
        BtnGuardar = wx.Button(self.panel, wx.ID_SAVE, pos = (350, 540))
        BtnExportar = wx.Button(self.panel, wx.ID_SAVEAS, pos = (450, 540))
        BtnImprimir = wx.Button(self.panel, wx.ID_PRINT, pos = (585, 540))
        self.Bind(wx.EVT_BUTTON, self.OnCloseCaja, BtnCancelar)
        self.Bind(wx.EVT_BUTTON, self.OnCalcularCaja, BtnRefrescar)
        self.Bind(wx.EVT_BUTTON, self.OnGuardarPlanilla, BtnGuardar)
        self.GasNuPerPr.Show(True)

    def OnCloseGastos(self, event):
        self.GNPPer.Destroy()

    #Selección de período a crear
    def OnRadioGastos(self, event):
        if self.selectedTextGastos:
            self.selectedTextGastos.Enable(False)
        radioSelected = event.GetEventObject()
        textGastos = self.texts[radioSelected.GetLabel()]
        textGastos.Enable(True)
        self.selectedTextGastos = textGastos

    #Cancelar Planilla
    def OnCloseCaja(self, event):
        self.GasNuPerPr.Destroy()

    #Calcular Saldo de Caja
    def OnCalcularCaja(self, event):
        ingreso = 0
        egreso = 0
        for entrada in range (125):
            try:
                ingreso = ingreso + float(self.grilla.GetCellValue(entrada, 3))
            except ValueError:
                pass
            try:
                egreso = egreso + float(self.grilla.GetCellValue(entrada, 4))
            except ValueError:
                pass
        self.saldo = ingreso - egreso
        self.labelsaldo.SetLabel(u'El saldo del período es : %s' %(str(self.saldo)))

    #Guardar Planilla actual
    def OnGuardarPlanilla(self, event):
        ahora = wx.Now()
        anio = ahora[-4:]
        f=open('./planillas/%s_%s' %(self.mes, anio), 'w')
        for y in range (125):
            for x in range (6):
                    valor = self.grilla.GetCellValue(y, x)
                    f.write('%s;' %valor),
            f.write('\n')

# Abrir gasto por período
    def OnAbrGastPer(self, evt):
        pass

# Gastos nuevos por proyecto
    def OnGastNuProy(self, evt):
        import wx.grid
        # Creo el diálogo para darle al proyecto un nombre
        self.dlg = wx.TextEntryDialog(None, u'Nombre del proyecto', u'Nombre del proyecto', u'', style=wx.OK|wx.CANCEL, pos=(300, 300))
        if self.dlg.ShowModal() == wx.ID_OK:
            self.proyectonuevo = self.dlg.GetValue()
        else:
            self.dlg.Destroy()
            return
        self.dlg.Destroy()
        self.GasNuProy = wx.Frame(self, -1, u'Gastos por proyecto', (10,10), (800, 600))
        self.panel = wx.Panel(self.GasNuProy, -1)
        label = wx.StaticText(self.panel, -1, u'Gastos correspondientes al proyecto : %s' %(self.proyectonuevo) , pos = (20, 15))
        self.grilla = wx.grid.Grid(self.panel, -1, (25, 50), (750, 400), style=wx.WANTS_CHARS)
        self.grilla.CreateGrid(125, 6)
        colLabels = [u'Fecha', u'Descripción', u'Responsable', u'In', u'Out', u'Observaciones']
        for col in range (6):
            self.grilla.SetColLabelValue(col, colLabels[col])
        self.grilla.SetColSize(0, 80)
        self.grilla.SetColSize(1, 210)
        self.grilla.SetColSize(2, 103)
        self.grilla.SetColSize(3, 70)
        self.grilla.SetColSize(4, 70)
        self.grilla.SetColSize(5, 110)
        self.saldo = 0
        self.labelsaldo = wx.StaticText(self.panel, -1, u'El saldo de la caja es : %s' %(str(self.saldo)),
         pos = (20, 500))
        BtnCancelar = wx.Button(self.panel, wx.ID_CANCEL, pos = (685, 540))
        BtnRefrescar = wx.Button(self.panel, wx.ID_REFRESH, pos = (250, 540))
        BtnGuardar = wx.Button(self.panel, wx.ID_SAVE, pos = (350, 540))
        BtnExportar = wx.Button(self.panel, wx.ID_SAVEAS, pos = (450, 540))
        BtnImprimir = wx.Button(self.panel, wx.ID_PRINT, pos = (585, 540))
        self.Bind(wx.EVT_BUTTON, self.OnCloseCajaProy, BtnCancelar)
        self.Bind(wx.EVT_BUTTON, self.OnCalcularCajaProy, BtnRefrescar)
        self.Bind(wx.EVT_BUTTON, self.OnGuardarPlanillaProy, BtnGuardar)
        self.GasNuProy.Show(True)

#Cancelar Planilla
    def OnCloseCajaProy(self, event):
        self.GasNuProy.Destroy()

#Guardar Planilla actual
    def OnGuardarPlanillaProy(self, event):
        ahora = wx.Now()
        anio = ahora[-4:]
        f=open('./proyectos/%s' %(self.proyectonuevo), 'w')
        for y in range (125):
            for x in range (6):
                    valor = self.grilla.GetCellValue(y, x)
                    f.write('%s;' %valor),
            f.write('\n')

# Abrir gasto por proyecto
    def OnAbrGastProy(self, evt):
        import os
        import wx.grid
        listado = os.listdir('./proyectos')
        dlg = wx.SingleChoiceDialog(self, u'Seleccione el proyecto a editar:',
         u'Abrir planilla de gastos', listado)
        if (dlg.ShowModal() == wx.ID_OK):
            self.proyecto = dlg.GetStringSelection()
            dlg.Destroy()
            self.GasAbrProy = wx.Frame(self, -1, u'Gastos por proyecto', (10,10), (800, 600))
            self.panel = wx.Panel(self.GasAbrProy, -1)
            label = wx.StaticText(self.panel, -1, u'Gastos correspondientes al proyecto : %s' %(self.proyecto),
            pos = (20, 15))
            self.grilla = wx.grid.Grid(self.panel, -1, (25, 50), (750, 400), style=wx.WANTS_CHARS)
            self.grilla.CreateGrid(125, 6)
            colLabels = [u'Fecha', u'Descripción', u'Responsable', u'In', u'Out', u'Observaciones']
            for col in range (6):
                self.grilla.SetColLabelValue(col, colLabels[col])
            self.grilla.SetColSize(0, 80)
            self.grilla.SetColSize(1, 210)
            self.grilla.SetColSize(2, 103)
            self.grilla.SetColSize(3, 70)
            self.grilla.SetColSize(4, 70)
            self.grilla.SetColSize(5, 110)
            self.saldo = 0
            self.labelsaldo = wx.StaticText(self.panel, -1, u'El saldo de la caja es : %s' %(str(self.saldo)),
             pos = (20, 500))
            BtnCancelar = wx.Button(self.panel, wx.ID_CANCEL, pos = (685, 540))
            BtnRefrescar = wx.Button(self.panel, wx.ID_REFRESH, pos = (250, 540))
            BtnGuardar = wx.Button(self.panel, wx.ID_SAVE, pos = (350, 540))
            BtnExportar = wx.Button(self.panel, wx.ID_SAVEAS, pos = (450, 540))
            BtnImprimir = wx.Button(self.panel, wx.ID_PRINT, pos = (585, 540))
            self.Bind(wx.EVT_BUTTON, self.OnCloseCajaProyAbrProy, BtnCancelar)
            self.Bind(wx.EVT_BUTTON, self.OnCalcularCajaProy, BtnRefrescar)
            self.Bind(wx.EVT_BUTTON, self.OnGuardarPlanillaExistenteAbrProy, BtnGuardar)
            f = open('./proyectos/%s' %(self.proyecto), 'r')
            c = 0
            for linea in f.readlines():
                a = linea.split(';')
                for i in range (6):
                    self.grilla.SetCellValue(c, i, a[i])
                c = c + 1
            f.close()
            ingreso = 0
            egreso = 0
            for entrada in range (125):
                try:
                    ingreso = ingreso + float(self.grilla.GetCellValue(entrada, 3))
                except ValueError:
                    pass
                try:
                    egreso = egreso + float(self.grilla.GetCellValue(entrada, 4))
                except ValueError:
                    pass
            self.saldo = ingreso - egreso
            self.labelsaldo.SetLabel(u'El saldo de la caja es : %s' %(str(self.saldo)))
            self.GasAbrProy.Show(True)

    #Cancelar Planilla
    def OnCloseCajaProyAbrProy(self, event):
        self.GasAbrProy.Destroy()

    #Guardar Planilla existente
    def OnGuardarPlanillaExistenteAbrProy(self, event):
        ahora = wx.Now()
        anio = ahora[-4:]
        f=open('./proyectos/%s' %(self.proyecto), 'w')
        for y in range (125):
            for x in range (6):
                    valor = self.grilla.GetCellValue(y, x)
                    f.write('%s;' %valor),
            f.write('\n')

    #Calcular Saldo de Caja
    def OnCalcularCajaProy(self, event):
        ingreso = 0
        egreso = 0
        for entrada in range (125):
            try:
                ingreso = ingreso + float(self.grilla.GetCellValue(entrada, 3))
            except ValueError:
                pass
            try:
                egreso = egreso + float(self.grilla.GetCellValue(entrada, 4))
            except ValueError:
                pass
        self.saldo = ingreso - egreso
        self.labelsaldo.SetLabel(u'El saldo de la caja es : %s' %(str(self.saldo)))

# Agenda
    def OnAgenda(self, evt):
        import subprocess
        subprocess.Popen(['sunbird'])

# Nueva gestión
    def OnNuevaGestion(self, evt):
        import editor
        ventana = editor.RichTextFrame(self, -1, u'Nuevo documento de gestión', size=(700, 500), style = wx.DEFAULT_FRAME_STYLE)
        ventana.CenterOnScreen()
        ventana.Show(True)

# Temario vacío
    def OnTemario(self, evt):
        from reportlab.lib.pagesizes import legal
        import temario
        c = temario.canvas.Canvas("./planillas/temario.pdf", pagesize=legal)
        temario.temarios(c)
        c.showPage()
        c.save()
        dlg = wx.MessageDialog(self, u"Un temario ha sido generado\n en el directorio '/planillas'",
                               u"Planilla de temario",
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

# Ficha de curso vacía
    def OnFichadeCurso(self, evt):
        from reportlab.lib.pagesizes import legal, landscape
        import fichacurso
        c = fichacurso.canvas.Canvas("./planillas/fichacurso.pdf", pagesize=landscape(legal))
        fichacurso.fichacursos(c)
        c.showPage()
        c.save()
        dlg = wx.MessageDialog(self, u"Una ficha de curso ha sido generada\n en el directorio '/planillas'",
                               u"Ficha de curso",
                               wx.OK | wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

# Acta de examen vacía
    def OnActaExamen(self,evt):
        from reportlab.lib.pagesizes import legal, landscape
        import actaexamen
        c = actaexamen.canvas.Canvas('./planillas/actaexamen.pdf', pagesize = landscape(legal))
        actaexamen.actaexamenes(c)
        c.showPage()
        c.save()
        dlg = wx.MessageDialog(self, u"Un acta de examen ha sido generada\n en el directorio '/planillas'",
                                u"Acta de examen",
                                wx.OK | wx.ICON_INFORMATION
                                )
        dlg.ShowModal()
        dlg.Destroy()

# Legajo Oficial vacío
    def OnLegajo(self, evt):
        from reportlab.lib.pagesizes import legal, portrait
        import legajo_dgce
        c = legajo_dgce.canvas.Canvas('./planillas/legajo.pdf', pagesize = portrait(legal))
        legajo_dgce.legajo(c)
        c.showPage()
        c.save()
        c = legajo_dgce.canvas.Canvas('./planillas/legajo_reverso.pdf', pagesize = portrait(legal))
        legajo_dgce.legajo_reverso(c)
        c.showPage()
        c.save()
        dlg = wx.MessageDialog(self, u"Se han generado las dos páginas del legajo en el directorio '/planillas'",
                                u"Legajo oficial vacío",
                                wx.OK | wx.ICON_INFORMATION
                                )
        dlg.ShowModal()
        dlg.Destroy()



# Acerca de
    def OnAbout(self, evt):
        try:
            self.frame.Close()
        finally:
            # En el about se incorpora la GPL original en inglés que es la que vale
            from wx.lib.wordwrap import wordwrap
            import gpl
            info = wx.AboutDialogInfo()
            info.Name = u'Administrador SancaBase'
            info.Version = u'0.9.9.0'
            info.Copyright = u'Copyright Javier Castrillo'
            info.Description = u'''Esta aplicación está pensada desde el CFP 401
            de Vicente López hacia todos los centros
            de Formación Profesional que día a día ponen
            lo mejor de sí en pos de enriquecer a la siempre
            olvidada y rezagada educación de los pueblos.'''
            info.WebSite = (u'http://trac.usla.org.ar/proyectos/sanca', u'Sitio del proyecto')
            info.Developers = [ u'Javier Castrillo  riverplatense at gmail dot com']
            info.License = wordwrap(gpl.licenseText, 500, wx.ClientDC(self))
            wx.AboutBox(info)

    def OnAyuda(self, event):
        import  wx.html as  html
        ventana = wx.Frame(parent = None, title = u'Ayuda de Sancabase', size = (600, 500))
        ventana.CenterOnScreen()
        nav = html.HtmlWindow(ventana , id = -1)
        nav.LoadPage('./html/index.html')
        ventana.Show()
        return True


# Cancelar (válido para cualquiera de los diálogos)
    def OnCancelar(self, event):
        self.frame.Close()

# Clase Listado de Alumnos
class ListAlumFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de estudiantes:', pos=(30, 120), size=(800, 490))
        self.CenterOnScreen()
        f=open('./py/listalum.py', 'r')
        imp.load_module('listalum', f, 'listalum', ('.py', 'U', 1))
        import py.listalum as listalum
        f.close()
        reload(listalum)
        panel = wx.Panel(self, -1)
        LblLa = wx.StaticText(panel, -1, u'Listado General de Estudiantes:')
        LblLa.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(800, 390), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(listalum.columns):
            self.list.InsertColumn(col, text.decode('utf-8'))
        self.itemDataMap = {}
        for item in listalum.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(listalum.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT)
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLa, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de alumnos
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listalum.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de alumnos</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado general de alumnos</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Id</th><th>Apellidos</th><th>Nombres</th><th>DNI</th><th>Calle</th><th>N°</th><th>Localidad</th><th>TE</th>\n')
        it = 0
        while it < 100000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 8):
                a = self.GetColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/listalum.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def GetColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Clase listado de cursos
class ListCursosFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de cursos:', pos=(30, 120), size=(800, 490))
        self.CenterOnScreen()
        panel = wx.Panel(self, -1)
        import py.listcursos as listcursos
        reload(listcursos)
        LblLc = wx.StaticText(panel, -1, u'Listado de cursos:')
        LblLc.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(840, 400), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(listcursos.columns):
            self.list.InsertColumn(col, text.decode('utf-8'))
        self.itemDataMap = {}
        for item in listcursos.rows:
            index = self.list.InsertStringItem(sys.maxint, item[0])
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(listcursos.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT, pos=(520, 440))
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL, pos=(620, 440))
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLc, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado cursos
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listcursos.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de cursos</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado completo de cursos.</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>Orden</th><th>N° Curso</th><th>Tipo</th><th>Especialidad</th><th>Instructor/a</th><th>Horas</th><th>Establecimiento</th>\n')
        it = 0
        while it < 10000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 6):
                a = self.GetColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/listcursos.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def GetColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Clase Listados Cursos por número
class ListCurNumFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de curso por número:', pos=(30, 120), size=(800, 490))
        panel = wx.Panel(self, -1)
        import py.list_curso_num as list_curso_num
        reload(list_curso_num)
        self.num_curso = list_curso_num.num_curso
        LblLcn = wx.StaticText(panel, -1, u'Listado de curso Número %s:' %(self.num_curso))
        LblLcn.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(800, 400), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(list_curso_num.columns):
            self.list.InsertColumn(col, text.decode('utf-8'))
        self.itemDataMap = {}
        for item in list_curso_num.rows:
            index = self.list.InsertStringItem(sys.maxint, item[0])
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(list_curso_num.columns))
        #self.checkListCur = wx.CheckBox (panel, -1, u'Formato ficha de curso', pos=(210, 440))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT)
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLcn, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        #btnSizer.Add(self.checkListCur)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado cursos por número
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listcursonum.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de curso N° %s</title>\n' %(self.num_curso))
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado de curso N° %s.</h2>\n' %(self.num_curso))
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Apellidos</th><th>Nombres</th><th>DNI</th><th>Calle</th><th>N°</th><th>Localidad</th><th>TE</th><th>Correo</th>\n')
        it = 0
        while it < 10000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 8):
                a = self.GetColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/listcursonum.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def GetColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Clase Listados Cursos por Instructor
class ListCurInsFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de curso por instructor/a:', size=(800, 490))
        panel = wx.Panel(self, -1)
        self.CenterOnScreen()
        import py.list_curso_ins as list_curso_ins
        reload(list_curso_ins)
        self.instructor = list_curso_ins.instructor
        LblLcn = wx.StaticText(panel, -1, u'Listado de curso del/de la instructor/a %s:' %(self.instructor))
        LblLcn.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(800, 400), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(list_curso_ins.columns):
            self.list.InsertColumn(col, text.decode('UTF-8'))
        self.itemDataMap = {}
        for item in list_curso_ins.rows:
            index = self.list.InsertStringItem(sys.maxint, item[0])
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(list_curso_ins.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT)
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLcn, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado cursos por Instructor
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listcursoinst.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de curso por instructor/a - %s</title>\n' %(self.instructor.encode('UTF-8')))
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado de curso por instructor/a - %s.</h2>\n' %(self.instructor.encode('UTF-8')))
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<th>Orden</th><th>N° Curso</th><th>Especialidad</th><th>Ciclo</th><th>Establecimiento</th>\n')
        f.write('<table border="1">\n' )
        it = 0
        while it < 10000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (2, 5):
                a = self.GetColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/listcursoinst.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def GetColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

#Clase Listado de Instructores
class ListInstFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        f=open('./py/listinstruc.py', 'r')
        imp.load_module('listinstruc', f, 'listinstruc', ('.py', 'U', 1))
        import py.listinstruc as listinstruc
        f.close()
        reload(listinstruc)
        wx.Frame.__init__(self, None, -1, u'Listado de Instructores/as:', pos=(30, 120), size=(800, 490))
        panel = wx.Panel(self, -1)
        LblLi = wx.StaticText(panel, -1, u'Listado General de Instructores/as:', (30, 20))
        LblLi.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(790, 390), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(listinstruc.columns):
            self.list.InsertColumn(col, text)
        self.itemDataMap = {}
        for item in listinstruc.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(listinstruc.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT, pos=(520, 440))
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL, pos=(620, 440))
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLi, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de Instructores
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listinstruc.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de instructores/as</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado general de instructores/as</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Id</th><th>Apellidos</th><th>Nombres</th><th>TE</th><th>Dirección</th><th>Correo-e</th>\n')
        it = 0
        while it < 10000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 6):
                a = self.getColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/listinstruc.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def getColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

class ListCoordFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de Coordinadores/as:', pos=(30, 120), size=(800, 490))
        f=open('./py/listcoord.py', 'r')
        imp.load_module('listcoord', f, 'listcoord', ('.py', 'U', 1))
        import py.listcoord as listcoord
        f.close()
        reload(listcoord)
        panel = wx.Panel(self, -1)
        LblLc = wx.StaticText(panel, -1, u'Listado General de Coordinadores/as:', (30, 20))
        LblLc.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(790, 390), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(listcoord.columns):
            self.list.InsertColumn(col, text)
        self.itemDataMap = {}
        for item in listcoord.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(listcoord.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT, pos=(520, 440))
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL, pos=(620, 440))
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLc, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de Coordinadores
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listcoord.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de coordinadores/as</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado general de coordinadores/as</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Id</th><th>Apellidos</th><th>Nombres</th><th>TE</th><th>Domicilio</th><th>Correo-e</th>\n')
        it = 0
        while it < 10000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 6):
                a = self.getColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/listcoord.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def getColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Clase listado de administrativos
class ListAdmFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de Administrativos/as:', pos=(30, 120), size=(800, 490))
        f=open('./py/listadm.py', 'r')
        imp.load_module('listadm', f, 'listadm', ('.py', 'U', 1))
        import py.listadm as listadm
        reload(listadm)
        f.close()
        panel = wx.Panel(self, -1)
        LblLad = wx.StaticText(panel, -1, u'Listado General de Administrativos/as:', (30, 20))
        LblLad.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(790, 390), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(listadm.columns):
            self.list.InsertColumn(col, text.decode('UTF-8'))
        self.itemDataMap = {}
        for item in listadm.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(8, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(listadm.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT, pos=(520, 440))
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL, pos=(620, 440))
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLad, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de administrativos
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listadm.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de administrativos/as</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado general de administrativos/as</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Cargo</th><th>Apellidos</th><th>Nombres</th><th>Calle</th><th>N°</th><th>Localidad</th><th>TE</th><th>Celular</th><th>Correo</th>\n')
        it = 0
        while it < 10000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 9):
                a = self.getColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/listadm.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def getColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()


# Clase listado de auxiliares
class ListAuxFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de Auxiliares:', pos=(30, 120), size=(800, 490))
        #f=open('./py/listaux.py', 'r')
        #imp.load_module('listaux', f, 'listaux', ('.py', 'U', 1))
        #import py.listaux as listaux
        #f.close()
        import py.listaux as listaux
        reload(listaux)
        panel = wx.Panel(self, -1)
        LblLad = wx.StaticText(panel, -1, u'Listado General de Auxiliares:', (30, 20))
        LblLad.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(790, 390), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(listaux.columns):
            self.list.InsertColumn(col, text.decode('UTF-8'))
        self.itemDataMap = {}
        for item in listaux.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(8, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(9, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(listaux.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT, pos=(520, 440))
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL, pos=(620, 440))
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLad, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de auxiliares
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listaux.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de auxiliares</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado general de auxiliares</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Cargo</th><th>Apellidos</th><th>Nombres</th><th>Calle</th><th>N°</th><th>Localidad</th><th>TE</th><th>Documento</th><th>Correo</th><th>Fecha inicio</th>\n')
        it = 0
        while it < 10000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 10):
                a = self.getColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 400))
        self.html.LoadPage('./html/listaux.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def getColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Clase Listado de Centros
class ListCentrosFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de Centros:', pos=(30, 120), size=(800, 490))
        f=open('./py/listcentros.py', 'r')
        imp.load_module('listcentros', f, 'listcentros', ('.py', 'U', 1))
        import py.listcentros as listcentros
        reload(listcentros)
        f.close()
        panel = wx.Panel(self, -1)
        LblLgc = wx.StaticText(panel, -1, u'Listado General de Centros:')
        LblLgc.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(800, 400),
         style=wx.LC_REPORT | wx.LC_SORT_ASCENDING | wx.HSCROLL)
        for col, text in enumerate(listcentros.columns):
            self.list.InsertColumn(col, text)
        self.itemDataMap = {}
        for item in listcentros.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(8, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(listcentros.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT)
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLgc, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de centros
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/listcentros.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de centros</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado general de centros</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Id</th><th>Nombre</th><th>Calle</th><th>N°</th><th>Localidad</th><th>CP</th><th>TE</th><th>Correo-e</th><th>Coordinador/a</th>\n')
        it = 0
        while it < 10000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('UTF-8')))
            for i in range (1, 9):
                a = self.getColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('UTF-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/listcoord.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def getColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Clase Listado de Movimientos de caja
class ListMovFechaFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de movimientos por fecha:', pos=(30, 120), size=(800, 490))
        self.CenterOnScreen()
        f=open('./py/movporfecha.py', 'r')
        imp.load_module('movporfecha', f, 'movporfecha', ('.py', 'U', 1))
        import py.movporfecha as movporfecha
        reload(movporfecha)
        import datetime
        f.close()
        panel = wx.Panel(self, -1)
        LblLa = wx.StaticText(panel, -1, u'Listado de movimientos por fecha:')
        LblLa.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(800, 390), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(movporfecha.columns):
            self.list.InsertColumn(col, text.decode('utf-8'))
        self.itemDataMap = {}
        for item in movporfecha.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(movporfecha.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT)
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLa, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de movimientos por fecha
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/movporfecha.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de movimientos por fecha</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado de movimientos por fecha</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Id</th><th>Fecha</th><th>Tipo</th><th>Comprobante</th><th>Responsable</th><th>Debe</th><th>Haber</th><th>destino</th>\n')
        it = 0
        while it < 100000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 8):
                a = self.GetColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/movporfecha.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def GetColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Impresión de listado por destino
class ListMovDestinoFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de movimientos por destino:', pos=(30, 120), size=(800, 490))
        self.CenterOnScreen()
        f=open('./py/movpordestino.py', 'r')
        imp.load_module('movpordestino', f, 'movpordestino', ('.py', 'U', 1))
        import py.movpordestino as movpordestino
        reload(movpordestino)
        import datetime
        f.close()
        panel = wx.Panel(self, -1)
        LblLa = wx.StaticText(panel, -1, u'Listado de movimientos por destino:')
        LblLa.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(800, 390), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(movpordestino.columns):
            self.list.InsertColumn(col, text.decode('utf-8'))
        self.itemDataMap = {}
        for item in movpordestino.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(movpordestino.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT)
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLa, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de movimientos por fecha
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/movpordestino.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de movimientos por destino</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado de movimientos por destino</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Id</th><th>Fecha</th><th>Tipo</th><th>Comprobante</th><th>Responsable</th><th>Debe</th><th>Haber</th><th>destino</th>\n')
        it = 0
        while it < 100000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 8):
                a = self.GetColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/movpordestino.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def GetColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

# Impresión de listado por responsable
class ListMovResponsableFrame(wx.Frame, wx.lib.mixins.listctrl.ColumnSorterMixin):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Listado de movimientos por responsable:', pos=(30, 120), size=(800, 490))
        self.CenterOnScreen()
        f=open('./py/movporresponsable.py', 'r')
        imp.load_module('movporresponsable', f, 'movporresponsable', ('.py', 'U', 1))
        import py.movporresponsable as movporresponsable
        reload(movporresponsable)
        import datetime
        f.close()
        panel = wx.Panel(self, -1)
        LblLa = wx.StaticText(panel, -1, u'Listado de movimientos por responsable:')
        LblLa.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.list = wx.ListCtrl(panel, -1, size=(800, 390), style=wx.LC_REPORT | wx.LC_SORT_ASCENDING)
        for col, text in enumerate(movporresponsable.columns):
            self.list.InsertColumn(col, text.decode('utf-8'))
        self.itemDataMap = {}
        for item in movporresponsable.rows:
            index = self.list.InsertStringItem(sys.maxint, str(item[0]))
            for col, text in enumerate(item[1:]):
                self.list.SetStringItem(index, col+1, text)
            self.list.SetItemData(index, index)
            self.itemDataMap[index] = item
        self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(4, wx.LIST_AUTOSIZE_USEHEADER)
        self.list.SetColumnWidth(5, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(6, wx.LIST_AUTOSIZE)
        self.list.SetColumnWidth(7, wx.LIST_AUTOSIZE)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(movporresponsable.columns))
        BtnImpresion = wx.Button(panel, wx.ID_PRINT)
        BtnCancelarImp = wx.Button(panel, wx.ID_CANCEL)
        self.Bind(wx.EVT_BUTTON, self.OnImpresion, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCancelarImp, BtnCancelarImp)
        ppalSizer = wx.BoxSizer(wx.VERTICAL)
        ppalSizer.Add(LblLa, 0, wx.ALL, 5)
        ppalSizer.Add(wx.StaticLine(panel), 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
        datosSizer = wx.FlexGridSizer(cols=1, hgap=5, vgap=5)
        datosSizer.AddGrowableCol(0)
        datosSizer.Add(self.list, 1, wx.EXPAND)
        ppalSizer.Add(datosSizer, 0, wx.EXPAND|wx.ALL, 10)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnImpresion)
        btnSizer.Add((20,20), 1)
        btnSizer.Add(BtnCancelarImp)
        btnSizer.Add((20,20), 1)
        ppalSizer.Add(btnSizer, 0, wx.EXPAND|wx.BOTTOM, 10)
        panel.SetSizer(ppalSizer)
        ppalSizer.Fit(self)
        ppalSizer.SetSizeHints(self)

#Función impresión del listado de movimientos por fecha
    def OnImpresion(self, evt):
        # Creo un html con el listado para su posterior impresión
        f = open('./html/movporresponsable.html', 'w')
        f.write('<html>\n')
        f.write('<head>\n')
        f.write('<meta http-equiv="content-type" content="text/html; charset=UTF-8">\n')
        f.write('<title>Impresión de listado de movimientos por responsable</title>\n')
        f.write('<body>\n')
        f.write('<font size="2">')
        f.write('<h2>Listado de movimientos por responsable</h2>\n')
        f.write('<br>\n')
        f.write('<center>\n')
        f.write('<table border="1">\n' )
        f.write('<th>N°</th><th>Id</th><th>Fecha</th><th>Tipo</th><th>Comprobante</th><th>Responsable</th><th>Debe</th><th>Haber</th><th>destino</th>\n')
        it = 0
        while it < 100000:
            a = self.list.GetItemText(it)
            if a == '':
                break
            f.write('<tr>\n')
            f.write('  <td>%s</td><td>%s</td>\n' % (it, a.encode('utf-8')))
            for i in range (1, 8):
                a = self.GetColumnText(it, i)
                f.write('  <td>%s</td>\n' % (a.encode('utf-8')))
            f.write('</tr>\n')
            it = it + 1
        f.write('</table>\n')
        f.write('</center>\n')
        f.write('</font>')
        f.write('</body>\n')
        f.write('</html>')
        f.close()
        #Una vez creado el html con el listado lo muestro en un frame como vista previa
        import wx.html as htm
        self.frame = wx.Frame(self, -1, u'Vista previa de la impresión', (20, 20), (800, 600))
        self.panel = wx.Panel(self.frame, -1)
        self.html = htm.HtmlWindow(self.panel, -1, (5,5), (790, 500))
        self.html.LoadPage('./html/movporresponsable.html')
        self.printer = htm.HtmlEasyPrinting()
        BtnImpresion = wx.Button(self.panel, wx.ID_PRINT, pos=(520, 540))
        BtnCancelarImp = wx.Button(self.panel, wx.ID_CANCEL, pos=(620, 540))
        self.Bind(wx.EVT_BUTTON, self.OnImp, BtnImpresion)
        self.Bind(wx.EVT_BUTTON, self.OnCanc, BtnCancelarImp)
        self.frame.Show()

    # Dado el ID y la columna traigo el item deseado.
    def GetColumnText(self, index, col):
        item = self.list.GetItem(index, col)
        return item.GetText()

    def OnCancelarImp(self, evt):
        self.Close()

    def OnCanc (self, evt):
        self.frame.Destroy()
        self.Close()

    def GetListCtrl (self):
        return self.list

    def OnImp (self,evt):
        self.printer.GetPrintData().SetPaperId(wx.PAPER_LETTER)
        self.printer.PrintFile(self.html.GetOpenedPage())
        self.Close()

#Loop Principal
if __name__== '__main__':
    app = App()
    app.MainLoop()
