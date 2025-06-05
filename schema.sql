-- PostgreSQL schema for Library Book Inventory System

-- books table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR NOT NULL,
    isbn VARCHAR UNIQUE NOT NULL,
    publication_date DATE NOT NULL,
    category VARCHAR NOT NULL,
    status VARCHAR NOT NULL
);

-- rentals table
CREATE TABLE rentals (
    rental_id SERIAL PRIMARY KEY,
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    checkout_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE
);

-- waitlist table
CREATE TABLE waitlist (
    waitlist_id SERIAL PRIMARY KEY,
    book_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    position INTEGER NOT NULL,
    request_date DATE NOT NULL
);
