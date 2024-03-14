-- migrate:up
CREATE TABLE jobs (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    created_date TEXT DEFAULT CURRENT_TIMESTAMP
);

-- migrate:down
DROP TABLE jobs;
