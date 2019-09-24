

# Desenvolvido pela IDrick .Inc



import time
import random
import socket
import os
import requests
import threading
import hashlib
import string




##### Funções >>>>>


# Testar host ON/OFF
def ping():
	host = input("\n[#] Host >> ")
	response = os.system("ping -c 1 " +  host)
	print ("\n")
	if response == 0:
		fff = "\033[32m ✓ \033[0;0m"
		print (fff, host, "está online.\n")
	else:
		fff = "\033[31m X \033[0;0m"
		print (fff, host, "está offline ou inacessível.\n")
	
	
# Capturar IP
def cap_ip():
	try:
		ent = input("\n[#] Host >> ")
		ip = socket.gethostbyname(ent)
		ip = "\033[32m" + ip + "\033[0;0m"
		capt = ("\nIP:")
		print (capt, ip)
	except:
		print("\nComando inválido.")
	


# Testar porta especifica
def porth():
    try:
    	host = input("\n[#] Host >> ")
    	port = int(input("[#] Porta >> "))
    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	if sock.connect_ex((host,port)):
    		str = "\033[31mestá fechada. \033[0;0m"
    		print ("\nPorta", port, str)
    	else:
    		str = "\033[32mestá aberta. \033[0;0m"
    		print ("\nPorta", port, str)
    except:
    	print("\nComando inválido.")

# Localizador de IP
def geo_ip():
	
	inp = input("\n[#] Host >> ")
	host = "http://api.db-ip.com/v2/free/" + inp
	r = requests.get(host)
	r = r.text
	print ("\n", r, "\n")


# Capturar Banner
def cap_ban():
	try:
		host = input("\n[#] Host >> ")
		porta = int(input("[#] Porta >> "))
		s = socket.socket()
		s.settimeout(3)
		s.connect((host, porta))
		rf = s.recv(1030)
		print ("\033[32m" + "\nBanner capturado" + "/033[0;0m", rf, "\n")
	except:
		print("\nErro: protocolo / porta ou host inacessível.")
	




