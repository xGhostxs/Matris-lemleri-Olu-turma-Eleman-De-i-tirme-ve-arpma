
---

### matris_islemleri.py

```python
import numpy as np

def matrix(size, value_range):
    """Belirtilen boyutta ve aralıkta iki rastgele tam sayılı kare matris oluşturur."""
    A = np.random.randint(value_range[0], value_range[1] + 1, (size, size))
    B = np.random.randint(value_range[0], value_range[1] + 1, (size, size))
    return A, B

def degistir(A, B, row, col):
    """A ve B matrislerinin belirtilen satır ve sütunundaki elemanların yerlerini değiştirir."""
    A[row, col], B[row, col] = B[row, col], A[row, col]
    return A, B

def main():
    size = 5
    value_range = (0, 10)

    while True:
        A, B = matrix(size, value_range)

        print("Matris A:\n", A) 
        print("Matris B:\n", B)
        
        try:
            row = int(input("Satır numarasını girin (0-4): "))
            col = int(input("Sütun numarasını girin (0-4): "))
            if row < 0 or row >= size or col < 0 or col >= size:
                print("Geçersiz satır veya sütun numarası.")
                continue
            else:
                A, B = degistir(A, B, row, col)
                print("Güncellenmiş Matris A:\n", A)
                print("Güncellenmiş Matris B:\n", B)
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue

        C = np.dot(A, B)
        print("Matris C (A x B):\n", C)

        choice = input("Devam etmek istiyor musunuz? (E/H): ")
        if choice.lower() != "e":
            break

    print("Program sonlandırılıyor... Hoşçakal!")

if __name__ == "__main__":
    main()
