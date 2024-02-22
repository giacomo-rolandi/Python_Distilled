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


    In questo esempio sono andato a modificare la lista usando lo slicing operator, 
    Nonostante io abbia inserito come range 0 <= k < 2. 
    Non ho ricevuto nessun errore in quanto python permette nel caso in cui vengano inseriti più elementi del range di andare ad
    aggiungerli esattamente come con la funzione .insert()

    example = ["angelo", "paulo", "giacomo"]

    example.insert(1, " ciao fra")

    print(example[0:2])

    example[0:2] = ["ciao", "forza", "daje"]

    print(example)


    E' possibile concatenare una lista con l'operatore  +

    example = ["io", "sono"]
    example2 = ["in", "treno"]


    print(example+example2)
    print(example := example+example2)



    La funzione built-in list() permette di inizializzare una lista, inoltre nel caso in cui venga inserito qualcosa al suo interno
    verrà trasformato in una lista

    example = list("giacomo")
    print(example)                  output= ["g","i","a","c","o","m","o"]    


    """


def Tuples(chapter):    #(1.9)
    
    #Tuples (1.9)

    """
    Le tuple sono strutture dati semplici e immutabili ovvero che non possono cambiare e si 
    inizializzano utilizzano le parentesi tonde

    tupla = (1,2,3)

    
    In generale le tuple vengono unpacked in altre variabili

    company = ("Amazon", 150, 1998)

    name, employees, birth = company


    Immaginiamo portfolio[] una lista contenente per ogni indice una tupla con 3 elementi,
    possiamo iterare ognuno di questi e effettuare una somma nella seguente maniera:

    total = 0

    for name, price, shares in portfolio:
        total += shares*price
    
    In alternativa possiamo usare una list comprehension

    total = sum([price*shares for _, price, shares in portfolio])

    
    
    """


def Sets(chapter):      #(1.10)
    
    #Sets (1.10)
    
    """

    Un Set è una collezione di oggetti non ordinato, per inizializzarlo si utilizzano le {}

    example = {"giacomo", "daniele", "francesco"}

    In generale si tratta di oggetti immutabili, inoltre non essendo ordinato non è possibile utilizzare gli indici
    Non sono presenti doppioni, se un elemento viene inserito più volte, apparirà comunque una volta sola

    Altro modo per inizializzarlo

    example = set()

    I set comprendono una collezione di operatori utilizzabili tra di loro:

        a = t | s       Unione = Saranno presenti tutti gli elementi di t e di s (sempre univoci)

        a = t & s       Intersezione = Elementi presenti sia in t che in s

        a = t - s       Differenza = In questo caso gli elementi di t che non sono presenti in s

        a = s - t       Differenza = Stessa cosa solo al contrario

        a = t ^ s       Differenza Simmetrica = Il contrario dell'intersezione, ovvero gli elementi che sono presenti o in t o in s ma non in entrambi

    
    Per aggiungere elementi è possibile farlo in due modi:

        .add()      In questo caso si aggiunge un solo elemento

        .update()       In questo caso si agggiungono più elementi

    
    Al contrario per rimuovere gli elementi si utilizzano:

        .remove()       In questo caso se l'elemento non è presente apparirà un errore

        .discard()      In questo caso invece se l'elemento da eliminare non è presente si andrà avanti comunque

    
    

    """


def Dictionaries(chapter):      #(1.11)

    #Dictionaries (1.11)

    """
    
    Un dizionario è una mappatura  chiave:valore  e lo puoi inizializzare utilizzando le {}

    example = {
        
        "name" : "Giona",
        "age"  :    23,
        "wealth" : "money"    
        }

    
    Per verificare la presenza di una chiave si possono utilizzare due modi:

        if "name" in example:
            .....
        else:
            ,,,,,,
        
            
        prova = example.get("name", "default")          Nel caso in cui la chiave "name" è presente allora prova sarà uguale al valore di name, altrimenti avrà "default"

    
    Per rimuovere un elemento si utilizza "del"

    del example["name"]


    N.B. non è possibile usare come chiavi oggetti mutabili quali: liste, set e dizionari


    Esiste anche la dictionary comprehension così formata:

    total = {[s[0]:0 for s in portfolio}


    Per creare un dizionario vuoto ci sono due modi:

        example = {}

        example = dict()

    
    Immaginiamoci una lista con all'interno per ogni elemento una tupla con una coppia di valori: una stringa e un intero.
    E' possibile realizzare un dizionario di questi elementi con chiave il primo elemento (string) e valore il secondo (int).

    example = dict(pair)        con pair che si riferisce a quella lista.


    
    In questo esempio possiamo vedere come attraverso la funzione list() abbiamo inserito all'interno di prova tutte le chiavi, stessa cosa con
    la funzione .keys().
    La differenza tra i due sta che nel secondo caso anche se apportiamo una modifica al dizionario originale, la variabile prova2 tiene traccia della
    modifica.

    dizionario = {
        "nome" : "giacomo",
        "età" : 19,
        "professione" : "trying to be a soft-dev"
        }

    prova = list(dizionario)

    prova2 = dizionario.keys()

    print(prova)
    print (prova2)

    N.B. Nel caso in cui volessi solo i valori utilizza la funzione .values(). Mentre per sia chiave che valore .items()
    
    """


def Iteration_and_Looping(chapter):     #(1.12)

    #Iteration and Looping (1.12)

    """
    
    Il for è uno degli elementi più potenti. 
    è possibile usarlo in molte situazioni.

    la funzione range(i, j [, step]) permette di creare un range di numeri da i fino a <j con un incremento o decremento di step.

    Questo minicapitolo parla brevemente del for e di come viene utilizzato (facendo piccoli esempi) ma molto semplice e con utilizzi già visti.


    """


def Functions(chapter):     #(1.13)

    #Functions (1.13)

    """
    
    Le funzioni vengono definite tramite def, invece per chiamarla basta scrivere il nome e inserire all'interno delle parentesi tonde i vari argo
    menti necessari.

    Durante l'inizializzazione della funzione è possiblile anche definire il tipo di variabile degli argomenti:

    def somma (first : int, second : int)


    Nonostante ciò è possibile "mandare" come argomenti un altro tipo di variabile, e la funzione funzionerà comunque    

    def somma (first: str, second : int):
        sum = first+second
        return sum

    res = somma(2,3)
    print(res)          output= 5

    

    E' possibile ritornare una tupla con più valori, per poi essere suddivisa in più variabili.
    ex.
        def somma (first: str, second : int):
            sum = first+second
            return (first,second)

    primo,secondo = somma(2,3)


    E' possibile assegnare un valore di default ad uno dei parametri della funzione, ma è possibile comunque nella chiamata modificare questo valore
    andando a specificarlo tra gli argomenti.

    Se ci si ricorda i nomi dei vari parametri è possibili andarli a specificare tra gli argomenti, in tal caso l'ordine non è importante.

    Le variabili assegnate all'interno di una funzione hanno scopo solo all'interno di esse. Al contrario però se una variabile è stata
    inizializzata globalmente allora anche la singola funzione potrà usufruirne.
    
    
    """


def Exceptions(chapter):        #(1.14)
    
    #Exceptions (1.14)

    """
    Le eccezioni (excepts) si verificano quando sorge un problema durante l'esecuzione di uno script.
    Per gestire questi problemi si utilizzano per lo appunto le eccezioni, che,
    possono ad esempio: stampare un messaggio, modificare qualcosa ecc.

    ex.
            try:
                print("Inizio del blocco try")
                x = 1 / 0  # Questo solleverà un'eccezione
                print("Fine del blocco try")  # Questo non verrà mai stampato
            except ZeroDivisionError:
                print("Eccezione gestita")

            print("Dopo il blocco except")

    L'eccezione è così gestita:
    Inizia tramite il blocco try: all'interno del quale viene scritto il codice che potrebbe sollevare un errore. 
    Viene fatto ciò perchè se un errore si presenta al di fuori del try questo non verrà gestito dall'eccezione.

    Successivamente si utilizza il blocco except "nome eccezione": per scegliere cosa fare per lo appunto.

    
    N.B.
    Quando viene gestita un eccezione, il programma riparte subito dopo l'eccezione, e NON riparte dove l'eccezione si è verificata, ovvero all'interno
    del blocco try:

    

    Un altro comando utile è "raise". 
    Questo viene utilizzata per due motivi principali:

        1) Se accompagnato da il nome dell'eccezione allora, per far si che questa venga chiamata manualmente. 
            Ovvero viene utilizzata spesso quando a seguito della verifica di una condizione si vuole eseguire un eccezione particolare.
            ex.
            if condizione_non_valida:
                raise Exception("Errore: condizione non valida")

            A seguito di ciò lo script si ferma. Al contrario una semplice eccezione dopo essere stata gestita può permettere la continuazione dello
            script

        2) Se invece non accompagnata da nulla permette di gestire l'eccezione al livello successivo, ad esempio immaginiamoci un eccezione
            avvenuta all'interno di una funzione. Tramite il raise questa viene eseguita dal main.

            def funzione():
                try:
                    x = 1 / 0  # Questo solleverà un'eccezione ZeroDivisionError
                except ZeroDivisionError:
                    print("Eccezione gestita nella funzione")
                    raise  # Risolleva l'eccezione

            try:
                funzione()
            except ZeroDivisionError:
                print("Eccezione gestita fuori dalla funzione")

            N.B. nel caso in cui ci siano delle istruzioni dopo il raise in questo caso non verrano utilizzate.
        
    
    Esiste anche il finally: che crea un blocco successivo al try: che verrà utilizzato come ultima risorsa.

    Il with viene molto utilizzato per script che riguardano lock,files e connessioni di rete.
    Questo perchè spesso questi utilizzi richiedono l'apertura e la chiusura, e tramite il with tutto ciò avviene in automatico.

    Quando usi lock.acquire(), stai cercando di acquisire il lock. Se il lock è già detenuto da un altro thread, il thread chiamante verrà bloccato
    (o restituirà immediatamente False se l' argomento blocking è impostato su False) fino a quando il lock non viene rilasciato.

    D' altra parte, quando usi un lock in un blocco with, Python chiama automaticamente lock.acquire() all' inizio del blocco e lock.release() 
    alla fine del blocco, indipendentemente da come viene lasciato il blocco (ad esempio, se il codice all' interno del blocco genera un' eccezione
    o se il blocco viene lasciato normalmente). Questo è un modo molto comodo e sicuro per gestire i lock, 
    perché garantisce che il lock venga sempre rilasciato, anche se si verifica un errore.

    """


def Program_Termination(chapter):       #(1.15)

    #Program Termination (1.15)

    """
    
    Un programma termina quando non ha più statement da eseguire o nel caso in cui si verifichi un errore.
    E' possibile forzare l'interruzione del programma tramite questo comando:

    raise SystemExit("Something is wrong")

    In generale all'uscita l'interprete cerca di raccimolare più informazioni possibili, nonostante ciò è possibile tramite un modulo (atexit)
    far eseguire delle operazioni alla chiusura dello script

    
    """


def Objects_And_Classes(chapter):       #(1.16)

    #Objects and Classes (1.16)

    """
    

    
    
    """

print("Al prossimo capitolo")