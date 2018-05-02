# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:52:59 2018
Cut the square-4-dislocation sample to a Rhombus shape with only one dislocation dipole, (output lam file)
@author: shengyin
"""
import math

class Point:
    def __init__(self,pid,ptype,coordx,coordy,coordz,status):
	self.id=pid
	self.type=ptype
	self.x=coordx
	self.y=coordy
	self.z=coordz
	self.status=status
    def sum(self):
        return self.x+self.y+self.z


with open("2.square_with_dislocations.lam","r") as infile:
    with open("4.Rhombus_with_Screw.lam","w") as outfile:     
        
	temp=infile.readline()
	temp=infile.readline()
        
	temp=infile.readline()
        data=temp.split()
        atom_num=int(data[0])
        
	temp=infile.readline()
	temp=infile.readline()

	temp=infile.readline()
        data=temp.split()
        xlo=float(data[0])
	xhi=float(data[1]);
	lx=xhi-xlo

	temp=infile.readline()
        data=temp.split()
        ylo=float(data[0])
	yhi=float(data[1])
	ly=yhi-ylo

	temp=infile.readline()
        data=temp.split()
        zlo=float(data[0])
	zhi=float(data[1])
	lz=zhi-zlo
	all_atoms=[]

	for i in range(0,7):
            temp=infile.readline()

        for i in range(0,atom_num):
            temp=infile.readline()
            data=temp.split()
            p_id=int(data[0])
            p_type=int(data[1])
            p_x=float(data[2])
            p_y=float(data[3])
            p_z=float(data[4])
	    temp_p=Point(p_id,p_type,p_x,p_y,p_z,1)
	    if p_z>(lz/2.0-0.001):   
		temp_p.status=0
	    if p_z>(lz/ly*p_y+0.25*lz) and temp_p.status!=0: # move one part
		temp_p.y=temp_p.y+ly
	    if p_z<(lz/ly*p_y-0.75*lz) and temp_p.status!=0: # move another part
		temp_p.y=temp_p.y-ly
	    
	    if temp_p.status!=0:
                all_atoms.append(temp_p)
	#output first several lines
	outfile.write('LAMMPS data file\n\n')
	temp=str(len(all_atoms))+' '+'atoms\n'
	outfile.write(temp)
	outfile.write('1 atom types\n\n')
	temp=str(xlo)+' '+str(xhi)+' xlo xhi\n'
	outfile.write(temp)
	temp=str(ylo-0.25*ly)+' '+str(yhi-0.25*ly)+' ylo yhi\n'
	outfile.write(temp)
	temp=str(zlo)+' '+str(zhi/2.0)+' zlo zhi\n'
	outfile.write(temp)
	temp=str(0.0)+' '+str(lx/2.0)+' '+str(ly/2.0)+' xy xz yz\n\n'
	outfile.write(temp)
	outfile.write('Atoms\n\n')
	
	#output all atoms
	for i in range(0,len(all_atoms)):
	    p=all_atoms[i]
	    temp=str(p.id)+' '+str(p.type)+' '+str(p.x)+' '+str(p.y)+' '+str(p.z)+'\n'	
    	    outfile.write(temp)	
"""
shifted sample
"""
with open("2.square_with_dislocations_shifted.lam","r") as infile:
    with open("4.Rhombus_with_Screw_shifted.lam","w") as outfile:     
        
	temp=infile.readline()
	temp=infile.readline()
        
	temp=infile.readline()
        data=temp.split()
        atom_num=int(data[0])
        
	temp=infile.readline()
	temp=infile.readline()

	temp=infile.readline()
        data=temp.split()
        xlo=float(data[0])
	xhi=float(data[1]);
	lx=xhi-xlo

	temp=infile.readline()
        data=temp.split()
        ylo=float(data[0])
	yhi=float(data[1])
	ly=yhi-ylo

	temp=infile.readline()
        data=temp.split()
        zlo=float(data[0])
	zhi=float(data[1])
	lz=zhi-zlo
	all_atoms=[]

	for i in range(0,7):
            temp=infile.readline()

        for i in range(0,atom_num):
            temp=infile.readline()
            data=temp.split()
            p_id=int(data[0])
            p_type=int(data[1])
            p_x=float(data[2])
            p_y=float(data[3])
            p_z=float(data[4])
	    temp_p=Point(p_id,p_type,p_x,p_y,p_z,1)
	    if p_z>(lz/2.0-0.001):   
		temp_p.status=0
	    if p_z>(lz/ly*p_y+0.25*lz) and temp_p.status!=0: # move one part
		temp_p.y=temp_p.y+ly
	    if p_z<(lz/ly*p_y-0.75*lz) and temp_p.status!=0: # move another part
		temp_p.y=temp_p.y-ly
	    
	    if temp_p.status!=0:
                all_atoms.append(temp_p)
	#output first several lines
	outfile.write('LAMMPS data file\n\n')
	temp=str(len(all_atoms))+' '+'atoms\n'
	outfile.write(temp)
	outfile.write('1 atom types\n\n')
	temp=str(xlo)+' '+str(xhi)+' xlo xhi\n'
	outfile.write(temp)
	temp=str(ylo-0.25*ly)+' '+str(yhi-0.25*ly)+' ylo yhi\n'
	outfile.write(temp)
	temp=str(zlo)+' '+str(zhi/2.0)+' zlo zhi\n'
	outfile.write(temp)
	temp=str(0.0)+' '+str(lx/2.0)+' '+str(ly/2.0)+' xy xz yz\n\n'
	outfile.write(temp)
	outfile.write('Atoms\n\n')
	
	#output all atoms
	for i in range(0,len(all_atoms)):
	    p=all_atoms[i]
	    temp=str(p.id)+' '+str(p.type)+' '+str(p.x)+' '+str(p.y)+' '+str(p.z)+'\n'	
    	    outfile.write(temp)	