#    MFR-5
def mfr5():
	
	print("\033[32m","\n\n\n             [ • ] Monitor de flutuação remota 5\n\n\n", "\033[0;0m")
	
	print("\n[1] Monitoramento livre (definir n° de pacotes)")
	print("[2] Monitoramento 2 etapas (gera comparações)")
	print("[3] Fechar execução")
	
	print("\n\nEscolha um metodo:\n")
	
	xfg = True
	while xfg == True:
		
		imp = input("\n\n[#] >> ")

		
		# ------------------ FUNÇÃO 1 --------
		if imp == "1":
			
			print("\n\n[ + ]", "\033[33m", "Monitoramento livre\n", "\033[0;0m")
			
			try:
				host = input("\n[#] Host >> ")
				porta = int(input("[#] Porta >> "))
				npa = int(input("[#] N° de pacotes >> "))
				print("\n")
				sta = time.monotonic()
				xx = 0
				x = True
				list = []
				while x == True:
					xx += 1
					localtime = time.asctime( time.localtime(time.time()) )
					start = time.monotonic()
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.connect((host, porta))
					segx =  (localtime[10: -5])
					end = time.monotonic()
					tp = ('{:>9.2f}'.format(end - start))
					tp = str(tp)
					tp = tp.replace(" ", "")
					tx = float(tp)
					
					if xx == 1:
						print("\n")
						zc = tp
						zc = zc.replace(' ', '')
						zc = float(zc)
					else:
						if tx < 0.5:
							print("Variação:", "\033[32m" + tp + "\033[0;0m", "   tmp:", segx, "N:", xx)
						elif tx > 1.0:
							print ("Variação:", "\033[33m", tp, "\033[0;0m", "   tmp:", segx, "N:", xx)
					
					if xx != 1:
						list.append(tp)
						toi = npa
						
						zeta = 0
						for xv in list:
							if max(list) == xv:
								zeta += 1
								
						zeta1 = 0
						for xr in list:
							if min(list) == xr:
								zeta1 += 1
						
						if xx == npa:
							x = False
							sto = time.monotonic()
							txc = ('{:>9.2f}'.format(sto - sta))
							txc = txc.replace(' ', '')
							txd = float(txc)
							med = txd / toi
							med = str(med)
							med = med[:7]
							text = txd - zc
							text = str(text)
							text = text[:5]
							flutu = (float(max(list)) - float(min(list)))
							flutu = str(flutu)
							flutu = flutu[:8]
							flutu = float(flutu)
							ocs = flutu * 100
							print ("\033[33m","\n\n\n[#] RELATORIO:", "\033[0;0m")
							print ("\nMaior tempo de transmissão:", "\033[32m", max(list), "\033[0;0m", "\nN° de taxas iguais:", "\033[32m", zeta, "\033[0;0m", "x", "\033[32m", max(list), "\033[0;0m", "\n","\nMenor tempo de transmissão:", "\033[32m" ,min(list), "\033[0;0m" "\nN° de taxas iguais:","\033[32m" , zeta1, "\033[0;0m", "x", "\033[32m", min(list), "\033[0;0m", "\n\nArea de oscilação:", "\033[32m" , ocs, "\033[0;0m", "%", "\n\nVariavel flutuante:", "\033[32m", flutu, "\033[0;0m", "\nTotal de tempo:", "\033[32m", text, "\033[0;0m", "segundos.", "\nMédia de tempo:", "\033[32m", med, "\033[0;0m", "por pacote")
							
							
			except:
				print("\nComando inválido.")
						
								
		elif imp == "2":
			
			print("\n\n[ + ]", "\033[33m", "Monitoramento 2 Etapas\n", "\033[0;0m")
			
			try:
				host = input("\n[#] Host >> ")
				porta = int(input("[#] Porta >> "))
				npa = 100
				print("\n")
				ay = 0
				
				while ay < 2:
					sta = time.monotonic()
					xx = 0
					x = True
					list = []
					while x == True:
						xx += 1
						localtime = time.asctime( time.localtime(time.time()) )
						start = time.monotonic()
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect((host, porta))
						segx =  (localtime[10: -5])
						end = time.monotonic()
						tp = ('{:>9.2f}'.format(end - start))
						tp = str(tp)
						tp = tp.replace(" ", "")
						tx = float(tp)
						
						if xx == 1:
							print("\n")
							zc = tp
							zc = zc.replace(' ', '')
							zc = float(zc)
						else:
							if tx < 0.5:
								print("Variação:", "\033[32m" + tp + "\033[0;0m", "   tmp:", segx, "N:", xx)
							elif tx > 1.0:
								print ("Variação:", "\033[33m", tp, "\033[0;0m", "   tmp:", segx, "N:", xx)
						
						if xx != 1:
							list.append(tp)
							toi = npa
						
						zeta = 0
						for xv in list:
							if max(list) == xv:
								zeta += 1
						
						zeta1 = 0
						for xr in list:
							if min(list) == xr:
								zeta1 += 1
						
						if xx == npa:
							x = False
							sto = time.monotonic()
							txc = ('{:>9.2f}'.format(sto - sta))
							txc = txc.replace(' ', '')
							txd = float(txc)
							med = txd / toi
							med = str(med)
							med = med[:7]
							text = txd - zc
							text = str(text)
							text = text[:5]
							flutu = (float(max(list)) - float(min(list)))
							flutu = str(flutu)
							flutu = flutu[:8]
							flutu = float(flutu)
							ocs = flutu * 100
							print ("\033[33m","\n\n\n[#] RELATORIO:", "\033[0;0m")
							print ("\nMaior tempo de transmissão:", "\033[32m", max(list), "\033[0;0m", "\nN° de taxas iguais:", "\033[32m", zeta, "\033[0;0m", "x", "\033[32m", max(list), "\033[0;0m", "\n","\nMenor tempo de transmissão:", "\033[32m" ,min(list), "\033[0;0m" "\nN° de taxas iguais:","\033[32m" , zeta1, "\033[0;0m", "x", "\033[32m", min(list), "\033[0;0m", "\n\nArea de oscilação:", "\033[32m" , ocs, "\033[0;0m", "%", "\n\nVariavel flutuante:", "\033[32m", flutu, "\033[0;0m", "\nTotal de tempo:", "\033[32m", text, "\033[0;0m", "segundos.", "\nMédia de tempo:", "\033[32m", med, "\033[0;0m", "por pacote")
							ay += 1
							if ay == 1:
								max1 = max(list)
								zet1 = zeta
								min1 = min(list)
								zet2 = zeta1
								aro1 = ocs
								tempo1 = text
								med1 = med
								
								osc1= ocs
								
								orc1 = str(osc1)
								orc1 = orc1[:9]
								orc1 = float(orc1)
								med_env1 = float(med)
							
							if ay == 2:
								max2 = max(list)
								zet3 = zeta
								min2 = min(list)
								zet4 = zeta1
								aro2 = ocs
								tempo2 = text
								med2 = med
								osc2 = ocs
								orc2 = str(osc2)
								orc2 = orc2[:9]
								orc2 = float(orc2)
								med_env2= float(med)
							
							if ay == 2:
								print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
								print("\n\n[#] RELATORIO: 1")
								print("\nTeste 1°:\n", "\nMaior tempo de transferencia:",  "\033[32m", max1,  "\033[0;0m","\nN° de ocorrencias:",  "\033[32m", zet1,  "\033[0;0m", "\nMenor tempo de transferencia:",  "\033[32m", min1,  "\033[0;0m", "\nN° de ocorrencias:",  "\033[32m",zet2,  "\033[0;0m", "\nArea de oscilação:", "\033[32m", osc1, "\033[0;0m", "%", "\nTempo:",  "\033[32m", tempo1,  "\033[0;0m", "\nMedia de tempo por pacote:",  "\033[32m", med1,  "\033[0;0m")
								print("\n\n[#] RELATORIO: 2")
								print("\nTeste 2°:\n", "\nMaior tempo de transferencia:",  "\033[32m", max2,  "\033[0;0m","\nN° de ocorrencias:",  "\033[32m", zet3,  "\033[0;0m", "\nMenor tempo de transferencia:",  "\033[32m", min2,  "\033[0;0m", "\nN° de ocorrencias:",  "\033[32m",zet4,  "\033[0;0m", "\nArea de oscilação:", "\033[32m", osc2, "\033[0;0m", "%", "\nTempo:", "\033[32m", tempo2,  "\033[0;0m", "\nMedia de tempo por pacote:",  "\033[32m", med2,  "\033[0;0m")
								print ("\033[33m","\n\n[#] COMPARAÇÃO:", "\033[0;0m")
								
								if max1 > max2:
									maior = "TESTE 1 > " + max1
									maior = maior.replace("-", "")
								elif max2 > max1:
									maior = "TESTE 2 > " + max2
									maior = maior.replace("-", "")
								else:
									maior = "TESTE 1 E 2 IGUAIS"
								
								if orc1 > orc2:
									dif = orc1 - orc2
									dif = str(dif)
									dif = dif.replace(" ", "")
									dif = dif + "%"
									orcz1 = str(orc1)
									maior_o = "TESTE 1 > " + orcz1
									task = "TESTE 2"
								
								elif orc2 > orc1:
									dif = orc2 - orc1
									dif = str(dif)
									dif = dif.replace(" ", "")
									dif = dif + "%"
									orcz2 = str(orc2)
									maior_o = "TESTE 2 > " + orcz2
									task = "TESTE 1"
								else:
									maior_o = "TESTE 1 E 2 IGUAIS"
									dif = "TESTE 1 E 2 IGUAIS"
									task = "NULO"
								
								if med_env1 > med_env2:
									med_a = med_env1
									dt = med_env1 - med_env2
									dt = str(dt)
									dt = dt.replace(" ", "")
									taske = "TESTE 2"
								else:
									med_a = med_env2
									dt = med_env2 - med_env1
									dt = str(dt)
									dt = dt.replace(" ", "")
									taske = "TESTE 1"
								
								if tempo1 > tempo2:
									temp1 = float(tempo1)
									temp2 = float(tempo2)
									ert = temp1 - temp2
									temp1 = str(tempo1)
									temp2 = str(tempo2)
									maior_t = "TESTE 1 > " + temp1
									atq = "TESTE 2"
								elif tempo2 > tempo1:
									temp1 = float(tempo1)
									temp2 = float(tempo2)
									ert = temp2 - temp1
									temp1 = str(tempo1)
									temp2 = str(tempo2)
									maior_t = "TESTE 2 > " + temp2
									atq = "TESTE 1"
								
								else:
									ert = "TESTE 1 E 2 IGUAIS"
									atq = "NULO"
								
								print("\nMaior tempo de transferencia por pacote:", "\033[32m", maior, "\033[0;0m", "\nMaior area de oscilação:", "\033[32m", maior_o, "%", "\033[0;0m", "\nDiferença de area:", "\033[32m+", dif, "\033[0;0m", "!=", "\033[32m", task, "\033[0;0m", "\nMaior tempo total:", "\033[32m", maior_t, "\033[0;0m", "\nDiferença de:", "\033[32m", "+", ert, "\033[0;0m", "!=", "\033[32m", atq, "\033[0;0m","\nOscilação por pacote:", "\033[32m", "+", dt, "\033[0;0m", "!=", "\033[32m", taske, "\033[0;0m")
			except:
				print("\nComando Inválido.")
							
		elif imp == "3":
			xfg = False
			print("\nMFR ENCERRADO.")





