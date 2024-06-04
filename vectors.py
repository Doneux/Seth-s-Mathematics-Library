#Seth Doneux's Vector Classes and Solver UI
#2d and 3d

#Vectors handle vector components only. UI handles norm and deg. See implementation.

import math
from tkinter import * #UI functionality

#Classes
#3D Vector
class Vector3d:
    def __init__(self, i=0, j=0, k=0):
        self.dim = 3
        self.i = i
        self.j = j
        self.k = k
    
    def __add__(self, u1):
        return Vector2d(self.i + u1.i, self.j + u1.j, self.k + u1.k)
    
    def __sub__(self, u1):
        return Vector2d(self.i - u1.i, self.j - u1.j, self.k - u1.k)
    
    def __mul__(self, c1):
        ##Scalar multiplication. For cross and dot, see cross and dot.
        return Vector2d(self.i * c1, self.j * c1, self.k * c1)
    
    def __neg__(self):
        return Vector2d(-self.i, -self.j, -self.k)
    
    def __div__(self, c1):
        #I really don't like scalar division. Please just multiply by a fractional scalar.
        if c1 != 0:
            return Vector2d(self.i / c1, self.j / c1, self.k / c1)
        else:
            return None
        
    def norm(self):
        return math.sqrt((self.i * self.i) + (self. j * self.j) + (self.k * self.k))

    def dot(self, u1):
        return ((self.i * u1.i) + (self.j * u1.j) + (self.k * u1.k))
    
    def cross(self, u1):
        #following cross prod. formula using components.
        return Vector3d((self.j * u1.k - self.k * u1.j), -(self.i * u1.k - self.k * u1.i), (self.i * u1.j - self.j * u1.i))
#end 3D Vector

#2D Vector
class Vector2d:
    def __init__(self, i=0, j=0):
        self.dim = 2
        self.i = i
        self.j = j
    
    def __add__(self, u1):
        return Vector2d(self.i + u1.i, self.j + u1.j)
    
    def __sub__(self, u1):
        return Vector2d(self.i - u1.i, self.j - u1.j)
    
    def __mul__(self, c1):
        ##Scalar multiplication. For cross and dot, see cross and dot.
        return Vector2d(self.i * c1, self.j * c1)
    
    def __neg__(self):
        return Vector2d(-self.i, -self.j)
    
    def __div__(self, c1):
        #I really don't like scalar division. Please just multiply by a fractional scalar.
        if c1 != 0:
            return Vector2d(self.i / c1, self.j / c1)
        else:
            return None
        
    def norm(self):
        return math.sqrt((self.i * self.i) + (self. j * self.j))

    def cross(self, u1):
        return ((self.i * u1.i) + (self.j * u1.j))
    
    def dot(self, u1):
        #will return a 3d vector
        return Vector3d((0), (0), (self.i * u1.j - self.j * u1.i))
#end 2D Vector

