from Tkinter import *
import tkFileDialog
import tkMessageBox
import tkFont


letter = []

unname = ['none']
untypea = ['none']
unwidth = ['none']
uncolor = ['none']
unposx = ['none']
unposy = ['none']
unposx1 = ['none']
unposy1 = ['none']
unpic = ['none']

rename = ['none']
retypea = ['none']
rewidth = ['none']
recolor = ['none']
reposx = ['none']
reposy = ['none']
reposx1 = ['none']
reposy1 = ['none']
repic = ['none']


### THICKNESS ###

def minus(event):
	global wid,Label1
	if wid > 0:
		wid -= 1
		if wid == 0:
			wid = 1

	else:
		print 'min'
		wid = 1

	Label1.destroy()
	Label1 = Label(root, text = 'Thickness : %s'%wid)
	Label1.grid(row=2,column=0)

def plus(event):
	global wid,Label1,butplus,butminus
	if wid < 100:
		wid += 1

	else:
		print 'max'

	Label1.destroy()
	Label1 = Label(root, text = 'Thickness : %s'%wid)
	Label1.grid(row=2,column=0)

### THICKNESS ###

def Open():
	global test,picture
	filename = tkFileDialog.askopenfilename()

	picture = PhotoImage(file=filename)
	gifdict[filename] = picture

	rep = tkMessageBox.askyesno(picture,'Do you want to adjust the canvas with the picture ?')

	if rep == True:
		Canevas.create_image(0,0,anchor=NW,image=picture)
		Canevas.config(height=picture.height(),width=picture.width())

	else:
		test = 'picture'
		tkMessageBox.showinfo('test','Press the left button to place the center of the picture')
		root.config(cursor='tcross')


### TOOLS #######

def pencil():
	global test
	test = 'pencil'
	root.config(cursor='pencil')

def rubber():
	global test
	test = 'rubber'
	root.config(cursor='dotbox')

def line():
	global test
	test = 'line'
	root.config(cursor='tcross')

def filled_rectangle():
	global test
	test = 'filled_rectangle'
	root.config(cursor='tcross')

def filled_oval():
	global test
	test = 'filled_oval'
	root.config(cursor='circle')

def filled_circle():
	global test
	test = 'filled_circle'
	root.config(cursor='circle')

def rectangle():
	global test
	test = 'rectangle'
	root.config(cursor='tcross')

def oval():
	global test
	test = 'oval'
	root.config(cursor='circle')

def circle():
	global test
	test = 'circle'
	root.config(cursor='circle')

def arrow():
	global test
	test = 'arrow'
	root.config(cursor='arrow')

def text():
	global test
	test = 'text'
	root.config(cursor='xterm')

### TOOLS #######

def undo1(event):
	key = event.keysym
	undo()

