# gezogene Farbe kartenwert // 13
# gezogene Karte kartenwert % 13
import functools
# es gibt 52 Karten

# mögliche Kombinationen
# 1. Paar - zwei gleiche Zahlen
# 2. Zwei Paare - zwei Paare
# 3. Drilling - drei gleiche Zahlen
# 4. Straight - 5 aufeinanderfolgende Zahlen
# 5. Flush - 5 gleiche Farben
# 6. Full House - Drilling und Paar
# 7. Vierling - vier gleiche Zahlen
# 8. Straight Flush - Straight und Flush
# 9. Royal Flush - 10, Bube, Dame, K, Ass und gleiche Farben

import random
import sys
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Funktion {func.__name__} mit {args[0]} Versuchen fertig in {run_time:.4f} Sekunden")
        return value
    return wrapper_timer

def getcolor(cardvalue, amountonecardset):
    number = cardvalue // amountonecardset
    return number

def getnumber(cardvalue, amountonecardset):
    number = cardvalue % amountonecardset
    return number

def ispair(numbers):
    value_count = {}
    for n in numbers:
        if n in value_count:
            value_count[n] += 1
        else:
            value_count[n] = 1
    for count in value_count.values():
        if count == 2:
            return True
    return False

def istwopairs(numbers):
    value_count = {}
    pairs = 0
    for n in numbers:
        if n in value_count:
            value_count[n] += 1
        else:
            value_count[n] = 1
    for count in value_count.values():
        if count == 2:
            pairs += 1
    return pairs == 2

def isdrilling(numbers):
    value_count = {}
    for n in numbers:
        if n in value_count:
            value_count[n] += 1
        else:
            value_count[n] = 1
    for count in value_count.values():
        if count == 3:
            return True
    return False

def isstraight(numbers):
    sorted_numbers = sorted(numbers)
    for i in range(1, len(sorted_numbers)):
        if sorted_numbers[i] - sorted_numbers[i - 1] != 1:
            return False
    return True

def isflush(colors):
    for i in range(1, len(colors)):
        if colors[i] != colors[i - 1]:
            return False
    return True

def isfullhouse(numbers):
    value_count = {}
    has_triple = False
    has_pair = False

    for n in numbers:
        if n in value_count:
            value_count[n] += 1
        else:
            value_count[n] = 1

    for count in value_count.values():
        if count == 3:
            has_triple = True
        elif count == 2:
            has_pair = True

    if has_triple and has_pair:
        return True
    return False

def isvierling(numbers):
    value_count = {}
    for n in numbers:
        if n in value_count:
            value_count[n] += 1
        else:
            value_count[n] = 1
    for count in value_count.values():
        if count == 4:
            return True
    return False

def isstraightflush(numbers, colors):
    return isstraight(numbers) and isflush(colors)

def isroyalflush(numbers, colors):
    if isstraightflush(numbers, colors) and sorted(numbers)[0] == 8:
        return True
    return False

def pokerspiel(amountofcards):
    cards = []
    colors = []
    numbers = []
    for i in range(amountofcards):
        card = random.randint(0, 51)
        while card in cards:
            card = random.randint(0, 51)
        cards.append(card)
        colors.append(getcolor(card, 13))
        numbers.append(getnumber(card, 13))
    if isroyalflush(numbers, colors) == True:
        return "Royal Flush"
    if isstraightflush(numbers, colors) == True:
        return "Straight Flush"
    if isvierling(numbers) == True:
        return "Vierling"
    if isfullhouse(numbers) == True:
        return "Full House"
    if isflush(colors) == True:
        return "Flush"
    if isstraight(numbers) == True:
        return "Straight"
    if isdrilling(numbers) == True:
        return "Drilling"
    if istwopairs(numbers) == True:
        return "Zwei Paare"
    if ispair(numbers) == True:
        return "Paar"
    return "Nichts"

@timer
def pokersimulation(amountofgames):
    anzkarten = int(input("Mit wie vielen Karten soll gespielt werden? "))
    if anzkarten != 5 and anzkarten != 7:
        print("Ungültige Eingabe")
        return
    kombinationen = {
        "Nichts": 0,
        "Paar": 0,
        "Zwei Paare": 0,
        "Drilling": 0,
        "Straight": 0,
        "Flush": 0,
        "Full House": 0,
        "Vierling": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }
    for i in range(amountofgames):
        kombination = pokerspiel(anzkarten)
        if kombination in kombinationen:
            kombinationen[kombination] += 1
        else:
            kombinationen[kombination] = 1

    print("--------------------------------------------")
    print(f"Es wurden {amountofgames} Poker-Spiele durchgeführt")
    print("--------------------------------------------")
    print("Kombination          | Anzahl     | Anteil")
    print("--------------------------------------------")
    for key in kombinationen:
        anteil = kombinationen[key] / amountofgames * 100
        print(f"{key:<20} | {kombinationen[key]:<10} | {anteil:>8.2f}%")

    return "--------------------------------------------"

#print(ispair([1,3,12,14]))
#print(istwopairs([1,3,16,14]))
#print(isdrilling([5,18,31,7,43]))
#print(isstraight([5,19,7,8,9]))
#print(isflush([14,15,16,17,18]))
#print(isfullhouse([5,18,31,1,14]))
#print(isvierling([5,18,31,7,44]))
#print(isstraightflush([14,15,16,17,18]))
#print(isroyalflush([8,9,10,11,12]))

def main():
    anzgames = int(input("Wie oft soll die Poker-Simulation durchgeführt werden? "))
    if anzgames < 1:
        print("Ungültige Eingabe")
        return
    print(pokersimulation(anzgames))
    #print("Richtige Anteile aus Internet:")
    #print("Nichts: 50,12%, Paar: 42.26%, Zwei Paare: 4.75%, Drilling: 2.11%, "
    #      "Straight: 0.39%, Flush: 0.2%, Full House: 0.14%, Vierling: 0.02%, Straight Flush: 0.00%, Royal Flush: 0.00%")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        sys.exit(1)