# Extrator de Links - ELINK

def link_extrator():
	
	print("\n                 [ • ] Extrator de links\n\n")
	host = input("[#] Host >> ")
	link1 = []
	host = "http://" + host
	response = requests.get(host)
	content = str(response.content)
	content = content.split(" ")
	cont = 0
	
	for n in content:
		if "http://"  in n:
			n = n
			if 'href="' in n:
				n1 = n.replace('href="', '')
				link1.append(n1)
				cont += 1
		if "https://"  in n:
			n = n
			if 'href="' in n:
				n2 = n.replace('href="', '')
				link1.append(n2)
				cont += 1
	
	
	print("\n\n\n")
	nn1 = 0
	linkz = []
	for link in link1:
		nn1 += 1
		g = 0
			
		for letra in link:
			g += 1
			if '"' in letra:
				nn = g
				nn = nn - 1
				final = (link[:nn])
				print("\n", final, "\n")
				linkz.append(final)
	print ("\n\n", len(link1), "links indexados.\n\n\n")






# Scanner de Portas:
	
# UPGRADE DESSE SCANNER ×××××××××××××× • 

def port_scan():
	print("\n     ____SCANNER DE PORTAS____\n")
	
	
	host = input("[#] Host >> ")
	portas = [20, 21, 22, 23, 25, 53, 67, 68, 80, 110, 123, 143, 156, 161, 179, 443, 1723, 3128, 3389]
	print("\n")
	xz = ""
	for ports in portas:
		if ports == 20:
			x = "• FTP"
		if ports == 21:
			x = "• FTP"
		if ports == 22:
			x = "• SSH"
		if ports == 23:
			x = "• TELNET"
		if ports == 25:
			x = "• SMTP"
		if ports == 53:
			x = "• DNS"
		if ports == 67:
			x = "• DHCP SRV"
		if ports == 68:
			x = "• DHCP CLI"
		if ports == 80:
			x = "• HTTP"
		if ports == 110:
			x = "- POP3"
		if ports == 123:
			x = "- NTP"
		if ports == 143:
			x = "- IMAP4"
		if ports == 156:
			x = "- SQL"
		if ports == 161:
			x = "- SNMP"
		if ports == 179:
			x = "- BGP"
		if ports == 443:
			x = "- HTTPS"
		if ports == 1723:
			x = "+ PPTP"
		if ports == 3128:
			x = "+ SQUID"
		if ports == 3389:
			x = "+ TERMINAL SERVER"
		
			
			
		print ("TESTANDO: ", ports, "\033[33m         ", x,"\033[0;0m")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.4)
		if s.connect_ex((host, ports)) == 0:
			print ("PORTA", ports, "\033[32m", "ABERTA", "\033[0;0m")
			s.close()





# Criptografia Nosrednaw (NRW)