def undo():
	global test1
	do = 2
	if len(untypea) == 0:
		print 'error'

	elif untypea[len(untypea)-1] == 'none':

		rename.append(unname[len(unname)-1])
		unname.pop()

		retypea.append(untypea[len(untypea)-1])
		untypea.pop()

		rewidth.append(unwidth[len(unwidth)-1])
		unwidth.pop()

		recolor.append(uncolor[len(uncolor)-1])
		uncolor.pop()

		reposx.append(unposx[len(unposx)-1])
		unposx.pop()

		reposy.append(unposy[len(unposy)-1])
		unposy.pop()

		reposx1.append(unposx1[len(unposx1)-1])
		unposx1.pop()

		reposy1.append(unposy1[len(unposy1)-1])
		unposy1.pop()

		root.after(1,undo)

	elif untypea[len(untypea)-1] == 'pencil' or untypea[len(untypea)-1] == 'rubber' or untypea[len(untypea)-1] == 'link_pencil' or untypea[len(untypea)-1] == 'link_gomme':

		Canevas.delete(unname[len(unname)-1])

		rename.append(unname[len(unname)-1])
		unname.pop()

		retypea.append(untypea[len(untypea)-1])
		untypea.pop()

		rewidth.append(unwidth[len(unwidth)-1])
		unwidth.pop()

		recolor.append(uncolor[len(uncolor)-1])
		uncolor.pop()

		reposx.append(unposx[len(unposx)-1])
		unposx.pop()

		reposy.append(unposy[len(unposy)-1])
		unposy.pop()

		reposx1.append(unposx1[len(unposx1)-1])
		unposx1.pop()

		reposy1.append(unposy1[len(unposy1)-1])
		unposy1.pop()


		if len(untypea) == 1 or len(untypea) != 'pencil' or len(untypea) != 'rubber' or len(untypea) != 'link_pencil' or len(untypea) == 'link_gomme':
			do = 1

		if len(untypea) != 0 and (untypea[len(untypea)-do] == 'pencil' or untypea[len(untypea)-do] == 'rubber' or untypea[len(untypea)-do] == 'link_pencil' or untypea[len(untypea)-do] == 'link_rubber'):
			root.after(1,undo)


	elif untypea[len(untypea)-1] == 'line' or untypea[len(untypea)-1] == 'filled_rectangle' or untypea[len(untypea)-1] == 'rectangle' or untypea[len(untypea)-1] == 'filled_oval' or untypea[len(untypea)-1] == 'oval' or untypea[len(untypea)-1] == 'filled_circle' or untypea[len(untypea)-1] == 'circle':

		Canevas.delete(unname[len(unname)-1])

		rename.append(unname[len(unname)-1])
		unname.pop()

		retypea.append(untypea[len(untypea)-1])
		untypea.pop()

		rewidth.append(unwidth[len(unwidth)-1])
		unwidth.pop()

		recolor.append(uncolor[len(uncolor)-1])
		uncolor.pop()

		reposx.append(unposx[len(unposx)-1])
		unposx.pop()

		reposy.append(unposy[len(unposy)-1])
		unposy.pop()

		reposx1.append(unposx1[len(unposx1)-1])
		unposx1.pop()

		reposy1.append(unposy1[len(unposy1)-1])
		unposy1.pop()

	'''elif untypea[len(untypea)-1] == 'picture':

		Canevas.delete(unname[len(unname)-1])

		rename.append(unname[len(unname)-1])
		unname.pop()

		retypea.append(untypea[len(untypea)-1])
		untypea.pop()

		reposx.append(unposx[len(unposx)-1])
		unposx.pop()

		reposy.append(unposy[len(unposy)-1])
		unposy.pop()

		repic.append(unpic[len(unpic)-1])
		unpic.pop()'''


def redo1(event):
	key = event.keysym
	redo()

