# Loading from CSV files

From the psql terminal, we can load these files with

```
\copy cat (name, color, personality) from 'data/cat.csv' csv header
\copy dog (name, breed, chip) from 'data/dog.csv' csv header
```

These commands assume that we launched `psql` front he project root, and that these two files are in a directory called `data`, as they are here.

A useful pattern for getting back to a "clean" database is to delete the existing database, recreate it, perform the upgrade (to restore the tables), then load the sample data, as follows

```
dropdb flasky_development
createdb flasky_development
flask db upgrade
psql -U postgres
```

And then run the copy commands in `psql`
```
\copy cat (name, color, personality) from 'data/cat.csv' csv header
\copy dog (name, breed, chip) from 'data/dog.csv' csv header
```

If this feels useful to you, try adapting it to your own project!