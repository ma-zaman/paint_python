from Tkinter import *
from PIL import Image, ImageDraw
import pygame
import tkFileDialog
import tkMessageBox
import subprocess
import tkFont


lettre = []


unname = ['none']
untypea = ['none']
unwidth = ['none']
uncolor = ['none']
unposx = ['none']
unposy = ['none']
unposx1 = ['none']
unposy1 = ['none']

rename = ['none']
retypea = ['none']
rewidth = ['none']
recolor = ['none']
reposx = ['none']
reposy = ['none']
reposx1 = ['none']
reposy1 = ['none']


### EPAISSEUR ###

def moins(event):
	global wid,Label1,Valeur
	if wid > 0:
		wid -= 1
		if wid == 0:
			wid = 1

	else:
		print 'min'
		wid = 1

	Valeur.set(wid/2)


def plus(event):
	global wid,Label1,Valeur
	if wid < 100:
		wid += 1

	else:
		print 'max'

	Valeur.set(wid/2)


### EPAISSEUR ###

def ouvrir():
	global test,photo
	filename = tkFileDialog.askopenfilename()

	if filename != () and filename !='':
		photo = PhotoImage(file=filename)
		gifdict[filename] = photo

		rep = tkMessageBox.askyesno(photo,'Voulez-vous ajuster le fond avec l\'image?')

		if rep == True:
			Canevas.delete(ALL)
			Canevas.create_image(0,0,anchor=NW,image=photo)
			Canevas.config(height=photo.height(),width=photo.width())

		else:
			test = 'image'
			tkMessageBox.showinfo(photo,'Appuyez sur le bouton gauche pour placer le centre de l\'image')
			Mafenetre.config(cursor='tcross')

	Canevas.update()
	Canevas.postscript(file="testazerty.ps", colormode='color')
	im = Image.open("testazerty.ps")
	draw = ImageDraw.Draw(im)

	print filename
	print type(filename)
	print gifdict

def ouvrir_musique():
	global son1,volume,musiqueplay
	filename = tkFileDialog.askopenfilename()
	musiqueplay = True
	pygame.mixer.init()
	pygame.mixer.music.load(filename)
	pygame.mixer.music.set_volume(volume)
	pygame.mixer.music.play(-1)

'''

def reglage_musique():
	global son1,volume,volume1
	volume1.set(volume*100)
	echelle_volume = Scale(Mafenetre,from_=0,to=100,resolution=1,orient=HORIZONTAL,length=100,width=10,variable=volume1,command=reglage_volume)
	echelle_volume.grid(row=0,column=3)


def reglage_volume(valeur):
        global volume,volume1,musiqueplay
        if musiqueplay == True:
                volume = float(valeur)/100.0
                pygame.mixer.music.set_volume(volume)

'''


### OUTILS #######

def crayon():
	global test
	test = 'crayon'
	Mafenetre.config(cursor='pencil')

def gomme():
	global test
	test = 'gomme'
	Mafenetre.config(cursor='dotbox')

def ligne():
	global test
	test = 'ligne'
	Mafenetre.config(cursor='tcross')

def rectangle_rempli():
	global test
	test = 'rectangle_rempli'
	Mafenetre.config(cursor='tcross')

def oval_rempli():
	global test
	test = 'oval_rempli'
	Mafenetre.config(cursor='circle')

def cercle_rempli():
	global test
	test = 'cercle_rempli'
	Mafenetre.config(cursor='circle')

def rectangle():
	global test
	test = 'rectangle'
	Mafenetre.config(cursor='tcross')

def oval():
	global test
	test = 'oval'
	Mafenetre.config(cursor='circle')

def cercle():
	global test
	test = 'cercle'
	Mafenetre.config(cursor='circle')

def fleche():
	global test
	test = 'fleche'
	Mafenetre.config(cursor='arrow')

def texte():
	global test
	test = 'texte'
	Mafenetre.config(cursor='xterm')

