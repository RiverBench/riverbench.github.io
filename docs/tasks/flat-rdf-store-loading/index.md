# Task: Loading data into an RDF store (development version)

Task identifier: `flat-rdf-store-loading`

A benchmark task measuring the time taken and resources used by RDF stores when loading flat RDF data (triples or quads).

## Methodology

### Data

Flat distributions of any dataset in the [`flat` category](../../categories/flat/index.md) of RiverBench may be used for this task.

### Workload

In this task, an RDF store is set up (for example, [Apache Jena TDB2](https://jena.apache.org/documentation/tdb2/index.html), [OpenLink Virtuoso Open Source v7.x](https://github.com/openlink/virtuoso-opensource/), or [RDF4J's NativeStore](https://rdf4j.org/documentation/programming/repository/)) and then loaded with a flat dump of RDF statements (triples or quads).

- When comparing multiple RDF stores, identical input data (serialized in the same format) should be used for all stores.
- The benchmark includes the time taken to deserialize the input data and insert the resulting RDF statements into the store, considering the entire process and the impact of the underlying I/O.
- Input data may be either batched or streamed statement by statement, depending on the capabilities of the RDF store being tested and the specific research questions being addressed.
    - When using batched input, the input dataset is split into chunks consisting of N statements, and each chunk is processed by the system separately. The metrics (see below) are typically calculated per chunk.
    - When using streamed input, the input dataset is processed as a continuous stream of individual statements (in RDF-STaX terminology: [flat RDF stream](https://w3id.org/stax/dev/taxonomy#flat-rdf-stream)). The metrics are typically calculated in regular time intervals or after processing a certain number of statements.

### Metrics

Benchmarks may choose to measure only some of the following metrics:

- **Load time** – time taken to deserialize the input data and insert the resulting RDF statements into the RDF store, including any indexing and I/O operations. From this measurement, the loading throughput can be calculated (see below).
- **Loading throughput** – the rate at which the RDF store can load data, measured in RDF statements (triples or quads) per second. This can be either calculated per chunk (in the case of batched input) or as an average over the entire loading process.
- **Memory usage** – main system memory usage in bytes, during and after the loading process.
- **Storage size** – size of the RDF store on disk, in bytes. May be measured during and after the loading process.
- **Total CPU time** – the total CPU time (across all processors) allocated to the RDF store. Measured during the loading process.

## Results

**See the results for this task reported by the community: [RESULTS](results.md).**

## This task in benchmarks outside of RiverBench

- The Berlin SPARQL Benchmark (BSBM) includes a data loading phase where the data is loaded into the RDF store. The time taken to load the data (*LT* metric) is one of the metrics used to evaluate the performance of the RDF store. The dataset used in BSBM is synthetic.
    - Bizer, C., & Schultz, A. (2009). The Berlin SPARQK Benchmark. International Journal on Semantic Web and Information Systems (IJSWIS), 5(2), 1-24. [https://doi.org/10.4018/jswis.2009040101](https://doi.org/10.4018/jswis.2009040101)
- Similarly, the Lehigh University Benchmark (LUBM) includes a data loading phase where the data is loaded into the RDF store. The time taken to load the data (*load time* metric) is one of the metrics used to evaluate the performance of the RDF store. The dataset used in LUBM is synthetic.
    - Guo, Y., Pan, Z., & Heflin, J. (2005). LUBM: A benchmark for OWL knowledge base systems. Journal of Web Semantics, 3(2-3), 158-182. [https://doi.org/10.1016/j.websem.2005.06.005](https://doi.org/10.1016/j.websem.2005.06.005)
- A load time benchmark was performed in a paper comparing several RDF stores on a few different IoT devices (Section 8). There, the authors measured the time taken to load the data and the memory usage. A single real dataset was used.
    - Le-Tuan, A., Hayes, C., Hauswirth, M., & Le-Phuoc, D. (2020). Pushing the Scalability of RDF Engines on IoT Edge Devices. Sensors, 20(10), 2788. [https://doi.org/10.3390/s20102788](https://doi.org/10.3390/s20102788)
- The RDF-3X paper also included a load time benchmark, with 3 different datasets (non-synthetic). They report the total load time in minutes and the size on disk of the resulting store.
    - Neumann, T., & Weikum, G. (2010). The RDF-3X engine for scalable management of RDF data. The VLDB Journal, 19, 91-113. [https://doi.org/10.1007/s00778-009-0165-y](https://doi.org/10.1007/s00778-009-0165-y)


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
- **<abbr title="An entity responsible for making contributions to the resource.">Contributor</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Ted Thibodeau Jr
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: TallTed
    - **<abbr title="This axiom needed so that Protege loads DCAT2 without errors.">Homepage</abbr>**: [http://id.myopenlink.net/dataspace/person/tthibodeau](http://id.myopenlink.net/dataspace/person/tthibodeau)
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [flat (dev)](https://w3id.org/riverbench/v/dev/categories/flat)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

