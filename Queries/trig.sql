
--update saldo PRZELEW (sprawdz czy masz tyle na koncie)
CREATE OR REPLACE FUNCTION update_saldo()
RETURNS trigger AS $$
DECLARE
    r_karty VARCHAR(20);
BEGIN
    select rodzaj_karty into r_karty
    from karta
    where nr_konta = (SELECT nr_konta_nadawcy FROM przelew WHERE przelew_id = NEW.przelew_id);

    if(r_karty = 'Debit' AND (SELECT saldo FROM konto WHERE nr_konta = (SELECT nr_konta_nadawcy FROM przelew WHERE przelew_id = NEW.przelew_id)) < (SELECT kwota FROM przelew WHERE przelew_id =  NEW.przelew_id)) then
        RAISE EXCEPTION 'za malo srodkow na koncie aby zrobic przelew';
    ELSE
    UPDATE konto
    SET saldo = saldo - (SELECT kwota FROM przelew WHERE przelew_id =  NEW.przelew_id)
    WHERE nr_konta = (SELECT nr_konta_nadawcy FROM przelew WHERE przelew_id = NEW.przelew_id);

    UPDATE konto
    SET saldo = saldo + (SELECT kwota FROM przelew WHERE przelew_id =  NEW.przelew_id)
    WHERE nr_konta = (SELECT nr_konta_odbiorcy FROM przelew WHERE przelew_id = NEW.przelew_id);
    
    END IF;
    return NEW;
END;
$$ LANGUAGE plpgsql;


create TRIGGER update_saldo_trigger
AFTER INSERT ON przelew
FOR EACH ROW
EXECUTE FUNCTION update_saldo();



--update saldo ATM (sprawdz czy masz tyle na koncie)
CREATE OR REPLACE FUNCTION update_saldo_atm()
RETURNS trigger AS $$
DECLARE
    saldo_u int;
    r_karty VARCHAR(20);
BEGIN
    select k.saldo into saldo_u
    from konto k
    join karta ka on k.nr_konta = ka.nr_konta
    where ka.nr_karty = NEW.nr_karty;

    select rodzaj_karty into r_karty
    from karta
    where nr_konta = (SELECT k.nr_konta FROM konto k JOIN karta kr on k.nr_konta=kr.nr_konta JOIN transakcja t ON kr.nr_karty=t.nr_karty  WHERE transakcja_id = NEW.transakcja_id);

    if(r_karty = 'Debit' AND (SELECT wplata_wyplata FROM transakcja WHERE transakcja_id =  NEW.transakcja_id) + saldo_u < 0) then
        RAISE EXCEPTION 'za malo srodkow na koncie aby wyplacic oczekiwana kwote';
    ELSE
    UPDATE konto
    SET saldo = saldo + (SELECT wplata_wyplata FROM transakcja WHERE transakcja_id =  NEW.transakcja_id)
    WHERE nr_konta = (SELECT nr_konta FROM karta WHERE nr_karty = NEW.nr_karty);
    END IF;
    return NEW;
END;
$$ LANGUAGE plpgsql;


create TRIGGER update_saldo_atm_trigger
AFTER INSERT ON transakcja
FOR EACH ROW
EXECUTE FUNCTION update_saldo_atm();



CREATE OR REPLACE FUNCTION czy_ma_mieszkanie() 
RETURNS TRIGGER AS $$
DECLARE 
    procent int;
    miesz boolean;
BEGIN
    SELECT oprocentowanie INTO procent
    FROM typ_kredytu
    WHERE typ_kredytu_id = NEW.typ_kredytu_id;

    SELECT mieszkanie INTO miesz
    FROM klient
    WHERE klient_id = NEW.klient_id;

    IF procent = 2 AND miesz THEN
        RAISE EXCEPTION 'Nie możesz wziąć kredytu z oprocentowaniem 2, jeśli posiadasz mieszkanie';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER czy_ma_mieszkanie_trigger
BEFORE INSERT ON kredyt_detale
FOR EACH ROW
EXECUTE FUNCTION czy_ma_mieszkanie();



--sprawdz czy klient nie ma juz kredytu
CREATE OR REPLACE FUNCTION czy_ma_juz_kredyt()
RETURNS TRIGGER AS $$
DECLARE 
    count int;
BEGIN
    SELECT COUNT(*) INTO count
    FROM kredyt_detale
    WHERE klient_id = NEW.klient_id;

    IF count > 0 THEN
        RAISE EXCEPTION 'Klient posiada już kredyt - nie moze dostac kolejnego';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER czy_ma_juz_kredyt_trigger
BEFORE INSERT ON kredyt_detale
FOR EACH ROW
EXECUTE FUNCTION czy_ma_juz_kredyt();



--sprawdz czy klient nie bierze kredytu o wysokosci wiekszej niz jego maksymalna kwota
CREATE OR REPLACE FUNCTION sprawdz_wysokosc_kredytu()
RETURNS TRIGGER AS $$
DECLARE 
    max_amount int;
