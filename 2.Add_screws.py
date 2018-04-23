# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 09:52:59 2018

@author: shengyin
"""
import math

lattice=3.147
berg=0.8660254*lattice

with open("1.initial_structure.lam","r") as infile:
    with open("2.square_with_dislocations.lam","w") as outfile:     
        
        outfile.write(infile.readline())
        outfile.write(infile.readline())
        
	temp=infile.readline()
        outfile.write(temp)
        data=temp.split()
        atom_num=int(data[0])
        
        outfile.write(infile.readline())
        outfile.write(infile.readline())
        outfile.write(infile.readline())

	temp=infile.readline()
        outfile.write(temp)
        data=temp.split()
        ylo=float(data[0])
	yhi=float(data[1])

	temp=infile.readline()
        outfile.write(temp)
        data=temp.split()
        zlo=float(data[0])
	zhi=float(data[1])

	berg1=0.8660254*lattice
	berg2=-0.8660254*lattice
	berg3=0.8660254*lattice
	berg4=-0.8660254*lattice

	screw1=[(yhi-ylo)/4.0,(zhi-zlo)/4.0]
	screw2=[(yhi-ylo)/4.0*3,(zhi-zlo)/4.0]
	screw3=[(yhi-ylo)/4.0*3,(zhi-zlo)/4.0*3]
	screw4=[(yhi-ylo)/4.0,(zhi-zlo)/4.0*3]

	for i in range(0,7):
            outfile.write(infile.readline())

        for i in range(0,atom_num):
            temp=infile.readline()
            data=temp.split()
            p_id=int(data[0])
            p_type=int(data[1])
            p_x=float(data[2])
            p_y=float(data[3])
            p_z=float(data[4])
            
            dy_1=p_y-screw1[0]
            dz_1=p_z-screw1[1]
            dy_2=p_y-screw2[0]
            dz_2=p_z-screw2[1]
            dy_3=p_y-screw3[0]
            dz_3=p_z-screw3[1]
            dy_4=p_y-screw4[0]
            dz_4=p_z-screw4[1]
            theta1=math.atan(dz_1/dy_1)
            theta2=math.atan(dz_2/dy_2)
            theta3=math.atan(dz_3/dy_3)
            theta4=math.atan(dz_4/dy_4)
            if dy_1<0:
                theta1=theta1+math.pi
            if dy_2<0:
                theta2=theta2+math.pi
            if dy_3<0:
                theta3=theta3+math.pi
            if dy_4<0:
                theta4=theta4+math.pi
            
	    
	    dx=(berg1*theta1+berg2*theta2+berg3*theta3+berg4*theta4)/2/math.pi
            
            output=str(p_id)+' '+str(p_type)+' '+str(p_x+dx)+' '+str(p_y)+' '+str(p_z)
            outfile.write(output)
            outfile.write("\n")


