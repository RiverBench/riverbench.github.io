# flat-quads-nonstandard (2.0.0)

Flat sequence of quads (with non-standard extensions)

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads-nonstandard.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads-nonstandard.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads-nonstandard.rdf)**, **[Jelly](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads-nonstandard.jelly)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat sequence of quads (non-standard) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-quads-nonstandard`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: 2.0.0
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [flat (2.0.0)](https://w3id.org/riverbench/v/2.0.0/categories/flat)
- **<abbr title="Indicates that this profile contains all datasets of the other profile">Is superset of profile</abbr>**: [flat-quads (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [flat-mixed-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-mixed-nonstandard)
    - [flat-mixed-rdfstar-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-mixed-rdfstar-nonstandard)
    - [flat-quads-rdfstar-nonstandard (2.0.0)](https://w3id.org/riverbench/v/2.0.0/profiles/flat-quads-rdfstar-nonstandard)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather-graphs (1.0.1)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/1.0.1)
    - [citypulse-traffic-graphs (1.0.1)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/1.0.1)
    - [nanopubs (1.0.1)](https://w3id.org/riverbench/datasets/nanopubs/1.0.1)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (2.0.0)](https://w3id.org/riverbench/v/2.0.0)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: no
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr> ([rb:usesRdfStar](https://w3id.org/riverbench/schema/metadata#usesRdfStar))
        - **Property (2)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**:     
                - <abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr> ([stax:hasStreamType](https://w3id.org/stax/ontology#hasStreamType))
                - <abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr> ([stax:hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage))
                - **Path (3)**    
                    - **<abbr title="The (single) value of this property represents a path that is matched zero or more times.">Zero or more path</abbr>**: [http://www.w3.org/2004/02/skos/core#broader](http://www.w3.org/2004/02/skos/core#broader)
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A dataset in the RiverBench benchmark suite">RiverBench dataset</abbr> ([rb:Dataset](https://w3id.org/riverbench/schema/metadata#Dataset))
- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has distribution shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
        - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A distribution of a dataset in the RiverBench benchmark suite.">RiverBench dataset distribution</abbr> ([rb:Distribution](https://w3id.org/riverbench/schema/metadata#Distribution))


## Download links

Below you will find links to download the profile's datasets in different lengths.

!!! warning

    Some datasets are shorter than others and a given distribution may not be available for all datasets.
    In that case, a link to the longest available distribution of the dataset is provided.

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/1.0.1) | [10K (5.04 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/1.0.1/files/flat_10K.nq.gz) | [100K (50.34 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/1.0.1/files/flat_100K.nq.gz) | [Full (353.01 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/1.0.1/files/flat_full.nq.gz) | [Full (353.01 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/1.0.1/files/flat_full.nq.gz)
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/1.0.1) | [10K (3.96 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/1.0.1/files/flat_10K.nq.gz) | [100K (39.64 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/1.0.1/files/flat_100K.nq.gz) | [1M (395.85 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/1.0.1/files/flat_1M.nq.gz) | [Full (1.69 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/1.0.1/files/flat_full.nq.gz)
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/1.0.1) | [10K (3.46 MB)](https://w3id.org/riverbench/datasets/nanopubs/1.0.1/files/flat_10K.nq.gz) | [100K (35.75 MB)](https://w3id.org/riverbench/datasets/nanopubs/1.0.1/files/flat_100K.nq.gz) | [1M (384.63 MB)](https://w3id.org/riverbench/datasets/nanopubs/1.0.1/files/flat_1M.nq.gz) | [Full (1.69 GB)](https://w3id.org/riverbench/datasets/nanopubs/1.0.1/files/flat_full.nq.gz)