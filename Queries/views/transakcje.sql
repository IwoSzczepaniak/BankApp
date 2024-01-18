
CREATE VIEW konta_klientow AS
SELECT
    (kl.imie || ' ' || kl.nazwisko) AS klient,
    CASE
        WHEN p.nr_konta_nadawcy = k.nr_konta THEN -p.kwota
        ELSE p.kwota
    END AS transakcja,
    'Przelew' AS typ
FROM przelew p
JOIN konto k ON p.nr_konta_nadawcy = k.nr_konta OR p.nr_konta_odbiorcy = k.nr_konta
JOIN karta kr ON kr.nr_konta = k.nr_konta
JOIN klient kl ON kl.klient_id = k.klient_id

UNION

SELECT
    (kl.imie || ' ' || kl.nazwisko) AS klient,
    t.wplata_wyplata AS transakcja,
    'Bankomat' AS typ
FROM transakcja t
JOIN karta kr ON kr.nr_karty = t.nr_karty
JOIN konto k ON kr.nr_konta = k.nr_konta
JOIN klient kl ON kl.klient_id = k.klient_id
ORDER BY  klient;