def nrw():
	str1 = "\033[33m" + "Nosrednaw" + "\033[0;0m"
	print("\n\n\n                Criptografia - (", str1, ")")
	str2 = "\033[32m" + "1" + "\033[0;0m"
	str3 = "\033[32m" + "2" + "\033[0;0m"
	str4 = "\033[32m" + "3" + "\033[0;0m"
	
	print("\n\n\n[", str2, "] Criptografar")
	print("[", str3, "] Descriptografar")
	print ("[", str4, "] Sair")
	zz = True
	while zz == True:
		ent = int(input("\n\n\n >> "))
		
		if ent == 1:
			cript = input("\n\nDigite a info a ser encriptada: ")
			
			chave = input("Chave: ")
			ee = chave[-4:]
			ee = int(ee)
			chave = int(chave)


			a = 101 * ee * chave
			b = 102 * ee * chave
			c = 103 * ee * chave
			d = 104 * ee * chave
			e = 105 * ee * chave
			f  = 106 * ee * chave
			g = 107 * ee * chave
			h = 108 * ee * chave
			i = 109 * ee * chave
			j = 110 * ee * chave
			k = 111 * ee * chave
			l = 112 * ee * chave
			m = 113 * ee * chave
			n = 114 * ee * chave
			o = 115 * ee * chave
			p = 116 * ee * chave
			q = 117 * ee * chave
			r = 118 * ee * chave
			s = 119 * ee * chave
			t = 120 * ee * chave
			u = 121 * ee * chave
			v = 122 * ee * chave
			w = 123 * ee * chave
			x = 124 * ee * chave
			y = 125 * ee * chave
			z = 126 * ee * chave
			
			A = 201 * ee * chave
			B = 202 * ee * chave
			C = 203 * ee * chave
			D  = 204 * ee * chave
			E = 205 * ee * chave
			F  = 206 * ee * chave
			G = 207 * ee * chave
			H = 208 * ee * chave
			I = 209 * ee * chave
			J = 210 * ee * chave
			K = 211 * ee * chave
			L = 212 * ee * chave
			M = 213 * ee * chave
			N = 214 * ee * chave
			O = 215 * ee * chave
			P = 216 * ee * chave
			Q = 217 * ee * chave
			R = 218 * ee * chave
			S = 219 * ee * chave
			T = 220 * ee * chave
			U = 221 * ee * chave
			V = 222 * ee * chave
			W = 223 * ee * chave
			X = 224 * ee * chave
			Y = 225 * ee * chave
			Z = 226 * ee * chave
			
			AA = 300 * ee * chave
			BB = 301 * ee * chave
			CC = 302 * ee * chave
			DD = 303 * ee * chave
			EE = 304 * ee * chave
			FF = 305 * ee * chave
			GG = 306 * ee * chave
			HH = 307 * ee * chave
			II = 308 * ee * chave
			JJ = 309 * ee * chave
			
			list = []
			
			for key in cript:
				if key == 'a':
					list.append(a)
				elif key == 'b':
					list.append (b)
				elif key == 'c':
					list.append (c)
				elif key == 'd':
					list.append (d)
				elif key == 'e':
					list.append (e)
				elif key == 'f':
					list.append (f)
				elif key == 'g':
					list.append (g)
				elif key == 'h':
					list.append (h)
				elif key == 'i':
					list.append (i)
				elif key == 'j':
					list.append (j)
				elif key == 'k':
					list.append (k)
				elif key == 'l':
					list.append (l)
				elif key == 'm':
					list.append (m)
				elif key == 'n':
					list.append (n)
				elif key == 'o':
					list.append (o)
				elif key == 'p':
					list.append (p)
				elif key == 'q':
					list.append (q)
				elif key == 'r':
					list.append (r)
				elif key == 's':
					list.append (s)
				elif key == 't':
					list.append (t)
				elif key == 'u':
					list.append (u)
				elif key == 'v':
					list.append (v)
				elif key == 'w':
					list.append (w)
				elif key == 'x':
					list.append (x)
				elif key == 'y':
					list.append (y)
				elif key == 'z':
					list.append (z)
				
				elif key == 'A':
					list.append (A)
				elif key == 'B':
					list.append (B)
				elif key == 'C':
					list.append (C)
				elif key == 'D':
					list.append (D)
				elif key == 'E':
					list.append (E)
				elif key == 'F':
					list.append (F)
				elif key == 'G':
					list.append (G)
				elif key == 'H':
					list.append (H)
				elif key == 'I':
					list.append (I)
				elif key == 'J':
					list.append (J)
				elif key == 'K':
					list.append (K)
				elif key == 'L':
					list.append (L)
				elif key == 'M':
					list.append (M)
				elif key == 'N':
					list.append (N)
				elif key == 'O':
					list.append (O)
				elif key == 'P':
					list.append (P)
				elif key == 'Q':
					list.append (Q)
				elif key == 'R':
					list.append (R)
				elif key == 'S':
					list.append (S)
				elif key == 'T':
					list.append (T)
				elif key == 'U':
					list.append (U)
				elif key == 'V':
					list.append (V)
				elif key == 'W':
					list.append (W)
				elif key == 'X':
					list.append (X)
				elif key == 'Y':
					list.append (Y)
				elif key == 'Z':
					list.append (Z)
				
				
				elif key == "0":
					list.append (AA)
				elif key == "1":
					list.append (BB)
				elif key == "2":
					list.append (CC)
				elif key == "3":
					list.append (DD)
				elif key == "4":
					list.append (EE)
				elif key == "5":
					list.append (FF)
				elif key == "6":
					list.append (GG)
				elif key == "7":
					list.append (HH)
				elif key == "8":
					list.append (II)
				elif key == "9":
					list.append (JJ)
				
				elif key == ".":
					list.append ("...")
				elif key == ",":
					list.append (",")
				elif key == "?":
					list.append ("?")
				elif key == "%":
					list.append ("%")
				elif key == "-":
					list.append ("-")
				elif key == "!":
					list.append ("!")
				elif key == " ":
					list.append (" ")
				elif key == "=":
					list.append ("=")
				elif key == "+":
					list.append ("+")
				elif key == "*":
					list.append ("*")
				elif key == ":":
					list.append (":")
				elif key == "_":
					list.append ("_")
				elif key == "(":
					list.append ("(")
				elif key == ")":
					list.append (")")
			
		
			list = str(list)
			list = list.replace(",", "")
			list = list.replace("'", "")
			list = list.replace("   ", " - ")
			list = list[1:-1]
			msg = ("\n\nInfo criptografada:\n\n\n\n")
			print (msg, "\033[32m", list, "\033[0;0m")
			
			
		elif ent == 2:
			
			list = []
			key = input("\n\nInsira o conteudo: ")
			chave = int(input("Chave: "))
			zx = str(chave)
			ee = zx[-4:]
			ee = int(ee)
			key = key.split(" ")
			print ("\n")
			
			for linha in key:
				if "0" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "1" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "2" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "3" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "4" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "5" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "6" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "7" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "8" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				elif "9" in linha:
					linha = int(linha)
					linha = linha / chave
					linha = linha / ee
				
				elif linha == "-":
					linha = linha
					linha = str(linha)
				
				if linha != "-":
					linha = str(linha)
					linha = linha[:-2]
				
				
				if linha == "101":
					list.append ("a")
				elif linha == "102":
					list.append ("b")
				elif linha == "103":
					list.append ("c")
				elif linha == "104":
					list.append ("d")
				elif linha == "105":
					list.append ("e")
				elif linha == "106":
					list.append ("f")
				elif linha == "107":
					list.append ("g")
				elif linha == "108":
					list.append ("h")
				elif linha == "109":
					list.append ("i")
				elif linha == "110":
					list.append ("j")
				elif linha == "111":
					list.append ("k")
				elif linha == "112":
					list.append ("l")
				elif linha == "113":
					list.append ("m")
				elif linha == "114":
					list.append ("n")
				elif linha == "115":
					list.append ("o")
				elif linha == "116":
					list.append ("p")
				elif linha == "117":
					list.append ("q")
				elif linha == "118":
					list.append ("r")
				elif linha == "119":
					list.append ("s")
				elif linha == "120":
					list.append ("t")
				elif linha == "121":
					list.append ("u")
				elif linha == "122":
					list.append ("v")
				elif linha == "123":
					list.append ("w")
				elif linha == "124":
					list.append ("x")
				elif linha == "125":
					list.append ("y")
				elif linha == "126":
					list.append ("z")
				elif linha == "-":
					list.append("*")
					
				elif linha == "201":
					list.append ("A")
				elif linha == "202":
					list.append ("B")
				elif linha == "203":
					list.append ("C")
				elif linha == "204":
					list.append ("D")
				elif linha == "205":
					list.append ("E")
				elif linha == "206":
					list.append ("F")
				elif linha == "207":
					list.append ("G")
				elif linha == "208":
					list.append ("H")
				elif linha == "209":
					list.append ("I")
				elif linha == "210":
					list.append ("J")
				elif linha == "211":
					list.append ("K")
				elif linha == "212":
					list.append ("L")
				elif linha == "213":
					list.append ("M")
				elif linha == "214":
					list.append ("N")
				elif linha == "215":
					list.append ("O")
				elif linha == "216":
					list.append ("P")
				elif linha == "217":
					list.append ("Q")
				elif linha == "218":
					list.append ("R")
				elif linha == "219":
					list.append ("S")
				elif linha == "220":
					list.append ("T")
				elif linha == "221":
					list.append ("U")
				elif linha == "222":
					list.append ("V")
				elif linha == "223":
					list.append ("W")
				elif linha == "224":
					list.append ("X")
				elif linha == "225":
					list.append ("Y")
				elif linha == "226":
					list.append ("Z")
				
				elif linha == "300":
					list.append ("0")
				elif linha == "301":
					list.append ("1")
				elif linha == "302":
					list.append ("2")
				elif linha == "303":
					list.append ("3")
				elif linha == "304":
					list.append ("4")
				elif linha == "305":
					list.append ("5")
				elif linha == "306":
					list.append ("6")
				elif linha == "307":
					list.append ("7")
				elif linha == "308":
					list.append ("8")
				elif linha == "309":
					list.append ("9")
				elif linha == ".":
					list.append (".")
				elif linha == ",":
					list.append (",")
				elif linha == "?":
					list.append ("?")
				elif linha == "%":
					list.append ("%")
				elif linha == "-":
					list.append ("-")
				elif linha == "!":
					list.append ("!")
				elif linha == " ":
					list.append (" ")
				elif linha == "=":
					list.append ("=")
				elif linha == "+":
					list.append ("+")
				elif linha == "*":
					list.append ("*")
				elif linha == ":":
					list.append (":")
				elif linha == "_":
					list.append ("_")
				elif linha == "(":
					list.append ("(")
				elif linha == ")":
					list.append (")")
			
			
			msg = ("\nDecodificado:\n\n")
			final = str(list)
			final = final.replace(",", "")
			final = final.replace("[", "")
			final = final.replace("]", "")
			final = final.replace("'", "")
			final = final.replace(" ", "")
			final = final.replace("*", " ")
			print (msg, "\033[32m", final, "\033[0;0m")
			
		elif ent == 3:
			print("\nPROGRAMA ENCERRADO.")
			zz = False



