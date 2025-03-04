import random

from python.Lib.idlelib.idle_test.test_editor import insert


class Domanda:
    def __init__(self,domanda, livello, risposte, giusta):
        self.domanda = domanda
        self.livello = livello
        self.risposte = risposte
        self.giusta = giusta

def aggiungiDomanda(domanda):
    if domanda.livello not in dizionarioDomande:
        dizionarioDomande[domanda.livello] = []
    dizionarioDomande[domanda.livello].append(domanda)


class Giocatore:
    def __init__(self, nome, punteggio):
        self.nome = nome
        self.punteggio = punteggio

dizionarioDomande = {}
giocatori = []


with open("domande.txt", "r", encoding="utf-8") as file:
    righe = file.readlines()
i = 0
while i < len(righe):
    d = Domanda(righe[i].strip(), righe[i+1].strip("\n"), [righe[i+2].strip("\n"), righe[i+3].strip("\n"), righe[i+4].strip("\n"), righe[i+5].strip("\n")], righe[i+2].strip("\n"))
    aggiungiDomanda(d)
    i += 7
file.close()
with open("punti.txt", "r", encoding="utf-8") as filePunti:
    righe1 = filePunti.readlines()
t =0
while t < len(righe1):
    parts = righe1[t].strip("\n").split(" ")
    g = Giocatore(parts[0], int (parts[1]))
    giocatori.append(g)
    t += 1



class Game:
    def __init__(self,domandegioco):
        self.domandegioco = domandegioco

    def inizia(self):
        livelli = sorted(self.domandegioco.keys())
        punteggio = 0
        for livello in livelli:
            if not self.domandegioco[livello]:
                continue
            domanda_casuale = random.choice(self.domandegioco[livello])
            print(f"Livello {domanda_casuale.livello}) {domanda_casuale.domanda}")
            risposta = domanda_casuale.giusta
            random.shuffle(domanda_casuale.risposte)
            print(f"1. {domanda_casuale.risposte[0]}")
            print(f"2. {domanda_casuale.risposte[1]}")
            print(f"3. {domanda_casuale.risposte[2]}")
            print(f"4. {domanda_casuale.risposte[3]}")
            scelta = input("Inserisci la risposta: ")
            if risposta == domanda_casuale.risposte[int(scelta) - 1]:
                print("Risposta corretta!")
                punteggio += 1
            else:
                n = 0
                for k in range(0, 4):
                    if domanda_casuale.risposte[k] == risposta:
                        n = k + 1
                print(f"Risposta sbagliata! La risposta corretta era {n}")
                print("\n",f"Hai totalizzato {punteggio} punti")
                nome = input("Inserisci il tuo nickname: ")
                giocatori.append(Giocatore(nome, punteggio))
                break
        if punteggio == 5:
            print("Hai finito! Hai totalizzato 5 punti")
            nome = input("Inserisci il tuo nickname: ")
            giocatori.append(Giocatore(nome, punteggio))
        giocatori.sort(key=lambda gi: gi.punteggio, reverse=True)
        with open("punti.txt", "w", encoding="utf-8") as puntiFinale:
            for giocatore in giocatori:
                puntiFinale.write(f"{giocatore.nome} {giocatore.punteggio}\n")



g = Game(dizionarioDomande)
g.inizia()