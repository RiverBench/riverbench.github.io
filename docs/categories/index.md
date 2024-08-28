{{ top_buttons() }}

# Benchmark categories

In RiverBench, benchmark tasks and profiles are grouped into **benchmark categories**, listed below. A benchmark task is simply a description (a recipe) for conducting benchmarks. Profiles are collections of datasets, grouped by shared technical characteristics (e.g., stream type, whether RDF-star is used or not). Within each category, each task may be used with any of the profiles.

Not sure where to start? See our **[getting started](../documentation/using.md)**, which explains how to use RiverBench's tasks and profiles.

## Categories

- **[Flat RDF (sequences of triples/quads)](flat/index.md)** – benchmarks for flat RDF collections (RDF graphs, RDF datasets) that can also be viewed as sequences of triples or quads.
    - *Example task: compressing an RDF graph.*
- **[Grouped RDF streaming](stream/index.md)** – benchmarks for streams of RDF graphs or datasets.
    - *Example task: measuring the throughput of streaming RDF datasets over the network.*

## See also

- [Benchmark results](../results/index.md)
- [Creating a new bechmark category](../documentation/categories.md)
- [Creating a new benchmark task](../documentation/creating-new-task.md)
