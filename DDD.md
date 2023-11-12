# Model bezpiecznej aplikacji bankowej przy użyciu zasady Domain Driven Design

## Treść zadania

Celem zadania jest zamodelowanie bezpiecznej aplikacji bankowej (fragmentu) wykorzystując zasady Domain Driven Design.

## Opis modelu

Dla danego zadania zdefiniowano cztery konteksty: Zarządzanie Kontami, Uwierzytelnianie, Zarządzanie Przelewami oraz Współdzielone Jądro. Skupiono się głównie nad rozwinięciem kontekstu Zarządzania Kontami.

| ![bank_model_DDD](https://github.com/mwiszenko/task1/assets/45533659/4c664490-f5fd-467c-a68a-c44da6a8fb14) |
|:--:| 
| Diagram modelu |

## Agregaty

Zdefiniowano trzy agregaty: KontoBankowe, Użytkownik, oraz Przelew.

## Encje

### Użytkownik

- login - String, unikatowy
- hasło - String, zaszyfrowane
- IdUżytkownika

### KontoBankowe

Atrybuty:

- nazwa - String
- numerKonta - String
- dataOtwarcia - String
- TypKonta - Enum
- SaldoKonta
- Klient
- IdKonta

### Klient

- imię - String
- nazwisko - String
- dataUrodzenia - String
- pesel - String, unikalny
- Adres
- DaneKontaktowe
- IdKlienta

### Przelew

- tytuł - String
- data - String
- WartośćPrzelewu
- IdTransakcji

## Obiekty wartości

### SaldoKonta

- kwota - Decimal
- waluta - String

### DaneKontaktowe

- email - String
- telefon - String

### Adres

- ulica - String
- miasto - String
- kodPocztowy - String

### WartośćPrzelewu

- kwota - Decimal
- waluta - String

### IdKonta

- identyfikator - String, unikalny

### IdUżytkownika

- identyfikator - String, unikalny

### IdKlienta

- identyfikator - String, unikalny

### IdTransakcji

- identyfikator - String, unikalny
