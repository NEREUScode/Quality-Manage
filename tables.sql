-- Create the module table
CREATE TABLE module (
    date TEXT PRIMARY KEY,
    fabriant TEXT,
    dateFab TEXT,
    typeCompteur TEXT,
    diametreNominal TEXT,
    classe TEXT,
    Pression TEXT,
    debitPermanent TEXT,
    rpDebit1 TEXT,
    rpDebit2 TEXT,
    rp TEXT
);

-- Create the Erreur table
CREATE TABLE Erreur (
    id INTEGER PRIMARY KEY,
    date TEXT,
    nSerie TEXT,
    debitActuel TEXT,
    temperature TEXT,
    indexInitial TEXT,
    indexFinal TEXT,
    volumeIndique TEXT,
    volumeReel TEXT,
    erreur TEXT,
    emt TEXT,
    FOREIGN KEY(date) REFERENCES module(date)
);

-- Create the Essai table
CREATE TABLE Essai (
    date TEXT PRIMARY KEY,
    methode TEXT,
    banc TEXT,
    TempAmbiante TEXT,
    HumiditeRelative TEXT,
    TempEau1 TEXT,
    TempEau2 TEXT,
    preEau1 TEXT,
    preEau2 TEXT,
    echelon TEXT,
    FOREIGN KEY(date) REFERENCES module(date)
);

-- Create the Quantité table
CREATE TABLE Quantité (
    id INTEGER PRIMARY KEY,
    date TEXT,
    m1 TEXT,
    m2 TEXT,
    m3 TEXT,
    v1 TEXT,
    v2 TEXT,
    v3 TEXT,
    FOREIGN KEY(date) REFERENCES Erreur(date)
);

