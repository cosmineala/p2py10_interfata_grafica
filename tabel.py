
from tkinter import*
from random import*

from celula import*

class tabel(object): # Folosim obiectul tabel pentru a afisa toate celule si pentru a rula anumite metode 
	
	def __init__( self , root , nr_randuri , nr_coloane ) :

		self.matrice_celule = [] # Creeaza o lista in care tinem toate obiectele de tip celula

		self.root = root # retinem fereastra

		self.zona_top = Frame( root ) # creem o zona in partea de sus pentru a separa celulele de butoane sau alte obicte
		self.zona_top.pack( side = TOP ) # afisam zona

		self.zona_bot = Frame( root ) # creem o zona in partea de jos pentru butoane
		self.zona_bot.pack( side = BOTTOM ) # afisam zona

		self.nr_randuri = nr_randuri # nr randuri
		self.nr_coloane = nr_coloane # nr coloane

		self.nr_gen = 0 # tine minte la ce generatie am ajuns

		self.b_next_gen = Button( self.zona_bot , text = "next gen" ) # creeaza un obiect de tip buton
		self.b_next_gen.pack() # afiseaza obiectul

		for i in range( self.nr_randuri ) : # cele 2 for-uri sunt folosite pentru a un numar de bucle egal cu numarul de celume

			for j in range( self.nr_coloane ) :

				self.matrice_celule.append( celula( randint( 0 , 1 ) , i , j , self.zona_top ) ) # Obiectul celula primeste parametri si este adaugat in lista

		self.b_next_gen["command"] = self.run_next_gen # Butonul primeste o comanda cand este apasat ( mai exact sa rulexe metoda care stabileste generatia urmatoare )



	def set_celula( self , x , y , stare ) : # se poate modifica starea unei celule la alegere cu aceasta metoda

		self.matrice_celule[ nr_in_lista( x , y ) ].set_stare = stare


	def get_nr_gen( self ) : # returneaza numarul generatie pe care o simulam in acel moment

		return self.nr_gen


	def run_next_gen( self ) : # Transmite starile celulelor pentru urmatoare generatie

		self.nr_gen += 1

		self.root.title( "generatia " + str( self.get_nr_gen() ) ) # modifica titlul ferestrei sa fie numarul generatie curente

		#print ("da_run_next_gen")

		for i in range( self.nr_randuri ) :

			for j in range( self.nr_coloane ) :

				self.next_gen( i , j ) # stabileste care este stare celeulei in generatia viitoare 

		for i in range( self.nr_randuri ) :

			for j in range( self.nr_coloane ) :

				self.matrice_celule[ self.nr_in_lista( i , j ) ].c_next_gen() # Ruleaza o metoda in obiectele de tip celula si acestea se auto modifica


	def next_gen( self , x , y ) : # stabileste daca celula in urmatoare generatiei o sa fie 1 ( vie ) sau 0 ( moarta )


		vecini = self.nr_vecini( x , y ) # ruleaza metoda nr_vecini care ii returneaza cati vecini vi are

		if self.matrice_celule[ self.nr_in_lista( x , y ) ].get_stare() == 1 : # verifica daca celula este vie

			if vecini > 3 or vecini < 2 : # verifica dac celula are mai mult de 3 sau mai puti ne 2 vecini vi

				self.matrice_celule[ self.nr_in_lista( x , y ) ].set_next_gen( 0 ) # celula devine moarta

		else : 

			if vecini == 3 : # verifica daca are 3 vecini ( in cazul in care ste moarta ca sa stie daca devine vie )

				self.matrice_celule[ self.nr_in_lista( x , y ) ].set_next_gen( 1 ) # starea celulei devine 1


	def nr_in_lista( self , x , y ) :  # returneaza numarul celulai in lista ( celulele sunt salvate intr-o lista dar pentru simplitate le tratez ca si cum ar fi intr-o matrice  )

	 	return	x * self.nr_coloane + y


	def nr_vecini( self , x , y ) : # verifica cati vecini sunt vi

		vecini = 0

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
