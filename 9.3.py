import csv

with open("filmy.txt", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["Top Gun",
                    "Ocean's Eleven",
                    "Raport mniejszośći"])
    write.writerow(["Pulp fiction",
                    "Człowiek w ogniu",
                    "Seksmisja"])    
