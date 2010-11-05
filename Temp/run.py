"""
Author: Isaac Goodin
Date Created: 7/13/2010
Last Updated: 11/5/2010
"""

from CA import *

#create an instance of cellular automata
run=CA("n1",200,1.0)

#randomly seed the matrix
run.randomfill(22.0)

#iterate and plot 
for i in range(30):
	run.show()
	run.step()

run.video()
