#Secondo capitolo del libro

chapter = 2


def Literals(chapter):      #(2.1)

    #Literals (2.1)

    """
    
    Una lettera (Literal) è un qualsiasi valore digitato direttamente nel programmma, può essere un numero come una consonante o vocale.

    I integer literals sono i numeri interi e possono essere rappresentati non solo nel formato decimale bensì anche in binario, octal e esadecimale.

    I prefissi sono:

        0b  Binary
        
        0o  Octal

        0x  Hexadecimal

    In alternativa possono essere rappresentati in maniera diversa esplicitamente, ad esempio: bin(x), oct(x), hex(x)

    
    I floating-point number possono essere scritti usando il punto oppure usando la notazione scientifica, ovvero:

        4.2e2   significa 4.2 * 10^2
    
    Internamente sono salvati i floating-point number in un formato 64 bit.

    L'underscore può essere usato per numeri molto grandi per renderli più facili da leggere, esempio:

    123_456_789     è uguale a scrivere 123456789

    

    """


def Expressions_And_Locations(chapter):     #(2.2)
    
    #Expressions and Locations


    """
    
    In questo minicapitolo semplicemente viene trattato la modalità con cui l'interprete assegna i valori ad una variabile tramite delle espressioni
    che possono essere direttamente dei valori oppure dei valori legati a delle variabili.

    Non è possibile assegnare un valore e allo stesso tempo effettuare una verifica di condizione con il normale operatore =, ma è possibile 
    con il walrus operator :=.

    
    
    """


def Standard_Operators(chapter):        #(2.3)

    #Standard Operators (2.3)


    """
    
    Tratta semplicemente gli operatori più comuni e i loro utilizzi.

    Un utilizzo di % come operatore tra stringhe:

    nome = "Giacomo"
    età = "19"
    message = "%s ha %d anni" % (nome,età)      output = "Giacomo ha 19 anni"
    

    """


def In_Place_Assignment(chapter):      #(2.4)

    #In-Place Assignment (2.4)

    """
    
    Parte importante di questo minicapitolo è l'assegnazione di una variabile ad un'altra ovvero:
    a = [1,2,3]
    b = a

    In questo caso b ed a fanno parte dello stesso oggetto (puntano la stessa parte di memoria) perciò se modifico uno modifico anche l'altro

    Per evitare ciò è possibile usare due modi:

        b = a.copy()

        b = a[:]

    in alternativa se si tratta di oggetti più complessi si importa la libreria copy

        b = copy.deepcopy(a)
    
    """



x = 4
y = 7

if  y and x/y:
    print("ciao")

result = y and x/y


print("See you at the next chapter!")