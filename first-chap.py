#Primo Capitolo del libro

chapter = 1



def Primitives_Variables_Expressions(chapter):  #(1.3)
    
    
    #Primitives, Variables, Expressions (1.3)


    """
    Tipi di variabili: Int (intero) Float (Numero decimale) String (stringa) Bool (True/False)
    Di base python interpreta il tipo di variabile in automatico
    In alternativa si può esplicitare:


    x: int = 7    esplicito

    y = 4         implicito


    
    Tramite print(f'....') 
    possiamo usare la formatted-string literal che ci permette di stampare le variabili in {} e la stringa normalmente:

    ex.

    print(f'Il prezzo di x è: {x} euro')

    possiamo anche formattarli in maniera diversa:

    con >3d andiamo ad allineare il testo di 3 cifre a destra
    con 0.2f invece andiamo a definire massimo 2 cifre decimali

    ex. 

    print(f'{ordine: >3d} {prezzo: 0.2f})
    
    
    """


    pass


def Arithmetic_Operators(chapter):   #(1.4)
    
    
    #Arithmetic Operators (1.4)


    """

    x= 7

    y= 4.5

    print (x/y)  Stampa la divisione tra 7 e 4.5 come floating-point number (1.55555556)
    print (x//y) Stampa la divisione tra 7 e 4.5 troncata per difetto (1.0)
    print (x%y)  Stampa il resto della divisione (se tra due interi stampa un intero) (In questo caso 2.5)
                                                                                        x-(x//y)*y

    
    
    ALCUNE FUNZIONI MATEMATICHE COMUNI

    print(abs(-(x/y)))   Stampa il valore assoluto
    print(divmod(x,y))   Stampa due valori (divisione tra x // y )  (modulo tra x % y)
    print(pow(x, 2, 7))  Stampa x elevato a 2, se aggiunto un terzo valore: (x**2 % 7)
    print(round(x/y))    Stampa il numero arrotondato al numero pari più vicino



    OPERATORI DI MANIPOLAZIONE DEI BIT

    x << y      permette di spostare i valori di bit di x, di y posti (ex. 11 = 3 << 2  -> 1100 = 12 
    x >> y      permette di fare lo stesso verso destra (ex. 1100 = 12 >> 2  ->  0011 = 30) 
    x & y       permette di fare l'operazione logica AND
    x | y       permette di fare l'operazione logica OR
    x ^ y       permette di fare l'operazione logica XOR
    ~x          permette di fare l'operazione logica NOT (a livello di bit)

    

    STAMPA BINARIO

    n1 = 9
    n2 = -23

    print(bin(n2))
    print(" " + bin(n1))
    print(bin(~n1))
    print(~n1)

    
    
    CONDIZIONI E CONTROLLO DEL FLUSSO

    walrus operator

    x = 0

    while (x := x +1) < 10:
        print (x)               stamperà 1,2,3,4,5,6,7,8,9

        
    pass        permette di non fare nulla e andare avanti
    break       permette di uscire dal ciclo
    continue    permette di skippare il turno attuale e di andare al turno successivo

    
    
    STRINGHE DI TESTO
  
    per estrarre una sotto-stringa possiamo utilizzare lo slicing operator 
    data una stringa s= "Hello World"

    con s[i:j]
    andiamo a prendere una sotto-stringa che inzia dall'indice i e arriva fino a <j
    print (s[1:5]) output:  ello
    indichiamo con k gl'indici di s che stamperà 
    allora avremo  i <= k < j

    se omessi andranno a rispecchiare rispettivamente l'inizio o la fine

    la funzione .replace() permette di rimpiazzare una sotto-stringa con un'altra
    ex.
        string_replaced = s.replace("Hello", "Hello Cruel")
        
        output:     Hello Cruel World
    
    
    FUNZIONI DI STRINGHE COMUNI

    
    1) .endswith() / .startswith()

            s = "Hello World"

            result = s.endswith("Worl", -5, -1)

            print (result)      Stamperà "True" perchè partendo dall'indice -5 (ovvero da W) e arrivando fino all'indice -1
                                (ovvero l) la sottostringa finisce con Worl. Perciò è vero
    
    2) .find()
      
            result = s.find("o", 1, -1)

            print (result)      Stamperà 4 in quanto partendo dall'indice 1 fino ad arrivare a -1, la prima volta in cui si trova 
                                "o" è all'indice 4
    
    3) .lower() / .upper()

            converte tutti i caratteri in minuscolo / maiuscolo
        
    4) .replace()
            
            s = "Hello World, Hello buddy"

            result = s.replace("Hello", "Fottiti", 1)

            print(result)       Stamperà Fottiti World, Hello buddy, in quanto ho specificato un massimo di 1 di replacement, 
                                se lo avessi lasciato di default (-1) avrebbe cambiato tutte le occorrenze.
    
    5) .split()

            s = "Giacomo 19"

            name, age = s.split(" ")

            print(age)      Stamperà 19 in quanto avendo splittato la stringa in due (dato lo spazio in mezzo), la prima parte
                            parte assegnata a name e la seconda ad age

    6) .strip()

            s = " Giacomo 19"

            s.strip()
            result = s.strip("19")

            print(result)   Stamperà la stringa senza spazi iniziali e finali (data la prima chiamata)
                            e senza il 19 finale (data la seconda chiamata)

    
    Nel primo caso stampa la stringa con le varie funzioni, nel secondo così com'è scritto
    N.B. Per selezionare più righe premere SHIFT, Per spostarle ALT, e per ricopiarle su o giù SHIFT+ALT

    print(str("\n \n \n"))
    print(repr("\n \n \n"))
    


            
    """

    pass


