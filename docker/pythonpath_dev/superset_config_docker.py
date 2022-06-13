#
# This is an example "local" configuration file. In order to set/override config
# options that ONLY apply to your local environment, simply copy/rename this file
# to docker/pythonpath/superset_config_docker.py
# It ends up being imported by docker/superset_config.py which is loaded by
# superset/config.py
#

ALERT_REPORTS_NOTIFICATION_DRY_RUN = False

SMTP_HOST = ...
SMTP_USER = ...
SMTP_PASSWORD = ...
SMTP_MAIL_FROM = ...
SMTP_STARTTLS = False
SMTP_SSL = True
SMTP_PORT = 465


CSV_EXPORT = {"sep": ";", "escapechar": "\\"}
