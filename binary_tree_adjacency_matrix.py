#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  binary_tree_adjacency_matrix.py
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
#  
#  


# please be aware that this algorithm works online for full binary trees with "n" codes
def main():
	#choses the number of nodes and either it will be direction or non directinal
	n = int(input("how many nodes the tree has? (it needs to be a full tree): "))
	try:
		
		choice=input('"d" for directional and "n" for non directional: ').lower()
		if choice not in ("d","n"):
			raise Exception("not d")
			
	except "neither d or f":
		
		print("please only d or n")
		while choice not in ("d","n"):
			choice=input('"d" for directional and "n" for non directional ').lower()
			
	matrix=[]
	line=[]
	
	#initializes a "n x n" matrix
	
	for lines in range(n):
		for columns in range(n):
			line.append(0)
		matrix.append(line)
		line=[]
	
	#begins to change the matrix values (thinking of a tree with the root as node 1)
	
	finalnode=(n//2)
	
	for posi in range(1,finalnode+1,1):
		matrix[posi-1][(posi*2)-1]=1
		matrix[posi-1][(posi*2)]=1
		if choice == "n":
			matrix[(posi*2)-1][posi-1]=1
			matrix[posi*2][posi-1]=1
	
	#prints the matrix
	
	for l in range(n):
		for c in range(n):
			print("%d"%(matrix[l][c]),end=" ")
		print(" ")
					
		
			
	
	
if __name__ == "__main__":
	main()

