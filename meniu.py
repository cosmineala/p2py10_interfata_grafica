
from tkinter import*

from tabel import*

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

		err = 0

		y = self.r_nr_coloane.get()

		x = self.r_nr_randuri.get()

		try: # verifica daca se poate face conversia din str la int
			int( x )
		except ValueError:
			print( " x not a int " ) # printeza in consola faptul ca s-a introdus o valoare care nu este int
			err = 1
		
		try: # verifica daca se poate face conversia din str la int
			int( y )
		except ValueError:
			print( " y not a int " )
			err = 1  # printeza in consola faptul ca s-a introdus o valoare care nu este int


		if err == 0 : # verifica daca exista o eroare de introducere a datelor
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
