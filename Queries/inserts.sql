ALTER SEQUENCE konto_nr_konta_seq
restart with 1001;

ALTER SEQUENCE karta_nr_karty_seq
restart with 5001;


INSERT INTO oddzial_banku ( adres) VALUES ('Rakowicka 12');
INSERT INTO oddzial_banku ( adres) VALUES ('Krowoderska 12');

INSERT INTO klient (imie, nazwisko, pesel, mieszkanie, najblizszy_oddzial_id) VALUES ('Jan', 'Kowalski', '12345678901', true, 1);
INSERT INTO klient (imie, nazwisko, pesel, mieszkanie, najblizszy_oddzial_id) VALUES ('Piotr', 'Nowak', '23456789012', false, 2);
INSERT INTO klient (imie, nazwisko, pesel, mieszkanie, najblizszy_oddzial_id) VALUES ('Pola', 'Duda', '12345678903', false, 1);
INSERT INTO klient (imie, nazwisko, pesel, mieszkanie, najblizszy_oddzial_id) VALUES ('Katarzyna', 'Cegla', '23456789013', true, 2);
INSERT INTO klient (imie, nazwisko, pesel, mieszkanie, najblizszy_oddzial_id) VALUES ('Katarzyna', 'Opiols', '23456789017', false, 2);


INSERT INTO konto (klient_id, saldo) VALUES ( 1, 5001);
INSERT INTO konto ( klient_id, saldo) VALUES ( 2, 7500);
INSERT INTO konto ( klient_id, saldo) VALUES ( 3, 10000);
INSERT INTO konto ( klient_id, saldo) VALUES ( 4, 15000);

INSERT INTO karta ( nr_konta, rodzaj_karty) VALUES ( 1001, 'Debit');
INSERT INTO karta ( nr_konta, rodzaj_karty) VALUES ( 1002, 'Credit');
INSERT INTO karta ( nr_konta, rodzaj_karty) VALUES ( 1003, 'Debit');
INSERT INTO karta ( nr_konta, rodzaj_karty) VALUES ( 1004, 'Credit');

INSERT INTO typ_kredytu ( oprocentowanie, maksymalna_kwota, pula_srodkow, aktualna_pula_srodkow, oddzial_id) VALUES (2, 100000, 500000, 500000, 1);
INSERT INTO typ_kredytu ( oprocentowanie, maksymalna_kwota, pula_srodkow, aktualna_pula_srodkow, oddzial_id) VALUES (8, 150000, 500000, 500000, 1);
INSERT INTO typ_kredytu ( oprocentowanie, maksymalna_kwota, pula_srodkow, aktualna_pula_srodkow, oddzial_id) VALUES ( 2, 200000, 500000, 500000, 2);
INSERT INTO typ_kredytu ( oprocentowanie, maksymalna_kwota, pula_srodkow, aktualna_pula_srodkow, oddzial_id) VALUES ( 8, 250000, 750000, 750000, 2);

INSERT INTO kredyt_detale (klient_id, typ_kredytu_id, kwota, data_zaciagniecia, data_splaty) VALUES (1, 4, 5000, '2023-01-15', null);
INSERT INTO kredyt_detale (klient_id, typ_kredytu_id, kwota, data_zaciagniecia, data_splaty) VALUES (2, 2, 7500, '2020-02-20', '2023-02-20');
INSERT INTO kredyt_detale (klient_id, typ_kredytu_id, kwota, data_zaciagniecia, data_splaty) VALUES (3, 1, 100000, '2023-03-25', null);
INSERT INTO kredyt_detale (klient_id, typ_kredytu_id, kwota, data_zaciagniecia, data_splaty) VALUES (4, 2, 150000, '2023-04-30', '2023-04-30');

INSERT INTO przelew (nr_konta_nadawcy, nr_konta_odbiorcy, kwota) VALUES (1001, 1002, 1000);
INSERT INTO przelew (nr_konta_nadawcy, nr_konta_odbiorcy, kwota) VALUES (1002, 1001, 2500);
INSERT INTO przelew (nr_konta_nadawcy, nr_konta_odbiorcy, kwota) VALUES (1003, 1004, 5000);

INSERT INTO bankomat (oddzial_id) VALUES(1);
INSERT INTO bankomat (oddzial_id) VALUES(2);
INSERT INTO bankomat (oddzial_id) VALUES(1);
  
INSERT INTO transakcja (bankomat_id, nr_karty, wplata_wyplata) VALUES (1, 5001, 1000);
INSERT INTO transakcja (bankomat_id, nr_karty, wplata_wyplata) VALUES (2, 5002, 2500);
