-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "player" (
    "ID" INT   NOT NULL,
    "Age" INT   NOT NULL,
    "Gender" VARCHAR   NOT NULL,
    "Sexuality" VARCHAR   NOT NULL,
    "Country" VARCHAR   NOT NULL,
    "Server" VARCHAR   NOT NULL,
    CONSTRAINT "pk_player" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "character" (
    "ID" INT   NOT NULL,
    "Faction" VARCHAR   NOT NULL,
    "Main" VARCHAR   NOT NULL,
    "Role" VARCHAR   NOT NULL,
    "Class" VARCHAR   NOT NULL,
    "Race" VARCHAR   NOT NULL,
    "Type" VARCHAR   NOT NULL,
    CONSTRAINT "pk_character" PRIMARY KEY (
        "ID"
     )
);

