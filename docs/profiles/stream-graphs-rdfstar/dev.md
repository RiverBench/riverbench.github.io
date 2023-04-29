# stream-graphs-rdfstar (development version)

Streaming graphs (with RDF-star)

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming graphs (RDF-star)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-graphs-rdfstar
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: [stream-graphs (dev)](https://w3id.org/riverbench/profiles/stream-graphs/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-graphs-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-graphs-rdfstar-nonstandard/dev)
    - [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar/dev)
    - [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
    - [stream-quads-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-quads-rdfstar/dev)
    - [stream-quads-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-quads-rdfstar-nonstandard/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
    - **Has restriction (2)**    
        - **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Graph streams are a special case of quad streams, where each element contains exactly one named RDF graph.">Graphs</abbr> ([rb:graphs](https://w3id.org/riverbench/schema/metadata#graphs))
    - **Has restriction (3)**    
        - **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes

