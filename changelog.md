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
