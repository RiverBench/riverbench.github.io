# Flat RDF (sequences of triples/quads)

Benchmark category of generic tasks involving flat RDF streams (elements are either RDF triples or RDF quads). Each dataset in this category can be also treated as a single RDF graph/RDF dataset.
## Benchmark tasks

Below you will find a list of tasks that are part of this benchmark category.

!!! tip

    Benchmark tasks and profiles in RiverBench have machine-readable metadata in RDF.
    You can find RDF download links for each profile on its documentation page.
    You can also use the [HTTP content negotiation mechanism](../../documentation/metadata.md).

--8<-- "docs/categories/flat/task_table.md"

## Benchmark profiles

Profiles in RiverBench group datasets that share common technical characteristics.
For example, whether the datasets consist of triples or quads, if they use RDF-star, etc.
The profiles are intended to be used in benchmarks to compare the performance of different systems on a well-defined collection of datasets.

See the **[quick start guide](../../documentation/using.md)** for more information on how to use the profiles, tasks, and datasets.

--8<-- "docs/categories/flat/profile_table.md"



## Metadata



!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/2.0.0/categories/flat.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/2.0.0/categories/flat.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/2.0.0/categories/flat.rdf)**, **[Jelly](https://w3id.org/riverbench/v/2.0.0/categories/flat.jelly)**



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat RDF (sequences of triples/quads) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: 2.0.0
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (2.0.0)](https://w3id.org/riverbench/v/2.0.0)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

### Content

- **<abbr title="For benchmark categories this property indicates tasks that belong to the category.">Has benchmark task</abbr>**: 
    - [flat-compression (2.0.0)](https://w3id.org/riverbench/v/2.0.0/tasks/flat-compression)
    - [flat-deserialization-throughput (2.0.0)](https://w3id.org/riverbench/v/2.0.0/tasks/flat-deserialization-throughput)
    - [flat-rdf-store-loading (2.0.0)](https://w3id.org/riverbench/v/2.0.0/tasks/flat-rdf-store-loading)
    - [flat-serialization-throughput (2.0.0)](https://w3id.org/riverbench/v/2.0.0/tasks/flat-serialization-throughput)
- **<abbr title="For benchmark categories this property indicates profiles that belong to the category.">Has benchmark profile</abbr>**: 
    - [flat-mixed (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-mixed)
    - [flat-mixed-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-mixed-nonstandard)
    - [flat-mixed-rdfstar (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-mixed-rdfstar)
    - [flat-mixed-rdfstar-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-mixed-rdfstar-nonstandard)
    - [flat-quads (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads)
    - [flat-quads-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads-nonstandard)
    - [flat-quads-rdfstar (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads-rdfstar)
    - [flat-quads-rdfstar-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads-rdfstar-nonstandard)
    - [flat-triples (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-triples)
    - [flat-triples-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-triples-nonstandard)
    - [flat-triples-rdfstar (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-triples-rdfstar)
    - [flat-triples-rdfstar-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-triples-rdfstar-nonstandard)