# Criptografia AGUIAR-4

def a4():
	print("\n\n                   CRIPTOGRAFIA AGUIAR-4\n\n")
	print("[1] Criptografar\n[2] Descriptografar\n[3] Sair")
	abc = True
	while abc == True:
		z = True
		while z == True:
			
			imp = int(input("\n >> "))
						
			if imp == 1:
				info = input("\nInfo: ")
				ent = int(input("\n\nN° Alfabeto: "))
				chave = int(input("Chave: "))
				print("\n")
				z1 = str(ent)
				z2 = str(chave)
				z3 = z1 + z2 
				z3 = int(z3)
				
				list1 = []
				for i in info:
					
					if i == "a":
						a = ent * chave ** z3 * 10
						list1.append(a)
					elif i == "b":
						b = ent * chave ** z3 * 11
						list1.append(b)
					elif i == "c":
						c = ent * chave ** z3 * 12
						list1.append(c)
					elif i == "d":
						d = ent * chave ** z3 * 13
						list1.append(d)
					elif i == "e":
						e = ent * chave ** z3 * 14
						list1.append(e)
					elif i == "f":
						f = ent * chave ** z3 * 15
						list1.append(f)
					elif i == "g":
						g = ent * chave ** z3 * 16
						list1.append(g)
					elif i == "h":
						h = ent * chave ** z3 * 17
						list1.append(h)
					elif i == "i":
						i = ent * chave ** z3 * 18
						list1.append(i)
					elif i == "j":
						j = ent * chave ** z3 * 19
						list1.append(j)
					elif i == "k":
						k = ent * chave ** z3 * 20
						list1.append(k)
					elif i == "l":
						l = ent * chave ** z3 * 21
						list1.append(l)
					elif i == "m":
						m = ent * chave ** z3 * 22
						list1.append(m)
					elif i == "n":
						n = ent * chave ** z3 * 23
						list1.append(n)
					elif i == "o":
						o = ent * chave ** z3 * 24
						list1.append(o)
					elif i == "p":
						p = ent * chave ** z3 * 25
						list1.append(p)
					elif i == "q":
						q = ent * chave ** z3 * 26
						list1.append(q)
					elif i == "r":
						r = ent * chave ** z3 * 27
						list1.append(r)
					elif i == "s":
						s = ent * chave ** z3 * 28
						list1.append(s)
					elif i == "t":
						t = ent * chave ** z3 * 29
						list1.append(t)
					elif i == "u":
						u = ent * chave ** z3 * 30
						list1.append(u)
					elif i == "v":
						v = ent * chave ** z3 * 31
						list1.append(v)
					elif i == "w":
						w = ent * chave ** z3 * 32
						list1.append(w)
					elif i == "x":
						x = ent * chave ** z3 * 33
						list1.append(x)
					elif i == "y":
						y = ent * chave ** z3 * 34
						list1.append(y)
					elif i == "z":
						z = ent * chave ** z3 * 35
						list1.append(z)
					elif i == " ":
						list1.append("-")
						
				list1 = str(list1)
				list1 = list1.replace("[", "")
				list1 = list1.replace("]", "")
				list1 = list1.replace(",", "")
				list1 = list1.replace(",", "")
				list1 = list1.replace("'", "")
				print("\nENCRIPTADO:  ", list1)
				z = False
            			
			if imp == 2:
				listf = []
				cod = input("\nInfo a decifrar: ")
				cod = cod.split(" ")
				print ("\n")
				ent1 = int(input("\nN° Afabeto: "))
				chave1 = int(input("Chave: "))
				
				z1 = str(ent1)
				z2 = str(chave1)
				z3 = z1 + z2
				z3 = int(z3)
				
				aa = ent1 * chave1 ** z3 * 10
				bb = ent1 * chave1 ** z3 * 11
				cc = ent1 * chave1 ** z3 * 12
				dd = ent1 * chave1 ** z3 * 13
				ee = ent1 * chave1 ** z3 * 14
				ff = ent1 * chave1 ** z3 * 15
				gg = ent1 * chave1 ** z3 * 16
				hh = ent1 * chave1 ** z3 * 17
				ii = ent1 * chave1 ** z3 * 18
				jj = ent1 * chave1 ** z3 * 19
				kk = ent1 * chave1 ** z3 * 20
				ll = ent1 * chave1 ** z3 * 21
				mm = ent1 * chave1 ** z3 * 22
				nn = ent1 * chave1 ** z3 * 23
				oo = ent1 * chave1 ** z3 * 24
				pp = ent1 * chave1 ** z3 * 25
				qq = ent1 * chave1 ** z3 * 26
				rr = ent1 * chave1 ** z3 * 27
				ss = ent1 * chave1 ** z3 * 28
				tt = ent1 * chave1 ** z3 * 29
				uu = ent1 * chave1 ** z3 * 30
				vv = ent1 * chave1 ** z3 * 31
				ww = ent1 * chave1 ** z3 * 32
				xx = ent1 * chave1 ** z3 * 33
				yy = ent1 * chave1 ** z3 * 34
				zz = ent1 * chave1 ** z3 * 35
				
				list2 = []
				for n in cod:
					n = int(n)
					if n == aa:
						list2.append("a")
					elif n == bb:
						list2.append("b")
					elif n == cc:
						list2.append("c")
					elif n == dd:
						list2.append("d")
					elif n == ee:
						list2.append("e")
					elif n == ff:
						list2.append("f")
					elif n == gg:
						list2.append("g")
					elif n == hh:
						list2.append("h")
					elif n == ii:
						list2.append("i")
					elif n == jj:
						list2.append("j")
					elif n == kk:
						list2.append("k")
					elif n == ll:
						list2.append("l")
					elif n == mm:
						list2.append("m")
					elif n == nn:
						list2.append("n")
					elif n == oo:
						list2.append("o")
					elif n == pp:
						list2.append("p")
					elif n == qq:
						list2.append("q")
					elif n == rr:
						list2.append("r")
					elif n == ss:
						list2.append("s")
					elif n == tt:
						list2.append("t")
					elif n == uu:
						list2.append("u")
					elif n == vv:
						list2.append("v")
					elif n == ww:
						list2.append("w")
					elif n == xx:
						list2.append("x")
					elif n == yy:
						list2.append("y")
					elif n == zz:
						list2.append("z")
					elif n == " ":
						list2.append("-")
				
				list2 = str(list2)
				list2 = list2.replace("[", "")
				list2 = list2.replace("]", "")
				list2 = list2.replace(",", "")
				list2 = list2.replace(",", "")
				list2 = list2.replace("'", "")
				list2 = list2.replace(" ", "")
				list2 = list2.replace("-", " ")
				print("\n\nDECRIPTADO: ", list2)
			
			if imp == 3:
				print("\n\nPROGRAMA ENCERRADO.\n")
				z = False
				abc = False
				

