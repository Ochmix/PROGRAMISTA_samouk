num = [1, 5, 7, 8, 10]

while True:
    x = input("Zgadnij liczbę z listy: (q aby zakończyć)")
    if x == "q":
        break
    try:
        x = int(x)
    except ValueError:
        print("Wpisz liczbę lub naciśnij q aby zakończyć")
        continue
    if x in num:
        print("Zgadłeś! (q aby zakończyć)")
    else:
        print("Niezgadłeś... (q aby zakończyć)")
    
