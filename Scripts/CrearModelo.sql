/* Creación de tablas */

CREATE TABLE Temp(
	TsuYear int,
	MaxWaterHeight float,
	TotalDeaths int,
	TotalDamage float,
	TotalHousesDestroyed int,
	TotalHousesDamaged int,
	Pais varchar(75)
);

CREATE TABLE Country(
	IdCountry int IDENTITY(1,1) PRIMARY KEY,
	Country VARCHAR(75)
);

CREATE TABLE Tsunami(
	Id int IDENTITY(1,1) PRIMARY KEY,
	TsuYear int,
	MaxWaterHeight float,
	TotalDeaths int,
	TotalDamage float,
	TotalHousesDestroyed int,
	TotalHousesDamaged int,
	IdCountry int,
	FOREIGN KEY (IdCountry) REFERENCES Country(IdCountry)
);