def gmax():
	print("\n   >>>> GMAX (GERADOR DE NÚMEROS RANDÔMICOS)")
	try:
		inp = input("\n\nQuantos numeros?: ")
		print("\n")
		inp = int(inp)
		ip = 0
		while ip < inp:
			a = (random.randint(21,27))
			b = (random.randint(992,999))
			c = (random.randint(100,999))
			d = (random.randint(100,999))
			ip += 1
			soma = [a,b,c,d]
			soma = str(soma)
			msg = (' telelefone N°:')
			nume = soma.replace(",", "")
			nume = nume.replace(' ', '')
			nume = nume[1:-1]
			xtc = "\033[33m" + nume + "\033[0;0m"
			print (xtc, msg, ip)
			
	except:
		print("\nComando Inválido.")










###################################










nomep = "\033[33m" + "DRICK FRAMEWORK [1.0]" "\033[0;0m"

print("\n\n#######  #######  ####   ##############      ###    ##   #")
print ("###########  ", nomep, "#### ###  ##### ####")
print("##### ####  #######   ## #### #######     ##      ####  ### \n\n")



ma = (random.randint(1, 14))
listag = [" ","Na verdade oque vale a pena?", "Não compre terrenos na lua.", "Use o MFR para calcular o número de dispositivos nescessários para derrubar uma rede.", "Vagabundo vai mais longe que a Nasa.", "Use o camando /limpar.", "O problema do ano 2038 (também conhecido como Y2K38, em referência ao Y2K) é uma falha na representação de datas em computadores, que pode causar erros em alguns programas de computador no ano de 2038.", "Obrigado pela preferência.", "Em 2038, às 3 horas, 14 minutos e 5 segundos de 19 de março, os computadores que estiverem usando sistemas de 32-bit não conseguirão lidar com a mudança de data, pois terão atingido seu limite máximo de contagem.", "Proxímos desenvolvedores atualizem o status sobre o bug de 2038 lá em 2038.", "Use o Hórus para adquirir endereços ip com determinados serviços e versões na rede.", "HÓRUS - PROGRAMA DE RASTREAMENTO E DETECÇÃO DE DISPOSITIVOS VULNERAVEIS.", "Use o indicativo (Oscilação por pacote) do NRW para calcular quantos dispositivos são nescessarios para causar um delay significativo no HOST em um ataque DDOS, por exemplo, 0.00470000000000001 * 1500 = 7.050000000000015. Aonde 1500 seria o número de dispositivos 7.050000000000015 segundos é o delay por pacote causado."]

fgh = "\033[31m" + "[+]" + "\033[0;0m"

if ma == 1:
	print(fgh, listag[1])
elif ma == 2:
	print(fgh, listag[2])
elif ma == 3:
	print(fgh, listag[3])
elif ma == 4:
	print(fgh, listag[4])
elif ma == 5:
	print(fgh, listag[5])
elif ma == 6:
	print(fgh, listag[6])
elif ma == 7:
	print(fgh, listag[7])
