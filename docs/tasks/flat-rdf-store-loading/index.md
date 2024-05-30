# Loading data into an RDF store

A benchmark task measuring the time taken and resources used by RDF stores when loading flat RDF data (triples or quads).

## Methodology

### Data

Flat distributions of any dataset in the [`flat` category](../../categories/flat/index.md) of RiverBench may be used for this task.

### Workload

In this task, an RDF store is set up (for example, [Apache Jena TDB2](https://jena.apache.org/documentation/tdb2/index.html) or Virtuoso) and then instructed to load a flat file containing RDF statements (triples or quads).

- When comparing multiple RDF stores, identical input data (serialized in the same format) should be used for all stores.
- The benchmark includes the time taken to deserialize the input data and insert the resulting RDF statements into the store, considering the entire process and the impact of the underlying I/O.
- Input data may be either batched or streamed, depending on the capabilities of the RDF store being tested and the specific research questions being addressed.
    - When using batched input, the input dataset is split into chunks consisting of N statements, and each chunk is processed by the system separately. The metrics (see below) are typically calculated per chunk.
    - When using streamed input, the input dataset is processed as a continuous stream of individual statements (in RDF-STaX terminology: [flat RDF stream](https://w3id.org/stax/dev/taxonomy#flat-rdf-stream)). The metrics are typically calculated in regular time intervals or after processing a certain number of statements.

### Metrics

- Time taken to deserialize the input data and insert the resulting RDF statements into the RDF store. From this measurement, the insertion throughput (in statements per second) can be calculated.
- Memory usage during and after the loading process.
- Storage space used by the RDF store during and after the loading process.
- Total CPU time used during the loading process.

## Results

There are no results with RiverBench available for this task yet.

## Examples and references

- Such a benchmark was performed in a paper comparing several RDF stores on IoT devices (Section 8). There, the authors measured the time taken to load the data and the memory usage.
    - Le-Tuan, A., Hayes, C., Hauswirth, M., & Le-Phuoc, D. (2020). Pushing the Scalability of RDF Engines on IoT Edge Devices. Sensors, 20(10), 2788. [https://doi.org/10.3390/s20102788](https://doi.org/10.3390/s20102788)


## Metadata



!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/tasks/flat-rdf-store-loading.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/tasks/flat-rdf-store-loading.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/tasks/flat-rdf-store-loading.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/tasks/flat-rdf-store-loading.jelly)**



### General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Loading data into an RDF store _(<abbr title="English">en</abbr>)_
- **<abbr title="An account of the resource.">Description</abbr>**: A benchmark task measuring the time taken and resources used by RDF stores when loading flat RDF data (triples or quads). _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-rdf-store-loading`
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