### OUTILS #######



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

		Mafenetre.after(1,undo)

	elif untypea[len(untypea)-1] == 'crayon' or untypea[len(untypea)-1] == 'gomme' or untypea[len(untypea)-1] == 'lien_crayon' or untypea[len(untypea)-1] == 'lien_gomme':

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


		if len(untypea) == 1 or len(untypea) != 'crayon' or len(untypea) != 'gomme' or len(untypea) != 'lien_crayon' or len(untypea) == 'lien_gomme':
			do = 1

		if len(untypea) != 0 and (untypea[len(untypea)-do] == 'crayon' or untypea[len(untypea)-do] == 'gomme' or untypea[len(untypea)-do] == 'lien_crayon' or untypea[len(untypea)-do] == 'lien_gomme'):
			Mafenetre.after(1,undo)


	elif untypea[len(untypea)-1] == 'ligne' or untypea[len(untypea)-1] == 'rectangle_rempli' or untypea[len(untypea)-1] == 'rectangle' or untypea[len(untypea)-1] == 'oval_rempli' or untypea[len(untypea)-1] == 'oval' or untypea[len(untypea)-1] == 'cercle_rempli' or untypea[len(untypea)-1] == 'cercle':

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

		Mafenetre.after(1,redo)

	elif retypea[len(retypea)-1] == 'crayon':

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

		if len(retypea) != 0 and retypea[len(retypea)-do] == 'crayon':
			Mafenetre.after(1,redo)

	elif retypea[len(retypea)-1] == 'lien_crayon':

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

		if len(retypea) != 0 and retypea[len(retypea)-do] == 'lien_crayon':
			Mafenetre.after(1,redo)


	elif retypea[len(retypea)-1] == 'gomme':

		rename[len(rename)-1] = Canevas.create_oval(reposx[len(reposx)-1],reposy[len(reposy)-1],reposx1[len(reposx1)-1],reposy1[len(reposy1)-1],width=wid,outline='white',fill='white')

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

		if len(retypea) != 0 and retypea[len(retypea)-do] == 'gomme':
			Mafenetre.after(1,redo)

	elif retypea[len(retypea)-1] == 'lien_gomme':

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

		if len(retypea) != 0 and retypea[len(retypea)-do] == 'lien_gomme':
			Mafenetre.after(1,redo)

	elif retypea[len(retypea)-1] == 'ligne':

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


	elif retypea[len(retypea)-1] == 'rectangle_rempli':

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


	elif retypea[len(retypea)-1] == 'oval_rempli' or retypea[len(retypea)-1] == 'cercle_rempli':

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


	elif retypea[len(retypea)-1] == 'oval' or retypea[len(retypea)-1] == 'cercle':

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

def undo1(event):
	touche = event.keysym
	undo()

def redo1(event):
	touche = event.keysym
	redo()

'''
def clic(event):
        X = event.x
        Y = event.y
        pix = Canevas
        print Canvas.

   '''


def Clic(event):
	global X,Y,n,m,X2,Y2,chaine
	X = event.x
	Y = event.y
	X1 = X
	Y1 = Y
	X2 = X
	Y2 = Y
	n += 1
	m = str(n)
	if test != 'fleche':
		unname.append('none')
		untypea.append('none')
		unwidth.append('none')
		uncolor.append('none')
		unposx.append('none')
		unposy.append('none')
		unposx1.append('none')
		unposy1.append('none')

	if test == 'crayon':
		m = Canevas.create_oval(X1-wid,Y1-wid,X1+wid,Y1+wid,outline=coul,fill=coul)

	if test == 'texte':
		chaine = ''
		taille = tkFont.Font(size=wid)
		m = Canevas.create_text(X,Y,anchor=NW,text=chaine,width=wid,font=taille)

	elif test == 'image':
		m = Canevas.create_image(X1,Y1,anchor=CENTER,image=photo)

