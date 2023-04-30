# Dataset metadata

## Versioning

Datasets are versioned, following a simplified [Semantic Versioning scheme](https://semver.org/).
* Only `MAJOR.MINOR.PATCH` version numbers are allowed. Pre-releases (e.g., `1.0.0-alpha`) and build metadata (e.g., `1.0.0+001`) are NOT allowed.
* PATCH version increments are used for changes that should not have any significant impact on the benchmark. For example: spelling fixes in the metadata.
* MINOR version increments change the content of the benchmark dataset, possibly introducing new distributions, but the existing distributions should remain backwards-compatible for most purposes. For example: the dataset is enlarged, introducing new size distributions (e.g., 10M), however the old size distributions (1M and smaller) are kept as-is.
* MAJOR version increments are used for significant changes, such as removing a part of the dataset, adding a new property, etc.

The versions are recorded manually by the dataset's maintainer in the `metadata.ttl` file, using the `dcat:version` property. When releasing the dataset, the main branch of the repository should be tagged with a corresponding name: `vX.Y.Z`, which will trigger the release pipeline.
