import sys
from calcwithbtn import *
from pythonds.basic.stack import Stack

a=''
b=''
c=''
def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token not in "+-/*":
            operandStack.push(float(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token not in "+-/*":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
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
		QtCore.QObject.connect(self.ui.bclear,QtCore.SIGNAL('clicked()'),self.cl)
		QtCore.QObject.connect(self.ui.dotbtn,QtCore.SIGNAL('clicked()'),self.dt)
		QtCore.QObject.connect(self.ui.bspace,QtCore.SIGNAL('clicked()'),self.bs)
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
	def bs(self):
		global a
		a=a[:-1]
		self.ui.num.setText(a)
	def dt(self):
		global a
		a=a+'.'
		self.ui.num.setText(a)
	def cl(self):
		global a
		a=''
		self.ui.num.clear()
	def ad(self):
		global a
		a=a+' '
		a=a+'+'
		a=a+' '
		self.ui.num.setText(a)
	def su(self):
		global a
		a=a+' '
		a=a+'-'
		a=a+' '
		self.ui.num.setText(a)
	def mu(self):
		global a
		a=a+' '
		a=a+'*'
		a=a+' '
		self.ui.num.setText(a)
	def di(self):
		global a
		a=a+' '
		a=a+'/'
		a=a+' ' 
		self.ui.num.setText(a)
	def cal(self):
		global a
		global b
		global c
		b=infixToPostfix(a)
		c=postfixEval(b)
		a=str(c)
		self.ui.num.setText(a)
		b=''
		c=''
if __name__=='__main__':
    app=QtGui.QApplication(sys.argv)
    ex=MyForm()
    ex.show()
    sys.exit(app.exec_())
