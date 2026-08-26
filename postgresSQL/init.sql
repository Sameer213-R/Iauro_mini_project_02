CREATE TABLE IF NOT EXISTS users (
    user_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_name VARCHAR(20),
    user_city VARCHAR(20),
    gender CHAR(2)
);