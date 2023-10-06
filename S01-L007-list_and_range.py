
def new_list(list,n):
    return list.copy()[:n]




colors = ["red", "oragne", "green", "violet", "blue", "yellow"]

for x in range(1, len(colors) + 1):
    colors_new = new_list(colors, x)
    print(colors_new)

text = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja," \
       " która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może " \
       "utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale " \
       "tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
text_sliced = text[text.find("("):text.find(")") + 1]
print(text_sliced)