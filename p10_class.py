from tkinter import*
from random import*
from PIL import*

class celula(object):
	
	def __init__(self , stare , x , y , root ) :
		
		self.stare = stare
		self.next_gen = stare 
		self.x = x
		self.y = y

		t_celula = Label( root , image = self.get_poza() )

		t_celula.grid( row = x + 1 , column = y )

	def set_stare( self , stare ) : 

		self.stare = stare

	def get_poza( self ) :

		photo1 = PhotoImage(file='c1.gif')
		photo0 = PhotoImage(file='c0.gif')

		if self.stare == 1 :
			return photo1
		else :
			return photo0

	def get_stare( self ) :
		
		return self.stare

	def set_next_gen( self , next_gen ) :

		self.next_gen = next_gen

	def get_next_gen( self ) :

		return self.next_gen

	def next_gen( self ) :
		
		self.stre = self.next_gen

	def set_x( self , x ) :

		self.x = x 

	def get_x( self ) :

		return self.x

	def set_y( self , y ) :

		self.y = y

	def get_y( self ) :

		return self.y

#-----------------------------------------------------------------------------

class tabel(object):
	
	def __init__( self , root , nr_x , nr_y ) :

		self.matrice_celule = []

		self.root = root

		self.nr_x = nr_x
		self.nr_y = nr_y

		self.nr_gen = 0

		self.b_next_gen = Button( self.root , text = "next gen" )
		self.b_next_gen.grid( row = self.nr_x + 1 )

		#self.b_next_gen["command"] = self.run_next_gen()    <-  se adauga linia dupa tezolvare bug mem mat

		for i in range( self.nr_x ) :

			for j in range( self.nr_y ) :

				self.matrice_celule.append( celula( randint( 0 , 1 ) , i , j , self.root ) )

				print( str( i ) + "<- i | j->" + str( j ) + "\n" )



	def set_celula( self , x , y , stare ) :

		self.matrice_celule[ x * self.nr_y + y ].set_stare = stare

	def get_nr_gen( self ) :

		return self.nr_gen

	def next_gen( self , x , y ) :

		vecini = 0

		if ( x - 1 ) * self.nr_y + y - 1 >= 0 and ( x - 1 ) * self.nr_y + y - 1 < self.nr_x * self.nr_y : # stanga sus
			if self.matrice_celule[ ( x - 1 ) * self.nr_y + y - 1 ].get_stare == 1 : 
				vecini += 1

		if ( x - 1 ) * self.nr_y + y >= 0 and ( x - 1 ) * self.nr_y + y < self.nr_x * self.nr_y : # sus
			if self.matrice_celule[ ( x - 1 ) * self.nr_y + y ].get_stare == 1 :
				vecini += 1

		if ( x - 1 ) * self.nr_y + y + 1 >= 0 and ( x - 1 ) * self.nr_y + y + 1 < self.nr_x * self.nr_y : # dreapta sus
			if self.matrice_celule[ ( x - 1 ) * self.nr_y + y + 1 ].get_stare == 1 : 
				vecini += 1

		if x * self.nr_y + y - 1 >= 0 and x * self.nr_y + y - 1 < self.nr_x * self.nr_y : # stanga
			if self.matrice_celule[ x * self.nr_y + y - 1 ].get_stare == 1 : 
				vecini += 1

		if x * self.nr_y + y + 1 >= 0 and x * self.nr_y + y + 1 < self.nr_x * self.nr_y : # dreapta
			if self.matrice_celule[ x * self.nr_y + y + 1 ].get_stare == 1 : 
				vecini += 1

		if ( x + 1 ) * self.nr_y + y - 1 >= 0 and ( x + 1 ) * self.nr_y + y - 1 < self.nr_x * self.nr_y : # stanga jos
			if self.matrice_celule[ ( x + 1 ) * self.nr_y + y - 1 ].get_stare == 1 : 
				vecini += 1

		if ( x + 1 ) * self.nr_y + y >= 0 and ( x + 1 ) * self.nr_y + y < self.nr_x * self.nr_y : # jos
			if self.matrice_celule[ ( x + 1 ) * self.nr_y + y ].get_stare == 1 :  
				vecini += 1

		if ( x + 1 ) * self.nr_y + y + 1 >= 0 and ( x + 1 ) * self.nr_y + y + 1 < self.nr_x * self.nr_y : # deapata jos
			if self.matrice_celule[ ( x + 1 ) * self.nr_y + y + 1 ].get_stare == 1 : 
				vecini += 1

		if self.matrice_celule[ x * self.nr_y + y ].get_stare == 1 : 

			if vecini > 3 and vecini < 2 : 

				self.matrice_celule[ x * self.nr_y + y ].set_next_gen( 0 )

		else : 

			if vecini == 3 :

				self.matrice_celule[ x * self.nr_y + y ].set_next_gen( 1 )


	def run_next_gen( self ) :

		self.nr_gen += 1

		for i in range( self.nr_x ) :

			for j in range( self.nr_y ) :

				self.next_gen( i , j )



		
# start ------------------------------------------------------------------------------- start ----------------

a = 2 # randuri

b = 3 # coloane

dim = str( b * 50 + 25 ) + "x" + str( a * 60 + 30 )

root = Tk()

tab1 = tabel( root , a , b )

root.title( "generatia " + str( tab1.get_nr_gen() ) )
root.geometry( dim )

root.mainloop()




		