CREATE TABLE Product(
    ID VARCHAR(10),
    Name VARCHAR(50),
    Type VARCHAR(10),
    Price VARCHAR(100),
    DateOfManufacture DATE,
    DateOfExpiry DATE
);
INSERT INTO Product
VALUES 
('001', 'Apple', 'fruit', '1$','2021-06-08', '2021-06-08'),
('002', 'Coca', 'drink', '1.3$','2021-06-08', '2021-06-08'),
('003', 'Orange', 'fruit', '1.1$','2021-06-08', '2021-06-08'),
('004', 'Peach', 'fruit', '1.1$','2021-06-08', '2021-06-08');
('005', 'Sausage', 'meat', '5$','2021-06-08', '2021-06-08'),
('006', 'Shovel', 'tool', '10$','2021-06-08', '2021-06-08'),
('007', 'Strongbow', 'drink', '1.5$','2021-06-08', '2021-06-08'),
('008', 'Smoked Classic Cut Bacon', 'meat', '15','2021-06-08', '2021-06-08');
('009', 'Soft Drink', 'drink', '1.25$','2021-06-08', '2021-06-08'),
('010', 'Banana', 'fruit', '6$','2021-06-08', '2021-06-08');


CREATE TABLE Manufacture(
    ID VARCHAR(10),
    Name VARCHAR(50),
    Country VARCHAR(10)
);
INSERT INTO Manufacture
VALUES 
('001', 'Apple', 'USA'),
('002', 'Coca', 'USA'),
('003', 'Orange', 'USA'),
('004', 'Peach', 'Japan');
('005', 'Sausage', 'USA'),
('006', 'Shovel', 'USA'),
('007', 'Strongbow', 'USA'),
('008', 'Smoked Classic Cut Bacon', 'USA');
('009', 'Soft Drink', 'Thailand'),
('010', 'Banana', 'USA');


CREATE TABLE Store(
    ID VARCHAR(10),
    Name VARCHAR(50),
    Address VARCHAR(100)
);
INSERT INTO Store
VALUES 
('001', 'Apple', 'USA'),
('002', 'Coca', 'USA'),
('003', 'Orange', 'USA'),
('004', 'Peach', 'Japan');
('005', 'Sausage', 'USA'),
('006', 'Shovel', 'USA'),
('007', 'Strongbow', 'USA'),
('008', 'Smoked Classic Cut Bacon', 'USA');
('009', 'Soft Drink', 'Thailand'),
('010', 'Banana', 'USA');

