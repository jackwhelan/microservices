# Version File Bumper
Just put together this primitive version file bump utility for use in CI/CD flows for these microservices. It's just a dockerized python script to read in a version file "VERSION" (No file extension) assuming it has a basic SemVer format, e.g. 1.0.0, 1.5.2 (Major.Minor.Patch) and bumping it's major, minor or patch version depending on whether you pass "major", "minor" or "patch" when you run it. See example below:  

```
docker build -t version-bumper .
docker run -v ${pwd}/VERSION:/app/VERSION version-bumper minor
```

In this example I am mounting the version file into the workspace of the image and passing "minor" as the version to bump.
