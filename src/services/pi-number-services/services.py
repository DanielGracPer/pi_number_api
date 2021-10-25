from math import ceil, log


class Pi:
    def __init__(self, digits):
        self.digits = digits
        self.iterators = ceil(log(digits,2))
        self.numerator = None
        self.denominator = None
        self.__gaussLegendre()

    
    def __gaussLegendre(self , a = 1, b = 1/(2**(1/2)), t = 1/4, p = 1):
        if(self.iterators > 0):
            self.iterators -= 1
            alfa = (a + b) / 2
            b = (a*b)**(1/2)
            t = t - p * (a - alfa)**2
            p *= 2
            a = alfa
            self.__gaussLegendre(a ,b ,t ,p)
        else:
            self.numerator = (a + b)**2
            self.denominator = 4 * t

    def getPiString(self):
        digits = self.digits
        
        numerator = self.numerator
        denominator = self.denominator
        hasDot = False
        string = ''
        while(digits > 0):
            divInt = numerator // denominator
            if(divInt >0):
                digits -= 1
                numerator -= denominator * divInt
                string += format(divInt,'.0f')
            elif(not hasDot):
                hasDot = True
                string += '.'
                numerator *= 10
            else:
                numerator *= 10
        return string

def getPiNumberString(digitsAmount):
    pi = Pi(digitsAmount)
    return pi.getPiString()

def getPiAlgorismValue(position):
    pi = Pi(position)
    string = pi.getPiString()
    string = string.replace('.','')
    return string[position - 1]

SERVICES = {
    'getPiNumberString': getPiNumberString,
    'getPiAlgorismValue': getPiAlgorismValue
}