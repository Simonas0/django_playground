CREATE USER django WITH PASSWORD 'xDpass';
DROP DATABASE django_playground;
CREATE DATABASE django_playground OWNER django;
\c django_playground;

CREATE TYPE custom_field AS (
	name text,
        file text);
