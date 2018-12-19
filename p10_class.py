


class celula(object):
	
	def __init__(self , stare , x , y ) :
		
		self.srate = stare
		self.next_gen = stare 
		self.x = x
		self.y = y

	def set_stare( self , stare ) : 

		self.stare = stare

	def get_stare():
		
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
	
	def __init__( self , nr_x , nr_y ) :

		self.nr_x = nr_x
		self.nr_y = nr_y

		matrice_celule = []

		for i in range( self.nr_x - 1 ) :

			for j in range( self.nr_y - 1 ) :

				matrice_celule.append( celula( randint( 0 , 2 ) , i , j ) )



	def set_celula( self , x , y , stare ) :

		matrice_celule[ x * self.nr_y + y ].set_stare = stare

	def next_gen( self , x , y ) :

		vecini = 0

		if ( x - 1 ) * self.nr_y + y - 1 >= 0 and ( x - 1 ) * self.nr_y + y - 1 <= nr_x * self.nr_y and matrice_celule[ ( x - 1 ) * self.nr_y + y - 1 ].get_stare == 1 : # stanga sus
			vecini = vecini + 1

		if ( x - 1 ) * self.nr_y + y >= 0 and ( x - 1 ) * self.nr_y + y <= nr_x * self.nr_y and matrice_celule[ ( x - 1 ) * self.nr_y + y ].get_stare == 1 : # sus
			vecini = vecini + 1

		if ( x - 1 ) * self.nr_y + y + 1 >= 0 and ( x - 1 ) * self.nr_y + y + 1 <= nr_x * self.nr_y and matrice_celule[ ( x - 1 ) * self.nr_y + y + 1 ].get_stare == 1 : # dreapta sus

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

			if vecini > 3 && vecini < 2 : 

				matrice_celule[ x * self.nr_y + y ].set_next_gen( 0 )

		else : 

			if vecini == 3 :

				matrice_celule[ x * self.nr_y + y ].set_next_gen( 1 )

		






		