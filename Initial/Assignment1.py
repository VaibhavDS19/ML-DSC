thriller = ["Dark", "Mindhunter", "Parasite", "Inception", "Insidious",
            "Interstellar", "Prison Break", "Money Heist", "War", "Jack Ryan"]

comedy = ["Friends", "3 Idiots", "Brooklyn 99", "How I Met Your Mother",
          "Rick And Morty", "The Big Bang Theory", "The Office", "Space Force"]

found = "false"

movie = input()

for i in thriller:
    if i.upper() == movie.upper():
        found = "thriller"
        break

if found == "false":
    for i in comedy:
        if i.upper() == movie.upper():
            found == "comedy"
            break

if found == "false":
    print("It is neither thriller nor comedy.")
else:
    print(f"It is a {found}")
