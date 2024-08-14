# Flat RDF compression

A benchmark task measuring the compression efficiency of flat RDF serializations.


## Methodology

### Data

Flat distributions of any dataset in the [`flat` category](../../categories/flat/index.md) of RiverBench may be used for this task.

### Workload

The task consists of serializing RDF data to bytes and measuring the size of the obtained representation.

In this task, the time taken to serialize and deserialize the data is not considered – see the [`flat-serialization-throughput`](../flat-serialization-throughput/index.md) and [`flat-deserialization-throughput`](../flat-deserialization-throughput/index.md) tasks for that aspect.

### Metrics

- The primary metric is the serialized representation size of the RDF data, in bytes.
- Additionally, the compression ratio can be calculated as the ratio of the reference size to the compressed size. The reference size is the size of the same data serialized using a baseline method, e.g., the N-Triples serialization format.
    - In the RDF literature, the "compression ratio" is often defined as the inverse of the above definition and expressed as a percentage. For example, a compression ratio of (50%) means that the compressed data is half the size of the reference data.

## Results

There are no results with RiverBench available for this task yet.

## Examples and references

- In a paper about an RDF compression method using MapReduce, a compression benchmark was performed in Section 5.1. The authors have measured the output size of their method (in gigabytes) in comparison to the input data size.
    - Urbani, J., Maassen, J., Drost, N., Seinstra, F., & Bal, H. (2013). Scalable RDF data compression with MapReduce. Concurrency and Computation: Practice and Experience, 25(1), 24-39. [https://doi.org/10.1002/cpe.2840](https://doi.org/10.1002/cpe.2840)
- In the paper about the HDT binary format, such a benchmark was performed in Section 5. The "Compression Ratio" metric there refers to the ratio between the compressed data size and the reference data size, with N-Triples used as the reference.
    - Fernández, J. D., Martínez-Prieto, M. A., Gutiérrez, C., Polleres, A., & Arias, M. (2013). Binary RDF representation for publication and exchange (HDT). Journal of Web Semantics, 19, 22-41. [https://doi.org/10.1016/j.websem.2013.01.002](https://doi.org/10.1016/j.websem.2013.01.002)
- In the paper about the ERI format, such a benchmark can be found in Section 4.2. The "Compression Ratio" metric there refers to the ratio between the compressed data size and the reference data size, with N-Triples used as the reference.
    - Fernández, J. D., Llaves, A., & Corcho, O. (2014). Efficient RDF interchange (ERI) format for RDF data streams. In The Semantic Web–ISWC 2014: 13th International Semantic Web Conference, Riva del Garda, Italy, October 19-23, 2014. Proceedings, Part II 13 (pp. 244-259). Springer International Publishing. [https://doi.org/10.1007/978-3-319-11915-1_16](https://doi.org/10.1007/978-3-319-11915-1_16)

## See also

- Version of this task for grouped RDF streams: [`stream-compression`](../stream-compression/index.md)


## Metadata



!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/tasks/flat-compression.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/tasks/flat-compression.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/tasks/flat-compression.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/tasks/flat-compression.jelly)**



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat RDF compression _(<abbr title="English">en</abbr>)_
- **<abbr title="An account of the resource.">Description</abbr>**: A benchmark task measuring the compression efficiency of flat RDF serializations. _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-compression`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
    - **<abbr title="This axiom needed so that Protege loads DCAT2 without errors.">Homepage</abbr>**:     
        -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
        - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [flat (dev)](https://w3id.org/riverbench/v/dev/categories/flat)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

