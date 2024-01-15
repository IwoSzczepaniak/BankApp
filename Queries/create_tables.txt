CREATE TABLE IF NOT EXISTS oddzial_banku (
    oddzial_id SERIAL PRIMARY KEY,
    adres VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS klient (
    klient_id SERIAL PRIMARY KEY,
    imie VARCHAR(20) NOT NULL,
    nazwisko VARCHAR(20) NOT NULL,
    pesel VARCHAR(11) NOT NULL,
    mieszkanie BOOLEAN NOT NULL,
    najblizszy_oddzial_id INT NOT NULL,
    FOREIGN KEY (najblizszy_oddzial_id) REFERENCES oddzial_banku (oddzial_id)
);

CREATE TABLE IF NOT EXISTS konto (
    nr_konta SERIAL PRIMARY KEY,
    klient_id INT,
    saldo INT,
    FOREIGN KEY (klient_id) REFERENCES klient (klient_id)
);

CREATE TABLE IF NOT EXISTS karta (
    nr_karty SERIAL PRIMARY KEY,
    nr_konta INT,
    rodzaj_karty VARCHAR(20),
    FOREIGN KEY (nr_konta) REFERENCES konto (nr_konta)
);

CREATE TABLE IF NOT EXISTS typ_kredytu (
    typ_kredytu_id SERIAL PRIMARY KEY,
    oprocentowanie INT,
    maksymalna_kwota INT,
    pula_srodkow INT,
    aktualna_pula_srodkow INT,
    oddzial_id INT,
    FOREIGN KEY (oddzial_id) REFERENCES oddzial_banku (oddzial_id)
);

CREATE TABLE IF NOT EXISTS kredyt_detale (
    kredyt_id SERIAL PRIMARY KEY,
    klient_id INT,
    typ_kredytu_id INT,
    kwota INT,
    data_zaciagniecia DATE,
    data_splaty DATE,
    FOREIGN KEY (klient_id) REFERENCES klient (klient_id),
    FOREIGN KEY (typ_kredytu_id) REFERENCES typ_kredytu (typ_kredytu_id)
);

CREATE TABLE IF NOT EXISTS przelew (
    przelew_id SERIAL PRIMARY KEY,
    nr_konta_nadawcy INT NOT NULL,
    nr_konta_odbiorcy INT NOT NULL,
    kwota INT NOT NULL,
    FOREIGN KEY (nr_konta_nadawcy) REFERENCES konto (nr_konta),
    FOREIGN KEY (nr_konta_odbiorcy) REFERENCES konto (nr_konta)
);

CREATE TABLE IF NOT EXISTS bankomat (
    bankomat_id SERIAL PRIMARY KEY,
    oddzial_id INT NOT NULL,
    FOREIGN KEY (oddzial_id) REFERENCES oddzial_banku (oddzial_id)
);

CREATE TABLE IF NOT EXISTS transakcja (
    transakcja_id SERIAL PRIMARY KEY,
    bankomat_id INT NOT NULL,
    nr_karty INT NOT NULL,
    wplata_wyplata INT NOT NULL,
    FOREIGN KEY (bankomat_id) REFERENCES bankomat (bankomat_id),
    FOREIGN KEY (nr_karty) REFERENCES karta (nr_karty)
);