def File_Input_and_Output(chapter):     #(1.7)

    #File Input and Output 


    """

    In questo esempio apriamo il contenuto del file e lo assegniamo a file,
    subito dopo con un for andiamo a prendere riga per riga e la andiamo a stampare
    
    with open (r"prova.txt") as file:
        for line in file:
            print (line, end="")
                        Di base con end impostato a \n
    

    Questa invece è una variante senza il with                N.B. con with andiamo a creare un ciclo (ciò spiega il motivo della identazione)
                                                                   perciò quando finisci il ciclo il file si chiude in automatico, al contrario del 
                                                                   secondo in cui dobbiamo chiuderlo il file.    

    file = open (r"prova.txt")

    for line in file:
        print(line, end="")
    file.close()
    

    with open ("prova.txt") as file:
        data = file.read()

    print(file)


    Questo esempio utilizza la variabile chunks per andare a leggere dal file in blocchi (in questo caso 101 caratteri)

    with open ("prova.txt") as file:
        while (chunks := file.read(101)):
            print(chunks, end="\n")
    
            
    Per far si che l'output vada a visualizzarsi o scriversi in un altro file è possibile in due modi:

    1    print(..., file="file.txt")

    2    file.write (....)



    """


def Lists(chapter):     #(1.8)
    
    #Lists (1.8)

    """
    
    Liste (array) sono una collezione ordinata di oggetti arbitrari

    example = [one, two, three]

    
    per aggiungere ulteriori oggetti utilizzare la funzione:

    .append(...)


    Per modificare un indice possiamo semplicemente fare:       example[n] = "..."
    in questo modo però andiamo a sostituire il vecchio elemento e lo perdiamo

    al contrario invece se utilizziamo la funzione .insert() allora andremo sempre a sostituirlo, 
    ma il vecchio elemento si sarà spostato di un indice e stessa cosa per quelli successivi    

    
    example = ["angelo", "paulo", "giacomo"]

    example.insert(1, " ciao fra")

    print(example)          output = ["angelo", " ciao fra", "paulo", "giacomo"]



    
    """


example = ["angelo", "paulo", "giacomo"]

example.insert(1, " ciao fra")

print(example[0:2])

example[0:2] = ["ciao", "forza", "daje"]

print(example)
