-- Crear la base de datos en SQLite
PRAGMA foreign_keys = ON;

-- Tabla `monitoring`
CREATE TABLE IF NOT EXISTS monitoring (
    id TEXT PRIMARY KEY,
    projects_id TEXT NOT NULL,
    technical_managers_id TEXT NOT NULL,
    status TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla `zones`
CREATE TABLE IF NOT EXISTS zones (
    id TEXT PRIMARY KEY,
    monitoring_id TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (monitoring_id) REFERENCES monitoring (id)
);

-- Tabla `crops`
CREATE TABLE IF NOT EXISTS crops (
    id TEXT PRIMARY KEY,
    laboratories_id TEXT NOT NULL,
    crop TEXT,
    humidity_min REAL,
    humidity_max REAL,
    temperature_min REAL,
    temperature_max REAL,
    conductivity_min REAL,
    conductivity_max REAL,
    ph_min REAL,
    ph_max REAL,
    nitrogen_min REAL,
    nitrogen_max REAL,
    phosphorus_min REAL,
    phosphorus_max REAL,
    potassium_min REAL,
    potassium_max REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tabla `crops_zone`
CREATE TABLE IF NOT EXISTS crops_zone (
    id TEXT PRIMARY KEY,
    suitable REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    crops_id TEXT NOT NULL,
    details TEXT,
    zones_id TEXT NOT NULL,
    FOREIGN KEY (crops_id) REFERENCES crops (id),
    FOREIGN KEY (zones_id) REFERENCES zones (id)
);

-- Tabla `result_zone`
CREATE TABLE IF NOT EXISTS result_zone (
    id TEXT PRIMARY KEY,
    humidity REAL,
    temperature REAL,
    conductivity REAL,
    ph REAL,
    nitrogen REAL,
    phosphorus REAL,
    potassium REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id) REFERENCES zones (id)
);

-- Tabla `reads`
CREATE TABLE IF NOT EXISTS reads (
    id TEXT PRIMARY KEY,
    zones_id TEXT NOT NULL,
    humidity REAL,
    temperature REAL,
    conductivity REAL,
    ph REAL,
    nitrogen REAL,
    phosphorus REAL,
    potassium REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (zones_id) REFERENCES zones (id)
);

-- Tabla `details_result_zone`
CREATE TABLE IF NOT EXISTS details_result_zone (
    id TEXT PRIMARY KEY,
    requeriments TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    zones_id TEXT NOT NULL,
    FOREIGN KEY (zones_id) REFERENCES zones (id)
);

-- Tabla `results`
CREATE TABLE IF NOT EXISTS results (
    id TEXT PRIMARY KEY,
    monitoring_id TEXT NOT NULL,
    humidity REAL,
    temperature REAL,
    conductivity REAL,
    ph REAL,
    nitrogen REAL,
    phosphorus REAL,
    potassium REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (monitoring_id) REFERENCES monitoring (id)
);

-- Tabla `details_result`
CREATE TABLE IF NOT EXISTS details_result (
    id TEXT PRIMARY KEY,
    requeriments TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    results_id TEXT NOT NULL,
    FOREIGN KEY (results_id) REFERENCES results (id)
);

-- Tabla `crops_result`
CREATE TABLE IF NOT EXISTS crops_result (
    id TEXT PRIMARY KEY,
    results_id TEXT NOT NULL,
    crops_id TEXT NOT NULL,
    suitable REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    details TEXT,
    FOREIGN KEY (crops_id) REFERENCES crops (id),
    FOREIGN KEY (results_id) REFERENCES results (id)
);
