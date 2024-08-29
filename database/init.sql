-- init.sql

-- Connect to the newly created database
\c db_name;

-- Create exampleapidata table
CREATE TABLE IF NOT EXISTS exampleapidata (
    id VARCHAR(255) PRIMARY KEY,
    joke VARCHAR(255) NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

-- Create table for categories
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255) NOT NULL UNIQUE
);

-- Create examplewebdata table
CREATE TABLE IF NOT EXISTS examplewebdata (
    id SERIAL PRIMARY KEY,
    book_name VARCHAR(255) NOT NULL,
    book_price DECIMAL(10, 2) NOT NULL,
    book_rating VARCHAR(10) NOT NULL,
    book_currency CHAR(3)
);

-- Create an index on updated_at to enable efficient date searches
CREATE INDEX idx_updated_at ON exampleapidata(updated_at);