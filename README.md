# Proiect ASC 0x00
Criptare XOR

# Etapa 1
## Folosire
(parola data ca exemplu nu este folosita in criptarea fisierului output)

### Criptare
```bash
python encrypt.py 0ParolaLunga input.txt output
```

### Decriptare
```bash
python decrypt.py output 0ParolaLunga output.txt
```
# Etapa 2
## Date
Numele echipei: The Cyphers

Numele echipei adverse: G.E.T. team

Cheia echipei adverse: x1y2z3ABCdef

## Explicatii
### Metoda 1
Am folosit [crack.py](https://github.com/fredtux/ASC_Proiect_0x00/blob/main/crack.py) pentru a face XOR intre input si output. Deoarece output = input ^ cheie, atunci input ^ output = input ^ input ^ cheie = cheie. Deoarece cheia se repeta, dar stim din enunt ca este intre 10 si 15 caractere, am incercat toate variantele de primele 10 pana la 15 caractere din cheie si am comparat inputul criptat cu cheia rezultata cu outputul. Daca erau egale, am gasit cheia, iar numarul de pasi este mic.

### Metoda 2
Scriptul folosit si sursa de inspiratie se afla in [break.py](https://github.com/fredtux/ASC_Proiect_0x00/blob/main/break.py) .

Ne-am folosit din nou de faptul ca avem cheia intre 10 si 15 caractere. Am incercat in prima faza calcularea lungimii cheii cu ajutorul distantei Hamming, dar pentru ca este un proces prea complex pentru python (sau nu l-am implementat corect), am facut un script care returneaza cheile candidat. 

Pentru aflarea unei chei candidat ne-am bazat pe faptul ca cel mai folosit caracter din limba romana este spatiul. Asa ca am luat toti octetii din k in k (10 <= k <= 15, adica lungimea cheii) si am gasit cel mai folosit octet, pe care l-am XORat cu 0x20, adica spatiu. Asa am obtinut primul caracter. Apoi am trecut la caracterul cu numarul 1 de unde am inceput parcurgerea tuturor octetilor din k in k la fel ca mai inainte. Dat fiind un text suficient de lung, aceasta metoda are o probabilitate foarte mare de a gasi cheia.

Pentru filtrarea cheilor candidat am folosit excluderea celor care nu au caractere alfanumerice ca in enunt, asa ca au ramas doar o parte din chei. Nefiind multe, le-am incercat pe rand si am cautat intr-o lista cu cele mai folosite cuvinte din romana cate apar. Daca vocabularul fisierului decriptat continea cel putin jumatate din lista, atunci afisam cheia.

Ambii pasi tin de probabilitati, dar dat fiind un text destul de mare, atunci cheia afisata va fi unica.
