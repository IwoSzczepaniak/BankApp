create view kredyty_podsumowanie as
select
    o.oddzial_id,
    tk.oprocentowanie,
    count(*) as "liczba kredytow udzielonych",
    sum(td.kwota) as "suma kredytow udzielonych",
    tk.aktualna_pula_srodkow as pozostala_pula_srodkow
from kredyt_detale td
join typ_kredytu tk on td.typ_kredytu_id = tk.typ_kredytu_id
join oddzial_banku o on o.oddzial_id = tk.oddzial_id
group by o.oddzial_id, tk.typ_kredytu_id
order by o.oddzial_id;
