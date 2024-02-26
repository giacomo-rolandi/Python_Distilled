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


def Object_Comparison(chapter):        #(2.5)

    #Object Comparison


    """
    
    L'operatore == permette di verificare se due oggetti sono uguali, per essere uguali i due oggetti devono avere li stessi elementi e lo stesso valore per tutti gli elementi
    La comparazione tra due oggetti incompatibili non produce un errore ma bensì dà come risultato False
    In alcuni casi può succedere che nonostante siano diversi vengano comparati correttamente, ad esempio nel caso di un intero e un float.

    Comparatore is compara se due oggetti "lavorano" sulla stessa locazione di memoria

    ex.


    x = [1,2,3]
    y = x

    if y is x:
        print("Ciao")
                                    #output = "ciao"
    
    
    """


def Ordered_Comparison_Operators(chapter):      #(2.6)
    

    #Ordered Comparison Operator


    """
    
    Nelle comparazioni che includono gli operatori > e < si verifica che due oggetti sono rispettivamente uno maggiore dell'altro o minore dell'altro.

    Nel caso di verifica tra due sequenze si verifica elemento dopo elemento questa comparazione fino al termine degli elementi.

    Nel caso di sequenze di stringhe si verifica l'indice rispettivo di ogni lettera nella tabella ASCII
    
    
    
    """


def Boolean_Expression_And_Truth_Values(chapter):          #(2.7)

    #Boolean Expression And Truth Values

    
    """
    
    Negli operatori logici AND, OR e NOT si verifica tra due o più elementi delle condizioni
    
    AND
        se x è falso, ritorna x; altrimenti ritorna y
        ex.

            x = 4
            y = 7

            if  y and x/y:
                print("ciao")

            result = y and x/y

        In questo esempio possiamo vedere che nel primo if dato che un numero risulta sempre vero allora ritorna x/y che anch'esso essendo un numero risulta True
        Perciò esegue la condizione vera
        Nell'assegnazione di result possiamo vedere come y risulta di nuovo vero e dato che è vero ritorna y(ovvero x/y in questo caso) perciò result avrà come valore x/y

    OR
        se x è falso, ritorn y; altrimenti ritorna x
        ex.

            x = True
            y = False

            if y or x:
                print("ciao")

        In questo caso x(in questo caso y) risulta essere False perciò ritorna y(in questo caso x) che risulta essere True perciò la condizione è vera e viene eseguito il comando

    NOT
        se x è falso, ritorna True; altrimenti ritorna False

    

    
    """


def Operations_Involving_Iterables(chapter):        #(2.9)


    #Operations Involving Iterables (2.9)


    """
    
    Esistono diversi operatori che permettono di iterare degli oggetti.
    Ad esempio:

    for
        è sicuramente il più utilizzato e permette di iterare tutti gli elementi di un oggetto
    
    v1,v2,... = s   
        In questo caso l'oggetto s viene spacchettato (unpacked) rispettivamente in v1,v2,....

    in 
        é una verifica per vedere se almeno un elemento è nell'altro, ad esempio if 3 in [1,2,3] return True    output= True

    *s
        si tratta di un expansion e permette di espandere una lista, set o tupla


    esempi di unpacked:

    a = [a,b,c]

    v1,v2,v3 = a

    Può essere usata anche la variabile _ per i valori che non abbiamo la necessità di memorizzare

    Se non sappiamo il numero totale si può sempre usare una starred variable, ovvero una lista che va a memorizzare tutti gli elementi extra
    ex.

    a = [1,2,3,4,5]

    v1,*extra,v2 = a



    
    """


def Operations_On_Sequences(chapter):       #(2.10)

    #Operations On Sequences

    """
    
    
    
    
    """


print("See you at the next chapter!")