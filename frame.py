# -*- coding: utf-8 -*-
__author__ = 'ShengYue'
import wx
from lxml import etree
from index import main


class DemoFrame(wx.Frame):
    def __init__(self):
        self.cateList = []
        wx.Frame.__init__(self, None, -1, u"load goods",size=(400,200))


        self.draw()

    def draw(self):
        self.panel = wx.Panel(self, -1)
        wx.StaticText(self.panel, -1, u"输入网址:", (15, 15))
        wx.StaticText(self.panel, -1, u"选择分类:", (15, 50))
        sampleList = self.getCate()
        self.getCateList(sampleList)

        self.cate = wx.ComboBox(self.panel, -1, self.cateList[0], (80, 50), wx.DefaultSize, self.cateList)

        self.text = wx.TextCtrl(self.panel,-1,value='',pos=(80,15),size=(300,24))

        self.button = wx.Button(self.panel, -1, u"抓取", pos=(15, 90))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

    def OnClick(self, event):
        self.button.SetLabel(u'抓取中...')
        self.button.Enable(False)

        index = main()
        bool = index.init(self.text.GetValue(),self.cate.GetValue())
        if bool:
            self.button.SetLabel(u'抓取')
            self.button.Enable(True)

    def getCateList(self, cate):
        for s in cate:
            if type(s) == type([]):
                self.getCateList(s)
            else:
                self.cateList.append(s)


    def getCate(self, xpath=None, p=''):
        ret=[]
        if xpath == None:
            xtree = etree.parse(open('cate.xml'))
            cates = xtree.xpath('/root/cate')
            for cate in cates:
                row = cate.getchildren()
                if row :
                    ret.append(p+cate.get('name'))
                    ret.append(self.getCate(row, (p+cate.get('name')+'->')))
                else:
                    ret.append(p+cate.get('name'))
        else:
            for cate in xpath:
                row = cate.getchildren()
                if row:
                    ret.append(p+cate.get('name'))
                    ret.append(self.getCate(row,(p+cate.get('name')+'->')))
                else:
                    ret.append(p+cate.get('name'))
        return ret






app = wx.PySimpleApp()
frame = DemoFrame()
frame.Show()
app.MainLoop()
