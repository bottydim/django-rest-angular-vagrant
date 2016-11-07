CREATE DATABASE npss_tv;
CREATE USER uvh WITH PASSWORD 'uspeh2000';
ALTER ROLE uvh SET client_encoding TO 'utf8';
ALTER ROLE uvh SET default_transaction_isolation TO 'read committed';
ALTER ROLE uvh SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE npss_tv TO uvh;
