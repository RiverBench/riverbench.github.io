# stream-mixed-rdfstar (development version)

Streaming triples or quads (with RDF-star)

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming triples or quads (RDF-star)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-mixed-rdfstar
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: 
    - [stream-graphs (dev)](https://w3id.org/riverbench/profiles/stream-graphs/dev)
    - [stream-graphs-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-graphs-rdfstar/dev)
    - [stream-mixed (dev)](https://w3id.org/riverbench/profiles/stream-mixed/dev)
    - [stream-quads (dev)](https://w3id.org/riverbench/profiles/stream-quads/dev)
    - [stream-quads-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-quads-rdfstar/dev)
    - [stream-triples (dev)](https://w3id.org/riverbench/profiles/stream-triples/dev)
    - [stream-triples-rdfstar (dev)](https://w3id.org/riverbench/profiles/stream-triples-rdfstar/dev)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: [stream-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/stream-mixed-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [example-triples (dev)](https://w3id.org/riverbench/datasets/example-triples/dev)
    - [linked-spending (dev)](https://w3id.org/riverbench/datasets/linked-spending/dev)
    - [lod-katrina (dev)](https://w3id.org/riverbench/datasets/lod-katrina/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
    - [politiquices (dev)](https://w3id.org/riverbench/datasets/politiquices/dev)
    - [yago-annotated-facts (dev)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**:     
            - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
            - <abbr title="The dataset is distributed as a stream of RDF quads.">Quad stream distribution</abbr> ([rb:quadStreamDistribution](https://w3id.org/riverbench/schema/metadata#quadStreamDistribution))
            - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
    - **Has restriction (2)**    
        - **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes

