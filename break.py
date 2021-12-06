# Sursa 1: https://math.stackexchange.com/questions/28955/how-to-break-xor-cipher-with-repeating-key al 2-lea raspuns
# Sursa 2: https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/


from collections import Counter


def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


def decrypt(key, binput):
    rez = []
    i = 0
    kl = len(key)
    for index, value in enumerate(binput):
        rez.append(value ^ key[i])
        i = (i + 1) % kl  # Rotate through key
    return rez


candidates = []
with open("output", "rb") as f:
    binput = bytearray(f.read())
    for k in range(10, 16):
        key = []
        for j in range(k):
            highest = []
            for i in range(j, len(binput), k):
                highest.append(binput[i] ^ 0x20)
            key.append(chr(most_frequent(highest)))

        isValid = True

        for i in key:
            if not i.isalnum():
                isValid = False
                break
        if isValid:
            candidates.append("".join(key))

with open("output", "rb") as f:
    foutput = bytearray(f.read())

    for key in candidates:
        lkey = []
        lkey[:0] = key
        lkey = [ord(i) for i in lkey]

        dec = [chr(i) for i in decrypt(lkey, foutput)]
        dec = "".join(dec)

        romana = ["acasa", "acelasi", "acest", "acum", "aer", "ai", "ajuta", "ajutor", "al", "ale", "alerga", "alte",
                  "ani",
                  "apa", "apoi", "aproape", "ar", "asa", "asemenea", "asta", "astfel", "asupra", "atunci", "au", "avut",
                  "aur",
                  "baiat", "bani", "barbat", "barca", "bati", "bine", "bucati", "Bucuresti", "bun", "ca", "ca", "caine",
                  "cald",
                  "cand", "cantec", "cap", "capabil", "capat", "care", "casa", "cat", "cauza", "caz", "ce", "ceea",
                  "cei",
                  "cele", "cere", "chiar", "cine", "citit", "copil", "cred", "cu", "cuib", "cum", "cutie", "cuvant",
                  "da",
                  "daca", "dar", "de", "deal", "decat ", "deoarece", "despre", "devreme", "diferite", "dimineata",
                  "din",
                  "dintre", "doar", "doi", "doua", "dreapta", "drum", "dupa", "ei", "el", "ele", "emotii", "este",
                  "era", "etaj",
                  "eu", "exemplu", "exista", "face", "familie", "fata", "femeie", "ferestre", "fi", "fie", "fiecare",
                  "flori",
                  "foarte", "foc", "forma", "fost", "frate", "gasi", "grup", "guvern", "haina", "hartie", "ia", "iar",
                  "iarba",
                  "iata", "iepure", "imagine", "in", "inainte", "inapoi", "inca", "inceput", "incercati ", "inel",
                  "intoarce",
                  "intre", "intr-un", "joc", "jos", "la", "langa", "lapte", "lasa", "le", "lemn", "linie", "loc", "lor",
                  "lucreaza", "lucru", "lui", "lume", "lung", "luni", "mai", "mama", "mana ", "mare", "masa", "masina",
                  "mea",
                  "mere", "mi", "mic ", "mijloc", "mine", "mingea", "minute", "mod", "mult", "Mures", "nevoie", "nici",
                  "niciodata", "noapte", "noastre", "noi", "nu", "numai", "numar", "nume", "oamenii", "obtine", "ochi",
                  "oi",
                  "om", "ori", "orice", "ou", "paine", "pana", "pantofi", "papusa", "par ", "parinti", "parte",
                  "pasare", "pat",
                  "pe", "pentru", "persoana", "peste", "peste", "pisica", "ploaie", "poate", "pom", "porc", "pot",
                  "primul",
                  "prin", "proprii", "punct", "putin", "raspuns", "rata", "rau", "repede", "rog", "Romania", "sa", "sa",
                  "saptamana", "sau", "scazuta", "scoala", "scoala", "scrie", "se", "seminte", "si", "simt", "singur",
                  "soare",
                  "sora", "spre", "spune", "stanga", "stiu", "strada", "strain", "sunt", "sus", "tara", "tare",
                  "Tarnaveni",
                  "tarziu", "tata", "televizor", "teren", "timp", "toate", "tort", "toti", "trebuie", "trei", "uite",
                  "ultimul",
                  "un", "unde", "unor", "unui", "urmator", "urs", "usa", "utilizare", "va", "va", "vaca", "vant",
                  "vechi",
                  "veverita", "viata", "vin", "vor", "vrei", "zapada", "zi", "ziua"]

        nrcuv = 0
        for cuv in romana:
            if cuv in dec:
                nrcuv += 1

        if nrcuv >= len(romana) / 2:
            print(key)
