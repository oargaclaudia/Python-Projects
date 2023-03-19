def citireLista():
    l=[]
    listAsString=input("Dati lista ")
    numbersAsString=listAsString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l
def numereNegative(l):
    '''
    Afisarea tuturor numerelor negative nenule din lista
    :param l: o lista de numere intregi
    :return: o lista cu toate numerele negative nenule din lista l
    '''
    rezultat=[]
    for x in l:
        if x<0:
            rezultat.append(x)
    return rezultat
def testnumereNegative():
    assert numereNegative([-2,2,-3,0])==[-2,-3]
    assert numereNegative([])==[]
    assert numereNegative([-1,-2,-2])==[-1,-2,-2]
def celMaiMicNr(l,c):
    '''
    Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
    :param l: o lista de numere intregi
    :param c: o cifra citita de la tastatura
    :return: None, daca niciun nr nu are ultima cifra c. Altfel, returneaza cel mai mic nr care are ult cif egeala cu c
    '''
    ok=0
    for x in l:
        if x<0:
            if abs(x)%10==c:
                if ok==0:
                    min=x
                    ok=1
                elif x<min:
                    min=x
        elif x%10==c:
            if ok==0:
                min=x
                ok=1
            elif x<min:
                min=x
    if ok==0:
        return None
    return min

def testcelMaiMicNr():
    assert celMaiMicNr([1, 6, 34, 68, 40, 48, 20],8)==48
    assert celMaiMicNr([1,12,22],3)==None
    assert celMaiMicNr([1,11,21,2,222],2)==2
    assert celMaiMicNr([-2,-12,22,122],2)==-12
def isPrime(n):
    '''
    Determina daca un numar natural este prim
    :param n: un numar natural
    :return: True, daca numarul este prim. Returneaza False in caz contrar
    '''
    if n<2:
      return False
    if n==2:
      return True
    for i in range(2,n//2+1):
      if n%i==0:
        return False
    return True
def testIsPrime():
    assert isPrime(2)==True
    assert isPrime(3)==True
    assert isPrime(4)==False
def isSuperprime(n):
    '''
    Determina daca un numar este superprim
    :param n: un numar natural citit de la tastatura
    :return: True, daca numarul citit de la tastatura este superprim. False, in caz contrar.
    '''
    if n<2:
        return False
    while n!=0:
        if isPrime(n)==False:
            return False
        else:
            n=n//10
    return True
def testIsSuperprime():
    assert isSuperprime(15)==False
    assert isSuperprime(101)==False
    assert isSuperprime(233)==True
    assert isSuperprime(237)==False
def listaSuperPrime(l):
    '''
    Afișarea tuturor numerelor din listă care sunt superprime.
    :param l: o lista de numere
    :return: o noua lista cu numerele superprime
    '''
    rezultat=[]
    for x in l:
        if x>0 and isSuperprime(x):
            rezultat.append(x)
    return rezultat
def testlistaSuperPrime():
    assert listaSuperPrime([123,233])==[233]
    assert listaSuperPrime([])==[]
    assert listaSuperPrime([123,173,239])==[239]
def cmmdc(a,b):
    '''
    Returneaza cel mai mare divizor comun a doua numere
    :param a: un numar natural
    :param b: un numar natural
    :return: cel mai mare divizor comun al numerelor
    '''
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
def testcmmdc():
    assert cmmdc(2,10)==2
    assert cmmdc(2,3)==1
    assert cmmdc(12,22)==2
def celMaiMareDivizorPtNNumereNaturale(l):
    '''
    Returneaza cel mai mare divizor comun a n numere naturale pozitive
    :param l: o lista de numere
    :return: None, daca lista nu are numere pozitive. Altfel, returneeaza cmmdc
    '''
    rezultat=[]
    for x in l:
        if x>0:
            rezultat.append(x)
    if len(rezultat)==0:
        return None
    div=rezultat[0]
    for i in range(1,len(rezultat)):
        div=cmmdc(div,rezultat[i])
    return div
def testcelMaiMareDivizorPtNNumereNaturale():
    assert celMaiMareDivizorPtNNumereNaturale([12,22,23])==1
    assert celMaiMareDivizorPtNNumereNaturale([12,22])==2
    assert celMaiMareDivizorPtNNumereNaturale([23,34,45,66,5])==1
def oglindit(n):
    '''
    Returneaza oglinditul unui numar
    :param n: un numar natural
    :return: oglinditul numarului n dat
    '''
    og=0
    while n!=0:
        og=og*10+n%10
        n=n//10
    return og
def testoglindit():
    assert oglindit(12)==21
    assert oglindit(142)==241
    assert oglindit(5)==5
def ListaNoua(l):
    '''
    Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    :param l:lista de intregi
    :return: lista obtinuta din lista inițială l în care numerele pozitive și nenule au fost înlocuite cu
CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    '''
    rezultat=[]
    div=celMaiMareDivizorPtNNumereNaturale(l)
    for x in l:
        if x>0:
            rezultat.append(div)
        elif x<0:
            xstr=""
            y=oglindit(abs(x))
            xstr=xstr+"-"+str(y)
            rezultat.append(int(xstr))
        else:
            rezultat.append(x)
    return rezultat
def testListaNoua():
    assert ListaNoua([-76, 12, 24, -13, 144])==[-67, 12, 12, -31, 12]
    assert ListaNoua([-2, 2 ,22])==[-2,2,2]
    assert ListaNoua([])==[]
def main():
    l=[]
    testcelMaiMareDivizorPtNNumereNaturale()
    testcmmdc()
    testcelMaiMicNr()
    testnumereNegative()
    testIsPrime()
    testIsSuperprime()
    testlistaSuperPrime()
    testListaNoua()
    testoglindit()
    while True:
        print("1. Citire lista")
        print("2. Afișarea tuturor numerelor negative nenule din listă")
        print("3. Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.")
        print("4. Afișarea tuturor numerelor din listă care sunt superprime.")
        print("5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă. ")
        print("x. Iesire")
        optiune=input("Dati optiunea: ")
        if optiune=="1":
            l=citireLista()
        elif optiune=="2":
            print(numereNegative(l))
        elif optiune=="3":
            c=int(input("Dati cifra de la tastatura: "))
            if celMaiMicNr(l,c)==None:
                print("Niciun numar nu are ultima cifra data")
            else:
                print(celMaiMicNr(l,c))
        elif optiune=="4":
            print(listaSuperPrime(l))
        elif optiune=="5":
            print(ListaNoua(l))
        elif optiune=="x":
            break
        else:
            print("Optiune invalida")
main()