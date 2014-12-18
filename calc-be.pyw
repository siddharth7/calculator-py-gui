import sys
from calcwithbtn import *
a=''
b=''
d=''
class MyForm(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui=Ui_Dialog()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.b1,QtCore.SIGNAL('clicked()'),self.e1)
		QtCore.QObject.connect(self.ui.b2,QtCore.SIGNAL('clicked()'),self.e2)
		QtCore.QObject.connect(self.ui.b3,QtCore.SIGNAL('clicked()'),self.e3)
		QtCore.QObject.connect(self.ui.b4,QtCore.SIGNAL('clicked()'),self.e4)
		QtCore.QObject.connect(self.ui.b5,QtCore.SIGNAL('clicked()'),self.e5)
		QtCore.QObject.connect(self.ui.b6,QtCore.SIGNAL('clicked()'),self.e6)
		QtCore.QObject.connect(self.ui.b7,QtCore.SIGNAL('clicked()'),self.e7)
		QtCore.QObject.connect(self.ui.b8,QtCore.SIGNAL('clicked()'),self.e8)
		QtCore.QObject.connect(self.ui.b9,QtCore.SIGNAL('clicked()'),self.e9)
		QtCore.QObject.connect(self.ui.b0,QtCore.SIGNAL('clicked()'),self.e0)
		QtCore.QObject.connect(self.ui.add,QtCore.SIGNAL('clicked()'),self.ad)
		QtCore.QObject.connect(self.ui.sub,QtCore.SIGNAL('clicked()'),self.su)
		QtCore.QObject.connect(self.ui.mul,QtCore.SIGNAL('clicked()'),self.mu)
		QtCore.QObject.connect(self.ui.div,QtCore.SIGNAL('clicked()'),self.di)
		QtCore.QObject.connect(self.ui.calc,QtCore.SIGNAL('clicked()'),self.cal)
	def e1(self):
		global a
		a=a+'1'
		self.ui.num.setText(a)
	def e2(self):
		global a
		a=a+'2'
		self.ui.num.setText(a)
	def e3(self):
		global a
		a=a+'3'
		self.ui.num.setText(a)
	def e4(self):
		global a
		a=a+'4'
		self.ui.num.setText(a)
	def e5(self):
		global a
		a=a+'5'
		self.ui.num.setText(a)
	def e6(self):
		global a
		a=a+'6'
		self.ui.num.setText(a)
	def e7(self):
		global a
		a=a+'7'
		self.ui.num.setText(a)
	def e8(self):
		global a
		a=a+'8'
		self.ui.num.setText(a)
	def e9(self):
		global a
		a=a+'9'
		self.ui.num.setText(a)
	def e0(self):
		global a
		a=a+'0'
		self.ui.num.setText(a)
	def ad(self):
		global b
		global a
		global d
		self.ui.num.setText('\n+\n')
		d=d+'+'
		b=a
		a=''


	def su(self):
		global b
		global a
		global d
		self.ui.num.setText('\n-\n')
		d=d+'-'
		b=a
		a=''

		
	def mu(self):
		global b
		global a
		global d
		self.ui.num.setText('\nx\n')
		d=d+'x'
		b=a
		a=''
		
	def di(self):
		global b
		global a
		global d
		self.ui.num.setText('\n/\n')
		d=d+'/'
		b=a
		a=''
		

	def cal(self):
		global a
		global b
		global d
		self.ui.num.clear()
		self.ui.num.clear()
		if(d=='+'):
			c=int(a)+int(b)
			self.ui.num.setText(str(c))
			c=''
			b=''
			a=''
			d=''
		if(d=='-'):
			c=int(b)-int(a)
			self.ui.num.setText(str(c))
			c=''
			b=''
			a=''
			d=''
		if(d=='x'):
			c=int(a)*int(b)
			self.ui.num.setText(str(c))
			c=''
			b=''
			a=''
			d=''
		if(d=='/'):
			c=float(b)/float(a)
			self.ui.num.setText(str(c))
			c=''
			b=''
			a=''
			d=''


if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    ex=MyForm()
    ex.show()
    sys.exit(app.exec_())
