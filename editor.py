#!/usr/bin/python
# -*- coding: UTF8 -*-
# archivo : editor.py
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

import wx
import wx.richtext as rt
import images

#----------------------------------------------------------------------

class RichTextFrame(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)

        self.MakeMenuBar()
        self.MakeToolBar()
        self.CreateStatusBar()
        self.SetStatusText(u'Editor de documentos Sancabase')

        self.rtc = rt.RichTextCtrl(self, style=wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER);
        wx.CallAfter(self.rtc.SetFocus)
        self.rtc.Thaw()
        
        self.AddRTCHandlers()


    def AddRTCHandlers(self):
        # make sure we haven't already added them.
        if rt.RichTextBuffer.FindHandlerByType(rt.RICHTEXT_TYPE_HTML) is not None:
            return
        
        # This would normally go in your app's OnInit method.  I'm
        # not sure why these file handlers are not loaded by
        # default by the C++ richtext code, I guess it's so you
        # can change the name or extension if you wanted...
        rt.RichTextBuffer.AddHandler(rt.RichTextHTMLHandler())
        rt.RichTextBuffer.AddHandler(rt.RichTextXMLHandler())

        # ...like this
        #rt.RichTextBuffer.AddHandler(rt.RichTextXMLHandler(name="otros XML",
        #                                                   ext="ox",
        #                                                   type=99))

        # This is needed for the view as HTML option since we tell it
        # to store the images in the memory file system.
        wx.FileSystem.AddHandler(wx.MemoryFSHandler())

    
    def OnURL(self, evt):
        wx.MessageBox(evt.GetString(), "URL")
        

    def OnFileOpen(self, evt):
        # This gives us a string suitable for the file dialog based on
        # the file handlers that are loaded
        wildcard, types = rt.RichTextBuffer.GetExtWildcard(save=False)
        dlg = wx.FileDialog(self, u'Elija un nombre para el archivo',
                            wildcard=wildcard,
                            style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if path:
                fileType = types[dlg.GetFilterIndex()]
                self.rtc.LoadFile(path, fileType)
        dlg.Destroy()

        
    def OnFileSave(self, evt):
        if not self.rtc.GetFilename():
            self.OnFileSaveAs(evt)
            return
        self.rtc.SaveFile()

        
    def OnFileSaveAs(self, evt):
        wildcard, types = rt.RichTextBuffer.GetExtWildcard(save=True)

        dlg = wx.FileDialog(self, u'Elija un nombre para el archivo',
                            wildcard=wildcard,
                            style=wx.SAVE)
        
        path = './documentos/'
        dlg.SetPath(path)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            if path:
                fileType = types[dlg.GetFilterIndex()]
                ext = rt.RichTextBuffer.FindHandlerByType(fileType).GetExtension()
                if not path.endswith(ext):
                    path += '.' + ext
                self.rtc.SaveFile(path, fileType)
        dlg.Destroy()
        
                
    def OnFileViewHTML(self, evt):
        # Get an instance of the html file handler, use it to save the
        # document to a StringIO stream, and then display the
        # resulting html text in a dialog with a HtmlWindow.
        handler = rt.RichTextHTMLHandler()
        handler.SetFlags(rt.RICHTEXT_HANDLER_SAVE_IMAGES_TO_MEMORY)
        handler.SetFontSizeMapping([7,9,11,12,14,22,100])

        import cStringIO
        stream = cStringIO.StringIO()
        if not handler.SaveStream(self.rtc.GetBuffer(), stream):
            return

        import wx.html
        dlg = wx.Dialog(self, title=U'HTML', style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
        html = wx.html.HtmlWindow(dlg, size=(500,400), style=wx.BORDER_SUNKEN)
        html.SetPage(stream.getvalue())
        btn = wx.Button(dlg, wx.ID_CANCEL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 10)
        dlg.SetSizer(sizer)
        sizer.Fit(dlg)

        dlg.ShowModal()

        handler.DeleteTemporaryImages()
        

    
    def OnFileExit(self, evt):
        self.Close(True)

      
    def OnBold(self, evt):
        self.rtc.ApplyBoldToSelection()
        
    def OnItalic(self, evt): 
        self.rtc.ApplyItalicToSelection()
        
    def OnUnderline(self, evt):
        self.rtc.ApplyUnderlineToSelection()
        
    def OnAlignLeft(self, evt):
        self.rtc.ApplyAlignmentToSelection(rt.TEXT_ALIGNMENT_LEFT)
        
    def OnAlignRight(self, evt):
        self.rtc.ApplyAlignmentToSelection(rt.TEXT_ALIGNMENT_RIGHT)
        
    def OnAlignCenter(self, evt):
        self.rtc.ApplyAlignmentToSelection(rt.TEXT_ALIGNMENT_CENTRE)
        
    def OnIndentMore(self, evt):
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_LEFT_INDENT)
        ip = self.rtc.GetInsertionPoint()
        if self.rtc.GetStyle(ip, attr):
            r = rt.RichTextRange(ip, ip)
            if self.rtc.HasSelection():
                r = self.rtc.GetSelectionRange()

            attr.SetLeftIndent(attr.GetLeftIndent() + 100)
            attr.SetFlags(rt.TEXT_ATTR_LEFT_INDENT)
            self.rtc.SetStyle(r, attr)
       
        
    def OnIndentLess(self, evt):
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_LEFT_INDENT)
        ip = self.rtc.GetInsertionPoint()
        if self.rtc.GetStyle(ip, attr):
            r = rt.RichTextRange(ip, ip)
            if self.rtc.HasSelection():
                r = self.rtc.GetSelectionRange()

        if attr.GetLeftIndent() >= 100:
            attr.SetLeftIndent(attr.GetLeftIndent() - 100)
            attr.SetFlags(rt.TEXT_ATTR_LEFT_INDENT)
            self.rtc.SetStyle(r, attr)

        
    def OnParagraphSpacingMore(self, evt):
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_PARA_SPACING_AFTER)
        ip = self.rtc.GetInsertionPoint()
        if self.rtc.GetStyle(ip, attr):
            r = rt.RichTextRange(ip, ip)
            if self.rtc.HasSelection():
                r = self.rtc.GetSelectionRange()

            attr.SetParagraphSpacingAfter(attr.GetParagraphSpacingAfter() + 20);
            attr.SetFlags(rt.TEXT_ATTR_PARA_SPACING_AFTER)
            self.rtc.SetStyle(r, attr)

        
    def OnParagraphSpacingLess(self, evt):
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_PARA_SPACING_AFTER)
        ip = self.rtc.GetInsertionPoint()
        if self.rtc.GetStyle(ip, attr):
            r = rt.RichTextRange(ip, ip)
            if self.rtc.HasSelection():
                r = self.rtc.GetSelectionRange()

            if attr.GetParagraphSpacingAfter() >= 20:
                attr.SetParagraphSpacingAfter(attr.GetParagraphSpacingAfter() - 20);
                attr.SetFlags(rt.TEXT_ATTR_PARA_SPACING_AFTER)
                self.rtc.SetStyle(r, attr)

        
    def OnLineSpacingSingle(self, evt): 
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
        ip = self.rtc.GetInsertionPoint()
        if self.rtc.GetStyle(ip, attr):
            r = rt.RichTextRange(ip, ip)
            if self.rtc.HasSelection():
                r = self.rtc.GetSelectionRange()

            attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
            attr.SetLineSpacing(10)
            self.rtc.SetStyle(r, attr)
 
                
    def OnLineSpacingHalf(self, evt):
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
        ip = self.rtc.GetInsertionPoint()
        if self.rtc.GetStyle(ip, attr):
            r = rt.RichTextRange(ip, ip)
            if self.rtc.HasSelection():
                r = self.rtc.GetSelectionRange()

            attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
            attr.SetLineSpacing(15)
            self.rtc.SetStyle(r, attr)

        
    def OnLineSpacingDouble(self, evt):
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
        ip = self.rtc.GetInsertionPoint()
        if self.rtc.GetStyle(ip, attr):
            r = rt.RichTextRange(ip, ip)
            if self.rtc.HasSelection():
                r = self.rtc.GetSelectionRange()

            attr.SetFlags(rt.TEXT_ATTR_LINE_SPACING)
            attr.SetLineSpacing(20)
            self.rtc.SetStyle(r, attr)


    def OnFont(self, evt):
        if not self.rtc.HasSelection():
            return

        r = self.rtc.GetSelectionRange()
        fontData = wx.FontData()
        fontData.EnableEffects(False)
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_FONT)
        if self.rtc.GetStyle(self.rtc.GetInsertionPoint(), attr):
            fontData.SetInitialFont(attr.GetFont())

        dlg = wx.FontDialog(self, fontData)
        if dlg.ShowModal() == wx.ID_OK:
            fontData = dlg.GetFontData()
            font = fontData.GetChosenFont()
            if font:
                attr.SetFlags(rt.TEXT_ATTR_FONT)
                attr.SetFont(font)
                self.rtc.SetStyle(r, attr)
        dlg.Destroy()


    def OnColour(self, evt):
        colourData = wx.ColourData()
        attr = rt.TextAttrEx()
        attr.SetFlags(rt.TEXT_ATTR_TEXT_COLOUR)
        if self.rtc.GetStyle(self.rtc.GetInsertionPoint(), attr):
            colourData.SetColour(attr.GetTextColour())

        dlg = wx.ColourDialog(self, colourData)
        if dlg.ShowModal() == wx.ID_OK:
            colourData = dlg.GetColourData()
            colour = colourData.GetColour()
            if colour:
                if not self.rtc.HasSelection():
                    self.rtc.BeginTextColour(colour)
                else:
                    r = self.rtc.GetSelectionRange()
                    attr.SetFlags(rt.TEXT_ATTR_TEXT_COLOUR)
                    attr.SetTextColour(colour)
                    self.rtc.SetStyle(r, attr)
        dlg.Destroy()
        


    def OnUpdateBold(self, evt):
        evt.Check(self.rtc.IsSelectionBold())
    
    def OnUpdateItalic(self, evt): 
        evt.Check(self.rtc.IsSelectionItalics())
    
    def OnUpdateUnderline(self, evt): 
        evt.Check(self.rtc.IsSelectionUnderlined())
    
    def OnUpdateAlignLeft(self, evt):
        evt.Check(self.rtc.IsSelectionAligned(rt.TEXT_ALIGNMENT_LEFT))
        
    def OnUpdateAlignCenter(self, evt):
        evt.Check(self.rtc.IsSelectionAligned(rt.TEXT_ALIGNMENT_CENTRE))
        
    def OnUpdateAlignRight(self, evt):
        evt.Check(self.rtc.IsSelectionAligned(rt.TEXT_ALIGNMENT_RIGHT))

    
    def ForwardEvent(self, evt):
        # The RichTextCtrl can handle menu and update events for undo,
        # redo, cut, copy, paste, delete, and select all, so just
        # forward the event to it.
        self.rtc.ProcessEvent(evt)


    def MakeMenuBar(self):
        def doBind(item, handler, updateUI=None):
            self.Bind(wx.EVT_MENU, handler, item)
            if updateUI is not None:
                self.Bind(wx.EVT_UPDATE_UI, updateUI, item)
            
        fileMenu = wx.Menu()
        doBind( fileMenu.Append(-1, u'&Abrir\tCtrl+A', u'Abrir un archivo'),
                self.OnFileOpen )
        doBind( fileMenu.Append(-1, u'&Guardar\tCtrl+G', u'Guardar un archivo'),
                self.OnFileSave )
        doBind( fileMenu.Append(-1, u'G&uardar como...\tF12', u'Guardar en un nuevo archivo'),
                self.OnFileSaveAs )
        fileMenu.AppendSeparator()
        doBind( fileMenu.Append(-1, u'&Ver como HTML', u'Vista HTML'),
                self.OnFileViewHTML)
        fileMenu.AppendSeparator()
        doBind( fileMenu.Append(-1, u'Sali&r\tCtrl+Q', u'Salir del editor'),
                self.OnFileExit )
        
        editMenu = wx.Menu()
        doBind( editMenu.Append(wx.ID_UNDO, u'&Deshacer\tCtrl+Z'),
                self.ForwardEvent, self.ForwardEvent)
        doBind( editMenu.Append(wx.ID_REDO, u'&Rehacer\tCtrl+Y'),
                self.ForwardEvent, self.ForwardEvent )
        editMenu.AppendSeparator()
        doBind( editMenu.Append(wx.ID_CUT, u'Cor&tar\tCtrl+X'),
                self.ForwardEvent, self.ForwardEvent )
        doBind( editMenu.Append(wx.ID_COPY, u'&Copiar\tCtrl+C'),
                self.ForwardEvent, self.ForwardEvent)
        doBind( editMenu.Append(wx.ID_PASTE, u'&Pegar\tCtrl+V'),
                self.ForwardEvent, self.ForwardEvent)
        doBind( editMenu.Append(wx.ID_CLEAR, u'&Borrar\tDel'),
                self.ForwardEvent, self.ForwardEvent)
        editMenu.AppendSeparator()
        doBind( editMenu.Append(wx.ID_SELECTALL, u'S&eleccionar todo\tCtrl+A'),
                self.ForwardEvent, self.ForwardEvent )
        
        #doBind( editMenu.AppendSeparator(),  )
        #doBind( editMenu.Append(-1, "&Find...\tCtrl+F"),  )
        #doBind( editMenu.Append(-1, "&Replace...\tCtrl+R"),  )

        formatMenu = wx.Menu()
        doBind( formatMenu.AppendCheckItem(-1, u'&Negrita\tCtrl+B'),
                self.OnBold, self.OnUpdateBold)
        doBind( formatMenu.AppendCheckItem(-1, u'C&ursiva\tCtrl+I'),
                self.OnItalic, self.OnUpdateItalic)
        doBind( formatMenu.AppendCheckItem(-1, u'S&ubrayado\tCtrl+U'),
                self.OnUnderline, self.OnUpdateUnderline)
        formatMenu.AppendSeparator()
        doBind( formatMenu.AppendCheckItem(-1, u'Al&ineación izq.'),
                self.OnAlignLeft, self.OnUpdateAlignLeft)
        doBind( formatMenu.AppendCheckItem(-1, u'&Centrado'),
                self.OnAlignCenter, self.OnUpdateAlignCenter)
        doBind( formatMenu.AppendCheckItem(-1, u'Alineación &der.'),
                self.OnAlignRight, self.OnUpdateAlignRight)
        formatMenu.AppendSeparator()
        doBind( formatMenu.Append(-1, u'Indentar &Más'), self.OnIndentMore)
        doBind( formatMenu.Append(-1, u'Indentar Me&nos'), self.OnIndentLess)
        formatMenu.AppendSeparator()
        doBind( formatMenu.Append(-1, u'Aumentar es&paciado'), self.OnParagraphSpacingMore)
        doBind( formatMenu.Append(-1, u'Disminuir espaciad&o'), self.OnParagraphSpacingLess)
        formatMenu.AppendSeparator()
        doBind( formatMenu.Append(-1, u'Espaciado normal'), self.OnLineSpacingSingle)
        doBind( formatMenu.Append(-1, u'Espaciado 1.5'), self.OnLineSpacingHalf)
        doBind( formatMenu.Append(-1, u'Espaciado doble'), self.OnLineSpacingDouble)
        formatMenu.AppendSeparator()
        doBind( formatMenu.Append(-1, u'&Fuente...'), self.OnFont)
        
        mb = wx.MenuBar()
        mb.Append(fileMenu, u'&Archivo')
        mb.Append(editMenu, u'&Edición')
        mb.Append(formatMenu, u'F&ormato')
        self.SetMenuBar(mb)


    def MakeToolBar(self):
        def doBind(item, handler, updateUI=None):
            self.Bind(wx.EVT_TOOL, handler, item)
            if updateUI is not None:
                self.Bind(wx.EVT_UPDATE_UI, updateUI, item)
        
        tbar = self.CreateToolBar()
        doBind( tbar.AddTool(-1, images.get_rt_openBitmap(),
                            shortHelpString=u'Abrir'), self.OnFileOpen)
        doBind( tbar.AddTool(-1, images.get_rt_saveBitmap(),
                            shortHelpString=u'Guardar'), self.OnFileSave)
        tbar.AddSeparator()
        doBind( tbar.AddTool(wx.ID_CUT, images.get_rt_cutBitmap(),
                            shortHelpString=u'Cortar'), self.ForwardEvent, self.ForwardEvent)
        doBind( tbar.AddTool(wx.ID_COPY, images.get_rt_copyBitmap(),
                            shortHelpString=u'Copiar'), self.ForwardEvent, self.ForwardEvent)
        doBind( tbar.AddTool(wx.ID_PASTE, images.get_rt_pasteBitmap(),
                            shortHelpString=u'Pegar'), self.ForwardEvent, self.ForwardEvent)
        tbar.AddSeparator()
        doBind( tbar.AddTool(wx.ID_UNDO, images.get_rt_undoBitmap(),
                            shortHelpString=u'Deshacer'), self.ForwardEvent, self.ForwardEvent)
        doBind( tbar.AddTool(wx.ID_REDO, images.get_rt_redoBitmap(),
                            shortHelpString=u'Rehacer'), self.ForwardEvent, self.ForwardEvent)
        tbar.AddSeparator()
        doBind( tbar.AddTool(-1, images.get_rt_boldBitmap(), isToggle=True,
                            shortHelpString=u'Negrita'), self.OnBold, self.OnUpdateBold)
        doBind( tbar.AddTool(-1, images.get_rt_italicBitmap(), isToggle=True,
                            shortHelpString=u'Cursiva'), self.OnItalic, self.OnUpdateItalic)
        doBind( tbar.AddTool(-1, images.get_rt_underlineBitmap(), isToggle=True,
                            shortHelpString=u'Subrayado'), self.OnUnderline, self.OnUpdateUnderline)
        tbar.AddSeparator()
        doBind( tbar.AddTool(-1, images.get_rt_alignleftBitmap(), isToggle=True,
                            shortHelpString=u'Alineación izquierda'), self.OnAlignLeft, self.OnUpdateAlignLeft)
        doBind( tbar.AddTool(-1, images.get_rt_centreBitmap(), isToggle=True,
                            shortHelpString=u'Centrado'), self.OnAlignCenter, self.OnUpdateAlignCenter)
        doBind( tbar.AddTool(-1, images.get_rt_alignrightBitmap(), isToggle=True,
                            shortHelpString=u'Alineación derecha'), self.OnAlignRight, self.OnUpdateAlignRight)
        tbar.AddSeparator()
        doBind( tbar.AddTool(-1, images.get_rt_indentlessBitmap(),
                            shortHelpString=u'Indentar más'), self.OnIndentLess)
        doBind( tbar.AddTool(-1, images.get_rt_indentmoreBitmap(),
                            shortHelpString=u'Indentar menos'), self.OnIndentMore)
        tbar.AddSeparator()
        doBind( tbar.AddTool(-1, images.get_rt_fontBitmap(),
                            shortHelpString=u'Fuente'), self.OnFont)
        doBind( tbar.AddTool(-1, images.get_rt_colourBitmap(),
                            shortHelpString=u'Color de fuente'), self.OnColour)

        tbar.Realize()

       
