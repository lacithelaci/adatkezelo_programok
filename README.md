# 🎬 MovieReview – Filmes véleményező rendszer

## 📌 Leírás
Ez a projekt egy filmes véleményező alkalmazás, amely lehetővé teszi **felhasználók (Person)**, **filmek (Movie)** és **vélemények (Review)** kezelését.  
A cél egy olyan rendszer létrehozása, ami képes valósághű adatok generálására, tárolására, feldolgozására és exportálására különböző formátumokban (CSV, JSON, XLSX).  

A program a [Faker](https://faker.readthedocs.io/) könyvtárat használja az adatok előállításához, és támogatja az adattípusok közötti relációk létrehozását (1:N kapcsolatok).

---

## ⚡ Funkcionalitás
- **Adatgenerálás**
  - Véletlenszerű személyek, filmek és vélemények előállítása.
  - Összetett kapcsolatok létrehozása az adattípusok között (pl. egy felhasználó több véleményt is írhat).
- **Adatkezelés**
  - Adatok tárolása és visszatöltése CSV, JSON és XLSX formátumban.
  - Típusonként külön fájlok / munkalapok létrehozása exportáláskor.
- **Importálás és exportálás**
  - Adatok egyszerű visszatöltése a korábban mentett állapotból.
  - Könnyen feldolgozható, jól strukturált kimeneti formátumok.
- **Kapcsolatok kezelése**
  - Person ↔ Review: 1:N kapcsolat  
  - Movie ↔ Review: 1:N kapcsolat
- **Bővíthetőség**
  - Új adattípusok és extra funkciók egyszerűen hozzáadhatók.
  - Adatbázis-integráció (pl. Oracle) támogatott.

---

## 🧭 Telepítés és futtatás

### 1. Követelmények
- Python **3.10** vagy újabb  
- Függőségek telepítése:  
  ```bash
  pip install -r requirements.txt
```
python main.py

