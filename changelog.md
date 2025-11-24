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

## [12.0.0] - 2025-11-24

- Implemented ansible functionality for the microblogg & database
- Fixed loadbalancer and nginx config
- Implemented CD design for ansible and github actions
- Added route that shows which docker image microblogg is using
