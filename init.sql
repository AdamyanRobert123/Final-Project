CREATE USER sales_user WITH PASSWORD 'sales_pass';

CREATE DATABASE sales_db
    OWNER sales_user
    ENCODING 'UTF8';

GRANT ALL PRIVILEGES ON DATABASE sales_db TO sales_user;
