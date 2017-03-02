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
	butplus = Button(Mafenetre, text ='+', overrelief='solid', command = plus)
	butplus.pack(in_=bottom,side = RIGHT)

	Label1 = Label(Mafenetre, text = 'Thickness : %s'%wid)
	Label1.pack(in_=bottom,side = RIGHT)

	butminus = Button(Mafenetre, text ='-', overrelief='solid', command = minus)
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
	butplus = Button(Mafenetre, text ='+', overrelief='solid', command = plus)
	butplus.pack(in_=bottom,side = RIGHT)

	Label1 = Label(Mafenetre, text = 'Thickness : %s'%wid)
	Label1.pack(in_=bottom,side = RIGHT)

	butminus = Button(Mafenetre, text ='-', overrelief='solid', command = minus)
	butminus.pack(in_=bottom,side = RIGHT)

### THICKNESS ###



### COLORS #######

def red():
	global coul
	coul = 'red'

def blue():
	global coul
	coul = 'blue'

def black():
	global coul
	coul = 'black'

def yellow():
	global coul
	coul = 'yellow'

def green():
	global coul
	coul = 'green'

def white():
	global coul
	coul = 'white'

def brown():
	global coul
	coul = 'brown'

def dimgray():
	global coul
	coul = 'dim gray'

def orangered():
	global coul
	coul = 'orange red'

def salmon():
	global coul
	coul = 'salmon'

### COLORS #######



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


	Mafenetre.title("Image ")

def Close():
	Canevas.delete(ALL)
	Mafenetre.title("Image")






### TOOLS #######

def pencil():
	global test
	test = 'pencil'
	Mafenetre.config(cursor='pencil')

def rubber():
	global test
	test = 'rubber'
	Mafenetre.config(cursor='dotbox')

def line():
	global test
	test = 'line'
	Mafenetre.config(cursor='tcross')

def fill_rectangle():
	global test
	test = 'fill_rectangle'
	Mafenetre.config(cursor='tcross')

def fill_oval():
	global test
	test = 'fill_oval'
	Mafenetre.config(cursor='circle')

def fill_circle():
	global test
	test = 'fill_circle'
	Mafenetre.config(cursor='circle')

def rectangle():
	global test
	test = 'rectangle'
	Mafenetre.config(cursor='tcross')

def oval():
	global test
	test = 'oval'
	Mafenetre.config(cursor='circle')

def circle():
	global test
	test = 'circle'
	Mafenetre.config(cursor='circle')

def arrow():
	global test
	test = 'arrow'
	Mafenetre.config(cursor='arrow')

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

		Mafenetre.after(1,undo)

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
			Mafenetre.after(1,undo)


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

		Mafenetre.after(1,redo)

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
			Mafenetre.after(1,redo)


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
			Mafenetre.after(1,redo)

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



def dele():
	for i in unlista:
		Canevas.delete(i)

	while len(unlista)!=0:
		unlista.pop(0)

	n=0

def prin():
	print 'unlista =',unlista
	#print 'unposx =',unposx
	#print 'unposy =',unposy
	#print 'unposx1 =',unposx1
	#print 'unposy1 =',unposy1



Width = 500 #int(raw_input('Width :'))
Height = 500 #int(raw_input('Height :'))

Mafenetre = Tk()
Mafenetre.title('Pion')

W = Width
H = Height

test = 'pencil'
n = 0

test1 = 1

coul = 'black'

wid = 1

Canevas = Canvas(Mafenetre, width = W, height =H,bg = 'white')
Canevas.focus_set()




### BUTTON SETTTINGS

top = Frame(Mafenetre)
top.pack(side=TOP)

bottom = Frame(Mafenetre)
bottom.pack(side=BOTTOM)

### BUTTON SETTTINGS



### TOOLS BUTTON

Button(Mafenetre, text ='Pencil',relief=RAISED,cursor="pencil",command = pencil).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Rubber',relief=RAISED,cursor="dotbox", command = rubber).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Line',relief=RAISED,cursor="tcross", command = line).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Fill Rectangle',relief=RAISED,cursor="tcross", command = fill_rectangle).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Fill Oval',relief=RAISED,cursor="circle", command = fill_oval).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Fill Circle',relief=RAISED,cursor="circle", command = fill_circle).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Rectangle',relief=RAISED,cursor="tcross", command = rectangle).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Oval',relief=RAISED,cursor="circle", command = oval).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Circle',relief=RAISED,cursor="circle", command = circle).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='Arrow',relief=RAISED,cursor="arrow", command = arrow).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='test', command = dele).pack(in_=top,side = LEFT)
Button(Mafenetre, text ='test1', command = prin).pack(in_=top,side = LEFT)

### TOOLS BUTTON



butplus = Button(Mafenetre, text ='+', overrelief='solid', command = plus)
butplus.pack(in_=bottom,side = RIGHT)

Label1 = Label(Mafenetre, text = 'Thickness : %s'%wid)
Label1.pack(in_=bottom,side = RIGHT)

butminus = Button(Mafenetre, text ='-', overrelief='solid', command = minus)
butminus.pack(in_=bottom,side = RIGHT)



### COLORS BUTTON
Button(Mafenetre, text =' ', bg='red', fg='red', overrelief='solid', command = red).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='yellow', fg='yellow', overrelief='solid', command = yellow).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='blue', fg='blue', overrelief='solid', command = blue).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='black', fg='black', overrelief='solid', command = black).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='green', fg='green', overrelief='solid', command = green).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='brown', fg='brown', overrelief='solid', command = brown).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='dim gray', fg='dim gray', overrelief='solid', command = dimgray).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='Orange Red', fg='Orange Red', overrelief='solid', command = orangered).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='Salmon', fg='Salmon', overrelief='solid', command = salmon).pack(in_=bottom,side = LEFT)
Button(Mafenetre, text =' ', bg='white', fg='white', overrelief='solid', command = white).pack(in_=bottom,side = LEFT)

### COLORS BUTTON


### MENU ########

menubar = Menu(Mafenetre)

menufile = Menu(menubar,tearoff=0)
menufile.add_command(label="Open an image",command=Open)
menufile.add_command(label="New page",command=Close)
#menufile.add_command(label="Save",command=save)
menufile.add_command(label="Quit",command=Mafenetre.destroy)
menubar.add_cascade(label="File", menu=menufile)

menubar.add_command(label="Undo",command=undo)
menubar.add_command(label="Redo",command=redo)

Mafenetre.config(menu=menubar)

### MENU ########

Canevas.bind('<Button->',Clic)
Canevas.bind('<B1-Motion>',Drag)
Canevas.bind('<ButtonRelease-1>',Release)
Canevas.pack()


gifdict={}


Mafenetre.mainloop()

Mafenetre.quit()
