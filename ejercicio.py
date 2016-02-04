#!/usr/bin/python
# -*- coding: utf-8 -*-

fich = open ("/etc/passwd", 'r')
lineas = fich.readlines()

for line in lineas:
	lista_lineas = line.split(':')
	print lista_lineas[0], lista_lineas[-1] [:-1]
	
print "\nNumero de lineas:", len(lineas)
	

