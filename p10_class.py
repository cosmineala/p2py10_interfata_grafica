from tkinter import*
from random import*
from PIL import ImageTk, Image

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

		frame_com = Frame( root )
		frame_com.pack(  )

		frame_ma = Frame( root )
		frame_ma.pack( side = BOTTOM )

		b_next_gen = Button( frame_com , text = "next gen" )
		b_next_gen.grid()

		matrice_celule = []

		for i in range( self.nr_x ) :

			for j in range( self.nr_y ) :

				matrice_celule.append( celula( randint( 0 , 1 ) , i , j , frame_ma ) )



	def set_celula( self , x , y , stare ) :

		matrice_celule[ x * self.nr_y + y ].set_stare = stare

	def next_gen( self , x , y ) :

		vecini = 0

		if ( x - 1 ) * self.nr_y + y - 1 >= 0 and ( x - 1 ) * self.nr_y + y - 1 <= nr_x * self.nr_y and matrice_celule[ ( x - 1 ) * self.nr_y + y - 1 ].get_stare == 1 : # stanga sus
			vecini = vecini + 1

		if ( x - 1 ) * self.nr_y + y >= 0 and ( x - 1 ) * self.nr_y + y <= nr_x * self.nr_y and matrice_celule[ ( x - 1 ) * self.nr_y + y ].get_stare == 1 : # sus
			vecini = vecini + 1

		if ( x - 1 ) * self.nr_y + y + 1 >= 0 and ( x - 1 ) * self.nr_y + y + 1 <= nr_x * self.nr_y and matrice_celule[ ( x - 1 ) * self.nr_y + y + 1 ].get_stare == 1 : # dreapta sus
			vecini = vecini + 1

		if x * self.nr_y + y - 1 >= 0 and x * self.nr_y + y - 1 <= nr_x * self.nr_y and matrice_celule[ x * self.nr_y + y - 1 ].get_stare == 1 : # stanga
			vecini = vecini + 1

		if x * self.nr_y + y + 1 >= 0 and x * self.nr_y + y + 1 <= nr_x * self.nr_y and matrice_celule[ x * self.nr_y + y + 1 ].get_stare == 1 : # dreapta
			vecini = vecini + 1

		if ( x + 1 ) * self.nr_y + y - 1 >= 0 and ( x + 1 ) * self.nr_y + y - 1 <= nr_x * self.nr_y and matrice_celule[ ( x + 1 ) * self.nr_y + y - 1 ].get_stare == 1 : # stanga jos
			vecini = vecini + 1

		if ( x + 1 ) * self.nr_y + y >= 0 and ( x + 1 ) * self.nr_y + y <= nr_x * self.nr_y and matrice_celule[ ( x + 1 ) * self.nr_y + y ].get_stare == 1 : # jos 
			vecini = vecini + 1

		if ( x + 1 ) * self.nr_y + y + 1 >= 0 and ( x + 1 ) * self.nr_y + y + 1 <= nr_x * self.nr_y and matrice_celule[ ( x + 1 ) * self.nr_y + y + 1 ].get_stare == 1 : # deapata jos
			vecini = vecini + 1

		if matrice_celule[ x * self.nr_y + y ].get_stare == 1 : 

			if vecini > 3 and vecini < 2 : 

				matrice_celule[ x * self.nr_y + y ].set_next_gen( 0 )

		else : 

			if vecini == 3 :

				matrice_celule[ x * self.nr_y + y ].set_next_gen( 1 )

		
# start ------------------------------------------------------------------------------- start ----------------

root = Tk()

root.geometry( "400x400" )

a = tabel( root , 4 , 4 )

root.mainloop()




		