from MEDIA import media1
from MEDIANA import mediana1
from VARIANCIA import varianca1
from DESVIO import desvio1
from MODA import moda1


from matplotlib import pyplot as plt

empresa1 = [1000,6000,1200,8000,1400]
empresa1.sort()
empresa2 = [5000,4000,3000,2000,7000]
empresa2.sort()
empresa3 = [1200,1300,8000,3000,15000]
empresa3.sort()
empresa4 = [1400,1750,2000,4500,5900]
empresa4.sort()



cargo = ['Estagiários' , 'Técnico' , 'Assistente' , ' Analista' , 'Supervisor']




def hadle(lista, salarios):

    print('EMPRESA', salarios)
    print('----------------------------')
    media1(lista)
    mediana1(lista)
    moda1(lista)
    varianca1(lista)
    desvio1(lista)


hadle(empresa1, empresa1)  
hadle(empresa2, empresa2)   
hadle(empresa3, empresa3) 
hadle(empresa4, empresa4) 

plt.title('Cargos e Salários')
plt.xlabel('Cargos')
plt.ylabel('Salário')

plt.plot(cargo, empresa1, linestyle = '--', marker = "o")
plt.plot(cargo, empresa2, linestyle = '--', marker = "o")
plt.plot(cargo, empresa3, linestyle = '--', marker = "o")
plt.plot(cargo, empresa4, linestyle = '--', marker = "o")



plt.show()