def Drag(event):
	global X,Y,test,line,n,m,coul,X1,Y1,resx,resx,resy,resx1,resy1,W1,H,X2,Y2
	X1 = event.x
	Y1 = event.y

	if test == 'crayon':
		m = Canevas.create_oval(X1-wid,Y1-wid,X1+wid,Y1+wid,outline=coul,fill=coul)

	elif test == 'gomme':
		m = Canevas.create_oval(X1-wid,Y1-wid,X1+wid,Y1+wid,outline='white',fill='white')

	elif test == 'ligne':
		Canevas.delete(m)
		m = Canevas.create_line(X,Y,X1,Y1,width=wid,fill=coul)

	elif test == 'rectangle_rempli':
		Canevas.delete(m)
		m = Canevas.create_rectangle(X,Y,X1,Y1,outline=coul,fill=coul)

	elif test == 'oval_rempli':
		Canevas.delete(m)
		resx = X-X1
		resy = Y-Y1
		Canevas.delete(m)
		m = Canevas.create_oval(X+resx,Y+resy,X-resx,Y-resy,outline=coul,fill=coul)

	elif test == 'rectangle':
		Canevas.delete(m)
		m = Canevas.create_rectangle(X,Y,X1,Y1,width=wid,outline=coul)

	elif test == 'oval':
		Canevas.delete(m)
		resx = X-X1
		resy = Y-Y1
		Canevas.delete(m)
		m = Canevas.create_oval(X+resx,Y+resy,X-resx,Y-resy,width=wid,outline=coul)

	elif test == 'cercle':
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

	elif test == 'cercle_rempli':
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

	elif test == 'fleche':
		W1 = X1
		H = Y1
		if W1 <= 100:
			W1 = 100
		if H <= 100:
			H = 100
		Canevas.config(width = W1, height =H)
		if W1>580:
			Canevas.grid(row=0,column=0, columnspan=2,sticky=NW)

		else:
			Canevas.grid(row=0,column=0,sticky=NW)

	elif test == 'texte':
		Canevas.delete(m)
		m = Canevas.create_rectangle(X,Y,X1,Y1,width=1,outline='black')

	elif test == 'image':
		Canevas.delete(m)
		m = Canevas.create_image(X1,Y1,anchor=CENTER,image=photo)


	if len(unname)>1000000:
		unname.pop(0)
		untypea.pop(0)
		unwidth.pop(0)
		uncolor.pop(0)
		unposx.pop(0)
		unposy.pop(0)
		unposx1.pop(0)
		unposy1.pop(0)


	if test == 'crayon' or test == 'gomme':
		unname.append(str(m))
		untypea.append(test)
		unwidth.append(wid-1)
		uncolor.append(coul)
		unposx.append(X1)
		unposy.append(Y1)
		unposx1.append(X1)
		unposy1.append(Y1)



		if test == 'crayon':
			n += 1
			m = str(n)
			m = Canevas.create_line(X1,Y1,X2,Y2,width=wid*2,fill=coul)
			unname.append(str(m))
			untypea.append('lien_crayon')
			unwidth.append(wid)
			uncolor.append(coul)
			unposx.append(X1)
			unposy.append(Y1)
			unposx1.append(X2)
			unposy1.append(Y2)
			X2=X1
			Y2=Y1



		elif test == 'gomme':
			n += 1
			m = str(n)
			m = Canevas.create_line(X1,Y1,X2,Y2,width=wid*2,fill='white')
			unname.append(str(m))
			untypea.append('lien_gomme')
			unwidth.append(wid)
			uncolor.append('white')
			unposx.append(X1)
			unposy.append(Y1)
			unposx1.append(X2)
			unposy1.append(Y2)
			X2=X1
			Y2=Y1





def Release(event):
	global im
	if test != 'crayon' and test != 'gomme' and test != 'fleche':
		unname.append(str(m))
		untypea.append(test)
		unwidth.append(wid)
		uncolor.append(coul)
		if test == 'ligne' or test == 'rectangle_rempli' or test == 'rectangle':
			unposx.append(X)
			unposy.append(Y)
			unposx1.append(X1)
			unposy1.append(Y1)

		elif test == 'texte':
			Canevas.delete(m)

		elif test == 'oval_rempli' or test == 'oval':
			unposx.append(X+resx)
			unposy.append(Y+resy)
			unposx1.append(X-resx)
			unposy1.append(Y-resy)

		elif test == 'cercle_rempli' or test == 'cercle':
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

	Canevas.update()
	Canevas.postscript(file="testazerty.ps", colormode='color')
	im = Image.open("testazerty.ps")
	draw = ImageDraw.Draw(im)



def nouvelle_page():
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

