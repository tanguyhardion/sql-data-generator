INSERT INTO usager (numEtu, nom, prenom, categorie) VALUES
(48474, 'Gloria', 'Mickelson', 2),
(46227, 'Angela', 'Daniels', 3),
(57283, 'Brian', 'Ortiz', 2),
(51874, 'Christine', 'Gomez', 1),
(42876, 'Paul', 'Garza', 3),
(53502, 'Phillip', 'Soto', 2),
(50598, 'Christina', 'Burnell', 3);

INSERT INTO ouvrage VALUES
(9759800200, 1779048563631, 'Woman Of The Sea', 'Sidney Colli', 'Julliard', 1929, 'fiction', 'hindi', 7, 'Hernandez'),
(3384546667, 2538294843131, 'Pirate Without Time', 'Sharon Kidwell', 'Vérone', 1967, 'non-fiction', 'francais', 5, 'Jacobs'),
(6886217793, 5500820005787, 'Owls Of Stone', 'Kasey Puma', 'Albin Michel', 1946, 'religion', 'finnois', 4, 'Ridenour'),
(2049938254, 4235702197648, 'Priests Without Hate', 'Laura Pennington', 'Actes Sud', 1965, 'non-fiction', 'portugais', 6, 'Pinchback'),
(2771245145, 2213003553548, 'Turtles And Boys', 'Donald Neal', 'Hachette', 1936, 'aventure', 'géorgien', 6, 'Olson');

INSERT INTO emprunt (numEtu, isbn, dateEmp, rendu) VALUES
(53502, 3384546667, '2011-11-07', 1),
(48474, 9759800200, '2014-02-09', 1),
(50598, 2771245145, '2018-01-07', 1);

INSERT INTO suggestion_achat (numEtu, titreOuvrage, quantite, etat) VALUES
(50598, 'Mice And Boys', 7, 0),
(51874, 'Thieves Of The Day', 3, 1);