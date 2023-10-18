CREATE TABLE IF NOT EXISTS imports (
   id serial PRIMARY KEY,
   "filename" varchar(255) not null,
   cola varchar(255),
   colb varchar(255),
   colc varchar(255),
   cold varchar(255),
   created_at timestamp NOT NULL,
   updated_at timestamp
);

CREATE TABLE IF NOT EXISTS stocks (
   id serial PRIMARY KEY,
   fabrica varchar(255),
   gramatura varchar(255),
   formato varchar(255),
   disponivel_em timestamp default now(), -- data de chegada
   created_at timestamp NOT NULL,
   updated_at timestamp
);

create unique index imports_unique ON imports("filename", cola, colb, colc, cold);
