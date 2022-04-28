-- Create the database
CREATE DATABASE book;

-- Create an admin user for our app to use
CREATE USER book_admin WITH PASSWORD 'password';

-- Give that user permissins to manage the database:
GRANT ALL PRIVILEGES ON DATABASE book TO book_admin;