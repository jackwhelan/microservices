# Microservices
A repo for housing reusable microservices I plan to develop to use across personal projects. This repo will also house little tools and utilities to aid with the use, maintenance, development and CI/CD of these microservices.

## Current Microservices
- Data-Access
  - This microservice will act as an adapter for other microservices to interface with databases. The reason for this is to keep the other microservices independant of this data layer.
- Python-Microservice-Base
  - This is a base template for flask, python-based microservices. I often want to make small flask/express style micro-APIs so I plan to use this base template as a low boilerplate starter template for future small APIs I want to build.

## Current Tools
- Version-Bump
  - This is just a simple python tool wrapped in a docker container to aid in the version bumping of the VERSION files in this repo in my CI/CD pipelines.

## Versioning Strategy
### Repo Level Version File
- Major Increment:
  - New Microservice/Tool Added.
- Minor Increment:
  - When a microservice gets a major version bump.
- Patch Increment:
  - When a microservice gets a minor or patch version bump.

### Microservice Level Version File
- Major Increment:
  - Backwards incompatible change introduced.
- Minor Increment:
  - Backwards compatible change introduced.
- Patch Increment:
  - Backwards compatible bug fix introduced.
