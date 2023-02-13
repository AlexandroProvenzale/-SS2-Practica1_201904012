/* Consultas */

/* Consulta 1 */
SELECT COUNT(Tsunami.Id) AS 'Cantidad tsunamis',
(SELECT COUNT(Country.IdCountry) FROM Country) AS 'Cantidad paises'
FROM Tsunami;

/* Consulta 2 */
SELECT COUNT(Tsunami.Id) AS 'Cantidad tsunamis', Tsunami.TsuYear AS 'Anio'
FROM Tsunami
GROUP BY Tsunami.TsuYear ORDER BY Tsunami.TsuYear ASC;

/* Consulta 3 */
SELECT Country.Country AS Pais, STRING_AGG(Tsunami.TsuYear, ':')
WITHIN GROUP (ORDER BY Tsunami.TsuYear ASC) AS Anios
FROM Tsunami INNER JOIN Country
ON Tsunami.IdCountry = Country.IdCountry
GROUP BY Country.Country;

/* Consulta 4 */
SELECT AVG(Tsunami.TotalDamage) AS 'Total Damage Promedio', Country.Country AS 'Pais'
FROM Tsunami INNER JOIN Country
ON Tsunami.IdCountry = Country.IdCountry
GROUP BY Country.Country ORDER BY 'Total Damage Promedio' DESC;

/* Consulta 5 */
SELECT TOP 5 Country.Country AS Pais, SUM(Tsunami.TotalDeaths) AS Muertes
FROM Tsunami INNER JOIN Country
On Tsunami.IdCountry = Country.IdCountry
GROUP BY Country.Country ORDER BY Muertes DESC;

/* Consulta 6 */
SELECT TOP 5 Tsunami.TsuYear AS 'Anio', SUM(Tsunami.TotalDeaths) AS 'Muertes totales'
FROM Tsunami
GROUP BY Tsunami.TsuYear ORDER BY 'Muertes totales' DESC;

/* Consulta 7 */
SELECT TOP 5 Tsunami.TsuYear AS 'Anio', COUNT(Tsunami.Id) AS 'Cantidad tsunamis'
FROM Tsunami
GROUP BY Tsunami.TsuYear ORDER BY 'Cantidad tsunamis' DESC;

/* Consulta 8 */
SELECT TOP 5 Country.Country AS Pais, SUM(Tsunami.TotalHousesDestroyed) AS 'Casas destruidas'
FROM Tsunami INNER JOIN Country
On Tsunami.IdCountry = Country.IdCountry
GROUP BY Country.Country ORDER BY 'Casas destruidas' DESC;

/* Consulta 9 */
SELECT TOP 5 Country.Country AS Pais, SUM(Tsunami.TotalHousesDamaged) AS 'Casas daniadas'
FROM Tsunami INNER JOIN Country
On Tsunami.IdCountry = Country.IdCountry
GROUP BY Country.Country ORDER BY 'Casas daniadas' DESC;

/* Consulta 10 */
SELECT AVG(Tsunami.MaxWaterHeight) AS 'Altura maxima agua promedio', Country.Country AS 'Pais'
FROM Tsunami INNER JOIN Country
ON Tsunami.IdCountry = Country.IdCountry
GROUP BY Country.Country ORDER BY 'Altura maxima agua promedio' DESC;
