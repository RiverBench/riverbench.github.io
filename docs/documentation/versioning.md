# Versioning and releases

!!! tip "TL;DR"
    Always use a specific versioned release of the RiverBench suite (e.g., `2.0.1`). Results obtained with versions of the suite that differ by more than the PATCH version (last digit) **are usually not comparable**.

## Dataset versioning

Datasets are versioned following a simplified [Semantic Versioning scheme](https://semver.org/).

- Only `MAJOR.MINOR.PATCH` version numbers are allowed. Pre-releases (e.g., `1.0.0-alpha`) and build metadata (e.g., `1.0.0+001`) are **NOT** allowed.
- PATCH version increments are used for changes that should not have any significant impact on the benchmark. For example: changes in the metadata, but not the content of the dataset.
- MINOR version increments change the content of the benchmark dataset, possibly introducing new distributions, but the existing fixed-size distributions should remain backwards-compatible for most purposes. For example: the dataset is enlarged, introducing new size distributions (e.g., 10M), however the old fixed-size distributions (1M and smaller) are kept as-is.
- MAJOR version increments are used for significant changes, such as removing a part of the dataset, adding a new property, etc.

### Making a release

The `dev` version of each dataset is its latest development version, corresponding to the `main` branch of the repository. Tagged (versioned) releases are made by the dataset's maintainer.

To make a release:

1. Read the above versioning rules and decide which version number to use. If you are unsure, [ask the suite's maintainer for help](https://github.com/RiverBench/RiverBench/issues/new/choose).
2. Go to your dataset's repository and check out the `main` branch on your local machine.
3. Update the main branch by running `git pull`. Make sure the pull was successful.
4. Create a new tag with the version number you decided on: `git tag vX.Y.Z`.
5. Push the tag to GitHub: `git push origin --tag vX.Y.Z`.

Then, the CI will take over and will automatically add the new version to the dataset's metadata file and update the website.

## Schema versioning

Schemas and ontologies are versioned in the same manner, but independently of the suite.

The procudure for making a release is the same as for datasets.

## Suite versioning

The RiverBench suite is versioned in sync with benchmark categories, benchmark tasks, and profiles. The versioning schema is the same as for datasets, with MINOR version increments corresponding to possibly new distributions, new datasets, or tasks. MAJOR version increments correspond to significant backwards-incompatible changes (including large changes in the metadata structure).

New tagged releases of the suite will automatically use the latest tagged release of each dataset and each schema. The `dev` version of the suite always includes the latest development version of each dataset and schema.

### Making a suite release

It is very important to follow this specific procedure, otherwise a mixed release may be created, which would be "bad".

- Go to each category repository (e.g., [category-flat](https://github.com/RiverBench/category-flat)) and carry out the same procedure as for making a release of a dataset. Use the exact same version tag that you want to use for the suite.
- Wait for the CI jobs in each category repository to finish.
- Go to the [RiverBench main repository](https://github.com/RiverBench/RiverBench) and carry out the same procedure as for making a release of a dataset, using the same version tag as for the categories.

## Archive / backup

All releases (of schemas, datasets, profiles, and the suite) are archived in **[Zenodo](https://doi.org/10.5281/zenodo.7909063)**. This is however only a *backup* and it does not include the packaged datasets, only their sources, due to the excessive size of all the datasets.
