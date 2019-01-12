
# GitHub : https://github.com/cosmineala/p2py10_interfata_grafica

from tkinter import*
from random import*



class meniu(object): # Folosim obiectul meniu ca sa creem un meniu de setari al aplicatiei

	def __init__( self ) :

		self.meniu_f = Tk() # Creem o fereastra

		self.meniu_f.title( "Meniu") # Dam nume ferestrei

		self.meniu_f.geometry( "300x100" ) # Dam dimensiuni ferestrei

		self.p_nr_coloane = Label( self.meniu_f , text = "Nr. de coloane" ) # Creem un obiect care afiseaza un text
		self.p_nr_randuri = Label( self.meniu_f , text = "Nr. de randuri" ) # afisare text

		self.r_nr_coloane = Entry( self.meniu_f ) # creem un obiect in care se pot introduce date
		self.r_nr_randuri = Entry( self.meniu_f ) # introducere date

		self.run_button = Button( self.meniu_f , text = "Start simulation" ) # Creem un buton care porneste simularea ruland functiile necesare

		self.p_nr_coloane.grid( row = 0 , column = 0 ) # afisam un ubiect sub forma de matrice
		self.p_nr_randuri.grid( row = 1 , column = 0 ) # afisare forma matrice

		self.r_nr_coloane.grid( row = 0 , column = 1 ) # afisare forma matrice
		self.r_nr_randuri.grid( row = 1 , column = 1 ) # afisare forma matrice

		self.run_button.grid( row = 2 , column = 1 ) # afisare forma matrice

		self.run_button["command"] = self.pre_nun_matrice # Definim ce face butonul atunci cand este apasat


	def pre_nun_matrice(self) : # citeste datele introduse si apeleaza functia de rulare

		y = self.r_nr_coloane.get()
		x = self.r_nr_randuri.get()

		self.run_matrice( x , y )


	def run_matrice( self , a , b ) : # ruleaza simulatorul

		self.meniu_f.destroy() # distruge fereastra veche

		self.a = int ( a ) # randuri

		self.b = int( b ) # coloane

		dim = str( self.b * 55 + 25 ) + "x" + str( self.a * 55 + 30 ) # stabileste ce dimensiuni trebuie sa aiba fereastra in functie de cate celule contine

		root = Tk() # creeaza o fereastra noua

		root.title( "generatia 0") # stabileste cum se numeste fereastra ( ea se redenumeste automat la fiecare generatie )

		root.geometry( dim ) # seteaza dimensiunile calculate mai sus

		tab1 = tabel( root , self.a , self.b ) # creeaza un obiect de tip tabel






#------------------------------------------------------------------------------TABEL---START---------------------------------------------------

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

#-------------------------------------------------------------------------------------TABEL---END---------------------------------



#--------------------------------------------------------------------------------CELULA---START-----------------------------------

class celula(object): # Acest obiect contine datele si metodele necesare celulei dar si metodele necesare afisari celulelor
	
	def __init__( self , stare , x , y , zona_top ) :
		
		self.zona_top = zona_top # calveaza zona in care se vor afisa celulele
		self.stare = stare # salveaza stare
		self.next_gen = stare # salveaza starea urmatoare
		self.x = x # randuri
		self.y = y # coloane
		self.photo1 = PhotoImage(file="c1.gif") # salveaza textura pentru celulele vi
		self.photo0 = PhotoImage(file="c0.gif") # salveaza textura pentru celulele moarte

		self.t_celula = Label( zona_top , image = self.get_poza() ) # Creeaza celula

		self.t_celula.grid( row = x + 1 , column = y ) # Afiseaza celula


	def set_stare( self , stare ) : # seteaza starea

		self.stare = stare


	def get_poza( self ) : # returneaza textura corecta in functie de starea celulei

		if self.stare == 1 :
			return self.photo1
		else :
			return self.photo0


	def get_stare( self ) : # returneaza stare
		
		return self.stare


	def set_next_gen( self , next_gen ) : # seteaza starea generatiei urmatoare

		self.next_gen = next_gen


	def get_next_gen( self ) : # returneaza stare celulei in generatia urmatoare

		return self.next_gen


	def c_next_gen( self ) : # modifica texturile celulelor cand trece in urmatoare generatie
		
		self.stare = self.next_gen # stare actuala devine stare urmatoarei generatii

		self.t_celula.destroy() # distruge textura veche

		self.t_celula = Label( self.zona_top , image = self.get_poza() ) # creeaza textura noua

		self.t_celula.grid( row = self.x + 1 , column = self.y ) # afiseaza noua textura


	def set_x( self , x ) : # steaxa x

		self.x = x 


	def get_x( self ) : # returneaza x

		return self.x


	def set_y( self , y ) : # seteaza Y

		self.y = y


	def get_y( self ) : # returneza Y

		return self.y

#-------------------------------------------------------------------------------CELULA---END---------------------------------------------------





		
# start ------------------------------------------------------------------------------- start ------------------------------------

meniu_1 = meniu() # Creeaza un obiect de tip meniu

meniu_1.meniu_f.mainloop() # Face programul sa ruleze in bucla pana este terminat




		