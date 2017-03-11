from Tkinter import *
import tkFileDialog
import tkMessageBox



unlista = ['none']
untypea = ['none']
unwidth = ['none']
uncolor = ['none']
unposx = ['none']
unposy = ['none']
unposx1 = ['none']
unposy1 = ['none']

relista = ['none']
retypea = ['none']
rewidth = ['none']
recolor = ['none']
reposx = ['none']
reposy = ['none']
reposx1 = ['none']
reposy1 = ['none']


### THICKNESS ###

def minus():
	global wid,Label1,butplus,butminus
	if wid > 0:
		wid -= 1
		if wid == 0:
			wid = 1

	else:
		print 'min'
		wid = 1

	butplus.destroy()
	Label1.destroy()
	butminus.destroy()
	butplus = Button(root, text ='+', overrelief='solid', command = plus)
	butplus.pack(in_=bottom,side = RIGHT)

	Label1 = Label(root, text = 'Thickness : %s'%wid)
	Label1.pack(in_=bottom,side = RIGHT)

	butminus = Button(root, text ='-', overrelief='solid', command = minus)
	butminus.pack(in_=bottom,side = RIGHT)

def plus():
	global wid,Label1,butplus,butminus
	if wid < 100:
		wid += 1

	else:
		print 'max'

	butplus.destroy()
	Label1.destroy()
	butminus.destroy()
	butplus = Button(root, text ='+', overrelief='solid', command = plus)
	butplus.pack(in_=bottom,side = RIGHT)

	Label1 = Label(root, text = 'Thickness : %s'%wid)
	Label1.pack(in_=bottom,side = RIGHT)

	butminus = Button(root, text ='-', overrelief='solid', command = minus)
	butminus.pack(in_=bottom,side = RIGHT)

### THICKNESS ###

def Open():
	filename = tkFileDialog.askopenfilename()

	photo = PhotoImage(file=filename)
	gifdict[filename] = photo

	rep = tkMessageBox.askyesno(photo,'Do you want to adjust the canvas with the picture ?')

	if rep == True:
		Canevas.create_image(0,0,anchor=NW,image=photo)
		Canevas.config(height=photo.height(),width=photo.width())

	else:
		tkMessageBox.showinfo('test','look at the Terminal')
		pixx = int(raw_input('Choose an pixel for your anchor (X):'))
		pixy = int(raw_input('Choose an pixel for your anchor (Y):'))
		Canevas.create_image(pixx,pixy,anchor=NW,image=photo)


	root.title("Image ")



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

def fill_rectangle():
	global test
	test = 'fill_rectangle'
	root.config(cursor='tcross')

def fill_oval():
	global test
	test = 'fill_oval'
	root.config(cursor='circle')

def fill_circle():
	global test
	test = 'fill_circle'
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

### TOOLS #######



def undo():
	global test1
	do = 2
	if len(untypea) == 0:
		print 'error'

	elif untypea[len(untypea)-1] == 'none':

		relista.append(unlista[len(unlista)-1])
		unlista.pop()

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

	elif untypea[len(untypea)-1] == 'pencil' or untypea[len(untypea)-1] == 'rubber':

		Canevas.delete(unlista[len(unlista)-1])

		relista.append(unlista[len(unlista)-1])
		unlista.pop()

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


		if len(untypea) == 1 or len(untypea) != 'pencil' or len(untypea) != 'rubber':
			do = 1

		if len(untypea) != 0 and untypea[len(untypea)-do] == 'pencil' or  untypea[len(untypea)-do] == 'rubber' and len(untypea) != 0:
			root.after(1,undo)


	elif untypea[len(untypea)-1] == 'line' or untypea[len(untypea)-1] == 'fill_rectangle' or untypea[len(untypea)-1] == 'rectangle' or untypea[len(untypea)-1] == 'fill_oval' or untypea[len(untypea)-1] == 'oval' or untypea[len(untypea)-1] == 'fill_circle' or untypea[len(untypea)-1] == 'circle':

		Canevas.delete(unlista[len(unlista)-1])

		relista.append(unlista[len(unlista)-1])
		unlista.pop()

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


