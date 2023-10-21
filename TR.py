from tkinter import *

#---------------------------------GUI------------------------------
# Ein Fenster erstellen
#fenster = Tk()

# Den Fenstertitle erstellen
#fenster.title("Einfacher Taschenrechner")


# In der Ereignisschleife auf Eingabe des Benutzers warten.
#fenster.mainloop()
#------------------------------------------------------------------


while True:
    expr = str(input("Geben Sie einen arithmetischen Input (ohne Klammern) ein (oder 'Exit', falls Sie beenden wollen): "))
    if expr.lower() == "exit":
        break


    try:
        result = eval(expr)
        print("Ergebnis:", result)
    except Exception as e:
        print("Ungültige Eingabe:", e)

print("Taschenrechner beendet.")


def eval(expr):

    #Scanner teilt Tokens in kleinstmöglichste Einheit auf (z.B 3+4 in [3, +, 4] oder 3.45^2 in [3.45, ^, 2])
    arr = scan(expr)
    #Parsing (Grammatik)
    
    #Arith([^, *, +, -] Arith | / (1-9)*)*
    #Arith -> 0|1|2|3|4|5|6|7|8|9

    return result


#Ist Ausdruck regulär?
def scan(expr):
    return []

def parse(arr):
    return True