<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/profiles/flat-quads "Link to the permanent URL of this resource.")</div><div markdown>**[:material-database-edit: Edit this page](https://github.com/RiverBench/category-flat/edit/main/profiles/flat-quads.ttl "Edit this page's source in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../documentation/editing-docs.md "Need help with editing?")</div></div>

# Profile: flat-quads (development version)

Flat sequence of quads (RDF 1.1 standard only)

!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/profiles/flat-quads.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/profiles/flat-quads.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/profiles/flat-quads.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/profiles/flat-quads.jelly)**
    <br>:material-github: Source repository: **[category-flat](https://github.com/RiverBench/category-flat)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/dev/profiles/flat-quads`](https://w3id.org/riverbench/v/dev/profiles/flat-quads)



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Flat sequence of quads (standard) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-quads`
- **<abbr title="The version indicator (name or identifier) of a resource.">Version</abbr>**: `dev`
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [flat (dev)](https://w3id.org/riverbench/v/dev/categories/flat)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [flat-mixed (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-mixed)
    - [flat-mixed-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-mixed-rdfstar)
    - [flat-quads-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/flat-quads-rdfstar)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [assist-iot-weather-graphs (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)
    - [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
    - [nanopubs (dev)](https://w3id.org/riverbench/datasets/nanopubs/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (​1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**:     
                - <abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr> ([stax:hasStreamType](https://w3id.org/stax/ontology#hasStreamType))
                - <abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr> ([stax:hasStreamTypeUsage](https://w3id.org/stax/ontology#hasStreamTypeUsage))
                - **Path (​3)**    
                    - **<abbr title="The (single) value of this property represents a path that is matched zero or more times.">Zero or more path</abbr>**: [http://www.w3.org/2004/02/skos/core#broader](http://www.w3.org/2004/02/skos/core#broader)
        - **Property (​2)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: yes
            - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr> ([rb:conformsToRdf11](https://w3id.org/riverbench/schema/metadata#conformsToRdf11))
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A dataset in the RiverBench benchmark suite">RiverBench dataset</abbr> ([rb:Dataset](https://w3id.org/riverbench/schema/metadata#Dataset))
- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has distribution shape</abbr>**: 
    - **<abbr title="Specifies a list of shapes so that the value nodes must conform to at least one of the shapes.">Or</abbr>**:     
        - **Or (​1)**    
            - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
                - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
                - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
        - **Or (​2)**    
            - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
                - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
                - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A distribution of a dataset in the RiverBench benchmark suite.">RiverBench dataset distribution</abbr> ([rb:Distribution](https://w3id.org/riverbench/schema/metadata#Distribution))


## Download links

Below you will find links to download this profile's datasets in different lengths. The length of the dataset
is measured in stream elements (individual graphs or datasets) and is indicated in the table.
To see the size in statements (triples or quads), hover your mouse over the download link.

!!! warning

    Some datasets are shorter than others and a given fixed-size distribution may not be available for all datasets.

!!! note

    There are two available types of distributions for this profile: plain flat files, and the universal distribution in the Jelly format. See the [documentation](../documentation/dataset-release-format.md) for details.

### Plain flat distributions (N-Quads)

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | <abbr title="10,000 stream elements; 1,160,000 statements">[10K (5.0 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_10K.nq.gz)</abbr> | <abbr title="100,000 stream elements; 11,600,000 statements">[100K (50.3 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_100K.nq.gz)</abbr> | – | <abbr title="701,278 stream elements; 81,348,248 statements">[Full (353.0 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_full.nq.gz)</abbr>
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | <abbr title="10,000 stream elements; 370,000 statements">[10K (4.0 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_10K.nq.gz)</abbr> | <abbr title="100,000 stream elements; 3,700,000 statements">[100K (39.6 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_100K.nq.gz)</abbr> | <abbr title="1,000,000 stream elements; 37,000,000 statements">[1M (395.9 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_1M.nq.gz)</abbr> | <abbr title="4,382,599 stream elements; 162,156,163 statements">[Full (1.7 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_full.nq.gz)</abbr>
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | <abbr title="10,000 stream elements; 340,000 statements">[10K (3.5 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_10K.nq.gz)</abbr> | <abbr title="100,000 stream elements; 3,307,350 statements">[100K (35.7 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_100K.nq.gz)</abbr> | <abbr title="1,000,000 stream elements; 33,423,542 statements">[1M (384.6 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_1M.nq.gz)</abbr> | <abbr title="5,000,000 stream elements; 171,885,662 statements">[Full (1.7 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/flat_full.nq.gz)</abbr>

### Jelly distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[assist-iot-weather-graphs](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev) | <abbr title="10,000 stream elements; 1,160,000 statements">[10K (703.3 KB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 11,600,000 statements">[100K (6.8 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz)</abbr> | – | <abbr title="701,278 stream elements; 81,348,248 statements">[Full (47.7 MB)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz)</abbr>
[citypulse-traffic-graphs](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev) | <abbr title="10,000 stream elements; 370,000 statements">[10K (3.3 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 3,700,000 statements">[100K (32.9 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 37,000,000 statements">[1M (330.3 MB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="4,382,599 stream elements; 162,156,163 statements">[Full (1.4 GB)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_full.jelly.gz)</abbr>
[nanopubs](https://w3id.org/riverbench/datasets/nanopubs/dev) | <abbr title="10,000 stream elements; 340,000 statements">[10K (2.9 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 3,307,350 statements">[100K (29.6 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 33,423,542 statements">[1M (332.7 MB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="5,000,000 stream elements; 171,885,662 statements">[Full (1.5 GB)](https://w3id.org/riverbench/datasets/nanopubs/dev/files/jelly_full.jelly.gz)</abbr>