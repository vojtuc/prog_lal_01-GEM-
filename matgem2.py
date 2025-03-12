from fractions import Fraction as F

def gen_I(n):#generuje jednotkovou matici tvaru nxn
    I = []
    for i in range(n):
        line = [F(i==j) for j in range(n)]
        I.append(line)
    return I
    
def mult(a, line):#ekvivalentní úprava násobení řádku číslem
    return [a*i for i in line]

def add(line1, line2):#ekvivalentní úprava přičtení jiného řádku
    return [line1[i] + line2[i] for i in range(len(line1))]
  
#i index řádku, j index sloupce
def inv(X):#počítá inverzní matici pomocí Gaussovy eliminační metody
    A = X.copy()
    n = len(A)
    I = gen_I(n)#vygeneruje jednotkovou matici stejné velikosti, jakou má zadaná
    
    for i in range(n):#prochází matici po hlavní diagonále
        if A[i][i] == 0:#pokud je prvek na diagonále 0
            for j in range(i, n):#prochází prvky pod ním
                if A[j][i] != 0:#pokud najde nenulový
                    I[i], I[j] = I[j], I[i]#provede stejnou úpravu (jako v dalším řádku) s jednotkovou maticí
                    A[i], A[j] = A[j], A[i]#prohodí řádky v matici, tak aby na diagonále bylo nenulové číslo
                    break
            else:#pokud cyklus proběhne celý, tak pod nulou na diagonále již není nenulové číslo, tzn. matice není regulární
                return "ne"
            
        I[i] = mult(1/A[i][i], I[i])#provede stejnou úpravu (jako v dalším řádku) s jednotkovou maticí
        A[i] = mult(1/A[i][i], A[i])#vynásobí daný řádek převrácenou hodnotou čísla na diagonále, takže na diagonále vyrobí 1
        
        for j in range(n):#prochází ostatní čísla v daném sloupci
            if i != j:
                I[j] = add(mult(-A[j][i], I[i]), I[j])#provede stejnou úpravu (jako v dalším řádku) s jednotkovou maticí
                A[j] = add(mult(-A[j][i], A[i]), A[j])#celý sloupec nuluje pomocí jedničky na diagonále
        
    return I#vrátí matici, která vznikla stejnými úpravami z jednotkové

print("Tento program počítá inverzní matici k zadaným. Program by měl počítat přesně, pro výpis výsledné inverze se ale všechny prvky zaokrouhlují na dvě desetinná místa.")
while True:
    n = int(input("Zadejte počet řádků čtvercové matice, ke které chcete spočítat inverzi: "))
    A = []
    for i in range(n):
        line  = list(map(lambda x:F(x), input(f"Zadejte {i+1}. řádek matice. Čísla v řádku oddělujte mezerami, jiné znaky nezadávejte: ").split(" ")))
        while len(line) != n:
            print("Špatná délka řádku")
            line  = list(map(lambda x:F(x), input(f"Zadejte {i+1}. řádek matice. Čísla v řádku oddělujte mezerami, jiné znaky nezadávejte: ").split(" ")))
        A.append(line)
    invA = inv(A)
    if invA == "ne":
        print("Zadaná matice není regulární")
    else:
        print("Inverze k dané matici je:")
        for i in invA:
            print(list(map(lambda x:round(float(x), 2), i)))
    if input("""Zadejte "n", pokud chcete ukončit program, jinak napište cokoli jiného: """) == "n":
        break


