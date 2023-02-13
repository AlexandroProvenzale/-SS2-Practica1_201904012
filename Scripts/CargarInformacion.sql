/* Carga de datos */

BULK INSERT
	Temp
FROM
	'D:\PythonProjects\Semi_Practica1\historial_tsunamis.csv'
WITH(
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

/* Separación de datos */

INSERT INTO Country(Country)
(
	SELECT DISTINCT Temp.Pais
	FROM Temp
);

INSERT INTO Tsunami(
	TsuYear,
	MaxWaterHeight,
	TotalDeaths,
	TotalDamage,
	TotalHousesDestroyed,
	TotalHousesDamaged,
	IdCountry
)
(	SELECT Temp.TsuYear, Temp.MaxWaterHeight, Temp.TotalDeaths, Temp.TotalDamage, Temp.TotalHousesDestroyed, Temp.TotalHousesDamaged,
	(SELECT TOP 1 IdCountry FROM Country WHERE Temp.Pais = Country.Country) FROM Temp
);
