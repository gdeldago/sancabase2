#!/usr/bin/python
# -*- coding: UTF8 -*-
#
# archivo : fichaalumno.py
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

import wx

# begin wxGlade: extracode
# end wxGlade

class ModEstudiante(wx.Frame):
    def __init__(self, alumno, *args, **kwds):
        archivoBBDD = "sancabase2.db"
        bbdd = archivoBBDD
        import sqlite3 as sql3
        self.db = sql3.connect(bbdd)
        
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.alumno = alumno
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)
        self.label_titulo = wx.StaticText(self, -1, "Ficha de estudiante")
        self.static_line_1 = wx.StaticLine(self, -1)
        self.label_apellidos = wx.StaticText(self.notebook_1_pane_1, -1, "Apellidos:")
        self.text_ctrl_apellidos = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_nombres = wx.StaticText(self.notebook_1_pane_1, -1, "Nombres:")
        self.text_ctrl_nombres = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_sexo = wx.StaticText(self.notebook_1_pane_1, -1, "Sexo:")
        self.combo_box_sexo = wx.ComboBox(self.notebook_1_pane_1, -1, choices=["F", "M"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_tipo_doc = wx.StaticText(self.notebook_1_pane_1, -1, "Tipo doc:")
        self.combo_box_tipo_doc = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["DNI", "LC", "LE", "PAS", "ET"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_num_doc = wx.StaticText(self.notebook_1_pane_1, -1, u"Nº doc:")
        self.text_ctrl_num_doc = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_nacionalidad = wx.StaticText(self.notebook_1_pane_1, -1, "Nacionalidad:")
        self.combo_box_nacionalidad = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["AR", "BO", "BR", "CO", "CH", "EC", "ES", "IT", "PE", "PY", "UY", "VE"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN)
        self.label_fecha_nac = wx.StaticText(self.notebook_1_pane_1, -1, "Fecha nac:")
        self.datepicker_fechanac = wx.DatePickerCtrl(self.notebook_1_pane_1, -1, style=wx.DP_DROPDOWN|wx.DP_SHOWCENTURY)
        self.label_lugarnac = wx.StaticText(self.notebook_1_pane_1, -1, "Lugar nac:")
        self.text_ctrl_lugarnac = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_domicilio = wx.StaticText(self.notebook_1_pane_1, -1, "Domicilio:")
        self.label_vacio = wx.StaticText(self.notebook_1_pane_1, -1, "")
        self.label_calle = wx.StaticText(self.notebook_1_pane_1, -1, "Calle:")
        self.text_ctrl_calle = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_num = wx.StaticText(self.notebook_1_pane_1, -1, u"Número:")
        self.text_ctrl_numero = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_piso = wx.StaticText(self.notebook_1_pane_1, -1, "Piso:")
        self.text_ctrl_piso = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_dpto = wx.StaticText(self.notebook_1_pane_1, -1, "Dpto:")
        self.text_ctrl_dpto = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_cp = wx.StaticText(self.notebook_1_pane_1, -1, u"Cód postal:")
        self.text_ctrl_cp = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_localidad = wx.StaticText(self.notebook_1_pane_1, -1, "Localidad:")
        self.text_ctrl_localidad = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_pcia = wx.StaticText(self.notebook_1_pane_1, -1, "Provincia:")
        self.text_ctrl_pcia = wx.TextCtrl(self.notebook_1_pane_1, -1, "Buenos Aires")
        self.label_te = wx.StaticText(self.notebook_1_pane_1, -1, u"Teléfono:")
        self.text_ctrl_te = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_correo = wx.StaticText(self.notebook_1_pane_1, -1, "E-Correo:")
        self.text_ctrl_correo = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_estudios = wx.StaticText(self.notebook_1_pane_1, -1, "Estudios:")
        self.combo_box_estudios = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["Primarios", "Secundarios", "Terciarios", "Universitarios"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_hasta = wx.StaticText(self.notebook_1_pane_1, -1, "Hasta:")
        self.combo_box_anio = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["Completo", "Primero", "Segundo", "Tercero", "Cuarto", "Quinto", "Sexto", u"Séptimo", "Octavo", "Noveno"],
          style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_empleo = wx.StaticText(self.notebook_1_pane_1, -1, "Empleo:")
        self.combo_box_empleo = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["No aplica", "Empleado/a", "Cuentapropista", "Ama de casa", u"Changarín/a",
          "Comerciante", "Desocupado/a sin plan", "Desocupado/a con plan"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_vacio_jf = wx.StaticText(self.notebook_1_pane_1, -1, "")
        self.checkbox_jf = wx.CheckBox(self.notebook_1_pane_1, -1, "Es jefe/a de familia?")
        self.label_responsable = wx.StaticText(self.notebook_1_pane_1, -1, "Responsable:")
        self.label_vacio_resp = wx.StaticText(self.notebook_1_pane_1, -1, "")
        self.label_resp = wx.StaticText(self.notebook_1_pane_1, -1, "Parentezco:")
        self.combo_box_responsable = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["No aplica", "Madre", "Padre", "Tutor", "Encargado", "Resp. legal"],
          style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_resp_nombre = wx.StaticText(self.notebook_1_pane_1, -1, "Nombre:")
        self.text_ctrl_resp_nombre = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_resp_ej = wx.StaticText(self.notebook_1_pane_1, -1, "")
        self.checkbox_resp_ej = wx.CheckBox(self.notebook_1_pane_1, -1, "Es jefe/a  de familia?")
        self.label_resp_nac = wx.StaticText(self.notebook_1_pane_1, -1, "Nacionalidad:")
        self.combo_box_resp_nacionalidad = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["AR", "BO", "BR", "CO", "CH", "EC", "ES", "IT", "PE", "PY", "UY", "VE"],
          style=wx.CB_DROPDOWN|wx.CB_DROPDOWN)
        self.label_resp_profesion = wx.StaticText(self.notebook_1_pane_1, -1, u"Profesión:")
        self.text_ctrl_resp_profesion = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_resp_condicion = wx.StaticText(self.notebook_1_pane_1, -1, u"Condición:")
        self.combo_box_resp_cond = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["Empleado/a", "Cuentapropista", "Ama de casa", u"Changarín/a",
          "Comerciante", "Desocupado/a sin plan", "Desocupado/a con plan"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN)
        self.label_resp_estudios = wx.StaticText(self.notebook_1_pane_1, -1, "Estudios:")
        self.combo_box_resp_estudios = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["Primarios", "Secundarios", "Terciarios", "Universitarios"],
          style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_resp_hasta_estudios = wx.StaticText(self.notebook_1_pane_1, -1, "Hasta:")
        self.combo_box_resp_anio = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["Completo", "Primero", "Segundo", "Tercero", "Cuarto", "Quinto", "Sexto",
          u"Séptimo", "Octavo", "Noveno"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_resp_tipo_doc = wx.StaticText(self.notebook_1_pane_1, -1, "Tipo doc:")
        self.combo_box_resp_tipo_doc = wx.ComboBox(self.notebook_1_pane_1, -1,
         choices=["DNI", "LC", "LE", "PAS", "ET"], style=wx.CB_DROPDOWN|wx.CB_DROPDOWN|wx.CB_READONLY)
        self.label_resp_num_doc = wx.StaticText(self.notebook_1_pane_1, -1, u"Nº doc:")
        self.text_ctrl_resp_num_doc = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_resp_domicilio = wx.StaticText(self.notebook_1_pane_1, -1, "Domicilio:")
        self.label_resp_dom_vacio = wx.StaticText(self.notebook_1_pane_1, -1, "")
        self.label_resp_dom = wx.StaticText(self.notebook_1_pane_1, -1, "Calle:")
        self.text_ctrl_resp_dom = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_esopciador = wx.StaticText(self.notebook_1_pane_1, -1, "")
        self.label_resp_numero = wx.StaticText(self.notebook_1_pane_1, -1, u"Número")
        self.text_ctrl_resp_num_dom = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_resp_piso_dom = wx.StaticText(self.notebook_1_pane_1, -1, "Piso:")
        self.text_ctrl_resp_piso_dom = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_resp_dpto_dom = wx.StaticText(self.notebook_1_pane_1, -1, "Dpto:")
        self.text_ctrl_resp_dpto_dom = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_resp_cp_dom = wx.StaticText(self.notebook_1_pane_1, -1, u"Cód postal:")
        self.text_ctrl_resp_cp_dom = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_resp_localidad_dom = wx.StaticText(self.notebook_1_pane_1, -1, "Localidad:")
        self.text_ctrl_resp_loc_dom = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_resp_te = wx.StaticText(self.notebook_1_pane_1, -1, u"Teléfono:")
        self.text_ctrl_resp_te = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.label_vacio_btn = wx.StaticText(self.notebook_1_pane_1, -1, "")
        self.button_1 = wx.Button(self.notebook_1_pane_1, wx.ID_OK, "")
        self.button_Cancelar = wx.Button(self.notebook_1_pane_1, wx.ID_CANCEL, "")
        self.label_info = wx.StaticText(self.notebook_1_pane_2, -1, u"Información de Salud:")
        self.label_infosalud_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.label_obra_social = wx.StaticText(self.notebook_1_pane_2, -1, "Obra social:")
        self.text_ctrl_obra_social = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_num_afiliado = wx.StaticText(self.notebook_1_pane_2, -1, u"Nº afiliado:")
        self.text_ctrl_num_afiliado = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_enfermedad_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "Enfermedad:")
        self.checkbox_enfermedad = wx.CheckBox(self.notebook_1_pane_2, -1, u"¿Requiere control periódico?")
        self.label_enf_cual = wx.StaticText(self.notebook_1_pane_2, -1, u"¿Cuál?:")
        self.text_ctrl_enf_cual = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_internado = wx.StaticText(self.notebook_1_pane_2, -1, u"En los últimos tres años...")
        self.checkbox_internado = wx.CheckBox(self.notebook_1_pane_2, -1, u"Internaciones:")
        self.label_int_por = wx.StaticText(self.notebook_1_pane_2, -1, u"Causa de internación:")
        self.text_ctrl_int_por = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_alergia = wx.StaticText(self.notebook_1_pane_2, -1, "Alergia:")
        self.checkbox_alergia = wx.CheckBox(self.notebook_1_pane_2, -1, u"¿Padece?")
        self.label_alergia_man = wx.StaticText(self.notebook_1_pane_2, -1, "Manifestaciones:")
        self.text_ctrl_alergia_man = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_alergia_trat = wx.StaticText(self.notebook_1_pane_2, -1, "Tratamiento")
        self.checkbox_alergia_trat = wx.CheckBox(self.notebook_1_pane_2, -1, u"¿Está en tratamiento?")
        self.label_tratamiento = wx.StaticText(self.notebook_1_pane_2, -1, u"Trat. médico:")
        self.label_trat_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.label_trat_vacio_dos = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.checkbox_tratamiento = wx.CheckBox(self.notebook_1_pane_2, -1, u"¿Recibe tratamiento?:")
        self.label_espec = wx.StaticText(self.notebook_1_pane_2, -1, "Especifique:")
        self.text_ctrl_tratamiento = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_quirurgico_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.checkbox_1 = wx.CheckBox(self.notebook_1_pane_2, -1, u"¿Quirúrgicos?:")
        self.label_quir_edad = wx.StaticText(self.notebook_1_pane_2, -1, u"¿A qué edad?:")
        self.spin_ctrl_quir_edad = wx.SpinCtrl(self.notebook_1_pane_2, -1, "25", min=1, max=90)
        self.label_quir_tipo = wx.StaticText(self.notebook_1_pane_2, -1, u"¿De qué tipo?:")
        self.text_ctrl_quir_tipo = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_1 = wx.StaticText(self.notebook_1_pane_2, -1, u"Limitación:")
        self.label_2 = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.label_limitacion_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.checkbox_limitacion = wx.CheckBox(self.notebook_1_pane_2, -1, u"¿Limitación física?:")
        self.label_limit_aclarac = wx.StaticText(self.notebook_1_pane_2, -1, u"Descripción:")
        self.text_ctrl_limitacion_aclarac = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_otros = wx.StaticText(self.notebook_1_pane_2, -1, "Observaciones:")
        self.text_ctrl_otros = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_en_caso = wx.StaticText(self.notebook_1_pane_2, -1, "En caso de ", style=wx.ALIGN_RIGHT)
        self.label_un_problema = wx.StaticText(self.notebook_1_pane_2, -1, u" algún problema en la escuela:")
        self.label_recurrir = wx.StaticText(self.notebook_1_pane_2, -1, "Recurrir a:")
        self.label_recurrir_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.label_institucion = wx.StaticText(self.notebook_1_pane_2, -1, u"Institución:")
        self.text_ctrl_institucion = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_institucion_dom = wx.StaticText(self.notebook_1_pane_2, -1, "Domicilio:")
        self.text_ctrl_institucion_dom = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_telefono = wx.StaticText(self.notebook_1_pane_2, -1, u"Teléfono:")
        self.text_ctrl_institucion_te = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_linea_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.static_line_2 = wx.StaticLine(self.notebook_1_pane_2, -1)
        self.label_medico = wx.StaticText(self.notebook_1_pane_2, -1, u"Médico:")
        self.label_medico_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.label_medico_apellidos = wx.StaticText(self.notebook_1_pane_2, -1, "Apellido:")
        self.text_ctrl_medico_apellido = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_medico_nombres = wx.StaticText(self.notebook_1_pane_2, -1, "Nombres:")
        self.text_ctrl_medico_nombres = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_medico_telefono = wx.StaticText(self.notebook_1_pane_2, -1, u"Teléfono:")
        self.text_ctrl_medico_telefono = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_linea_vacio_copy = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.static_line_2_copy = wx.StaticLine(self.notebook_1_pane_2, -1)
        self.label_familiar = wx.StaticText(self.notebook_1_pane_2, -1, "Familiar:")
        self.label_familiar_vacio = wx.StaticText(self.notebook_1_pane_2, -1, "")
        self.label_familiar_apellidos = wx.StaticText(self.notebook_1_pane_2, -1, "Apellido:")
        self.text_ctrl_familiar_apellido = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_familiar_nombres = wx.StaticText(self.notebook_1_pane_2, -1, "Nombres:")
        self.text_ctrl_familiar_nombres = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.label_familiar_telefono = wx.StaticText(self.notebook_1_pane_2, -1, u"Teléfono:")
        self.text_ctrl_familiar_telefono = wx.TextCtrl(self.notebook_1_pane_2, -1, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnResponsable, self.combo_box_responsable)
        self.Bind(wx.EVT_BUTTON, self.OnAceptar, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnCancelar, self.button_Cancelar)
        self.Bind(wx.EVT_CHECKBOX, self.OnEnfermedad, self.checkbox_enfermedad)
        self.Bind(wx.EVT_CHECKBOX, self.OnInternado, self.checkbox_internado)
        self.Bind(wx.EVT_CHECKBOX, self.OnAlergia, self.checkbox_alergia)
        self.Bind(wx.EVT_CHECKBOX, self.OnTratamiento, self.checkbox_tratamiento)
        self.Bind(wx.EVT_CHECKBOX, self.OnQuirurgico, self.checkbox_1)
        self.Bind(wx.EVT_CHECKBOX, self.OnLimitacion, self.checkbox_limitacion)
        # end wxGlade

    def __set_properties(self):
        self.SetTitle(u"Ficha de Estudiante")
        self.SetSize((800, 600))
        self.label_titulo.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD, 0, ""))
        self.text_ctrl_apellidos.SetFocus()
        self.combo_box_sexo.SetSelection(1)
        self.combo_box_tipo_doc.SetSelection(0)
        self.combo_box_nacionalidad.SetSelection(0)
        self.combo_box_estudios.SetSelection(0)
        self.combo_box_anio.SetSelection(0)
        self.combo_box_empleo.SetSelection(0)
        self.combo_box_responsable.SetSelection(0)
        self.label_resp_nombre.Enable(False)
        self.text_ctrl_resp_nombre.Enable(False)
        self.checkbox_resp_ej.Enable(False)
        self.label_resp_nac.Enable(False)
        self.combo_box_resp_nacionalidad.Enable(False)
        self.combo_box_resp_nacionalidad.SetSelection(0)
        self.label_resp_profesion.Enable(False)
        self.text_ctrl_resp_profesion.Enable(False)
        self.label_resp_condicion.Enable(False)
        self.combo_box_resp_cond.Enable(False)
        self.combo_box_resp_cond.SetSelection(0)
        self.label_resp_estudios.Enable(False)
        self.combo_box_resp_estudios.Enable(False)
        self.combo_box_resp_estudios.SetSelection(0)
        self.label_resp_hasta_estudios.Enable(False)
        self.combo_box_resp_anio.Enable(False)
        self.combo_box_resp_anio.SetSelection(0)
        self.label_resp_tipo_doc.Enable(False)
        self.combo_box_resp_tipo_doc.Enable(False)
        self.combo_box_resp_tipo_doc.SetSelection(0)
        self.label_resp_num_doc.Enable(False)
        self.text_ctrl_resp_num_doc.Enable(False)
        self.label_resp_domicilio.Enable(False)
        self.label_resp_dom_vacio.Enable(False)
        self.label_resp_dom.Enable(False)
        self.text_ctrl_resp_dom.Enable(False)
        self.label_resp_numero.Enable(False)
        self.text_ctrl_resp_num_dom.Enable(False)
        self.label_resp_piso_dom.Enable(False)
        self.text_ctrl_resp_piso_dom.Enable(False)
        self.label_resp_dpto_dom.Enable(False)
        self.text_ctrl_resp_dpto_dom.Enable(False)
        self.label_resp_cp_dom.Enable(False)
        self.text_ctrl_resp_cp_dom.Enable(False)
        self.label_resp_localidad_dom.Enable(False)
        self.text_ctrl_resp_loc_dom.Enable(False)
        self.label_resp_te.Enable(False)
        self.text_ctrl_resp_te.Enable(False)
        self.button_1.SetDefault()
        self.button_Cancelar.SetDefault()
        self.label_enf_cual.Enable(False)
        self.text_ctrl_enf_cual.Enable(False)
        self.label_int_por.Enable(False)
        self.text_ctrl_int_por.Enable(False)
        self.label_alergia_man.Enable(False)
        self.text_ctrl_alergia_man.Enable(False)
        self.label_alergia_trat.Enable(False)
        self.checkbox_alergia_trat.Enable(False)
        self.label_espec.Enable(False)
        self.text_ctrl_tratamiento.Enable(False)
        self.label_quir_edad.Enable(False)
        self.spin_ctrl_quir_edad.Enable(False)
        self.label_quir_tipo.Enable(False)
        self.text_ctrl_quir_tipo.Enable(False)
        self.label_limit_aclarac.Enable(False)
        self.text_ctrl_limitacion_aclarac.Enable(False)
        ###############
        #Habilitaciones
        ###############
        self.OnEnfermedad(self.checkbox_enfermedad)
        self.OnInternado(self.checkbox_internado)
        self.OnAlergia(self.checkbox_alergia)
        self.OnTratamiento(self.checkbox_tratamiento)
        self.OnQuirurgico(self.checkbox_1)
        self.OnLimitacion(self.checkbox_limitacion)
        ###########
        #Precarga
        c = self.db.cursor()
        c.execute('''SELECT * FROM alumnos WHERE id_alumno = ?''', (self.alumno,))
        qr = c.fetchone()
        c.close()
        q = []
        for elemento in qr:
            if elemento == None:
                q.append('')
            else:
                q.append(elemento)
        self.text_ctrl_apellidos.SetValue(u'%s' % q[1])
        self.text_ctrl_nombres.SetValue(u'%s' % q[2])
        self.combo_box_sexo.SetValue(u'%s' % q[3])
        self.combo_box_tipo_doc.SetValue(u'%s' % q[4])
        self.text_ctrl_num_doc.SetValue(u'%s' % q[5])
        self.combo_box_nacionalidad.SetValue(u'%s' % q[6])
        # rearmar la fecha porque viene diferente desde la db
        nac = q[7]
        dia = int(nac[8:10])
        mes = int(nac[5:7])
        anio = int(nac[0:4])
        nacimiento = wx.DateTimeFromDMY(dia,mes-1,anio)
        self.datepicker_fechanac.SetValue(nacimiento)
        self.text_ctrl_lugarnac.SetValue(u'%s' % q[8])
        self.text_ctrl_calle.SetValue(u'%s' % q[9])
        self.text_ctrl_numero.SetValue(u'%s' % q[10])
        self.text_ctrl_piso.SetValue(u'%s' % q[11])
        self.text_ctrl_dpto.SetValue(u'%s' % q[12])
        self.text_ctrl_cp.SetValue(u'%s' % q[13])
        self.text_ctrl_localidad.SetValue(u'%s' % q[14])
        self.text_ctrl_pcia.SetValue(u'%s' % q[15])
        self.text_ctrl_te.SetValue(u'%s' % q[16])
        self.text_ctrl_correo.SetValue(u'%s' % q[19])
        self.combo_box_estudios.SetValue(u'%s' % q[17])
        self.combo_box_anio.SetValue(u'%s' % q[18])
        self.combo_box_empleo.SetValue(u'%s' % q[39])
        if q[38] == '1':
            chequeado = True
        else:
            chequeado = False
        self.checkbox_jf.SetValue(chequeado)
        if q[40] == 0:
            respons = u'No aplica'
        elif q[40] == 1:
            respons = u'Madre'
        elif q[40] == 2:
            respons = u'Padre'
        elif q[40] == 3:
            respons = u'Tutor'
        elif q[40] == 4:
            respons = u'Encargado'
        else:
            respons = u'Resp. legal'
        self.combo_box_responsable.SetValue(u'%s' % respons)
        self.OnResponsable(self.combo_box_responsable)
        self.Bind(wx.EVT_COMBOBOX, self.OnResponsable, self.combo_box_responsable)
        self.text_ctrl_resp_nombre.SetValue(u'%s' % q[42])
        if q[41] == '1':
            chequeado = True
        else:
            chequeado = False
        self.checkbox_resp_ej.SetValue(chequeado)
        self.combo_box_resp_nacionalidad.SetValue(u'%s' % q[43])
        self.text_ctrl_resp_profesion.SetValue(u'%s' % q[44])
        self.combo_box_resp_cond.SetValue(u'%s' % q[45])
        self.combo_box_resp_estudios.SetValue(u'%s' % q[46])
        self.combo_box_resp_anio.SetValue(u'%s' % q[47])
        self.combo_box_resp_tipo_doc.SetValue(u'%s' % q[48])
        self.text_ctrl_resp_num_doc.SetValue(u'%s' % q[49])
        self.text_ctrl_resp_dom.SetValue(u'%s' % q[50])
        self.text_ctrl_resp_num_dom.SetValue(u'%s' % q[51])
        self.text_ctrl_resp_piso_dom.SetValue(u'%s' % q[52])
        self.text_ctrl_resp_dpto_dom.SetValue(u'%s' % q[53])
        self.text_ctrl_resp_cp_dom.SetValue(u'%s' % q[55])
        self.text_ctrl_resp_loc_dom.SetValue(u'%s' % q[54])
        self.text_ctrl_resp_te.SetValue(u'%s' % q[56])
        self.text_ctrl_obra_social.SetValue(u'%s' % q[57])
        self.text_ctrl_num_afiliado.SetValue(u'%s' % q[58])
        # Enfermedad
        if q[59] == '1':
            chequeado = True
            self.text_ctrl_enf_cual.Enable(True)
            self.label_enf_cual.Enable(True)
        else:
            chequeado = False
        self.checkbox_enfermedad.SetValue(chequeado)
        self.text_ctrl_enf_cual.SetValue(u'%s' % q[60])
        # Internado
        if q[61] == '1':
            chequeado = True
            self.text_ctrl_int_por.Enable(True)
            self.label_int_por.Enable(True)
        else:
            chequeado = False
        self.checkbox_internado.SetValue(chequeado)
        self.text_ctrl_int_por.SetValue(u'%s' % q[62])
        # Alergia
        if q[63] == '1':
            chequeado = True
            self.text_ctrl_alergia_man.Enable(True)
            self.checkbox_tratamiento.Enable(True)
            self.label_alergia_man.Enable(True)
            self.label_alergia_trat.Enable(True)
        else:
            chequeado = False
        self.checkbox_alergia.SetValue(chequeado)
        self.text_ctrl_alergia_man.SetValue(u'%s' % q[64])
        # Alergia tratamiento
        if q[65] == '1':
            chequeado = True
            self.text_ctrl_tratamiento.Enable(True)
            self.label_espec.Enable(True)
            self.label_alergia_trat.Enable(True)
            self.checkbox_tratamiento.Enable(True)
        else:
            chequeado = False
        self.checkbox_alergia_trat.SetValue(chequeado)
        if q[66] == '1':
            chequeado = True
            self.text_ctrl_tratamiento.Enable(True)
            self.label_espec.Enable(True)
            self.label_alergia_trat.Enable(True)
            self.checkbox_tratamiento.Enable(True)
        else:
            chequeado = False
        self.checkbox_tratamiento.SetValue(chequeado)
        self.text_ctrl_tratamiento.SetValue(u'%s' % q[67])
        # Quirúrgico
        if q[68] == '1':
            chequeado = True
            self.spin_ctrl_quir_edad.Enable(True)
            self.text_ctrl_quir_tipo.Enable(True)
            self.label_quir_edad.Enable(True)
            self.label_quir_tipo.Enable(True)
        else:
            chequeado = False
        self.checkbox_1.SetValue(chequeado)
        if q[69] == '':
            quir_edad = 0
        else:
            quir_edad = int(q[69])
        self.spin_ctrl_quir_edad.SetValue(quir_edad)
        self.text_ctrl_quir_tipo.SetValue(u'%s' % q[70])
        # Limitación
        if q[71] == '1':
            chequeado = True
            self.text_ctrl_limitacion_aclarac.Enable(True)
            self.label_limit_aclarac.Enable(True)
        else:
            chequeado = False
        self.checkbox_limitacion.SetValue(chequeado)
        self.text_ctrl_limitacion_aclarac.SetValue(u'%s' % q[72])
        self.text_ctrl_otros.SetValue(u'%s' % q[73])
        self.text_ctrl_institucion.SetValue(u'%s' % q[74])
        self.text_ctrl_institucion_dom.SetValue(u'%s' % q[75])
        self.text_ctrl_institucion_te.SetValue(u'%s' % q[76])
        self.text_ctrl_medico_apellido.SetValue(u'%s' % q[77])
        self.text_ctrl_medico_nombres.SetValue(u'%s' % q[78])
        self.text_ctrl_medico_telefono.SetValue(u'%s' % q[80])
        self.text_ctrl_familiar_apellido.SetValue(u'%s' % q[81])
        self.text_ctrl_familiar_nombres.SetValue(u'%s' % q[82])
        self.text_ctrl_familiar_telefono.SetValue(u'%s' % q[84])
        #~ ###########
        self.Show(True)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AltaEstudiante.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_6 = wx.FlexGridSizer(15, 2, 3, 3)
        grid_sizer_5 = wx.FlexGridSizer(10, 2, 3, 3)
        grid_sizer_4 = wx.FlexGridSizer(10, 2, 3, 3)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_espaciador = wx.BoxSizer(wx.VERTICAL)
        sizer_botones = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_3 = wx.FlexGridSizer(6, 2, 2, 2)
        grid_sizer_2 = wx.FlexGridSizer(17, 2, 2, 2)
        grid_sizer_1 = wx.FlexGridSizer(18, 2, 2, 2)
        sizer_1.Add(self.label_titulo, 0, wx.LEFT, 5)
        sizer_1.Add(self.static_line_1, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 8)
        grid_sizer_1.Add(self.label_apellidos, 0, wx.LEFT|wx.TOP, 3)
        grid_sizer_1.Add(self.text_ctrl_apellidos, 0, wx.LEFT|wx.TOP|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_nombres, 0, wx.ALL, 3)
        grid_sizer_1.Add(self.text_ctrl_nombres, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_sexo, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.combo_box_sexo, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_tipo_doc, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.combo_box_tipo_doc, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_num_doc, 0, wx.LEFT, 5)
        grid_sizer_1.Add(self.text_ctrl_num_doc, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_nacionalidad, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.combo_box_nacionalidad, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_fecha_nac, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.datepicker_fechanac, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_lugarnac, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_lugarnac, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_domicilio, 0, wx.LEFT|wx.TOP|wx.BOTTOM, 4)
        grid_sizer_1.Add(self.label_vacio, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_calle, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_calle, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_num, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_numero, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_piso, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_piso, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_dpto, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_dpto, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_cp, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_cp, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_localidad, 0, wx.ALL, 3)
        grid_sizer_1.Add(self.text_ctrl_localidad, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_pcia, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_pcia, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_te, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_te, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.Add(self.label_correo, 0, wx.LEFT, 3)
        grid_sizer_1.Add(self.text_ctrl_correo, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_1.AddGrowableCol(1)
        sizer_3.Add(grid_sizer_1, 1, wx.ALL|wx.EXPAND, 4)
        grid_sizer_2.Add(self.label_estudios, 0, wx.LEFT|wx.TOP, 3)
        grid_sizer_2.Add(self.combo_box_estudios, 0, wx.LEFT|wx.TOP|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_hasta, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.combo_box_anio, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_empleo, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.combo_box_empleo, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_vacio_jf, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.checkbox_jf, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_responsable, 0, wx.LEFT|wx.BOTTOM, 3)
        grid_sizer_2.Add(self.label_vacio_resp, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp, 0, wx.LEFT|wx.TOP, 5)
        grid_sizer_2.Add(self.combo_box_responsable, 0, wx.LEFT|wx.TOP|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_nombre, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.text_ctrl_resp_nombre, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_ej, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.checkbox_resp_ej, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_nac, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.combo_box_resp_nacionalidad, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_profesion, 0, wx.LEFT, 5)
        grid_sizer_2.Add(self.text_ctrl_resp_profesion, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_condicion, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.combo_box_resp_cond, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_estudios, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.combo_box_resp_estudios, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_hasta_estudios, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.combo_box_resp_anio, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_tipo_doc, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.combo_box_resp_tipo_doc, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_num_doc, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.text_ctrl_resp_num_doc, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.Add(self.label_resp_domicilio, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.label_resp_dom_vacio, 0, wx.LEFT, 5)
        grid_sizer_2.Add(self.label_resp_dom, 0, wx.LEFT, 3)
        grid_sizer_2.Add(self.text_ctrl_resp_dom, 0, wx.LEFT|wx.EXPAND, 5)
        grid_sizer_2.AddGrowableCol(1)
        sizer_3.Add(grid_sizer_2, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 4)
        sizer_espaciador.Add(self.label_esopciador, 0, wx.ALL, 3)
        grid_sizer_3.Add(self.label_resp_numero, 0, wx.LEFT, 3)
        grid_sizer_3.Add(self.text_ctrl_resp_num_dom, 0, wx.RIGHT|wx.EXPAND, 10)
        grid_sizer_3.Add(self.label_resp_piso_dom, 0, wx.LEFT, 3)
        grid_sizer_3.Add(self.text_ctrl_resp_piso_dom, 0, wx.RIGHT|wx.EXPAND, 10)
        grid_sizer_3.Add(self.label_resp_dpto_dom, 0, wx.LEFT, 3)
        grid_sizer_3.Add(self.text_ctrl_resp_dpto_dom, 0, wx.RIGHT|wx.EXPAND, 10)
        grid_sizer_3.Add(self.label_resp_cp_dom, 0, wx.LEFT, 3)
        grid_sizer_3.Add(self.text_ctrl_resp_cp_dom, 0, wx.RIGHT|wx.EXPAND, 10)
        grid_sizer_3.Add(self.label_resp_localidad_dom, 0, wx.ALL, 3)
        grid_sizer_3.Add(self.text_ctrl_resp_loc_dom, 0, wx.RIGHT|wx.EXPAND, 10)
        grid_sizer_3.Add(self.label_resp_te, 0, wx.LEFT, 3)
        grid_sizer_3.Add(self.text_ctrl_resp_te, 0, wx.RIGHT|wx.EXPAND, 10)
        grid_sizer_3.AddGrowableCol(1)
        sizer_espaciador.Add(grid_sizer_3, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 4)
        sizer_botones.Add(self.label_vacio_btn, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 10)
        sizer_botones.Add(self.button_1, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 19)
        sizer_botones.Add(self.button_Cancelar, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_espaciador.Add(sizer_botones, 1, wx.TOP|wx.EXPAND, 70)
        sizer_3.Add(sizer_espaciador, 1, wx.TOP|wx.EXPAND, 128)
        self.notebook_1_pane_1.SetSizer(sizer_3)
        grid_sizer_4.Add(self.label_info, 0, wx.TOP|wx.BOTTOM, 6)
        grid_sizer_4.Add(self.label_infosalud_vacio, 0, wx.TOP|wx.EXPAND, 6)
        grid_sizer_4.Add(self.label_obra_social, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.text_ctrl_obra_social, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_num_afiliado, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.text_ctrl_num_afiliado, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_enfermedad_vacio, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.checkbox_enfermedad, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_enf_cual, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.text_ctrl_enf_cual, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_internado, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.checkbox_internado, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_int_por, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.text_ctrl_int_por, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_alergia, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.checkbox_alergia, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_alergia_man, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.text_ctrl_alergia_man, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.Add(self.label_alergia_trat, 0, wx.ALL, 5)
        grid_sizer_4.Add(self.checkbox_alergia_trat, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_4.AddGrowableCol(1)
        sizer_2.Add(grid_sizer_4, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 10)
        grid_sizer_5.Add(self.label_tratamiento, 0, wx.TOP|wx.BOTTOM, 6)
        grid_sizer_5.Add(self.label_trat_vacio, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_5.Add(self.label_trat_vacio_dos, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.checkbox_tratamiento, 0, wx.RIGHT|wx.TOP|wx.BOTTOM, 5)
        grid_sizer_5.Add(self.label_espec, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.text_ctrl_tratamiento, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_5.Add(self.label_quirurgico_vacio, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.checkbox_1, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_5.Add(self.label_quir_edad, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.spin_ctrl_quir_edad, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_5.Add(self.label_quir_tipo, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.text_ctrl_quir_tipo, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_5.Add(self.label_1, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.label_2, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_5.Add(self.label_limitacion_vacio, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.checkbox_limitacion, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_5.Add(self.label_limit_aclarac, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.text_ctrl_limitacion_aclarac, 0, wx.ALL|wx.EXPAND, 5)
        grid_sizer_5.Add(self.label_otros, 0, wx.ALL, 5)
        grid_sizer_5.Add(self.text_ctrl_otros, 0, wx.ALL|wx.EXPAND, 5)
        sizer_2.Add(grid_sizer_5, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, 10)
        grid_sizer_6.Add(self.label_en_caso, 0, wx.TOP|wx.BOTTOM|wx.ALIGN_RIGHT, 6)
        grid_sizer_6.Add(self.label_un_problema, 0, wx.TOP|wx.BOTTOM, 6)
        grid_sizer_6.Add(self.label_recurrir, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.label_recurrir_vacio, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_institucion, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_institucion, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_institucion_dom, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_institucion_dom, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_telefono, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_institucion_te, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_linea_vacio, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 3)
        grid_sizer_6.Add(self.static_line_2, 0, wx.EXPAND, 0)
        grid_sizer_6.Add(self.label_medico, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.label_medico_vacio, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_medico_apellidos, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_medico_apellido, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_medico_nombres, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_medico_nombres, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_medico_telefono, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_medico_telefono, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_linea_vacio_copy, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 3)
        grid_sizer_6.Add(self.static_line_2_copy, 0, wx.EXPAND, 0)
        grid_sizer_6.Add(self.label_familiar, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.label_familiar_vacio, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_familiar_apellidos, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_familiar_apellido, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_familiar_nombres, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_familiar_nombres, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.Add(self.label_familiar_telefono, 0, wx.ALL, 3)
        grid_sizer_6.Add(self.text_ctrl_familiar_telefono, 0, wx.ALL|wx.EXPAND, 3)
        grid_sizer_6.AddGrowableCol(1)
        sizer_2.Add(grid_sizer_6, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_2)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Datos personales")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "Antecedentes de salud")
        sizer_1.Add(self.notebook_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def OnResponsable(self, event): # wxGlade: AltaEstudiante.<event_handler>
        responsable = self.combo_box_responsable.GetSelection()
        lista = [self.label_resp_nombre, self.text_ctrl_resp_nombre, self.checkbox_resp_ej,
         self.label_resp_nac, self.combo_box_resp_nacionalidad, self.label_resp_profesion,
          self.text_ctrl_resp_profesion, self.label_resp_condicion, self.combo_box_resp_cond,
           self.label_resp_estudios, self.combo_box_resp_estudios, self.label_resp_hasta_estudios,
            self.combo_box_resp_estudios, self.label_resp_hasta_estudios, self.combo_box_resp_anio,
             self.label_resp_tipo_doc, self.combo_box_resp_tipo_doc, self.label_resp_num_doc,
              self.text_ctrl_resp_num_doc, self.label_resp_domicilio, self.label_resp_dom,
                self.text_ctrl_resp_dom, self.label_resp_numero, self.text_ctrl_resp_num_dom,
                 self.label_resp_piso_dom, self.text_ctrl_resp_piso_dom, self.label_resp_dpto_dom,
                  self.text_ctrl_resp_dpto_dom, self.label_resp_cp_dom, self.text_ctrl_resp_cp_dom,
                   self.label_resp_localidad_dom, self.text_ctrl_resp_loc_dom, self.label_resp_te,
                    self.text_ctrl_resp_te]
        if responsable != 0:
            for item in lista:
                item.Enable(True)
        else:
            for item in lista:
                item.Enable(False)
        

    def OnAceptar(self, event): 
        wx.MessageBox(u'Estos datos no son editables', u'Listado de Estudiante', wx.OK | wx.ICON_INFORMATION, self)
        
    def OnCancelar(self, event):
        self.Close()

    def OnEnfermedad(self, event):
        enfermedad = self.checkbox_enfermedad.GetValue()
        if enfermedad == 1:
            self.text_ctrl_enf_cual.Enable(True)
            self.label_enf_cual.Enable(True)
        else:
            self.text_ctrl_enf_cual.Enable(False)
            self.label_enf_cual.Enable(False)

    def OnInternado(self, event): # wxGlade: AltaEstudiante.<event_handler>
        internado = self.checkbox_internado.GetValue()
        if internado == 1:
            self.text_ctrl_int_por.Enable(True)
            self.label_int_por.Enable(True)
        else:
            self.text_ctrl_int_por.Enable(False)
            self.label_int_por.Enable(False)

    def OnAlergia(self, event): # wxGlade: AltaEstudiante.<event_handler>
        alergia = self.checkbox_alergia.GetValue()
        if alergia == 1:
            self.text_ctrl_alergia_man.Enable(True)
            self.checkbox_alergia_trat.Enable(True)
            self.label_alergia_man.Enable(True)
            self.label_alergia_trat.Enable(True)
            
        else:
            self.text_ctrl_alergia_man.Enable(False)
            self.checkbox_alergia_trat.Enable(False)
            self.label_alergia_man.Enable(False)
            self.label_alergia_trat.Enable(False)

    def OnTratamiento(self, event): # wxGlade: AltaEstudiante.<event_handler>
        tratamiento = self.checkbox_tratamiento.GetValue()
        if tratamiento == 1:
            self.text_ctrl_tratamiento.Enable(True)
            self.label_espec.Enable(True)
        else:
            self.text_ctrl_tratamiento.Enable(False)
            self.label_espec.Enable(False)

    def OnQuirurgico(self, event): # wxGlade: AltaEstudiante.<event_handler>
        quirurgico = self.checkbox_1.GetValue()
        if quirurgico == 1:
            self.text_ctrl_alergia_man.Enable(True)
            self.spin_ctrl_quir_edad.Enable(True)
            self.label_quir_edad.Enable(True)
            self.label_quir_tipo.Enable(True)
            self.text_ctrl_quir_tipo.Enable(True)
            
        else:
            self.text_ctrl_alergia_man.Enable(False)
            self.spin_ctrl_quir_edad.Enable(False)
            self.label_quir_edad.Enable(False)
            self.label_quir_tipo.Enable(False)
            self.text_ctrl_quir_tipo.Enable(False)

    def OnLimitacion(self, event): # wxGlade: AltaEstudiante.<event_handler>
        limitacion = self.checkbox_limitacion.GetValue()
        if limitacion == 1:
            self.text_ctrl_limitacion_aclarac.Enable(True)
            self.label_limit_aclarac.Enable(True)
        else:
            self.text_ctrl_limitacion_aclarac.Enable(False)
            self.label_limit_aclarac.Enable(False)


# end of class AltaEstudiante


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_Modestudiante = ModEstudiante(None, -1, "")
    app.SetTopWindow(frame_Modestudiante)
    frame_Modestudiante.Show()
    app.MainLoop()
