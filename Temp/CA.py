"""
Author: Isaac Goodin
Date Created: 7/13/2010
Last Updated: 11/5/2010
"""

import numpy
import matplotlib
import random
import math
import Image, ImageDraw
import os
from matplotlib import pyplot

class CA:
	"""
		Class to generate Cellular Automaton Layers
	"""

	def __init__(self,name="test",width=200,dt=1.0,type="test"):
		self.name=name
		self.width= width
		self.timestep= dt
		self.base = numpy.zeros((width,width),int)
		self.layer = numpy.zeros((width,width),int)
		self.time = 0.0
		self.cell=[]
		self.binary = ""
		self.surrounding = []
		self.type = "Moore"
			
	def step(self,T=[],iterations=1):

		#iterate the CA
		while(iterations>0):

			#operate on the temporary layer
			self.layer =numpy.zeros((self.width,self.width),int)
			for i in range(self.width):
				for j in range(self.width):
					self.cell = [i,j]
					self.getneighbors()
					self.layer[i][j]=self.group(3)
					if(len(T)>0):
						s=0.0
						for sample in T:
							s+=T[0].base[i][j]
						self.layer[i][j]+=s
						self.layer[i][j]=math.floor(self.layer[i][j]/(len(T)+1.0))
			self.base=self.layer
			
			self.time+=self.timestep
			iterations-=1		
		
	def group(self,num):
		"""
			Apply group rule
		"""
		sum=self.base[self.cell[0]][self.cell[1]]
		for c in self.surrounding:
			sum+=c
		if(sum>num):
			return 1
		return 0

	
	def getneighbors(self):
		"""
			Sets the neighbors of the cell based on the type of neighboring system
		"""
		i=self.cell[0]
		j=self.cell[1]
		
		w = self.width-1
		Center = self.base[i][j]
		if(self.type=="Neumann"):
			if(j==w and 0<i<w):
				North=self.base[i-1][j]
				East=self.base[i][0]
				South=self.base[i+1][j]
				West=self.base[i][j-1]

			if(i==w and 0<j<w):
				North=self.base[i-1][j]
				East=self.base[i][j+1]
				South=self.base[0][j]
				West=self.base[i][j-1]

			if(j==0 and 0<i<w):
				North=self.base[i-1][j]
				East=self.base[i][j+1]
				South=self.base[i+1][j]
				West=self.base[i][w]
			if(i==0 and 0<j<w):
				North=self.base[w][j]
				East=self.base[i][j+1]
				South=self.base[i+1][j]
				West=self.base[i][j-1]
	
			if(j==w and i==w):
				North=self.base[i-1][j]
				East=self.base[i][0]
				South=self.base[0][j]
				West=self.base[i][j-1]

			if(j==0 and i==0):
				North=self.base[w][j]
				East=self.base[i][j+1]
				South=self.base[i+1][j]
				West=self.base[i][w]

			if(j==0 and i==w):
				North=self.base[i-1][j]
				East=self.base[i][j+1]
				South=self.base[0][j]
				West=self.base[i][w]

			if(i==0 and j==w):
				North=self.base[w][j]
				East=self.base[i][0]
				South=self.base[i+1][j]
				West=self.base[i][j-1]

			if(0<i<w and 0<j<w):			
				North=self.base[i-1][j]
				East=self.base[i][j+1]
				South=self.base[i+1][j]
				West=self.base[i][j-1]

			self.surrounding = [North,South,East,West]
			self.binary= str(East)+str(West)+str(South)+str(North)+str(Center)
			
		elif(self.type=="Moore"):
			
			if(j==w and 0<i<w):
				North=self.base[i-1][j]
				East=self.base[i][0]
				South=self.base[i+1][j]
				West=self.base[i][j-1]
				NE = self.base[i-1][0]
				NW = self.base[i-1][j-1]
				SE = self.base[i+1][0]
				SW = self.base[i+1][j-1]
			if(i==w and 0<j<w):
				North=self.base[i-1][j]
				East=self.base[i][j+1]
				South=self.base[0][j]
				West=self.base[i][j-1]
				NE = self.base[i-1][j+1]
				NW = self.base[i-1][j-1]
				SE = self.base[0][j+1]
				SW = self.base[0][j-1]
			if(j==0 and 0<i<w):
				North=self.base[i-1][j]
				East=self.base[i][j+1]
				South=self.base[i+1][j]
				West=self.base[i][w]
				NE = self.base[i-1][j+1]
				NW = self.base[i-1][w]
				SE = self.base[i+1][j+1]
				SW = self.base[i+1][w]
			if(i==0 and 0<j<w):
				North=self.base[w][j]
				East=self.base[i][j+1]
				South=self.base[i+1][j]
				West=self.base[i][j-1]
				NE = self.base[w][j+1]
				NW = self.base[w][j-1]
				SE = self.base[i+1][j+1]
				SW = self.base[i+1][j-1]
							
			if(j==w and i==w):
				North=self.base[i-1][j]
				East=self.base[i][0]
				South=self.base[0][j]
				West=self.base[i][j-1]
				NE = self.base[i-1][0]
				NW = self.base[i-1][j-1]
				SE = self.base[0][0]
				SW = self.base[0][j-1]
			if(j==0 and i==0):
				North=self.base[w][j]
				East=self.base[i][j+1]
				South=self.base[i+1][j]
				West=self.base[i][w]
				NE = self.base[w][j+1]
				NW = self.base[w][w]
				SE = self.base[i+1][j+1]
				SW = self.base[i+1][w]
			if(j==0 and i==w):
				North=self.base[i-1][j]
				East=self.base[i][j+1]
				South=self.base[0][j]
				West=self.base[i][w]
				NE = self.base[i-1][j+1]
				NW = self.base[i-1][w]
				SE = self.base[0][j+1]
				SW = self.base[0][w]
			if(i==0 and j==w):
				North=self.base[w][j]
				East=self.base[i][0]
				South=self.base[i+1][j]
				West=self.base[i][j-1]
				NE = self.base[w][0]
				NW = self.base[w][j-1]
				SE = self.base[i+1][0]
				SW = self.base[i+1][j-1]
			if(0<i<w and 0<j<w):			
				North=self.base[i-1][j]
				East=self.base[i][j+1]
				South=self.base[i+1][j]
				West=self.base[i][j-1]
				NE = self.base[i-1][j+1]
				NW = self.base[i-1][j-1]
				SE = self.base[i+1][j+1]
				SW = self.base[i+1][j-1]
			
			
			self.surrounding = [North,South,East,West,NE,NW,SE,SW]
			self.binary= str(East)+str(West)+str(South)+str(North)+str(Center)+str(NE)+str(NW)+str(SE)+str(SW)
		
	def randomfill(self,percent):
		#randomly changes cells to 1 given a percent
		total=math.floor((self.width**2)*percent/100.0)
		fill=0
		while(fill<total):
			i=random.randint(0,self.width-1)
			j=random.randint(0,self.width-1)
			if(self.base[i][j]==0):
				self.base[i][j]=1
				fill+=1
		
	def video(self):
		#create a rough video using mencoder
		dir = os.getcwd()+"/Temp"
		os.chdir(dir)
		os.system("convert -delay 0.3 *.png animation.gif")

	def show(self):
		#show the CA at an iteration and save the image
		array=self.base
		pyplot.imshow(array)
		pyplot.imsave("Temp/ "+str(int(self.time))+".png",array)