#GUI functions
def vectorsolve():
    win1 = Toplevel()
    win1.geometry('250x500')
    win1.title('Vector Solver')

    '''
    2D Vector Solver - Solve for Norm and Angle given components and vice versa.
    '''
    #screen setup
    screentitle = Label(win1, text="Vectors:")
    screentitle.grid(columnspan=2)
    v2title = Label(win1, text="2D Vector Components:")
    v2title.grid(columnspan = 4)

    #i,j entry boxes
    v2i = Entry(win1, width=5)
    v2i.grid()
    v2j = Entry(win1, width=5)
    v2j.grid(column=2, row=2)
    message1 = Label(win1, text="i, j")
    message1.grid()

    #polar display
    v2polartitle = Label(win1, text="Norm and Angle(deg):")
    v2polartitle.grid(columnspan=4)
    v2norm = Entry(win1, width=5, state="readonly")
    v2norm.grid()
    v2deg = Entry(win1, width=5, state="readonly")
    v2deg.grid(column=2, row=5)
    message2 = Label(win1, text="Norm, Angle (deg only)")
    message2.grid(columnspan=4)

    #entry buttons
    def onEnterComponent(): #function when enter is pressed (component, see polar below)
        v2norm.config(state='normal')
        v2deg.config(state='normal')
        v2norm.delete(0, END)
        v2deg.delete(0, END)
        try: 
            v1i = float(v2i.get())
            v1j = float(v2j.get())
            u2 = Vector2d(v1i, v1j)
            v2norm.insert(0, str(round(u2.norm(), 3))) #computation of norm
            v2deg.insert(0, str(round(math.atan(v1j / v1i) * 180 / math.pi, 3))) #computation of angle (deg)
            v2norm.config(state='readonly')
            v2deg.config(state='readonly')
        except:
            v2norm.config(state='readonly')
            v2deg.config(state='readonly')
    enterComponent = Button(win1, text="Enter", command= onEnterComponent)
    enterComponent.grid(row=2, column=3)
    def onEnterPolar(): #polar
        v2i.config(state='normal')
        v2j.config(state='normal')
        v2i.delete(0, END)
        v2j.delete(0, END)
        try:
            v1norm = float(v2norm.get())
            v1deg = float(v2deg.get()) * math.pi / 180 #not actually a degree, but a radian. screw radians though.
            v2i.insert(0, str(round(math.cos(v1deg) * v1norm, 3)))
            v2j.insert(0, str(round(math.sin(v1deg) * v1norm, 3)))
            v2i.config(state='readonly')
            v2j.config(state='readonly')
        except:
            v2i.config(state='readonly')
            v2j.config(state='readonly')
    enterPolar = Button(win1, text="Enter", state='disabled', command=onEnterPolar)
    enterPolar.grid(column=3, row=5)

    #swap buttons
    def onPressComp():
        #swap buttons
        enablePolar.config(state='active')
        enableComponent.config(state='disabled')
        enterPolar.config(state='disabled')
        enterComponent.config(state='active')
        #clear windows
        v2i.config(state='normal')
        v2i.delete(0, END)
        v2j.config(state='normal')
        v2j.delete(0, END)
        v2norm.delete(0, END)
        v2norm.config(state='readonly')
        v2deg.delete(0, END)
        v2deg.config(state='readonly')
    def onPressPolar():
        enablePolar.config(state='disabled')
        enableComponent.config(state='active')
        enterPolar.config(state='active')
        enterComponent.config(state='disabled')
        v2norm.config(state='normal')
        v2norm.delete(0, END)
        v2deg.config(state='normal')
        v2deg.delete(0, END)
        v2i.delete(0, END)
        v2i.config(state='readonly')
        v2j.delete(0, END)
        v2j.config(state='readonly')
    enableComponent = Button(win1, command=onPressComp, state='disabled', text='Switch')
    enableComponent.grid(row=2, column=4)
    enablePolar = Button(win1, command=onPressPolar, text='Switch')
    enablePolar.grid(row=5, column=4)

    #end 2D Vector Solver
    barrier1 = Label(win1, text="------------------------")
    barrier1.grid(columnspan=4)

    '''
    3D Vector Solver - Solve for Norm given components.
    '''
    #screen setup
    title3d = Label(win1, text="3D Vector Components:")
    title3d.grid(columnspan=4)
    
    #i,j,k entry boxes
    v3i = Entry(win1, width=5)
    v3i.grid()
    v3j = Entry(win1, width=5)
    v3j.grid(column=2, row=9)
    v3k = Entry(win1, width=5)
    v3k.grid(column=3, row=9)
    message1 = Label(win1, text="i, j, k")
    message1.grid()

    #entry button 3d
    def onEnter3d():
        v3norm.config(state='normal')
        v3norm.delete(0, END)
        try:
            v31i = float(v3i.get())
            v31j = float(v3j.get())
            v31k = float(v3k.get())
            u3 = Vector3d(v31i, v31j, v31k)
            v3norm.insert(0, str(round(u3.norm(), 2)))
            v3norm.config(state='readonly')
        except:
            v3norm.config(state='readonly')
    enter3d = Button(win1, text='Enter', command=onEnter3d)
    enter3d.grid(column=4, row=9)

    #3d norm
    norm3dindic = Label(win1, text="Norm:")
    norm3dindic.grid()
    v3norm = Entry(win1, width=5, state='readonly')
    v3norm.grid()
    #end 3d vector solver

    barrier2 = Label(win1, text="------------------------")
    barrier2.grid(columnspan=4) 

    '''
    3D Vector Operations
    '''
    #u1
    u1lbl = Label(win1, text='u1:')
    u1lbl.grid()
    u1i = Entry(win1, width=5)
    u1i.grid()
    u1j = Entry(win1, width=5)
    u1j.grid(row=15, column=2)
    u1k = Entry(win1, width=5)
    u1k.grid(row=15, column=3)

    #u2
    u2lbl = Label(win1, text='u2:')
    u2lbl.grid()
    u2i = Entry(win1, width=5)
    u2i.grid()
    u2j = Entry(win1, width=5)
    u2j.grid(row=17, column=2)
    u2k = Entry(win1, width=5)
    u2k.grid(row=17, column=3)

    #operations
    def operationWrapper(op): #operation wrapper handles all operation types, since they reuse a lot of code.
        u3i.config(state='normal')
        u3j.config(state='normal')
        u3k.config(state='normal')
        u3i.delete(0, END)
        u3j.delete(0, END)
        u3k.delete(0, END)
        try:
            u11i = float(u1i.get())
            u11j = float(u1j.get())
            u11k = float(u1k.get())
            u22i = float(u2i.get())
            u22j = float(u2j.get())
            u22k = float(u2k.get())
            if op == "dot":
                u3i.insert(0, u11i * u22i)
                u3j.insert(0, u11j * u22j)
                u3k.insert(0, u11k * u22k)
            elif op == "cross":
                u11 = Vector3d(u11i, u11j, u11k)
                u22 = Vector3d(u22i, u22j, u22k)
                u33 = u11.cross(u22)
                u3i.insert(0, u33.i)
                u3j.insert(0, u33.j)
                u3k.insert(0, u33.k)
            elif op == "add":
                u3i.insert(0, u11i + u22i)
                u3j.insert(0, u11j + u22j)
                u3k.insert(0, u11k + u22k)
            elif op == "sub":
                u3i.insert(0, u11i - u22i)
                u3j.insert(0, u11j - u22j)
                u3k.insert(0, u11k - u22k)
            u3i.config(state='readonly')
            u3j.config(state='readonly')
            u3k.config(state='readonly')
        except:
            u3i.config(state='readonly')
            u3j.config(state='readonly')
            u3k.config(state='readonly')
    #dot
    def onDotPress():
        operationWrapper("dot")
    dotbut = Button(win1, text='Dot', command=onDotPress)
    dotbut.grid()
    #cross
    def onCrossPress():
        operationWrapper("cross")
    crossbut = Button(win1, text='Cross', command=onCrossPress)
    crossbut.grid(row=18, column=2)
    #add
    def onAddPress():
        operationWrapper("add")
    addbut = Button(win1, text='Add', command=onAddPress)
    addbut.grid(row=18, column=3)
    def onSubPress():
        operationWrapper("sub")
    subbut = Button(win1, text='Sub', command=onSubPress)
    subbut.grid(row=18, column=4)

    #result vector
    u3lbl = Label(win1, text='Result:')
    u3lbl.grid(columnspan= 2)
    u3i = Entry(win1, width=5, state='readonly')
    u3i.grid()
    u3j = Entry(win1, width=5, state='readonly')
    u3j.grid(row=20, column=2)
    u3k = Entry(win1, width=5, state='readonly')
    u3k.grid(row=20, column=3)
    #end 3d vector operations
#end GUI func

if __name__ == "__main__":
    win = Tk()
    win.geometry('200x200')
    win.title('Main Window - Shell')
    infbut = Button(win, text="Launch Vector Solver", command=vectorsolve)
    infbut.grid(row= 2, column=2)
    win.mainloop()
