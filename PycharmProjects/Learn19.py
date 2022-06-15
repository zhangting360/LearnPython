# -*- coding: utf-8
# 开发人员:zhangting
# 开始时间:2022/6/13 14:13
# 文件名称:Learn19
# 开发工具:PyCharm

'''
关于GUI 图形用户界面
'''

import wx
from tkinter import *

#使用tkinter
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

#使用wxPython
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None,title='Hello wxPython')
        frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self,parent,id,point,frameSize):
        wx.Frame.__init__(self,parent,id,title="我的Frame",size=frameSize,pos=point)

class TextFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='Text纯文本',size=(600,400))
        panel = wx.Panel(self)#创建画板
        #创建标题
        title = wx.StaticText(panel,label="标题在此",pos=(100,20))
        font = wx.Font(16,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        title.SetFont(font)
        #创建其它文本
        wx.StaticText(panel, label='无人问津也好，技不如人也罢。', pos=(50, 50))
        wx.StaticText(panel, label='你都要试着安静下来，', pos=(50, 70))
        wx.StaticText(panel, label='去做自己该做的是，', pos=(50, 90))
        wx.StaticText(panel, label='而不是让内心烦躁、焦虑，', pos=(50, 110))
        wx.StaticText(panel, label='毁掉你本就不多的热情和定力。', pos=(50, 130))
        wx.StaticText(panel, label='昨日之深渊，今日之浅谈。', pos=(50, 150))
        wx.StaticText(panel, label='路虽远，行则将至。', pos=(50, 170))
        wx.StaticText(panel, label='事虽难，做则可成。', pos=(50, 190))
        self.Centre()

class TextInputFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="Text输入",pos=(100,100),size=(400,300))
        #创建画板
        panel = wx.Panel(self)

        self.mainTitle = wx.StaticText(panel,label="输入用户名密码",pos=(140,20))

        self.userNameTitle = wx.StaticText(panel,label="用户名:",pos=(20,60))

        self.userNameTextInput = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)

        self.passwordTitle = wx.StaticText(panel, label="密 码:", pos=(20, 100))

        self.passwordTextInput = wx.TextCtrl(panel, pos=(100, 100), size=(235, 25), style=wx.TE_CENTER)

        self.buttonConfirm = wx.Button(panel,label="确定",pos=(105,150))
        self.buttonCancel = wx.Button(panel,label='取消',pos=(195,150))

        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.userNameTitle, proportion=0, flag=wx.ALL, border=5)
        hsizer_user.Add(self.userNameTextInput, proportion=0, flag=wx.ALL, border=5)

        hsizer_password = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_password.Add(self.passwordTitle,proportion=0,flag=wx.ALL,border=5)
        hsizer_password.Add(self.passwordTextInput, proportion=0, flag=wx.ALL, border=5)

        hsizer_button = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_button.Add(self.buttonConfirm,proportion=0,flag=wx.ALIGN_CENTER,border=5)
        hsizer_button.Add(self.buttonCancel, proportion=0, flag=wx.ALIGN_CENTER, border=5)

        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.mainTitle,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
        vsizer_all.Add(hsizer_user,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER,border=45)
        vsizer_all.Add(hsizer_password, proportion=0, flag=wx.EXPAND | wx.LEFT | wx.RIGHT|wx.ALIGN_CENTER, border=45)
        vsizer_all.Add(hsizer_button, proportion=0, flag=wx.ALIGN_CENTER|wx.TOP, border=15)

        panel.SetSizer(vsizer_all)

        self.buttonConfirm.Bind(wx.EVT_BUTTON,self.clickAction)

        self.Centre()

    def clickAction(self,event):
        wx.MessageBox("点击成功")


if __name__ == '__main__':
    '''tkinter'''
    # app = App()
    # app.MainLoop()
    '''wxPython Test'''
    # app = wx.App()
    # frame = MyFrame(parent=None,id=-1,point=(0,20),frameSize=(wx.DisplaySize()[0],wx.DisplaySize()[1]-300))
    # frame.Show()
    # app.MainLoop()
    '''wxPython Only Text'''
    # app = wx.App()
    # frame = TextFrame(parent=None,id=-1)
    # frame.Show()
    # app.MainLoop()
    '''wxPython TextInput'''
    app = wx.App()
    frame = TextInputFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()