# coding: utf-8
from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

def a (): #Importer les données
   
    texa=Label(fen1, textvariable=saisie1).grid(row=4, column=3)
    texb=Label(fen1, textvariable=saisie2).grid(row=5, column=3)
    texc=Label(fen1, textvariable=saisie3).grid(row=6, column=3)
    tex4=Label(fen1, text='a=').grid(row=4, column=2)
    tex5=Label(fen1, text='b=').grid(row=5, column=2)
    tex6=Label(fen1, text='c=').grid(row=6, column=2)
    A= entree1.get()
    B= entree2.get()
    C= entree3.get()

def b (): #Delta
    # avec float, on peut saisir des nombres décimaux pour a,b et c
    #si on remplace float par eval : on peut alors saisir par exemple 2/3
    #saisie4 = float(entree2.get())**2-4*float(entree1.get())*float(entree3.get())
    saisie4 = eval( entree2.get())**2-4*eval(entree1.get())*eval(entree3.get())
    delt.set(saisie4)
    texdelta= Label(fen1, text='delta=').grid(row=3, column=8)
    texdelta2=Label(fen1, textvariable=delt).grid(row=3, column=9)


def c (): # Les racines // a doit être différent de 0 ! (on ne peut pas diviser par 0)

    a1=float(entree1.get())
    a2=float(entree2.get())
    a3=float(entree3.get())
    saisie4 = a2**2-4*a1*a3
    if saisie4 == 0 :
        X0= -a2/(2*a1)#priorité des opérations !
        texsol1.config( text= 'X1=')
        texsol2.config(text= "")
        texsolu1.config(text=str(X0))
        texsolu2.config(text="")

    elif saisie4 > 0 :
        X1= (-a2-sqrt(saisie4))/(2*a1)
        X2= (-a2+sqrt(saisie4))/(2*a1)
        texsol1.config( text= 'X1=')
        texsol2.config(text= 'X2=')
        texsolu1.config(text=str(X1))
        texsolu2.config(text=str(X2))


    else :
        X3= (-a2-1j*sqrt(-saisie4 ))/(2*a1)
        X4= (-a2+1j*sqrt(-saisie4 ))/(2*a1)
        texsol1.config( text= 'X3=')
        texsol2.config(text= 'X4=')
        texsolu1.config(text=str(X3))
        texsolu2.config(text=str(X4))

def d (): #Dérivée  é= \xe9
    deriv= (2*float(entree1.get()))
    der1.set(deriv)
    texderiv= Label(fen1, text= 'd\xe9riv\xe9e de f:').grid(row=6, column=8)
    textderivsol= Label(fen1, textvariable=der1).grid(row=6, column=9)

    textderivsol2= Label(fen1, text='x +').grid(row=6, column=10)
    textderivsol3= Label(fen1, textvariable=saisie2).grid(row=6, column=11)


def e (): #Primitive
    primit1= (1/3)*float(entree1.get())
    primit2= (1/2)*float(entree2.get())
    prim1.set(primit1)
    prim2.set(primit2)
    texprimit= Label(fen1, text= 'primitive de f:').grid(row=7, column=8)
    textprimitsol= Label(fen1, textvariable=prim1).grid(row=7, column=9)
    textprimitsolbis= Label(fen1, text= 'x\xb3 +').grid(row=7, column=10)
    textprimitsol1= Label(fen1, textvariable=prim2).grid(row=7, column=11)
    textprimitsol1bis= Label(fen1, text= 'x\xb2 +').grid(row=7, column=12)
    textprimitsol2= Label(fen1, textvariable=saisie3)
    textprimitsol2.grid(row=7, column=13)
    textprimitsol2bis= Label(fen1, text= 'x + k').grid(row=7, column=14)



def f(): #fonction
    A= float(entree1.get())
    B= float(entree2.get())
    C= float(entree3.get())
    cadre = float((-B)/(2*A))

    def g(A,B,C,t):
        return(A*t**2+B*t+C)
     
    x= np.linspace(cadre+100,cadre-100,1000)
    y=  g( A,B,C,x)   
    plt.plot(x,y)
    plt.show()










fen1=Tk()
fen1.title('Math\xe9matux')
fen1.geometry('1000x600')

tex1=Label(fen1, text='Bienvenue sur Math\xe9matux ! Veuillez entrez votre formule.', fg='black', bg='white')
#Pour faire en sorte que l'affichage ne se superpose
saisie1=IntVar()
der1=StringVar()
prim1=StringVar()
prim2=StringVar()
delt=StringVar()


entree1=Entry(fen1,textvariable=saisie1,width=4)
entree1.grid(row=2, column=3)
tex2=Label(fen1, text='x\xb2+', fg='black', bg='white')
saisie2=IntVar()
entree2=Entry(fen1,textvariable=saisie2, width=4)
entree2.grid(row=2, column=5)
tex3=Label(fen1, text='x+', fg='black', bg='white')
saisie3=IntVar()
entree3=Entry(fen1,textvariable=saisie3, width=4)
entree3.grid(row=2,column=7)
tex4=Label(fen1, text='f(x)=',fg='black', bg='white')


tex1.grid(row=1, column=1)
tex2.grid(row=2, column=4)
tex3.grid(row=2, column=6)
tex4.grid(row=2, column=2)


bou1=Button(fen1, text='Quitter', command=fen1.destroy).grid(row=8, column=15)
bou2=Button(fen1, text='importer a;b;c', command=a).grid(row=3, column=1)
bou3=Button(fen1, text='Delta', command=b).grid(row=4, column=1)
bou4=Button(fen1, text='Racine(s)' , command=c).grid(row=5, column=1)
bou5=Button(fen1, text='Dérivée', command=d).grid(row=6, column=1)
bou6=Button(fen1, text='Primitive', command=e).grid(row=7, column=1)
bou7=Button(fen1, text='Graphique', command=f).grid(row=8, column=1)


texsolu1= Label(fen1 )
texsolu1.grid(row=4, column=9)
texsolu2= Label(fen1,text="")
texsolu2.grid(row=5, column=9)
texsol1= Label(fen1,text="")
texsol1.grid(row=4, column=8)
texsol2= Label(fen1,text="" )
texsol2.grid(row=5, column=8)




fen1.mainloop()