elif ma == 8:
	print(fgh, listag[8])
elif ma == 9:
	print(fgh, listag[9])
elif ma == 10:
	print(fgh, listag[10])
elif ma == 11:
	print(fgh,listag[11])
elif ma == 12:
	print(fgh,listag[12])
elif ma == 13:
	print(fgh,listag[13])
	
	
	
	
strr = "\033[32m" + "[+]" + "\033[0;0m"

print("\n")
print(" ", strr ,"Use (/c) para listar os comandos.")
print(" ", strr, "Use (/info) para mais informações.\n\n\n\n")







##########################







x = True

while x == True:
	
	y = input("\n\n[\033[33m#\033[0;0m] > ")
	
	# Comando para fechar o programa
	if y == "/sair":		
		x = False
	
	# Trata entradas direras
	elif y[0] == "!":
		teste = y.replace(" ", ",")
		print(teste)
		
	
	
		
	elif y == "/c":
		print("\n\n\nPARA USAR UMA FERRAMENTA UTILIZE O COMANDO ENTRE PARENTESES.\n \n\n[#] COMANDOS USUAIS:\n\nPing Host                               (\033[32mping\033[0;0m)\nCapturar IP                             (\033[32mcap ip\033[0;0m)\nTestar porta                            (\033[32mtporta\033[0;0m)\nCapturar banner                         (\033[32mcbanner\033[0;0m)\nLocalizar IP                            (\033[32mlocalizar ip\033[0;0m)\nGmax gerador                            (\033[32mgmax\033[0;0m)\nMonitor de flutuação remota             (\033[32mmfr5\033[0;0m)\nExtrator de Links                       (\033[32melink\033[0;0m)\nRetornar codigo-fonte                   (\033[32mcfonte\033[0;0m)\nEscaner de Portas                       (\033[32mpscan\033[0;0m)\nCriptografia Nosrednaw                  (\033[32mnrw\033[0;0m)\nCriptografia Aguiar 4                   (\033[32ma4\033[0;0m)")
		print("\n\n[#] Funções HASH")
		print("\nEncriptar em MD5                        (\033[32mmd5\033[0;0m)\nEncriptar em SHA-1                      (\033[32msha1\033[0;0m)\nEncriptar em SHA-224                    (\033[32msha224\033[0;0m)\nEncriptar em SHA-256                    (\033[32msha256\033[0;0m)\nEncriptar em SHA-384                    (\033[32msha384\033[0;0m)\nEncriptar em SHA-512                    (\033[32msha512\033[0;0m)")

	
		
		
				
	elif y == "/info":
		print("\n\n                      \033[32mDRICK FRAMEWORK\033[0;0m")
		print("\n O software (Drick Framework) é um pacote com vários algoritimos essênciais para um bom pentesting e uma boa análise de um sistema ou rede, o nosso software busca sempre agrupar as melhores alternativas para uma boa análise e uma rede de testes. Foi desenvolvido pela iDrick que tem como dono e fundador Wandrew Tischler que também é conhecido como Drick um apelido que sua mãe deu na infância, agora trabalhamos constantemente não só neste programa mas também em outros afim de resolver os problemas de pessoas comuns com o eu e você.\n")
		print("\n\n                    \033[32mCOMANDOS ADICIONAIS\033[0;0m")
		print("\n1 - Caso queira consultar alguma informação a respeito de algum programa da plataforma use o comando (/info) + Programa, por exemplo (/info ping), este comando retornará as principais informações sobre o mesmo.\n\n2 - Caso deseje fechar a framework utilize o comando (/sair)\n\n3 - Utilize o comando (/limpar) para limpar a tela.")
		
		
		
		
		
		
		
	#requisitar informações de determinadas funções
	
	elif y == "/info ping":
		print("\n\033[32m PING\n\033[0;0m\nPING é um algoritimo usado para testar uma máquina remota afim de determinar se ela está online ou offline e obter dados de sua requisição como tempo de resposta.")
	
	elif y == "/info cap ip":
		print("\n\033[32m CAP IP (CAPTURAR IP)\n\033[0;0m\nCAP IP tem como função obter o endereço remoto de uma determinada máquina na rede, o algoritimo captura o ip (Internet Protocol) através de uma requisição.")
	
	elif y == "/info tporta":
		print("\n\033[32m TPORTA (TESTAR PORTA)\n\033[0;0m\nTPORTA é um testador de porta específica nativo da plataforma, basicamente ele testa se uma determinada porta de um dispositivo na rede está aberta ou fechada.")
	
	elif y == "/info localizar ip":
		print("\n\033[32m LOCALIZAR IP\n\033[0;0m\nEsta função lhe permite rastrear um dispositivo e obter características de sua localização.")
	
	elif y == "/info cbanner":
			print("\n\033[32m CBANNER (CAPTURAR BANNER)\n\033[0;0m\nApartir de requisições ao alvo é possível obter o serviço e sua versão que está a rodar em uma determinada porta com esta informação é possível obter um exploit.")
		
	elif y == "/info mfr5":
			print("\n\033[32m MFR5 (Monitor de Flutuação Remota)\n\033[0;0m\nCom este algoritimo é possível enviar requisições para um determinado dispositivo na rede de computadores e compreender melhor como funciona sua rede e quão eficiente ela pode ser.\nFocado na parte de transmissão de dados o MFR pode detectar variações muito pequenas e importantes em um determinado host, variações essas que podem ser usadas em simulações para prever a integridade de uma rede dado um futuro evento.")
		
	elif y == "/info elink":
		print("\n\033[32m ELINK (Extraidor de Link)\n\033[0;0m\nEsse algoritimo tem como função extrair links de uma determinada página na web.")
	
	elif y == "/info pscan":
		print("\n\033[32m PSCAN (Scanner de Portas)\n\033[0;0m\nPSCAN é um scanner de portas simples que tem o intuito de testar as principais portas de um host e determinar se as mesmas estão abertas ou fechadas.")
	
	elif y == "/info nrw":
		print("\n\033[32m NRW (Criptografia Nosrednaw)\n\033[0;0m\nNosrednaw é uma criptografia desenvolvida pela iDrick que tem a função de tornar a transmissão de informações mais segura de acordo com a capacidade de processamento do dispositivo a cifrar e descifrar a informação.")
		
	elif y == "/info a4":
		print("\n\033[32m A4 (Criptografia Aguiar)\n\033[0;0m\nAguiar é uma criptografia desenvolvida pela iDrick que tem a função de tornar a transmissão de informações mais segura de acordo com a capacidade de processamento do dispositivo a cifrar e descifrar a informação. Segue o mesmo padrão de desenvolvimento da criptografia Nosrednaw, más com mudança na arquitetura criptografica.")
		
	elif y == "/info md5":
			print("\n\033[32m MD5\n\033[0;0m\nO MD5 (Message-Digest algorithm 5) é uma função de dispersão criptográfica (ou função hash criptográfica) de 128 bits unidirecional, por ser um algoritmo unidirecional, uma hash md5 não pode ser transformada novamente no texto que lhe deu origem.")
		
	
	elif y == "/info sha1":
		print("\n\033[32m SHA-1\n\033[0;0m\nEm criptografia, SHA-1 é uma função de dispersão criptográfica (ou função hash criptográfica) projetada pela Agência de Segurança Nacional dos Estados Unidos e é um Padrão Federal de Processamento de Informação dos Estados Unidos publicado pelo Instituto Nacional de Padrões e Tecnologia (NIST).SHA-1 produz um valor de dispersão de 160 bits (20 bytes) conhecido como resumo da mensagem. Um valor de dispersão SHA-1 é normalmente tratado como um número hexadecimal de 40 dígitos.")
	
	elif y == "/info sha224":
		print("\n\033[32m SHA-224\n\033[0;0m\n SHA-224 (224 bits) faz parte do conjunto de funções hash criptográficas SHA-2, desenvolvido pela Agência de Segurança Nacional dos EUA (NSA) e publicado em 2001 pelo NIST como um FIPS (Federal Information Processing Standard) dos EUA. Uma função hash é um algoritmo que transforma (hashes) um conjunto arbitrário de elementos de dados, como um arquivo de texto, em um único valor de tamanho fixo (o hash). O valor do hash computado pode então ser usado para verificar a integridade das cópias dos dados originais sem fornecer meios para derivar os dados originais. Irreversível, um valor de hash pode ser livremente distribuído, armazenado e usado para fins comparativos. SHA significa Secure Hash Algorithm. O SHA-2 inclui um número significativo de alterações em relação ao seu antecessor.")
	
	elif y == "/info cfonte":
		print("\n\033[32m CFONTE\n\033[0;0m\nCFONTE permite-nos fazer requisições de codigo fonte de uma determinada pagina na web.")
		
	elif y == "/info sha256":
		print("\n\033[32m SHA 256\n\033[0;0m\nSHA-256 é usado como parte do processo de autenticação de pacotes de software Debian GNU/Linux e no padrão DKIM de assinatura de mensagens, Várias criptomoedas como Bitcoin usam SHA-256 para verificar transações e calculam a prova-de-trabalho ou prova-de-participação (do inglês, proof of stake). A ascensão de chips aceleradores ASIC SHA-2 tem levado ao uso de esquemas de prova-de-trabalho baseados em scrypt.")
		
	elif y == "/info sha384":
		print("\n\033[32m SHA 384\n\033[0;0m\n SHA-384 é uma função do algoritmo criptográfico Sha-2, evolução de Sha-1 . É a mesma criptografia do Sha-512, exceto que a saída é truncada em 384 bits. Também há diferenças no processo de inicialização. Esta função faz parte do Padrão Federal de Processamento de Informações dos EUA.")
	
	elif y == "/info sha512":
		print('\n\033[32m SHA 512\n\033[0;0m\nSHA-512 é uma função do algoritmo criptográfico Sha-2, que é uma evolução do famoso Sha-1 . O Sha-512 está muito próximo do seu "irmão" Sha-256, exceto pelo uso de "blocos" de 1024 bits e aceita como entrada uma string de comprimento máximo de 2 ^ 128 bits. O Sha-512 também possui outras modificações algorítmicas em comparação com o Sha-256. Essa função criptográfica faz parte do Padrão Federal de Processamento de Informações dos EUA.')
		
		
			
		
	

	
	
	
	# Teste ON/OFF Host
	elif y == "ping":
		ping()
	
	# Capturar IP
	elif y == "cap ip":
		cap_ip()
		
	# Testar porta
	elif y == "tporta":
		porth()
	
	# Localizar IP
	elif y == "localizar ip":
		geo_ip()
	
	# Capturar banner
	elif y == "cbanner":
		cap_ban()
	
	# Monitoramento de Flutuação Remota 5
	elif y == "mfr5":
		mfr5()
		
	# Extrator de links
	elif y == "elink":
		link_extrator()
	
	# Scanner de portas
	elif y == "pscan":
		port_scan()
	
	# Criptografia Nosrednaw
	elif y == "nrw":
		nrw()
		
	# Limpar o console
	elif y == "/limpar":
		a = "           " * 10000
		print(a)
		
		
	# Retorna codigo fonte (WEB)
	elif y == "cfonte":
		print("\nLembre-se do protocolo HTTP / HTTPS.")
		host = input("\n[#] Host>> ")
		print("\n\n")
		r = requests.get(host)
		r = r.text
		print (r, "\n")
		
	# Crptografia A4
	elif y == "a4":
		a4()
	
	# Gmax gerador de número movel
	elif y == "gmax":
		gmax()
	
	
	
	
	
	
	###########  Hashs ##########
	elif y == "sha1":

		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha1(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
		
		
	elif y == "sha224":
		
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha224(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)

		
	elif y == "sha256":
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha256(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
				
		
	elif y == "sha384":
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha384(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
		
	elif y == "sha512":
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.sha512(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
	
	elif y == "md5":
		inp = input("\nEncriptar: ")
		def encrypt_string(hash_string):
			sha_signature = \
			hashlib.md5(hash_string.encode()).hexdigest()
			return sha_signature
		hash_string = inp
		sha_signature = encrypt_string(hash_string)
		print("\n")
		print("Encriptado:")
		rs = "\033[32m" + sha_signature + "\033[0;0m"
		print("\n", rs)
	
	
	
	# Trata as exceções
		
	elif y == " " or " ":
		print("\nESSE COMANDO NÃO EXISTE.")
		

