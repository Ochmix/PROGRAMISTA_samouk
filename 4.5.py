def yolo():
    """
    Zmienia łańcuch znaków na liczbę stałoprzecinkową
    """
    
    x = input("Podaj liczbę :")
    try:
        x = float(x)
        
    except ValueError:
        print("Liczbę frajerze!")
    return print(x)
yolo()
