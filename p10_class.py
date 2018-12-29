from tkinter import*
from random import*
from PIL import*

class celula(object):
	
	def __init__(self , stare , x , y , root ) :
		
		self.stare = stare
		self.next_gen = stare 
		self.x = x
		self.y = y

		t_celula = Label( root , text = str(stare) )

		t_celula.grid( row = x + 1 , column = y )

	def set_stare( self , stare ) : 

		self.stare = stare


	def get_stare( self ):
		
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

		self.root = root

		self.nr_x = nr_x
		self.nr_y = nr_y

		self.nr_gen = 0

		self.frame_com = Frame( root )
		self.frame_com.pack(  )

		self.frame_ma = Frame( root )
		self.frame_ma.pack( side = BOTTOM )

		self.b_next_gen = Button( self.frame_com , text = "next gen" )
		self.b_next_gen.grid()
		self.b_next_gen["command"] = self.run_next_gen()

		self.matrice_celule = []

		for i in range( self.nr_x ) :

			for j in range( self.nr_y ) :

				self.matrice_celule.append( celula( randint( 0 , 1 ) , i , j , self.frame_ma ) )



	def set_celula( self , x , y , stare ) :

		self.matrice_celule[ x * self.nr_y + y ].set_stare = stare

	def get_nr_gen( self ) :

		return self.nr_gen

	def next_gen( self , x , y ) :

		vecini = 0

		if ( x - 1 ) * self.nr_y + y - 1 >= 0 and ( x - 1 ) * self.nr_y + y - 1 < self.nr_x * self.nr_y and self.matrice_celule[ ( x - 1 ) * self.nr_y + y - 1 ].get_stare == 1 : # stanga sus
			vecini = vecini + 1

		if ( x - 1 ) * self.nr_y + y >= 0 and ( x - 1 ) * self.nr_y + y < self.nr_x * self.nr_y and self.matrice_celule[ ( x - 1 ) * self.nr_y + y ].get_stare == 1 : # sus
			vecini = vecini + 1

		if ( x - 1 ) * self.nr_y + y + 1 >= 0 and ( x - 1 ) * self.nr_y + y + 1 < self.nr_x * self.nr_y and self.matrice_celule[ ( x - 1 ) * self.nr_y + y + 1 ].get_stare == 1 : # dreapta sus
			vecini = vecini + 1

		if x * self.nr_y + y - 1 >= 0 and x * self.nr_y + y - 1 < self.nr_x * self.nr_y and self.matrice_celule[ x * self.nr_y + y - 1 ].get_stare == 1 : # stanga
			vecini = vecini + 1

		if x * self.nr_y + y + 1 >= 0 and x * self.nr_y + y + 1 < self.nr_x * self.nr_y and self.matrice_celule[ x * self.nr_y + y + 1 ].get_stare == 1 : # dreapta
			vecini = vecini + 1

		if ( x + 1 ) * self.nr_y + y - 1 >= 0 and ( x + 1 ) * self.nr_y + y - 1 < self.nr_x * self.nr_y and self.matrice_celule[ ( x + 1 ) * self.nr_y + y - 1 ].get_stare == 1 : # stanga jos
			vecini = vecini + 1

		if ( x + 1 ) * self.nr_y + y >= 0 and ( x + 1 ) * self.nr_y + y < self.nr_x * self.nr_y and self.matrice_celule[ ( x + 1 ) * self.nr_y + y ].get_stare == 1 : # jos 
			vecini = vecini + 1

		if ( x + 1 ) * self.nr_y + y + 1 >= 0 and ( x + 1 ) * self.nr_y + y + 1 < self.nr_x * self.nr_y  and self.matrice_celule[ ( x + 1 ) * self.nr_y + y + 1 ].get_stare == 1 : # deapata jos
			vecini = vecini + 1

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

a = 25

b = 25

dim = str( a * 16 + 30 ) + "x" + str( b * 20 + 30 )

root = Tk()

a = tabel( root , a , b )

root.title( "generatia " + str( a.get_nr_gen() ) )
root.geometry( dim )

root.mainloop()




		