<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/tasks/flat-serialization-throughput/results "Link to the permanent URL of this resource.")</div><div markdown><abbr title="This page is entirely automatically generated and cannot be edited.">:material-lock-reset: Auto-generated</abbr></div></div>

# Benchmark results for task flat-serialization-throughput

[:octicons-arrow-left-24: Back to task definition](index.md)

<div style="text-align: center" markdown>[:material-star-plus: Report your benchmark results](../../documentation/reporting-results.md){ .md-button }</div>

### RiverBench results for task flat-serialization-throughput with profile flat-mixed-rdfstar

<span id="RAocQCk-I5Br8F882ezPZ-CIBr3HoGkgp-uW14dwKGzK8"></span>

!!! info

    :fontawesome-solid-diagram-project: This benchmark result was reported in a Nanopublication: [https://w3id.org/np/RAocQCk-I5Br8F882ezPZ-CIBr3HoGkgp-uW14dwKGzK8](https://w3id.org/np/RAocQCk-I5Br8F882ezPZ-CIBr3HoGkgp-uW14dwKGzK8).

    The documentation here was generated automatically.




- **<abbr title="A description of the subject resource.">Comment</abbr>**: Flat streaming serialization throughput benchmark, comparing Jelly to W3C serializations implemented in Apache Jena, as well as Jena's own binary formats. The benchmark was run on a modern x86-64 workstation.
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**:  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
- **<abbr title="Date of creation of the resource.">Date Created</abbr>**: `2024-11-07T14:19:26.471Z`
- **<abbr title="The citing entity cites the cited entity as source of data.">Cites as data source</abbr>**: [https://w3id.org/jelly/1.0.x/performance/#flat-streaming-serialization-throughput](https://w3id.org/jelly/1.0.x/performance/#flat-streaming-serialization-throughput)
- **<abbr title="This property specifies the protocol that a benchmark follows">Has followed protocol</abbr>**: 
    - **Type**:     
        - <abbr title="The parameters of a performed benchmark (rb:PerformedBenchmark). Instances of this class specify the RiverBench profile, task, systems, and metrics that were used in the benchmark.">Benchmark protocol</abbr> ([rb:BenchmarkProtocol](https://w3id.org/riverbench/schema/metadata#BenchmarkProtocol))
        - <abbr title="A protocol is used to provide guidelines to execute certain tasks">Protocol</abbr> ([irao:Protocol](http://ontology.ethereal.cz/irao/Protocol))
    - **<abbr title="Indicates that the subject is using a specific RiverBench benchmark task.">Uses benchmark task</abbr>**: [flat-serialization-throughput (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/flat-serialization-throughput)
    - **<abbr title="Indicates that the subject is using a specific RiverBench benchmark profile.">Uses benchmark profile</abbr>**: [flat-mixed-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/flat-mixed-rdfstar)
    - **<abbr title="Indicates a benchmark metric that is used in a benchmark. Values of this property should be specified as the name of the metric, in the exact spelling as in the corresponding task definition. For example: 'Loading throughput'.">Uses metric</abbr>**: Serialization throughput
    - **<abbr title="Indicates that the subject is using a specific system (e.g., an RDF store).">Uses system under test</abbr>**:     
        - Jelly (Jelly-JVM) (2.2.2)
        - N-Triples/N-Quads (Apache Jena) (5.2.0)
        - RDF binary Protobuf (Apache Jena) (5.2.0)
        - RDF binary Thrift (Apache Jena) (5.2.0)
        - Turtle/TriG, streaming blocks variant (Apache Jena) (5.2.0)
- **<abbr title="This property specifies a system that measures a benchmark">Has measuring system</abbr>**: [https://github.com/Jelly-RDF/jvm-benchmarks/tree/dd58f5de0916c1223ca115052567c1fb39f4cd62](https://github.com/Jelly-RDF/jvm-benchmarks/tree/dd58f5de0916c1223ca115052567c1fb39f4cd62)



### RiverBench results for task flat-serialization-throughput with profile flat-mixed-rdfstar

<span id="RABVe90JkVlX8bh8XkF0XPepRShqx2VEO6WUtA7HEofbc"></span>

!!! info

    :fontawesome-solid-diagram-project: This benchmark result was reported in a Nanopublication: [https://w3id.org/np/RABVe90JkVlX8bh8XkF0XPepRShqx2VEO6WUtA7HEofbc](https://w3id.org/np/RABVe90JkVlX8bh8XkF0XPepRShqx2VEO6WUtA7HEofbc).

    The documentation here was generated automatically.




- **<abbr title="A description of the subject resource.">Comment</abbr>**: Flat streaming serialization throughput benchmark, comparing Jelly to N-Triples/N-Quads in RDF4J and the RDF4J Binary RDF Format. The benchmark was run on a modern x86-64 workstation.
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**:  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
- **<abbr title="Date of creation of the resource.">Date Created</abbr>**: `2024-11-07T14:45:40.256Z`
- **<abbr title="The citing entity cites the cited entity as source of data.">Cites as data source</abbr>**: [https://w3id.org/jelly/1.0.x/performance/rdf4j/#flat-streaming-serialization-throughput](https://w3id.org/jelly/1.0.x/performance/rdf4j/#flat-streaming-serialization-throughput)
- **<abbr title="This property specifies the protocol that a benchmark follows">Has followed protocol</abbr>**: 
    - **Type**:     
        - <abbr title="The parameters of a performed benchmark (rb:PerformedBenchmark). Instances of this class specify the RiverBench profile, task, systems, and metrics that were used in the benchmark.">Benchmark protocol</abbr> ([rb:BenchmarkProtocol](https://w3id.org/riverbench/schema/metadata#BenchmarkProtocol))
        - <abbr title="A protocol is used to provide guidelines to execute certain tasks">Protocol</abbr> ([irao:Protocol](http://ontology.ethereal.cz/irao/Protocol))
    - **<abbr title="Indicates that the subject is using a specific RiverBench benchmark task.">Uses benchmark task</abbr>**: [flat-serialization-throughput (2.1.0)](https://w3id.org/riverbench/v/2.1.0/tasks/flat-serialization-throughput)
    - **<abbr title="Indicates that the subject is using a specific RiverBench benchmark profile.">Uses benchmark profile</abbr>**: [flat-mixed-rdfstar (2.1.0)](https://w3id.org/riverbench/v/2.1.0/profiles/flat-mixed-rdfstar)
    - **<abbr title="Indicates a benchmark metric that is used in a benchmark. Values of this property should be specified as the name of the metric, in the exact spelling as in the corresponding task definition. For example: 'Loading throughput'.">Uses metric</abbr>**: Serialization throughput
    - **<abbr title="Indicates that the subject is using a specific system (e.g., an RDF store).">Uses system under test</abbr>**:     
        - Jelly (Jelly-JVM) (2.2.2)
        - N-Triples/N-Quads (RDF4J) (5.0.2)
        - RDF4J Binary RDF Format (5.0.2)
- **<abbr title="This property specifies a system that measures a benchmark">Has measuring system</abbr>**: [https://github.com/Jelly-RDF/jvm-benchmarks/tree/dd58f5de0916c1223ca115052567c1fb39f4cd62](https://github.com/Jelly-RDF/jvm-benchmarks/tree/dd58f5de0916c1223ca115052567c1fb39f4cd62)

