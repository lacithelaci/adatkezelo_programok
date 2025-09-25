# Projekt neve

## Leírás
Ez a projekt az *Adatkezelő programok fejlesztése* féléves beadandó feladata.  
A program célja egy adathalmaz generálása, tárolása és feldolgozása a félév során tanult adatformátumok (CSV, JSON, XLSX) segítségével.  
Az adatok a [Faker](https://faker.readthedocs.io/) könyvtár használatával kerülnek előállításra, több adattípus kezelésével és közöttük fennálló kapcsolatok definiálásával.  

## Funkcionalitás
- Adathalmaz generálása a Faker API segítségével.
- Többféle adattípus (pl. Person, Car, saját típus) kezelése.
- Kapcsolatok támogatása az adattípusok között (1:1, 1:N, N:M).
- Exportálás:
  - **CSV**: minden adattípus külön fájl, első sor a mezők neveivel.
  - **JSON**: minden adattípus külön lista, rekordokat leíró dokumentumokkal.
  - **XLSX**: minden adattípus külön munkalapon.
- Importálás: az adatok visszaolvasása a fenti formátumokból.
- (Közepes szinttől) harmadik, saját tervezésű típus is.
- (Jó szinttől) Oracle SQL kapcsolat, adattáblák és kapcsolatok létrehozása.
- (Jeles szinttől) extra funkciók az adatkezeléshez.  

## Telepítés és futtatás
1. **Követelmények**
   - Python 3.10
   - Függőségek (telepíthetők `requirements.txt` alapján):  
     ```bash
     pip install -r requirements.txt
     ```
2. **Futtatás**
   ```bash
   python main.py
