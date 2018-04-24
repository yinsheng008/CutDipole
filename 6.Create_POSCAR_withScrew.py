# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:52:59 2018

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

with open("Rhombus_with_Screw.lam","r") as infile:
    with open("Rhombus_POSCAR_withScrew","w") as outfile:     
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

	for i in range(0,4):
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
	    all_atoms.append(temp_p)
	#output first several lines
	outfile.write('POSCAR file written by 7.py\n')
	outfile.write('1   !scaling parameter\n') #scaling parameter
	temp=str(lx)+' 0.0 0.0\n'
	outfile.write(temp)
	temp='0.0 '+str(ly)+' 0.0\n'
	outfile.write(temp)
	temp=str(lx/2.0)+' '+str(ly/2.0)+' '+str(lz)+' \n'
	outfile.write(temp)
	temp=str(len(all_atoms))+'\n'     #num_type1 num_type2 ...
	outfile.write(temp)
	outfile.write('Direct\n')
	
	#output all atoms
	for i in range(0,atom_num):
	    print i
	    p=all_atoms[i]
	    zf=p.z/lz
	    xf=(p.x-zf*(lx/2.0))/lx
	    yf=(p.y+ly/4.0-zf*(ly/2.0))/ly
	    temp='%.6f '%xf+' %.6f '%yf+' %.6f '%zf+'\n'
    	    outfile.write(temp)	
	    
