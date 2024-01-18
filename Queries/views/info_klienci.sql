create view info_klienci as
select
    kl.klient_id as "id klienta",
    (kl.imie || ' ' || kl.nazwisko) as klient,
    kl.pesel,
    kr.nr_karty as "numer karty",
    kr.rodzaj_karty as "rodzaj karty",
    k.nr_konta as "numer konta",
    k.saldo AS "saldo"
from klient kl
join konto k on kl.klient_id = k.klient_id
join karta kr on k.nr_konta = kr.nr_konta
order by "id klienta";