def redo():
	global test1
	do = 2
	if len(retypea) == 0:
		print 'error'

	elif retypea[len(retypea)-1] == 'none':
		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()

		root.after(1,redo)

	elif retypea[len(retypea)-1] == 'pencil':

		rename[len(rename)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=rewidth[len(rewidth)-1],outline=recolor[len(recolor)-1],fill=recolor[len(recolor)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()


		if len(retypea) == 1:
			do = 1
			test1 += 1

		if len(retypea) != 0 and retypea[len(retypea)-do] == 'pencil':
			root.after(1,redo)

	elif retypea[len(retypea)-1] == 'link_pencil':

		rename[len(rename)-1] = Canevas.create_line(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=rewidth[len(rewidth)-1],fill=recolor[len(recolor)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()


		if len(retypea) == 1:
			do = 1
			test1 += 1

		if len(retypea) != 0 and retypea[len(retypea)-do] == 'link_pencil':
			root.after(1,redo)


	elif retypea[len(retypea)-1] == 'rubber':

		rename[len(rename)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=rewidth[len(rewidth)-1],outline='white',fill='white')

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()


		if len(retypea) == 1:
			do = 1

		if len(retypea) != 0 and retypea[len(retypea)-do] == 'rubber':
			root.after(1,redo)

	elif retypea[len(retypea)-1] == 'link_gomme':

		rename[len(rename)-1] = Canevas.create_line(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=rewidth[len(rewidth)-1],fill=recolor[len(recolor)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()


		if len(retypea) == 1:
			do = 1
			test1 += 1

		if len(retypea) != 0 and retypea[len(retypea)-do] == 'link_gomme':
			root.after(1,redo)

	elif retypea[len(retypea)-1] == 'line':

		rename[len(rename)-1] = Canevas.create_line(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=rewidth[len(rewidth)-1],fill=recolor[len(recolor)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()


	elif retypea[len(retypea)-1] == 'filled_rectangle':

		rename[len(rename)-1] = Canevas.create_rectangle(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],outline=recolor[len(recolor)-1],fill=recolor[len(recolor)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()


	elif retypea[len(retypea)-1] == 'rectangle':

		rename[len(rename)-1] = Canevas.create_rectangle(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],outline=recolor[len(recolor)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()


	elif retypea[len(retypea)-1] == 'filled_oval' or retypea[len(retypea)-1] == 'filled_circle':

		rename[len(rename)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],outline=recolor[len(recolor)-1],fill=recolor[len(recolor)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()


	elif retypea[len(retypea)-1] == 'oval' or retypea[len(retypea)-1] == 'circle':

		rename[len(rename)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],outline=recolor[len(recolor)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unwidth.append(rewidth[len(rewidth)-1])
		rewidth.pop()

		uncolor.append(recolor[len(recolor)-1])
		recolor.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unposx1.append(reposx1[len(reposx1)-1])
		reposx1.pop()

		unposy1.append(reposy1[len(reposy1)-1])
		reposy1.pop()

	'''elif retypea[len(retypea)-1] == 'picture':

		rename[len(rename)-1] = Canevas.create_image(reposx[len(reposx)-1],reposy[len(reposy)-1],anchor=CENTER,image=unpic[len(unpic)-1])

		unname.append(rename[len(rename)-1])
		rename.pop()

		untypea.append(retypea[len(retypea)-1])
		retypea.pop()

		unposx.append(reposx[len(reposx)-1])
		reposx.pop()

		unposy.append(reposy[len(reposy)-1])
		reposy.pop()

		unpic.append(unpic[len(unpic)-1])
		repic.pop()'''


def L_Clic(event):
	global X,Y,n,m,X1,Y1,X2,Y2,picture
	X = event.x
	Y = event.y
	X1 = X
	Y1 = Y
	X2 = X
	Y2 = Y
	n += 1
	m = str(n)
	if test != 'arrow':
		unname.append('none')
		untypea.append('none')
		unwidth.append('none')
		uncolor.append('none')
		unposx.append('none')
		unposy.append('none')
		unposx1.append('none')
		unposy1.append('none')
		unpic.append('none')

	if test == 'texte':
		string = ''
		size = tkFont.Font(size=wid)
		m = Canevas.create_text(X,Y,anchor=NW,text=string,width=wid,font=size)

	elif test == 'picture':
		m = Canevas.create_image(X1,Y1,anchor=CENTER,image=picture)



def Drag(event):
	global X,Y,test,line,n,m,coul,X1,Y1,resx,resx,resy,resx1,resy1,X2,Y2
	X1 = event.x
	Y1 = event.y

	if test == 'pencil':
		m = Canevas.create_oval(X1,Y1,X1,Y1,width=wid-1,outline=coul,fill=coul)

	elif test == 'rubber':
		m = Canevas.create_oval(X1,Y1,X1,Y1,width=wid-1,outline='white',fill='white')

	elif test == 'line':
		Canevas.delete(m)
		m = Canevas.create_line(X,Y,X1,Y1,width=wid,fill=coul)

	elif test == 'filled_rectangle':
		Canevas.delete(m)
		m = Canevas.create_rectangle(X,Y,X1,Y1,outline=coul,fill=coul)

	elif test == 'filled_oval':
		Canevas.delete(m)
		resx = X-X1
		resy = Y-Y1
		m = Canevas.create_oval(X+resx,Y+resy,X-resx,Y-resy,outline=coul,fill=coul)

	elif test == 'rectangle':
		Canevas.delete(m)
		m = Canevas.create_rectangle(X,Y,X1,Y1,width=wid,outline=coul)

	elif test == 'oval':
		Canevas.delete(m)
		resx = X-X1
		resy = Y-Y1
		m = Canevas.create_oval(X+resx,Y+resy,X-resx,Y-resy,width=wid,outline=coul)

	elif test == 'circle':
		Canevas.delete(m)
		resx = X-X1
		resy = Y-Y1

		if resx<=0 and resy<=0:
			if resx <= resy:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resx,Y+resx,X-resx,Y-resx,width=wid,outline=coul)

			elif resx > resy:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resy,Y+resy,X-resy,Y-resy,width=wid,outline=coul)

		elif resx>=0 and resy>=0:
			if resx >= resy:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resx,Y+resx,X-resx,Y-resx,width=wid,outline=coul)

			elif resx < resy:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resy,Y+resy,X-resy,Y-resy,width=wid,outline=coul)

		elif resx>=0 and resy<=0:
			resy1 = -resy
			if resx >= resy1:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resx,Y-resx,X-resx,Y+resx,width=wid,outline=coul)

			elif resx < resy1:
				Canevas.delete(m)
				m = Canevas.create_oval(X-resy,Y+resy,X+resy,Y-resy,width=wid,outline=coul)

		elif resx<=0 and resy>=0:
			resx1 = -resx
			if resy >= resx1:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resy,Y-resy,X-resy,Y+resy,width=wid,outline=coul)

			elif resy < resx1:
				Canevas.delete(m)
				m = Canevas.create_oval(X-resx,Y+resx,X+resx,Y-resx,width=wid,outline=coul)

	elif test == 'filled_circle':
		Canevas.delete(m)
		resx = X-X1
		resy = Y-Y1

		if resx<=0 and resy<=0:
			if resx <= resy:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resx,Y+resx,X-resx,Y-resx,outline=coul,fill=coul)

			elif resx > resy:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resy,Y+resy,X-resy,Y-resy,outline=coul,fill=coul)

		elif resx>=0 and resy>=0:
			if resx >= resy:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resx,Y+resx,X-resx,Y-resx,outline=coul,fill=coul)

			elif resx < resy:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resy,Y+resy,X-resy,Y-resy,outline=coul,fill=coul)

		elif resx>=0 and resy<=0:
			resy1 = -resy
			if resx >= resy1:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resx,Y-resx,X-resx,Y+resx,outline=coul,fill=coul)

			elif resx < resy1:
				Canevas.delete(m)
				m = Canevas.create_oval(X-resy,Y+resy,X+resy,Y-resy,outline=coul,fill=coul)

		elif resx<=0 and resy>=0:
			resx1 = -resx
			if resy >= resx1:
				Canevas.delete(m)
				m = Canevas.create_oval(X+resy,Y-resy,X-resy,Y+resy,outline=coul,fill=coul)

			elif resy < resx1:
				Canevas.delete(m)
				m = Canevas.create_oval(X-resx,Y+resx,X+resx,Y-resx,outline=coul,fill=coul)

	elif test == 'arrow':
		W1 = X1
		H = Y1
		if W1 <= 80:
			W1 = 80
		if H <= 80:
			H = 80
		Canevas.config(width = W1, height =H)
		if W1>580:
			Canevas.grid(row=0,column=0, columnspan=2,sticky=NW)

		else:
			Canevas.grid(row=0,column=0,sticky=NW)

	elif test == 'text':
		Canevas.delete(m)
		m = Canevas.create_rectangle(X,Y,X1,Y1,width=1,outline='black')

	elif test == 'picture':
		Canevas.delete(m)
		m = Canevas.create_image(X1,Y1,anchor=CENTER,image=picture)

	if len(unname)>1000000:
		unname.pop(0)
		untypea.pop(0)
		unwidth.pop(0)
		uncolor.pop(0)
		unposx.pop(0)
		unposy.pop(0)
		unposx1.pop(0)
		unposy1.pop(0)


	if test == 'pencil' or test == 'rubber':
		unname.append(str(m))
		untypea.append(test)
		unwidth.append(wid)
		uncolor.append(coul)
		unposx.append(X1)
		unposy.append(Y1)
		unposx1.append(X1)
		unposy1.append(Y1)

		if test == 'pencil':
			n += 1
			m = str(n)
			m = Canevas.create_line(X1,Y1,X2,Y2,width=wid,fill=coul)
			unname.append(str(m))
			untypea.append('link_pencil')
			unwidth.append(wid)
			uncolor.append(coul)
			unposx.append(X1)
			unposy.append(Y1)
			unposx1.append(X2)
			unposy1.append(Y2)
			X2=X1
			Y2=Y1

		elif test == 'rubber':
			n += 1
			m = str(n)
			m = Canevas.create_line(X1,Y1,X2,Y2,width=wid,fill='white')
			unname.append(str(m))
			untypea.append('link_rubber')
			unwidth.append(wid)
			uncolor.append('white')
			unposx.append(X1)
			unposy.append(Y1)
			unposx1.append(X2)
			unposy1.append(Y2)
			X2=X1
			Y2=Y1




def Release(event):
	if test != 'pencil' and test != 'rubber' and test != 'arrow':
		unname.append(str(m))
		untypea.append(test)
		unwidth.append(wid)
		uncolor.append(coul)
		if test == 'line' or test == 'filled_rectangle' or test == 'rectangle':
			unposx.append(X)
			unposy.append(Y)
			unposx1.append(X1)
			unposy1.append(Y1)

		elif test == 'filled_oval' or test == 'oval':
			unposx.append(X+resx)
			unposy.append(Y+resy)
			unposx1.append(X-resx)
			unposy1.append(Y-resy)

		elif test == 'filled_circle' or test == 'circle':
			if resx<=0 and resy<=0:
				if resx <= resy:
					unposx.append(X+resx)
					unposy.append(Y+resx)
					unposx1.append(X-resx)
					unposy1.append(Y-resx)

				elif resx > resy:
					unposx.append(X+resy)
					unposy.append(Y+resy)
					unposx1.append(X-resy)
					unposy1.append(Y-resy)

			elif resx>=0 and resy>=0:
				if resx >= resy:
					unposx.append(X+resx)
					unposy.append(Y+resx)
					unposx1.append(X-resx)
					unposy1.append(Y-resx)

				elif resx < resy:
					unposx.append(X+resy)
					unposy.append(Y+resy)
					unposx1.append(X-resy)
					unposy1.append(Y-resy)

			elif resx>=0 and resy<=0:
				resy1 = -resy
				if resx >= resy1:
					unposx.append(X+resx)
					unposy.append(Y-resx)
					unposx1.append(X-resx)
					unposy1.append(Y+resx)

				elif resx < resy1:
					unposx.append(X-resx)
					unposy.append(Y+resx)
					unposx1.append(X+resx)
					unposy1.append(Y-resx)

			elif resx<=0 and resy>=0:
				resx1 = -resx
				if resy >= resx1:
					unposx.append(X+resy)
					unposy.append(Y-resy)
					unposx1.append(X-resy)
					unposy1.append(Y+resy)

				elif resy < resx1:
					unposx.append(X-resy)
					unposy.append(Y+resy)
					unposx1.append(X+resy)
					unposy1.append(Y-resy)

		'''elif test == 'picture':
			unname.append(str(m))
			untypea.append(test)
			unposx.append(X1)
			unposy.append(Y1)
			unpic.append(picture)'''



def new_page():
	Canevas.delete(ALL)

	while len(unname)!=0:
		unname.pop(0)

	while len(rename)!=0:
		rename.pop(0)

	while len(unposx)!=0:
		unposx.pop(0)
		unposx1.pop(0)
		unposy.pop(0)
		unposy1.pop(0)
		untypea.pop(0)
		unwidth.pop(0)
		uncolor.pop(0)

	while len(reposx)!=0:
		reposx.pop(0)
		reposx1.pop(0)
		reposy.pop(0)
		reposy1.pop(0)
		retypea.pop(0)
		rewidth.pop(0)
		recolor.pop(0)

	unname.append('none')
	unposx.append('none')
	unposx1.append('none')
	unposy.append('none')
	unposy1.append('none')
	untypea.append('none')
	unwidth.append('none')
	uncolor.append('none')

	rename.append('none')
	reposx.append('none')
	reposx1.append('none')
	reposy.append('none')
	reposy1.append('none')
	retypea.append('none')
	rewidth.append('none')
	recolor.append('none')

	n=0

def color_palette(N,num):
	delta = 255. / (N/3)
	num=num*100
	if num < N/3:
		R = 0
		G = delta * num
		B = 255 - delta * num
	elif N/3 <= num < 2*N/3:
		R = delta * (num - N/3)
		G = 255
		B = 0
	elif 2*N/3 <= num <= N:
		R = 255
		G = 255 - delta * (num - 2*N/3)
		B = 0
	return '#' + hex(int(R))[2:].zfill(2) + hex(int(G))[2:].zfill(2)+ hex(int(B))[2:].zfill(2)

def color_chooser(event):
	global coul,coulx,couly,view,n
	Canevas1.delete(view)
	n= 100
	coulx = event.x
	couly = event.y
	coulx1 = (coulx/5)+1
	if coulx1 > 99:
		coulx1 = 99
	elif coulx1 < 0:
		coulx1 = 0
	coul = color_palette(n,1.0/float(n)*float(coulx1))
	view = Canevas1.create_oval(coulx-10,couly-10,coulx+10,couly+10,fill=coul)

def color_viewer(event):
	global view,coul
	coulx = event.x
	couly = event.y
	coulx1 = (coulx/5)+1
	if coulx1 > 99:
		coulx1 = 99
		coulx = 500
	elif coulx1 < 0:
		coulx1 = 0
		coulx = 0
	if couly > 50:
		couly = 50

	elif couly < 0:
		couly = 0
	coul = color_palette(n,1.0/float(n)*float(coulx1))
	Canevas1.delete(view)
	view = Canevas1.create_oval(coulx-10,couly-10,coulx+10,couly+10,fill=coul)


def color():
	global Canevas1,view
	Canevas1 = Canvas(root, width = 500, height =50,bg = 'white')
	Canevas1.config(cursor='tcross')
	Canevas1.bind('<Button-1>',color_chooser)
	Canevas1.bind('<B1-Motion>',color_viewer)
	Canevas1.grid(row=2,column=1)
	view = Canevas1.create_oval(-5,-5,0,0,fill=coul)
	k=0
	n= 100
	azex=0
	azex1=5
	azey=0
	azey1=50
	for k in range(n):
		c= color_palette(n,1.0/float(n)*float(k))
		Canevas1.create_rectangle(azex,azey,azex1,azey1,outline=c,fill=c)
		azex+=5
		azex1+=5

def save():
	Canevas.update()
	Canevas.postscript(file=tkFileDialog.asksaveasfilename(), colormode='color')

def writing(event):
	global X,Y,wid,string,m,n,X1,letter
	string = ''
	key = event.char
	key1 = event.keysym
	if test == 'text' and key1 != 'BackSpace' and key1 != 'Return':
		letter.append(key)
		for i in letter:
			string += i
			print 'hello'
		Canevas.delete(m)
		SIZE = tkFont.Font(size=wid)
		m = Canevas.create_text(X,Y,anchor=NW,text=string,width=X1-X,font=SIZE,fill=coul)

	elif key1 == 'Return':
		n += 1
		m = str(n)
		Y+=wid+(wid/2)

	elif key1 == 'BackSpace' and len(letter)>0:
		letter.pop()
		for i in letter:
			string += i
			print 'hello'
		Canevas.delete(m)
		SIZE = tkFont.Font(size=wid)
		m = Canevas.create_text(X,Y,anchor=NW,text=string,width=X1-X,font=SIZE,fill=coul)

W1 = 580
H = 500

root = Tk()
root.title('Paint')

test = 'arrow'
n = 0

test1 = 1

coul = 'black'

wid = 1

Canevas = Canvas(root, width = W1, height =H,bg = 'white')
Canevas.focus_set()



Label1 = Label(root, text = 'Thickness : %s'%wid)
Label1.grid(row=2,column=0)

### MENU ########

menubar = Menu(root)

menutools = Menu(menubar,tearoff=0)
menufilled = Menu(menutools,tearoff=0)
menuempty = Menu(menutools,tearoff=0)
menufile = Menu(menubar,tearoff=0)
menufile.add_command(label="Open an image",command=Open)
menufile.add_command(label="New page",command=new_page)
menufile.add_command(label="Save",command=save)
menufile.add_command(label="Quit",command=root.destroy)
menubar.add_cascade(label="File", menu=menufile)

menutools.add_command(label="Pencil",command = pencil)
menutools.add_command(label="Rubber", command = rubber)
menutools.add_command(label="Line", command = line)
menutools.add_command(label="Text", command = text)
menutools.add_command(label="Arrow", command = arrow)
menubar.add_cascade(label="Tools",menu=menutools)

menutools.add_cascade(label="Filled forms",menu=menufilled)
menufilled.add_command(label="Filled Rectangle", command = filled_rectangle)
menufilled.add_command(label="Filled Oval", command = filled_oval)
menufilled.add_command(label="Filled circle", command = filled_circle)

menutools.add_cascade(label="Empty forms",menu=menuempty)
menuempty.add_command(label="Rectangle", command = rectangle)
menuempty.add_command(label="Oval", command = oval)
menuempty.add_command(label="circle", command = circle)

menubar.add_command(label="Undo",command=undo)
menubar.add_command(label="Redo",command=redo)

root.config(menu=menubar)

### MENU ########

Canevas.bind('<Button-1>',L_Clic)
#Canevas.bind('<Button-3>',R_Clic)
Canevas.bind('<B1-Motion>',Drag)
Canevas.bind('<ButtonRelease-1>',Release)
Canevas.bind("<Button-4>", plus)
Canevas.bind("<Button-5>", minus)
Canevas.bind('<Control-z>',undo1)
Canevas.bind("<Control-y>", redo1)
Canevas.bind('<Key>',writing)
Canevas.grid(row=0,column=0, columnspan=2,sticky=NW)


gifdict={}
color()

root.mainloop()
