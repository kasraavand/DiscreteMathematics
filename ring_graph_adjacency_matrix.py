#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ring_graph_adjacency_matrix.py
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.  


#This code works for graphs with nodes positioned just like a ring network topology and numbered by crescent order.


def main(args):
	#initializes a nxn matrix full of zeros
	n=int(input("the number of nodes in this graph: "))
	matrix=[]
	line=[]
	
	for l in range(n):
		for c in range(n):
			line.append(0)
		matrix.append(line)
		line=[]
		
	#adds the "ones" in correct positions	
	for x in range(n-1):
		matrix[x][x+1]=1
		matrix[x+1][x]=1
		
	#adds the "ones" in the positions that don't follow any rule
	matrix[0][n-1]=1
	matrix[n-1][0]=1
	
	#prints the matrix
	
	for column in matrix:
		for item in column:
			print(item,end=" ")
		print("")
		
	
	return 0

if __name__ == '__main__':
				import sys
				sys.exit(main(sys.argv))
