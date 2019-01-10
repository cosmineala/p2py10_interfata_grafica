from tkinter import*
from random import*
from PIL import*

'''class proba(object):

	def __init__( self , num ) :

		self.num = num

	def get_num( self ) :

		return self.num

	def get_stare()( self ) :

		print(" 1 ")'''



class celula(object):
	
	def __init__( self , stare , x , y , root ) :
		
		self.stare = stare
		self.next_gen = stare 
		self.x = x
		self.y = y
		self.photo1 = PhotoImage(file='c1.gif')
		self.photo0 = PhotoImage(file='c0.gif')

		self.t_celula = Label( root , image = self.get_poza() )

		self.t_celula.grid( row = x + 1 , column = y )

	def set_stare( self , stare ) : 

		self.stare = stare

	def get_poza( self ) :

		if self.stare == 1 :
			return self.photo1
		else :
			return self.photo0

	def get_stare( self ) :
		
		return self.stare

	def set_next_gen( self , next_gen ) :

		print("da_set_next_gen")

		self.next_gen = next_gen

	def get_next_gen( self ) :

		return self.next_gen

	def c_next_gen( self ) :

		print("da_c_next_gen")
		
		self.stare = self.next_gen

		self.t_celula.destroy()

		self.t_celula = Label( root , image = self.get_poza() )

		self.t_celula.grid( row = self.x + 1 , column = self.y )





	def set_x( self , x ) :

		self.x = x 

	def get_x( self ) :

		return self.x

	def set_y( self , y ) :

		self.y = y

	def get_y( self ) :

		return self.y

#------------------------------------------------------------------------------

class tabel(object):
	
	def __init__( self , root , nr_randuri , nr_coloane ) :

		self.matrice_celule = []

		self.root = root

		self.zona_top = Frame( root )
		self.zona_top.pack( side = TOP )

		self.zona_bot = Frame( root )
		self.zona_bot.pack( side = BOTTOM )

		self.nr_randuri = nr_randuri # nr randuri
		self.nr_coloane = nr_coloane # nr coloane

		self.nr_gen = 0

		self.b_next_gen = Button( self.zona_bot , text = "next gen" )
		self.b_next_gen.pack()

		for i in range( self.nr_randuri ) :

			for j in range( self.nr_coloane ) :

				self.matrice_celule.append( celula( randint( 0 , 1 ) , i , j , self.zona_top ) )

		#self.b_next_gen["command"] = self.run_next_gen 

				#print( str( i ) + "<- i | j->" + str( j ) + "\n" )  <- printeaza i si j
		'''for i in range( 100000000 ) :

			self.matrice_celule.append( proba( i ) )'''



	def set_celula( self , x , y , stare ) :

		self.matrice_celule[ nr_in_lista( x , y ) ].set_stare = stare

	def get_nr_gen( self ) :

		return self.nr_gen

	def run_next_gen( self ) :

		self.nr_gen += 1
		print ("da_run_next_gen")

		for i in range( self.nr_randuri ) :

			for j in range( self.nr_coloane ) :

				self.next_gen( i , j )

		for i in range( self.nr_randuri ) :

			for j in range( self.nr_coloane ) :

				self.matrice_celule[ self.nr_in_lista( i , j ) ].c_next_gen()



	def next_gen( self , x , y ) :

		print( "da_next_gen" + str(x) + str(y) )

		vecini = self.nr_vecini( x , y )

		if self.matrice_celule[ self.nr_in_lista( x , y ) ].get_stare() == 1 : 

			if vecini > 3 or vecini < 2 : 

				self.matrice_celule[ self.nr_in_lista( x , y ) ].set_next_gen( 0 )
				print( "da_next_gen__0__" + str(x) + str(y) )


		else : 

			if vecini == 3 :

				self.matrice_celule[ self.nr_in_lista( x , y ) ].set_next_gen( 1 )
				print( "da_next_gen__1__" + str(x) + str(y) )


	def nr_in_lista( self , x , y ) : 

	 	return	x * self.nr_coloane + y

	def nr_vecini( self , x , y ) :

		vecini = 0
		#print( len(self.matrice_celule) )

		if x - 1 >= 0 and y - 1 >= 0 : # stanga sus
			if self.matrice_celule[ self.nr_in_lista( x - 1 , y - 1 ) ].get_stare() == 1 :
				vecini += 1

		if x - 1 >= 0 : # sus
			if self.matrice_celule[ self.nr_in_lista( x - 1 , y ) ].get_stare() == 1 :
				vecini += 1

		if x - 1 >= 0 and y + 1 < self.nr_coloane  : # dreapta sus
			if self.matrice_celule[ self.nr_in_lista( x - 1 , y + 1 ) ].get_stare() == 1 :
				vecini += 1

		if y - 1 >= 0 : # stanga
			if self.matrice_celule[ self.nr_in_lista( x , y - 1 ) ].get_stare() == 1 :
				vecini += 1

		if y + 1 < self.nr_coloane : # dreapta
			if self.matrice_celule[ self.nr_in_lista( x , y + 1 ) ].get_stare() == 1 :
				vecini += 1

		if x + 1 < self.nr_randuri and y - 1 >= 0 : # stanga jos
			if self.matrice_celule[ self.nr_in_lista( x + 1 , y - 1 ) ].get_stare() == 1 :
				vecini += 1

		if x + 1 < self.nr_randuri : # jos
			if self.matrice_celule[ self.nr_in_lista( x + 1 , y ) ].get_stare() == 1 :
				vecini += 1

		if x + 1 < self.nr_randuri and y + 1 < self.nr_coloane : # stanga jos
			if self.matrice_celule[ self.nr_in_lista( x + 1 , y + 1 ) ].get_stare() == 1 :
				vecini += 1

		return vecini







		
# start ------------------------------------------------------------------------------- start ----------------

a = 10 # randuri

b = 15 # coloane

dim = str( b * 55 + 25 ) + "x" + str( a * 55 + 30 )

root = Tk()

tab1 = tabel( root , a , b )

root.title( "generatia " + str( tab1.get_nr_gen() ) )
root.geometry( dim )

tab1.b_next_gen["command"] = tab1.run_next_gen

root.mainloop()




		