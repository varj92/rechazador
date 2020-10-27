# -*- coding: 1252 -*- 
import psycopg2
from bd import conexion

try:
    with conexion.cursor() as cursor:
        
        cursor.execute("SELECT keyx,SUBSTRING (difarchivo, 1, 11),SUBSTRING (difbasedatos, 1, 11) FROM tmpdiferenciasarchivoaclaraciones WHERE validado = '0' AND diagnostico = '0';")
        # Con fetchall traemos todas las filas
        registros = cursor.fetchall()
        count = len(registros)
        print("Total de Registros : ",count)
        
        for reg in registros:
            print(reg)
            
            nssarchivo = reg[1]
            nssbasedatos = reg[2]

            if nssarchivo == nssbasedatos:
                print("Registro Valido")
            
            else:
                print(reg[0])
                cursor.execute("UPDATE foliosporvalidar SET validado = '1', diagnostico = '0', fechavalidacion = NOW()::DATE WHERE keyx = ",reg[0])
                print("Registro Rechazado")

        print("Termina el proceso.")
            
except psycopg2.Error as e:
    print("Ocurrió un error al consultar: ", e)
finally:
    conexion.close()