# How to contribute?

**Hi there!** :wave: :blush:

RiverBench is an open, community-driven project, so you are more than welcome to contribute. This page explains how to do it.

## Contributing datasets

Do you have an interesting RDF dataset that would make a good addition to RiverBench? Great!

What datasets are we looking for?

- **Freely licensed** – the dataset must be licensed under a free license, such as [CC0](https://creativecommons.org/publicdomain/zero/1.0/), [CC BY](https://creativecommons.org/licenses/by/4.0/), or [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/). The license must allow commercial use and derivative works.
- **Somewhat streaming in nature** – streaming comes in many shapes and sizes. Have a look at the existing datasets – we have [streams of timestamped weather data](../datasets/assist-iot-weather/dev/index.md), but also [a stream of fact annotations in Wikidata](../datasets/yago-annotated-facts/dev/index.md). The important thing is that the dataset must be explicitly split into discrete elements.
- **Interesting technically** – we are especially interested in expanding the coverage of the rarer types of streams, such as those using RDF-star, generalized triples, or quads. Other interesting types of datasets include those that use RDF in atypical ways, like with large GeoSPARQL literals or dense vector embeddings. Anything exotic is welcome!
- **Interesting thematically and relevant** – does your dataset bring an interesting new use case? Perfect! Even better if the use case has seen real-world usage.
- **Large** – the stream must be at least 10 thousand elements long, preferably more. The larger the better.

If you think your dataset fits the bill, have a look at the [dedicated guide on creating new datasets](creating-new-dataset.md). If you still have questions, don't hesitate to contact RiverBench's maintainer by [opening an issue on GitHub](https://github.com/RiverBench/RiverBench/issues/new/choose).

## Reporting issues

Found a bug in a dataset or the metadata? Or in something else entirely? Feel free to [open an issue on GitHub](https://github.com/RiverBench/RiverBench/issues/new/choose). Please try to be as specific as possible on your issue, so that it can be resolved quickly.

## Improving the documentation

You can easily edit the documentation on this website – see the [dedicated guide](editing-docs.md) for more details.

## Improving the code or metadata

Have a look at our [GitHub organization page](https://github.com/RiverBench) and the repositories there. Some important ones are:

- [RiverBench](https://github.com/RiverBench/RiverBench) – the main repository
- [riverbench.github.io](https://github.com/RiverBench/riverbench.github.io) – the repository for the website
- [schema](https://github.com/RiverBench/schema) – schemas and ontologies
- [ci-worker](https://github.com/RiverBench/ci-worker) – source for the application that packages datasets, munges metadata, and generates documentation (Scala)
- [ci-workflows](https://github.com/RiverBench/ci-workflows) – GitHub Actions workflows for the CI
- [dataset-template](https://github.com/RiverBench/dataset-template) – template repository for new datasets

You are welcome to submit any pull requests to these repositories. If you are unsure where to submit your changes, feel free to [open an issue](https://github.com/RiverBench/RiverBench/issues/new/choose) and ask.

## Deeper changes

Do you see a glaring issue with the way RiverBench is organized? Or maybe you have a great idea for a new feature? Please contact the maintainer directly: [Piotr Sowiński (Ostrzyciel)](https://github.com/Ostrzyciel) by following the contact info on his profile page. **We are open to scientific collaboration.**