def azertyuiop(N,num):
	global R,G,B,num1
	delta = 255. / (N/3)
	num1=num*100
	if N/3 <= num1 < 2*N/3:
		R = delta * (num1 - N/3)
		G = 255 - delta * (num1 - N/3)
		B = 0

	return '#' + hex(int(R))[2:].zfill(2) + hex(int(G))[2:].zfill(2)+ hex(int(B))[2:].zfill(2)
'''

	elif 2*N/3 <= num1 <= N:
		R = 255
		G = 255 - delta * (num1 - 2*N/3)
		B = 0

'''



def couleur(N,num):
	global R,G,B,num1
	delta = 255. / (N/3)
	num1=num*100
	if num == 0:
		return '#000000'
	elif num == 1:
		return '#ffffff'
	elif num1 < N/3:
		R = 0
		G = delta * num1
		B = 255 - delta * num1

	elif N/3 <= num1 < 2*N/3:
		R = delta * (num1 - N/3)
		G = 255
		B = 0

	elif 2*N/3 <= num1 <= N:
		R = 255
		G = 255 - delta * (num1 - 2*N/3)
		B = 0

	return '#' + hex(int(R))[2:].zfill(2) + hex(int(G))[2:].zfill(2)+ hex(int(B))[2:].zfill(2)

def selecteur_couleur(event):
	global coul,coulx,couly,view,n,view1
	Canevas1.delete(view1)
	Canevas1.delete(view)
	n= 100
	coulx = event.x
	couly = event.y
	coulx1 = (coulx/5)+1
	if coulx1 > 99:

		coulx1 = 99
	elif coulx1 < 0:
		coulx1 = 1

	print coulx1
	coul = couleur(n,1.0/float(n)*float(coulx1))
	view = Canevas1.create_polygon(coulx-10,20,coulx+10,20,coulx,0,outline='black',fill='black')
	view1 = Canevas1.create_line(coulx,0,coulx,20,width=1,fill=coul)

def visionneuse_couleur(event):
	global view,coul,view1
	coulx = event.x
	couly = event.y
	coulx1 = (coulx/5)+1
	if coulx1 > 99:
		coulx1 = 100
		coulx = 500

	elif coulx1 < 1:
		coulx1 = 0
		coulx = 0

	if couly > 50:
		couly = 50

	elif couly < 0:
		couly = 0

	coul = couleur(n,1.0/float(n)*float(coulx1))
	Canevas1.delete(view)
	Canevas1.delete(view1)
	view = Canevas1.create_polygon(coulx-10,20,coulx+10,20,coulx,0,outline='black',fill='black')
	view1 = Canevas1.create_line(coulx,0,coulx,20,width=1,fill=coul)

def palette_couleurs():
	global Canevas1,view,view1
	Canevas1 = Canvas(Mafenetre, width = 500, height =20,bg = 'white')
	Canevas1.config(cursor='tcross')
	Canevas1.bind('<Button-1>',selecteur_couleur)
	Canevas1.bind('<B1-Motion>',visionneuse_couleur)
	Canevas1.grid(row=2,column=1)
	view = Canevas1.create_polygon(-20,-20,0,-20,-10,-10,fill='black')
	view1 = Canevas1.create_line(-10,-10,-20,-20,fill=coul)
	k=0
	n= 100
	azex=0
	azex1=5
	azey=0
	azey1=20
	for k in range(n):
		c= couleur(n,1.0/float(n)*float(k))
		Canevas1.create_rectangle(azex,azey,azex1,azey1,outline=c,fill=c)
		azex+=5
		azex1+=5

def sauvegarde():
	global im
	im.save(tkFileDialog.asksaveasfilename(), "gif")

	'''
	Canevas.update()
	Canevas.postscript(file=tkFileDialog.asksaveasfilename(), colormode='color')
	subprocess.call(["ps2pdf", "-dEPSCrop", "test.ps", "test.pdf"])
'''

