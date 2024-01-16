CREATE VIEW kredyty_klientow AS
SELECT
    o.oddzial_id,
    kl.imie,
    kl.nazwisko,
    td.typ_kredytu_id,
    tk.oprocentowanie,
    td.kwota AS kwota_kredytu,
    td.data_zaciagniecia,
    td.data_splaty
FROM kredyt_detale td
JOIN klient kl ON td.klient_id = kl.klient_id
JOIN typ_kredytu tk ON td.typ_kredytu_id = tk.typ_kredytu_id
JOIN oddzial_banku o ON o.oddzial_id = tk.oddzial_id
ORDER BY o.oddzial_id;

