# flat-quads (development version)

Flat sequence of quads (RDF 1.1 standard only)

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat sequence of quads (standard)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-quads
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [flat-mixed (dev)](https://w3id.org/riverbench/profiles/flat-mixed/dev)
    - [flat-mixed-nonstandard (dev)](https://w3id.org/riverbench/profiles/flat-mixed-nonstandard/dev)
    - [flat-mixed-rdfstar (dev)](https://w3id.org/riverbench/profiles/flat-mixed-rdfstar/dev)
    - [flat-mixed-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/flat-mixed-rdfstar-nonstandard/dev)
    - [flat-quads-nonstandard (dev)](https://w3id.org/riverbench/profiles/flat-quads-nonstandard/dev)
    - [flat-quads-rdfstar (dev)](https://w3id.org/riverbench/profiles/flat-quads-rdfstar/dev)
    - [flat-quads-rdfstar-nonstandard (dev)](https://w3id.org/riverbench/profiles/flat-quads-rdfstar-nonstandard/dev)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [https://w3id.org/riverbench/](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Has profile restriction. The restrictions are joined with the AND operator.">Has restriction</abbr>**: 
    - **Has restriction (1)**    
        - **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - **Has restriction (2)**    
        - **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**:     
            - <abbr title="Graph streams are a special case of quad streams, where each element contains exactly one named RDF graph.">Graphs</abbr> ([rb:graphs](https://w3id.org/riverbench/schema/metadata#graphs))
            - <abbr title="Quad streams consist of elements, where each element is an RDF dataset.">Quads</abbr> ([rb:quads](https://w3id.org/riverbench/schema/metadata#quads))
    - **Has restriction (3)**    
        - **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes

