from cuentaAhorros import CuentaAhorros
from cuentaCorriente import CuentaCorriente


class SimuladorBancario:
    '''
    #Atributos
    '''
    cedula = ''' caracter '''
    Nombres = ''' caracter '''
    mesactual= ''' '''

    ''' 
    #Asociaciones
    '''
    corriente = CuentaCorriente
    ahorros = CuentaAhorros 


    def ConsignarCuentaCorriente(self, valorConsignar):
        #Aqui va el codigo
        return self.corriente.saldoCuentaCorriente + valorConsignar 
    
    def CalcularSaldoTotal(self):
        #Aqui va el codigo del metodo
        return self.corriente + self.ahorros
    
    def PasarSaldoAhorrosaCorriente(self):
        #Aqui va el codigo del metodo
        CuentaCorriente= self.ahorro =+self.corriente

        if CuentaCorriente(CuentaCorriente):
            CuentaAhorros=0
            print("Pasado exitosamente")
        else: print ("no se pudo transladar el saldo, corrija")    