BEGIN
    
        SELECT maksymalna_kwota INTO max_amount
        FROM typ_kredytu
        WHERE typ_kredytu_id = NEW.typ_kredytu_id;
    
        IF NEW.kwota > max_amount THEN
            RAISE EXCEPTION 'Klient nie może wziąć tego kredytu w takiej wysokosci';
        END IF;
    
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER sprawdz_wysokosc_kredytu_trigger
BEFORE INSERT ON kredyt_detale
FOR EACH ROW
EXECUTE FUNCTION sprawdz_wysokosc_kredytu();



--update pula srodkow
CREATE OR REPLACE FUNCTION update_pula_srodkow()
RETURNS trigger AS $$
BEGIN
    UPDATE typ_kredytu
    SET aktualna_pula_srodkow = aktualna_pula_srodkow - NEW.kwota
    WHERE oddzial_id = (Select oddzial_id from typ_kredytu where typ_kredytu_id=NEW.typ_kredytu_id) AND typ_kredytu_id =  NEW.typ_kredytu_id;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

create TRIGGER update_pula_srodkow_trigger
AFTER INSERT ON kredyt_detale
FOR EACH ROW
EXECUTE FUNCTION update_pula_srodkow();



--sprawdz czy pula srodkow nie jest wyczerpana
CREATE OR REPLACE FUNCTION czy_pula_wyczerpana() 
RETURNS TRIGGER AS $$
DECLARE
    dostepne_srodki int;
BEGIN
    SELECT aktualna_pula_srodkow INTO dostepne_srodki
    FROM typ_kredytu
    WHERE typ_kredytu_id = NEW.typ_kredytu_id;
    IF dostepne_srodki < NEW.kwota THEN
        RAISE EXCEPTION 'pula srodkow dla tego typu kredytu sie wyczerpala, bądz jest na wyczerpaniu';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER czy_pula_wyczerpana_trigger
BEFORE INSERT ON kredyt_detale
FOR EACH ROW
EXECUTE FUNCTION czy_pula_wyczerpana();




--sprawdz czy klient o takim peselu juz istnieje
CREATE OR REPLACE FUNCTION czy_klient_w_bazie() 
RETURNS TRIGGER AS $$
BEGIN
    if(SELECT pesel
    FROM klient
    WHERE pesel = NEW.pesel) IS NOT NULL
    THEN
        RAISE EXCEPTION 'Klient o takim numerze PESEL już istnieje w bazie';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER czy_klient_w_bazie_trigger
BEFORE INSERT ON klient
FOR EACH ROW
EXECUTE FUNCTION czy_klient_w_bazie();



--czy poprawny nr pesel
CREATE OR REPLACE FUNCTION czy_pesel_jedenastocyfrowy()
RETURNS TRIGGER AS $$
BEGIN
    IF (LENGTH(NEW.pesel) <> 11) THEN
        RAISE EXCEPTION 'Pesel musi miec 11 cyfr';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER czy_pesel_jedenastocyfrowy_trigger
BEFORE INSERT ON klient
FOR EACH ROW EXECUTE PROCEDURE czy_pesel_jedenastocyfrowy();


--kazdy oddzial moze miec w ofercie tylko jeden kredyt o danym oprocentowaniu
CREATE OR REPLACE FUNCTION czy_oddzial_ma_juz_taki_procent()
RETURNS TRIGGER AS $$
DECLARE
    procent numeric;
BEGIN
    SELECT oprocentowanie INTO procent
    FROM typ_kredytu tk
    WHERE tk.oddzial_id = NEW.oddzial_id;

    IF procent = NEW.oprocentowanie THEN
        RAISE EXCEPTION 'w tym oddziale już istnieje kredyt o takim oprocentowaniu';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER czy_oddzial_ma_juz_taki_procent_trigger
BEFORE INSERT ON typ_kredytu
FOR EACH ROW EXECUTE PROCEDURE czy_oddzial_ma_juz_taki_procent();




CREATE OR REPLACE FUNCTION czy_klient_ma_juz_konto()
RETURNS TRIGGER AS $$
    DECLARE
        klient_id integer;
        ilosc_kont integer;
    BEGIN
        SELECT count(*) INTO ilosc_kont
        FROM konto k
        WHERE k.klient_id = NEW.klient_id;

        IF ilosc_kont > 0 THEN
            RAISE EXCEPTION 'Ten klient ma juz konto w banku';
        END IF;

        RETURN NEW;
    END;

$$ LANGUAGE plpgsql;

CREATE TRIGGER czy_klient_ma_juz_konto_trigger
BEFORE INSERT ON konto
FOR EACH ROW EXECUTE PROCEDURE czy_klient_ma_juz_konto();



CREATE OR REPLACE FUNCTION czy_konto_ma_juz_karte()
RETURNS TRIGGER AS $$
    DECLARE
        ilosc_kart integer;
    BEGIN
        SELECT count(*) INTO ilosc_kart
        FROM karta k
        WHERE k.nr_konta = NEW.nr_konta;

        IF ilosc_kart > 0 THEN
            RAISE EXCEPTION 'Konto o podanym numerze ma juz przypisana karte';
        END IF;

        RETURN NEW;
    END;

$$ LANGUAGE plpgsql;

CREATE TRIGGER czy_konto_ma_juz_karte_trigger
BEFORE INSERT ON karta
FOR EACH ROW EXECUTE PROCEDURE czy_konto_ma_juz_karte();