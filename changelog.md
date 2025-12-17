# Changelog

All notable changes to this project will be documented in this file.

### Added

## [11.0.0] - 2025-11-07

- Docker file that runs the app, located in ./docker/Docker_prod
- Commit template
- Github Actions, running python runner for app
- Changelog added

### Added

## [11.0.0] - 2025-11-07

- Added docker compose file to run the docker containers
- Added Dockerfile to run tests inside a container
<!-- ### Changed

### Removed

### Fixed -->

## [11.0.1] - 2025-11-12

- Added following / unfollowing other users
- View followed users in 'Home' feed
- Github Actions will publish app to Docker Hub on new release

## [12.0.0] > [12.0.27] - 2025-11-20 - 2025-11-25

- Added a loadbalancer VM
- Added two appserver VMs
- Added a database VM
- Created a Hosts.ini file
- Added users for management of the VMs

- Added ansible/microblog_app.yml
- Added ansible/microblog_db.yml
- Fixed Loadbalancer to redirect trafic to appservers.
- Added Actions Pipeline on new release

## [12.0.28] - 2025-11-26

- Added Rolling updates
- Integrated Rolling updates into the actions pipeline

## [12.0.29] - 2025-11-26

- Rolling updates Fix

## [12.0.30] - 2025-11-26

- Rolling updates Fix

## [12.0.31] - 2025-12-01

- Added an ansible playbook for updating security rule. (update_sg.yml)

## [13.0.0] - Datum

- Lägg till

## [13.0.1] - Datum

- Lägg till

## [13.0.2] - Datum

- Lägg till

## [13.0.4] - 2025-12-05

- Added task inside 10 first minutes so that new ssh config auto pushes to all servers

- Fixed with microblogg route problem for endpoint version.

## [13.0.5] - 2025-12-07

- Added tests for bandit, trivy and dockler to run in actions

## [14.0.0] - [14.0.11] - 2025-12-16
- Added Grafana
- Added Prometheus
- Added Node-Exporter
- Added AlertManager
- Added webhook to AlertManager


## [15.0.1] - 2025-12-17
- Sync fork form upstream
- New structure in kubernets folder