import create_registre as cr
import read_registre as rr

#Trucada per executar la funció a l'arxiu create_registre.py
cr.create_reg()

#Trucada per read_reg()
results = rr.read_reg()

for i in results:
    print('\n')
    print('Nom: ' + i[0])
    print('Adreça: ' + i[1])
    print('telèfon: ' + i[2])
    print('email: ' + i[3])
    print('neixament: ' + i[4])
