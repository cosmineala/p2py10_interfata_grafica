
from tkinter import*

#from t import*

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
