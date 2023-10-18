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

create unique index imports_unique ON imports("filename", cola, colb, colc, cold);