def ecriture(event):
	global X,Y,wid,chaine,m,n,X1,lettre
	chaine = ''
	touche = event.char
	touche1 = event.keysym
	if test == 'texte' and touche1 != 'BackSpace' and touche1 != 'Return':
		lettre.append(touche)
		for i in lettre:
			chaine += i
			print 'salut'
		Canevas.delete(m)
		taille = tkFont.Font(size=wid)
		m = Canevas.create_text(X,Y,anchor=NW,text=chaine,width=X1-X,font=taille,fill=coul)

	elif touche1 == 'Return':
		n += 1
		m = str(n)
		Y+=wid+(wid/2)

	elif touche1 == 'BackSpace' and len(lettre)>0:
		lettre.pop()
		for i in lettre:
			chaine += i
			print 'salut'
		Canevas.delete(m)
		taille = tkFont.Font(size=wid)
		m = Canevas.create_text(X,Y,anchor=NW,text=chaine,width=X1-X,font=taille,fill=coul)

	print event
	print event.char
	print event.keysym

def testezez():
	global son1
	Canevas.create_polygon(0,0,100,100,0,100,outline='black',fill='black')

def maj(nouvelleValeur):
        global wid
        wid = int(nouvelleValeur)/2

def avolume():
	global Canevas2,k,n,cache,fond,cachex,triangle,triangle1,triangle2,triangle3,taillevol,textvol,sonx
	Canevas2 = Canvas(Mafenetre, width = 100, height =20,bg = 'white')
	Canevas2.config(cursor='tcross')
	Canevas2.bind('<Button-1>',selecteur_son)
	Canevas2.bind('<B1-Motion>',visionneuse_son)
	Canevas2.grid(row=0,column=4)
	fond='#' + hex(int(240))[2:].zfill(2) + hex(int(240))[2:].zfill(2) + hex(int(240))[2:].zfill(2)
	k=0
	n= 100
	azex=0
	azex1=5
	sonx=50
	azey=0
	azey1=20
	cachex=50
	for k in range(n):
		c= azertyuiop(n,1.0/float(n)*float(k))
		if 66 >= num1 >= 33:
			Canevas2.create_rectangle(azex,azey,azex1,azey1,outline=c,fill=c)
			azex += 3
			azex1 += 3

	Canevas2.create_polygon(0,0,0,20,110,0,fill=fond)
	cache = Canevas2.create_rectangle(cachex,0,110,20,fill=fond,outline=fond)
	taillevol = tkFont.Font(size=7)
	textvol = Canevas2.create_text(20,2,anchor=NW,text="%02d%%" %sonx,width=100,font=taillevol,fill="black")
	triangle1=Canevas2.create_line(0,20,100,20,fill='black')
	triangle2=Canevas2.create_line(0,20,110,0,fill='black')
	triangle3=Canevas2.create_line(100,20,100,0,fill='black')

def selecteur_son(event):
	global volume,cache,triangle1,triangle2,triangle3,taillevol,textvol,sonx
	if musiqueplay == True:
		sonx = event.x
		if sonx > 100:
			sonx = 100

		elif sonx < 0:
			sonx = 0

		Canevas2.delete(cache)
		Canevas2.delete(triangle1)
		Canevas2.delete(triangle2)
		Canevas2.delete(triangle3)
		Canevas2.delete(textvol)
		cache = Canevas2.create_rectangle(sonx,0,110,20,fill=fond,outline=fond)
		textvol = Canevas2.create_text(20,2,anchor=NW,text="%02d%%" %sonx,width=100,font=taillevol,fill="black")
		triangle1=Canevas2.create_line(0,20,100,20,fill='black')
		triangle2=Canevas2.create_line(0,20,110,0,fill='black')
		triangle3=Canevas2.create_line(100,20,100,0,fill='black')

		volume = sonx/100.0
		pygame.mixer.music.set_volume(volume)


def visionneuse_son(event):
	global volume,cache,triangle1,triangle2,triangle3,taillevol,textvol,sonx
	if musiqueplay == True:
		sonx = event.x
		if sonx > 100:
			sonx = 100

		elif sonx < 0:
			sonx = 0

		Canevas2.delete(cache)
		Canevas2.delete(triangle1)
		Canevas2.delete(triangle2)
		Canevas2.delete(triangle3)
		Canevas2.delete(textvol)
		cache = Canevas2.create_rectangle(sonx,0,110,20,fill=fond,outline=fond)
		textvol = Canevas2.create_text(20,2,anchor=NW,text="%02d%%" %sonx,width=100,font=taillevol,fill="black")
		triangle1=Canevas2.create_line(0,20,100,20,fill='black')
		triangle2=Canevas2.create_line(0,20,110,0,fill='black')
		triangle3=Canevas2.create_line(100,20,100,0,fill='black')

		volume = sonx/100.0
		pygame.mixer.music.set_volume(volume)




