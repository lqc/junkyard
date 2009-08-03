#!/usr/bin/python
#-*- coding: utf-8 -*-


from string import *
from socket import *
from struct import *
import threading

#Budujemy pakiet!
class BudujPakieta():

	def __init__(self, socket, user, pwd, pokoj, referrer, serwer, konfig, klient):
		self.pokoj = pokoj
		self.serwer = serwer
		self.referrer = referrer
		self.user = user
		self.pwd = pwd
		self.konfig = konfig
		self.klient = klient
		self.tresc = ''
		self.s = socket
		self.ilosc_userow = 0

	def login(self):
		data = pack('!hhh', 1, 8, 1400)	#Nagłówek (bez długości pakietu)
		data += pack('!h', len(self.user))	#Długość nazwy uzytkownika
		for i in self.user: data += pack('c', i)	#Nazwa uzytkownika
		data += pack('!xh', len(self.pwd))	#Pusty bajt i długość hasła
		for i in self.pwd: data += pack('c', i)	#Hasło
		data += pack('!xxxxh', len(self.pokoj))	#Cookies (nieuzywane - puste) i długość nazwy pokoju
		for i in self.pokoj: data += pack('c', i)	#Nazwa pokoju
		data += pack('!xh', len(self.referrer))	#Długość nazwy referrera
		for i in self.referrer: data += pack('c', i) 	#Referrer
		data += pack('!xh', len(self.serwer)) #Długość nazwy serwera
		for i in self.serwer: data += pack('c', i)	#Serwer
		data += pack('!xh', len(self.konfig))	#Długość konfiga
		for i in self.konfig: data += pack('c', i)	#Konfig
		data += pack('!xh', len(self.klient))	#Długość nazwy klienta
		for i in self.klient: data += pack('c', i)	#Klient
		data += pack('!x')		#Kończymy pustym bajtem...
		dlugosc = len(data)+4		#...a zaczynamy...
		data = pack('!i', dlugosc)+data	#...długością pakietu
		self.s.send(data)

	def wyslij(self):					#Pakiet wysyłanej wiadomości
		data = pack('!hhh', 1, 2, 410)
		data += pack('!h', len(self.tresc))	#Główny człon pakietu - ilość intów, ilość stringów, id i długość wiadomości
		for i in self.tresc: data += pack('c', i)	#Dodajemy treść
		data += pack('!xh', len(self.pokoj)) #oraz pustego bajta i długość nazwy pokoju
		for i in self.pokoj: data += pack('c', i)	#Teraz nazwa pokoju
		data += pack('!x')		#Kończymy pustym bajtem...
		dlugosc = len(data)+4		#...a zaczynamy...
		data = pack('!i', dlugosc)+data	#...długością pakietu
		self.s.send(data)

	def pong(self):
		data = pack('!ihh', 8, 0, 0)
		self.s.send(data)


class OdbierzPakieta():

	def __init__(self, data):
		self.tresc_odb = ''
		self.dlugosc = 0
		self.ile_int = 0
		self.ile_str = 0
		self.ajdi = 0
		self.nazwa_pokoju = ''
		self.data = data
		self.dlugosc_tresci = 0
		self.dlugosc_nazwy_pokoju = 0
		self.il_userow = 0


	def czytaj_naglowek(self):
		tresc_odb = ''
		self.dlugosc = unpack('!i', self.data[:4])[0]
		self.data = self.data[4:]
		self.ile_int = unpack('!h', self.data[:2])[0]
		self.data = self.data[2:]
		self.ile_str = unpack('!h', self.data[:2])[0]
		self.data = self.data[2:]
		self.ajdi = unpack('!h', self.data[:2])[0]
		self.data = self.data[2:]
		return self.ajdi

	def czytaj_tresc(self):
		self.dlugosc_tresci = unpack('!h', self.data[:2])[0]
		self.data = self.data[2:]
		i = 0
		while i < self.dlugosc_tresci:
			self.tresc_odb += unpack('!s', self.data[:1])[0]
			self.data = self.data[1:]
			i += 1
		self.dlugosc_nazwy_pokoju = unpack('!h', self.data[:2])[0]
		self.data = self.data[2:]
		i = 0
		while i < self.dlugosc_nazwy_pokoju:
			self.nazwa_pokoju += unpack('!s', self.data[:1])[0]
			self.data = self.data[1:]
			i +=1
		return self.tresc_odb

	def czytaj_userliste(self):			#Jeszcze nie działa - do zrobienia!!!
		self.il_userow = (self.ile_str)/2
		self.data = self.data[8:]
		i = 0
		return self.il_userow



user = ''
pwd = ''
pokoj = ''
referrer = ''
serwer = 's1.polchat.pl'
konfig = 'nlst=1&nnum=1&jlmsg=true&ignprv=false'
klient = 'KKlient'
port = 14003


s = socket(AF_INET, SOCK_STREAM)
s.connect((serwer, port))
pakiet = BudujPakieta(s, user, pwd, pokoj, referrer, serwer, konfig, klient)
pakiet.login()
f = open('log.html', 'w')
f.write ('<head><meta http-equiv="Content-Type" content="text/html;charset=utf-8"></head>')
f.close()

class Wysylanie(threading.Thread):

	def run(self):
1.
		Odbieranie().start()
		pakiet.tresc = raw_input()
		pakiet.wyslij()


class Odbieranie(threading.Thread):

	def run(self):
1.
			try:
				data_odb = s.recv(1024)
				o = OdbierzPakieta(data_odb)
				ajdi = o.czytaj_naglowek()
				if ajdi == 1: pakiet.pong()



				if ajdi == 610:
					tresc_o = o.czytaj_tresc()
					f = open('log.html', 'a')
					f.write(tresc_o + '<br>')
					f.close()
					print tresc_o


			except:
				s.close()
				f = open('log.html', 'a')
				f.write('<b>***ROZŁĄCZYŁO***</b><br>')
				f.close()
				try:
					s.connect((serwer, port))
					pakiet.login()
				except: pass



\
Wysylanie().start()
Odbieranie().start()