def redo():
	global test1
	do = 2
	if len(retypea) == 0:
		print 'error'

	elif retypea[len(retypea)-1] == 'none':
		unlista.append(relista[len(relista)-1])
		relista.pop()

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

		relista[len(relista)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=rewidth[len(rewidth)-1],outline=recolor[len(recolor)-1],fill=recolor[len(recolor)-1])

		unlista.append(relista[len(relista)-1])
		relista.pop()

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


	elif retypea[len(retypea)-1] == 'rubber':

		relista[len(relista)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=wid,outline='white',fill='white')

		unlista.append(relista[len(relista)-1])
		relista.pop()

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

	elif retypea[len(retypea)-1] == 'line':

		relista[len(relista)-1] = Canevas.create_line(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=rewidth[len(rewidth)-1],fill=recolor[len(recolor)-1])

		unlista.append(relista[len(relista)-1])
		relista.pop()

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


	elif retypea[len(retypea)-1] == 'fill_rectangle':

		relista[len(relista)-1] = Canevas.create_rectangle(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],outline=recolor[len(recolor)-1],fill=recolor[len(recolor)-1])

		unlista.append(relista[len(relista)-1])
		relista.pop()

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

		relista[len(relista)-1] = Canevas.create_rectangle(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],outline=recolor[len(recolor)-1])

		unlista.append(relista[len(relista)-1])
		relista.pop()

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


	elif retypea[len(retypea)-1] == 'fill_oval' or retypea[len(retypea)-1] == 'fill_circle':

		relista[len(relista)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],outline=recolor[len(recolor)-1],fill=recolor[len(recolor)-1])

		unlista.append(relista[len(relista)-1])
		relista.pop()

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

		relista[len(relista)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],outline=recolor[len(recolor)-1])

		unlista.append(relista[len(relista)-1])
		relista.pop()

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


def Clic(event):
	global X,Y,n,m
	X = event.x
	Y = event.y
	n += 1
	m = str(n)
	if test != 'arrow':
		unlista.append('none')
		untypea.append('none')
		unwidth.append('none')
		uncolor.append('none')
		unposx.append('none')
		unposy.append('none')
		unposx1.append('none')
		unposy1.append('none')

def Drag(event):
	global X,Y,test,line,n,m,coul,X1,Y1,resx,resx,resy,resx1,resy1
	X1 = event.x
	Y1 = event.y

	if test == 'pencil':
		m = Canevas.create_oval(X1-1,Y1-1,X1+1,Y1+1,width=wid,outline=coul,fill=coul)

	elif test == 'rubber':
		m = Canevas.create_oval(X1-1,Y1-1,X1+1,Y1+1,width=wid,outline='white',fill='white')

	elif test == 'line':
		Canevas.delete(m)
		m = Canevas.create_line(X,Y,X1,Y1,width=wid,fill=coul)

	elif test == 'fill_rectangle':
		Canevas.delete(m)
		m = Canevas.create_rectangle(X,Y,X1,Y1,outline=coul,fill=coul)

	elif test == 'fill_oval':
		Canevas.delete(m)
		resx = X-X1
		resy = Y-Y1
		Canevas.delete(m)
		m = Canevas.create_oval(X,Y,X-resx,Y-resy,outline=coul,fill=coul)

	elif test == 'rectangle':
		Canevas.delete(m)
		m = Canevas.create_rectangle(X,Y,X1,Y1,width=wid,outline=coul)

	elif test == 'oval':
		Canevas.delete(m)
		resx = X-X1
		resy = Y-Y1
		Canevas.delete(m)
		m = Canevas.create_oval(X,Y,X-resx,Y-resy,width=wid,outline=coul)

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

	elif test == 'fill_circle':
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


	if len(unlista)>3000:
		unlista.pop(0)
		untypea.pop(0)
		unwidth.pop(0)
		uncolor.pop(0)
		unposx.pop(0)
		unposy.pop(0)
		unposx1.pop(0)
		unposy1.pop(0)


	if test == 'pencil' or test == 'rubber':
		unlista.append(str(m))
		untypea.append(test)
		unwidth.append(wid)
		uncolor.append(coul)
		unposx.append(X1-1)
		unposy.append(Y1-1)
		unposx1.append(X1+1)
		unposy1.append(Y1+1)




def Release(event):
	if test != 'pencil' and test != 'rubber' and test != 'arrow':
		unlista.append(str(m))
		untypea.append(test)
		unwidth.append(wid)
		uncolor.append(coul)
		if test == 'line' or test == 'fill_rectangle' or test == 'rectangle':
			unposx.append(X)
			unposy.append(Y)
			unposx1.append(X1)
			unposy1.append(Y1)

		elif test == 'fill_oval' or test == 'oval':
			unposx.append(X)
			unposy.append(Y)
			unposx1.append(X-resx)
			unposy1.append(Y-resy)

		elif test == 'fill_circle' or test == 'circle':
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

def prin():
	print 'unname =',unname
	print 'unposx =',unposx
	print 'unposy =',unposy
	print 'unposx1 =',unposx1
	print 'unposy1 =',unposy1
	print 'untypea =',untypea
	print 'unwidth =',unwidth
	print 'uncolor =',uncolor

	print 'rename =',rename
	print 'reposx =',reposx
	print 'reposy =',reposy
	print 'reposx1 =',reposx1
	print 'reposy1 =',reposy1
	print 'retypea =',retypea
	print 'rewidth =',rewidth
	print 'recolor =',recolor

def color_palette(N,num):
	delta = 255. / (N/3)
	num=num*100
	if num < N/3:
		R = 0
		G = delta * num
		B = 255 - delta * num
		print '1',num
	elif N/3 <= num < 2*N/3:
		R = delta * (num - N/3)
		G = 255
		B = 0
		print '2'
	elif 2*N/3 <= num <= N:
		R = 255
		G = 255 - delta * (num - 2*N/3)
		B = 0
		print '3'
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
	coul = var_coul(n,1.0/float(n)*float(coulx1))
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
	coul = var_coul(n,1.0/float(n)*float(coulx1))
	Canevas1.delete(view)
	view = Canevas1.create_oval(coulx-10,couly-10,coulx+10,couly+10,fill=coul)


def color():
	global Canevas1,view
	root1 = Tk()
	root1.title('Pion')
	root1.config(cursor='tcross')
	Canevas1 = Canvas(root1, width = 500, height =50,bg = 'white')
	Canevas1.bind('<Button-1>',color_chooser)
	Canevas1.bind('<B1-Motion>',color_viewer)
	Canevas1.focus_set()
	Canevas1.pack()
	view = Canevas1.create_oval(-5,-5,0,0,fill=coul)
	k=0
	n= 100
	azex=0
	azex1=5
	azey=0
	azey1=50
	for k in range(n):
		c= var_coul(n,1.0/float(n)*float(k))
		Canevas1.create_rectangle(azex,azey,azex1,azey1,outline=c,fill=c)
		azex+=5
		azex1+=5
		Canevas1.focus_set()

def save():
	Canevas.update()
	name = str(raw_input('Picture name: '))
	fil=Canevas.postscript(file="%s.ps"%name, colormode='color')
	print '%s has been saved'%name



W = int(raw_input('Width :'))
H = int(raw_input('Height :'))

root = Tk()
root.title('Pion')

test = 'pencil'
n = 0

test1 = 1

coul = 'black'

wid = 1

Canevas = Canvas(root, width = W, height =H,bg = 'white')
Canevas.focus_set()




### BUTTON SETTTINGS

top = Frame(root)
top.pack(side=TOP)

bottom = Frame(root)
bottom.pack(side=BOTTOM)

### BUTTON SETTTINGS



### TOOLS BUTTON

Button(root, text ='Pencil',relief=RAISED,cursor="pencil",command = pencil).pack(in_=top,side = LEFT)
Button(root, text ='Rubber',relief=RAISED,cursor="dotbox", command = rubber).pack(in_=top,side = LEFT)
Button(root, text ='Line',relief=RAISED,cursor="tcross", command = line).pack(in_=top,side = LEFT)
Button(root, text ='Fill Rectangle',relief=RAISED,cursor="tcross", command = fill_rectangle).pack(in_=top,side = LEFT)
Button(root, text ='Fill Oval',relief=RAISED,cursor="circle", command = fill_oval).pack(in_=top,side = LEFT)
Button(root, text ='Fill Circle',relief=RAISED,cursor="circle", command = fill_circle).pack(in_=top,side = LEFT)
Button(root, text ='Rectangle',relief=RAISED,cursor="tcross", command = rectangle).pack(in_=top,side = LEFT)
Button(root, text ='Oval',relief=RAISED,cursor="circle", command = oval).pack(in_=top,side = LEFT)
Button(root, text ='Circle',relief=RAISED,cursor="circle", command = circle).pack(in_=top,side = LEFT)
Button(root, text ='Arrow',relief=RAISED,cursor="arrow", command = arrow).pack(in_=top,side = LEFT)
Button(root, text ='test1', command = prin).pack(in_=top,side = LEFT)

### TOOLS BUTTON



butplus = Button(root, text ='+', overrelief='solid', command = plus)
butplus.pack(in_=bottom,side = RIGHT)

Label1 = Label(root, text = 'Thickness : %s'%wid)
Label1.pack(in_=bottom,side = RIGHT)

butminus = Button(root, text ='-', overrelief='solid', command = minus)
butminus.pack(in_=bottom,side = RIGHT)


### MENU ########

menubar = Menu(root)

menufile = Menu(menubar,tearoff=0)
menufile.add_command(label="Open an image",command=Open)
menufile.add_command(label="New page",command=new_page)
menufile.add_command(label="Save",command=save)
menufile.add_command(label="Color palette",command=color)
menufile.add_command(label="Quit",command=root.destroy)
menubar.add_cascade(label="File", menu=menufile)

menubar.add_command(label="Undo",command=undo)
menubar.add_command(label="Redo",command=redo)

root.config(menu=menubar)

### MENU ########

Canevas.bind('<Button-1>',Clic)
Canevas.bind('<B1-Motion>',Drag)
Canevas.bind('<ButtonRelease-1>',Release)
Canevas.pack()


gifdict={}


root.mainloop()
