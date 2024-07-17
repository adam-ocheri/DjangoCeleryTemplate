# Grafana Dashboards setup

These Grafana dashboards are automatically set-up to be provisioned into Grafana, via the `docker-compose.yml` configuration.
To make the dashboards compatible with the aotumatic setup, the json files of the dashboards have been modified to point to the Prometheus data source.

**If you want a fresh version of these files, visit their origin**

## Origins of dashboards
- **CeleryWorkerStatus**: Created manually
- **DjangoMonitoring**: https://grafana.com/grafana/dashboards/17658-django/
- **CeleryMonitoring**: https://github.com/mher/flower/blob/master/examples/celery-monitoring-grafana-dashboard.json