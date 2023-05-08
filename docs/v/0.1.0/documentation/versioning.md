# Versioning and releases

!!! tip "TL;DR"
    Always use a specific versioned release of the RiverBench suite (e.g., `1.0.1`). Results obtained with versions of the suite that differ by more than the PATCH version (last digit) **are not comparable** for most purposes.

## Dataset versioning

Datasets are versioned following a simplified [Semantic Versioning scheme](https://semver.org/).

- Only `MAJOR.MINOR.PATCH` version numbers are allowed. Pre-releases (e.g., `1.0.0-alpha`) and build metadata (e.g., `1.0.0+001`) are **NOT** allowed.
- PATCH version increments are used for changes that should not have any significant impact on the benchmark. For example: spelling fixes in the metadata.
- MINOR version increments change the content of the benchmark dataset, possibly introducing new distributions, but the existing fixed-size distributions should remain backwards-compatible for most purposes. For example: the dataset is enlarged, introducing new size distributions (e.g., 10M), however the old fixed-size distributions (1M and smaller) are kept as-is.
- MAJOR version increments are used for significant changes, such as removing a part of the dataset, adding a new property, etc.

### Making a release

The `dev` version of each dataset is its lateset development version, corresponding to the `main` branch of the repository. Tagged (versioned) releases are made by the dataset's maintainer.

To make a release:

1. Read the above versioning rules and decide which version number to use. If you are unsure, [ask the suite's maintainer for help](https://github.com/RiverBench/RiverBench/issues/new/choose).
2. Go to your dataset's repository and check out the `main` branch on your local machine.
3. Update the main branch by running `git pull`. Make sure the pull was successful.
4. Create a new tag with the version number you decided on: `git tag vX.Y.Z`.
5. Push the tag to GitHub: `git push origin --tag vX.Y.Z`.

Then, the CI will take over and will automatically add the new version to the dataset's metadata file and update the website.

## Profile and suite versioning

The profiles and the suite are versioned in sync. The versioning schema is the same as for datasets, with MINOR version increments corresponding to possibly new distributions or new datasets, and MAJOR version increments corresponding to significant backwards-incompatible changes.

The procedure for making a release is the same as for datasets. New tagged releases will automatically use the latest tagged release of each dataset.

## Schema versioning

Schemas and ontologies are versioned in the same manner, but independently of the suite.

The procudure for making a release is the same as for datasets.
