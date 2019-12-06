# Submitted by-: Diptiman Senapati (1741012062)
#				 Deepkalyan Priyadarshi (1741012167)
#                Jeeban Prakash Nayak (17401012155)
# 				 Rohan Lenka (1741012340)

#Input Method= S->AB/BC A->BA/a B->CC/b C->AB/a
#String input= baaba

class CYKP:
	V=[]#List of All Variables
	T=[]#List of All Terminals
	p=[]#List For All Production

	def __init__(self,a):#Constructor
		a=a.split() #Spliting 
		i=0
		j=1
		#Extracting the Production From Strings
		while i<len(a):
			b=a[i].split('/')#Dividing each production 
			if len(b)>1:
				self.p.append(b[0])
				while j<len(b):
					self.p.append(a[i][0]+'->'+b[j])
					j+=1
				j=1
			else:
				self.p.append(b[0])
			i+=1


	# Checking for Presence Existing Variables in Production
	def checkpresence(self,v):
		actual=''
		for x in range(len(self.p)):
			if v in self.p[x]:
				actual=actual+self.p[x][0]
		return actual


	#Union Operations
	def checkunion(self,vtab,i,j,k):
		u=[]#Contains the Concatenated String
		c=0
		for x in range(len(vtab[k-1][i-1])):
			for y in range(len(vtab[(j-k)-1][i+k-1])):

				u.append(vtab[k-1][i-1][x]+vtab[(j-k)-1][i+k-1][y])
		presence=''
		for x in range(len(u)):
			y=self.checkpresence(u[x])
			if y !=' ':
				presence=presence+y
		if presence=='':
			presence='#'
		return presence

	# CYK Algorithm
	def cyk(self,s):
		length=len(s)
		rows, cols = (length, length) 
		vtab = [['' for i in range(cols)] for j in range(rows)] 

		for i in range(len(s)):
			vtab[0][i]=self.checkpresence(s[i])#V[i,1]=checkpresence(s[i])


		j=2
		while j<=length:
			i=1
			while i<=length-j+1:
				k=1
				while k<=j-1:
					result=self.checkunion(vtab,i,j,k)
					if result=='#' and vtab[j-1][i-1] =='':
						vtab[j-1][i-1]='#'
					elif result!='#':
						if vtab[j-1][i-1]=='#': 
							vtab[j-1][i-1]=''
						if result not in vtab[j-1][i-1] : 
							vtab[j-1][i-1]=vtab[j-1][i-1]+result
					k+=1
				i+=1
			j+=1
		
		print("  ")
		print("Triangular Table")
		for record in vtab:
			print(record)
		print("  ")

		if self.p[0][0] in vtab[rows-1][0]:
			print (s,' is Accepted')
		else:
			print(s,' is Rejected')

	#Taking out Variables And Terminals
	def terminals_and_variables(self):
		for x in range(len(self.p)):
			for y in range(len(self.p[x])):
				if self.p[x][y] !='-' and self.p[x][y] !='>' and str(self.p[x][y]).isupper():
					if self.p[x][y] not in self.V:
						self.V.append(self.p[x][y])
				elif self.p[x][y] !='-' and self.p[x][y] !='>' and str(self.p[x][y]).islower() or self.p[x][y]=='#':
					if self.p[x][y] not in self.T:
						self.T.append(self.p[x][y])

		print("  ")
		print('Production')
		for x in range(len(self.p)):
			print(self.p[x])
		print("  ")
		print ('Terminal')
		for x in range(len(self.T)):
			print (self.T[x])
		print("  ")
		print ('Variables')
		for x in range(len(self.V)):
			print (self.V[x])
		print("  ")

c=CYKP(input('Keep on entering the Production by Giving Space in between the Production(Must Be In CNF and use epsilon as #) :'))
c.terminals_and_variables()
c.cyk(input('Enter the String to be checked (without giving space) :'))

