DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS merchants;

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    activated BOOLEAN
);

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    spending_limit DECIMAL(19,4),
    savings_goal DECIMAL(19,4)
);

CREATE TABLE transactions(
    id SERIAL PRIMARY KEY,
    amount DECIMAL(19,2),
    category VARCHAR(255),
    date DATE,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE CASCADE 
);