W1 = 580
H = 500


Mafenetre = Tk()
Mafenetre.title('Pint')


test = 'fleche'
n = 0

test1 = 1

coul = 'black'

wid = 1

volume = 0.5

musiqueplay = False

'''

Back = PhotoImage(file="degrad.gif")
lab = Label(Mafenetre,image=Back)
lab.grid(row=0,column=0,rowspan=5,columnspan=5)


'''

Note = PhotoImage(file="volume.gif")

Canevas = Canvas(Mafenetre, width = W1, height =H,bg = 'white')
Canevas.focus_set()

Canevas.update()
Canevas.postscript(file="testazerty.ps", colormode='color')
im = Image.open("testazerty.ps")
draw = ImageDraw.Draw(im)

volume1 = StringVar()
volume1.set(50)

Valeur = StringVar()
Valeur.set(50)
echelle = Scale(Mafenetre,from_=100,to=1,resolution=1,orient=VERTICAL,length=500,width=20,variable=Valeur,command=maj)
echelle.grid(row=0,column=2,rowspan=3)

'''

echelle_volume = Scale(Mafenetre,from_=0,to=100,resolution=1,orient=HORIZONTAL,length=100,width=10,variable=volume1,command=reglage_volume)
echelle_volume.grid(row=0,column=3)

'''

### MENU ########

menubar = Menu(Mafenetre)

menuoutils = Menu(menubar,tearoff=1)
menurempli = Menu(menuoutils,tearoff=0)
menuvide = Menu(menuoutils,tearoff=0)
menufichier = Menu(menubar,tearoff=0)

menufichier.add_command(label="Ouvrir une image",command=ouvrir)
menufichier.add_command(label="Ouvrir une musique",command=ouvrir_musique)
#menufichier.add_command(label="Reglage musique",command=reglage_musique)
menufichier.add_command(label="Nouvelle page",command=nouvelle_page)
menufichier.add_command(label="Sauvegarder",command=sauvegarde)
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menufichier)

menuoutils.add_command(label="Crayon",command = crayon)
menuoutils.add_command(label="Gomme", command = gomme)
menuoutils.add_command(label="Ligne", command = ligne)
menuoutils.add_command(label="Texte", command = texte)
menuoutils.add_command(label="Fleche", command = fleche)
menubar.add_cascade(label="Outils",menu=menuoutils)

menuoutils.add_cascade(label="Formes remplis",menu=menurempli)
menurempli.add_command(label="Rectangle rempli", command = rectangle_rempli)
menurempli.add_command(label="Oval rempli", command = oval_rempli)
menurempli.add_command(label="Cercle rempli", command = cercle_rempli)

menuoutils.add_cascade(label="Formes vides",menu=menuvide)
menuvide.add_command(label="Rectangle", command = rectangle)
menuvide.add_command(label="Oval", command = oval)
menuvide.add_command(label="Cercle", command = cercle)

menubar.add_command(label="Undo",command=undo)
menubar.add_command(label="Redo",command=redo)
menubar.add_command(label="test",command=testezez)

Mafenetre.config(menu=menubar)

### MENU ########

Canevas.bind('<Button-1>',Clic)
#Canevas.bind('<Button-3>',clic)
Canevas.bind('<B1-Motion>',Drag)
Canevas.bind('<ButtonRelease-1>',Release)
Canevas.bind("<Button-4>", plus)
Canevas.bind("<Button-5>", moins)
Canevas.bind('<Control-z>',undo1)
Canevas.bind("<Control-y>", redo1)
Canevas.bind('<Key>',ecriture)
Canevas.grid(row=0,column=0,rowspan=2,columnspan=2,sticky=NW)

gifdict={}
palette_couleurs()
avolume()


Mafenetre.mainloop()

Mafenetre.quit()
