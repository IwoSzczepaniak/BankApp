create view kredyty_podsumowanie as
select
    o.oddzial_id,
    tk.oprocentowanie,
    tk.maksymalna_kwota,
    COUNT(td.typ_kredytu_id) as "liczba kredytow udzielonych",
    sum(td.kwota) as "suma kredytow udzielonych",
    tk.pula_srodkow as "poczatkowa pula srodkow",
    tk.aktualna_pula_srodkow as "pozostala pula srodkow"
from kredyt_detale td
right join typ_kredytu tk on td.typ_kredytu_id = tk.typ_kredytu_id
right join oddzial_banku o on o.oddzial_id = tk.oddzial_id
group by o.oddzial_id, tk.typ_kredytu_id
order by o.oddzial_id;
