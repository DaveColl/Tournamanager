CREATE TABLE Teams (
    Team_ID INT AUTO_INCREMENT  PRIMARY KEY,
    Team_Name VARCHAR(25) NOT NULL
);

CREATE TABLE Spieler (
    Spieler_ID INT AUTO_INCREMENT PRIMARY KEY,
    Spieler_Name VARCHAR(20) NOT NULL,
    Team_ID INT,
    FOREIGN KEY (Team_ID) REFERENCES Teams(Team_ID)
);

CREATE TABLE Matches (
    Match_ID INT AUTO_INCREMENT PRIMARY KEY,
    Team_ID1 INT NOT NULL,
    Team_ID2 INT NOT NULL,
    Punkte_Team1 INT DEFAULT 0,
    Punkte_Team2 INT DEFAULT 0,
    FOREIGN KEY (Team_ID1) REFERENCES Teams(Team_ID),
    FOREIGN KEY (Team_ID2) REFERENCES Teams(Team_ID)
);

Insert INTO Teams (Team_Name) VALUES ('Pixel Tigers');
Insert INTO Spieler (Spieler_Name, Team_ID) VALUES ('DaveColl', 1), ('NeonViper', 1);

Insert INTO Teams (Team_Name) VALUES ('Byte Falcons');
Insert INTO Spieler (Spieler_Name, Team_ID) VALUES ('DeltaJunk', 2), ('CodeCobra', 2);

Insert INTO Teams (Team_Name) VALUES ('Code Foxes');
Insert INTO Spieler (Spieler_Name, Team_ID) VALUES ('Nrvous', 3), ('ShadowStriker', 3);

Insert INTO Teams (Team_Name) Values ('Data Wolves');
Insert INTO Spieler (Spieler_Name, Team_ID) VALUES ('Waterrigel', 4), ('QuantumFang', 4);