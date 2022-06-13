# DEMO Superset Reports

## Set Up

### Sample Data

Uncomment `init` service in docker compose to load sample data

### Set SMTP Config in superset_config_docker.py

```
SMTP_HOST=...
SMTP_USER=...
SMTP_PASSWORD=...
SMTP_MAIL_FROM=...
```

### Build

`docker build . -t superset-1.5.1-extended`

### Run

`docker compose up`

## Test

- `http://localhost:8088`
- sign in with `admin` / `admin`
- set up a report
