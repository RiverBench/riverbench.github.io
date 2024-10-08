<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/tasks/flat-deserialization-throughput "Link to the permanent URL of this resource.")</div><div markdown>**[:material-file-edit: Edit this page](https://github.com/RiverBench/category-flat/edit/main/tasks/flat-deserialization-throughput/index.md "Edit this page's source in Markdown on GitHub.")**</div><div markdown>**[:material-database-edit: Edit metadata](https://github.com/RiverBench/category-flat/edit/main/tasks/flat-deserialization-throughput/metadata.ttl "Edit this page's metadata in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../../documentation/editing-docs.md "Need help with editing?")</div></div>

# Task: Flat RDF deserialization throughput (development version)

Task identifier: `flat-deserialization-throughput`

A benchmark task measuring the throughput (in statements per second) of deserializing a byte stream into a flat sequence of RDF triples or RDF quads.

## Methodology

### Data

Flat distributions of any dataset in the [`flat` category](../../categories/flat/index.md) of RiverBench may be used for this task.

### Workload

The task consists of deserializing serialized RDF data stored in memory to a flat sequence of RDF statements. To isolate the performance of the deserializer itself, the following steps are taken:

- The data (serialized RDF statements in the tested serialization format) is preloaded into memory before the benchmark starts.
- The deserialization process is repeated multiple times to amortize the cost of the initial setup, just-in-time code recompilation, and other external factors.
- The deserialized statements are not inserted into any data structure or database, but just temporarily stored in memory and immediately discarded. This is to avoid the overhead of maintaining additional data structures.
    - See the [`flat-rdf-store-loading`](../flat-rdf-store-loading/index.md) task for a benchmark that measures the time taken to load the deserialized data into a database.

### Metrics

- **Deserialization throughput** – the primary metric, measured in RDF statements (triples or quads) per second. This is calculated as the total number of RDF statements deserialized divided by the total time taken to deserialize them.


## Results

**See the results for this task reported by the community: [RESULTS](results.md).**

## This task in benchmarks outside of RiverBench

- In the paper about the ERI format, a similar benchmark can be found in Section 4.3. The corresponding task in the paper is named "Decompression time" and measures the time taken to deserialize the entire sequence of triples.
    - Fernández, J. D., Llaves, A., & Corcho, O. (2014). Efficient RDF interchange (ERI) format for RDF data streams. In The Semantic Web–ISWC 2014: 13th International Semantic Web Conference, Riva del Garda, Italy, October 19-23, 2014. Proceedings, Part II 13 (pp. 244-259). Springer International Publishing. [https://doi.org/10.1007/978-3-319-11915-1_16](https://doi.org/10.1007/978-3-319-11915-1_16)

## See also

- Version of this task for grouped RDF streams: [`stream-deserialization-throughput`](../stream-deserialization-throughput/index.md)
- The inverse task: [`flat-serialization-throughput`](../flat-serialization-throughput/index.md)


## Metadata



!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/tasks/flat-deserialization-throughput.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/tasks/flat-deserialization-throughput.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/tasks/flat-deserialization-throughput.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/tasks/flat-deserialization-throughput.jelly)**
    <br>:material-github: Source repository: **[category-flat](https://github.com/RiverBench/category-flat)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/dev/tasks/flat-deserialization-throughput`](https://w3id.org/riverbench/v/dev/tasks/flat-deserialization-throughput)



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat RDF deserialization throughput _(<abbr title="English">en</abbr>)_
- **<abbr title="An account of the resource.">Description</abbr>**: A benchmark task measuring the throughput (in statements per second) of deserializing a byte stream into a flat sequence of RDF triples or RDF quads. _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-deserialization-throughput`
- **<abbr title="The version indicator (name or identifier) of a resource.">Version</abbr>**: `dev`
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
    - **<abbr title="This axiom needed so that Protege loads DCAT 3 without errors.">Homepage</abbr>**:     
        -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
        - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [flat (dev)](https://w3id.org/riverbench/v/dev/categories/flat)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

