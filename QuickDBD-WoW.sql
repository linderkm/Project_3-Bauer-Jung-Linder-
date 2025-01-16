-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "player" (
    id INT   NOT NULL,
    age VARCHAR   NOT NULL,
    gender VARCHAR   NOT NULL,
    sexuality VARCHAR   NOT NULL,
    country VARCHAR,
    server VARCHAR   NOT NULL,
    CONSTRAINT "pk_player" PRIMARY KEY (
        "ID"
     )
);

CREATE TABLE "character" (
    id INT   NOT NULL,
    faction VARCHAR   NOT NULL,
    main VARCHAR   NOT NULL,
    role VARCHAR   NOT NULL,
    class VARCHAR   NOT NULL,
    race VARCHAR   NOT NULL,
    type VARCHAR   NOT NULL,
    CONSTRAINT "pk_character" PRIMARY KEY (
        "ID"
     )
);

