#Este archivo es usado para probar diferentes cosas que pueden ayudar a desarrollar el proyecto

# Python program to get 
# dictionary keys as list

from __future__ import print_function


dict = {
    'a':'Geeks', 
    'b':'for', 
    'c':'geeks',
    'horario':
                    {
            'lunes' :  {
                        '7' :  (), '8' :  (), '9' :  (), '10' : (), '11' : (), '12' : (), '13' : (),'14' : (), '15' : (), '16' : (),'17' : (),'18' : (),'19' : (),
                        },
            'a' :  {
                        '7' :  (), '8' :  (), '9' :  (), '10' : (), '11' : (), '12' : (), '13' : (),'14' : (), '15' : (), '16' : (),'17' : (),'18' : (),'19' : (),
                        },
                    }
        }
  





llaves = list
llaves = dict['horario'].keys()
for a in llaves:
    print(a)

