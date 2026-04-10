\# Online Sales Analysis



\## Opis projekta

Ovaj projekat predstavlja sistem za upravljanje online prodajom koristeći Python i OOP principe.  

Omogućava rad sa proizvodima, upravljanje inventarom i korpom kupca.



\---



\## Klase i funkcionalnosti



\### Product

\- Atributi: `name`, `price`, `quantity`

\- Metodi:

&#x20; - `display\_info()` – prikazuje informacije o proizvodu

&#x20; - `update\_quantity(new\_quantity)` – ažurira količinu proizvoda



\### ProductManager

\- Atribut: lista svih dostupnih proizvoda

\- Metodi:

&#x20; - `add\_product(product)` – dodaje novi proizvod

&#x20; - `show\_products()` – prikazuje sve proizvode

&#x20; - `total\_value()` – prikazuje ukupnu vrednost inventara

&#x20; - `remove\_product(product\_name)` – uklanja proizvod po imenu



\### Cart

\- Atribut: `cart\_items` – lista proizvoda u korpi

\- Metodi:

&#x20; - `add\_product(product)` – dodaje proizvod u korpu

&#x20; - `total\_price()` – računa ukupnu vrednost korpe

&#x20; - `show\_cart()` – prikazuje sadržaj korpe



\---



\## Git funkcionalnosti

\- Korišćene grane:

&#x20; - `main`

&#x20; - `add-product-removal`

&#x20; - `add-cart-functionality`

\- Merge operacije i simulacija konflikta

\- Upravljanje verzijama i commit poruke



\---



\## Pokretanje projekta

1\. Otvori CMD/terminal u folderu projekta

2\. Pokreni:



```bash

python main.py

