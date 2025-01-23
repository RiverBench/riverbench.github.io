<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs "Link to the permanent URL of this resource.")</div><div markdown>**[:material-database-edit: Edit this page](https://github.com/RiverBench/category-stream/edit/main/profiles/stream-subject-graphs.ttl "Edit this page's source in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../documentation/editing-docs.md "Need help with editing?")</div></div>

# Profile: stream-subject-graphs (development version)

Streaming unnamed subject graphs (RDF 1.1 standard only)

!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs.ttl)**, **[N-Triples](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs.nt)**, **[RDF/XML](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs.rdf)**, **[Jelly](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs.jelly)**
    <br>:material-github: Source repository: **[category-stream](https://github.com/RiverBench/category-stream)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs`](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs)



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Streaming unnamed subject graphs (standard) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-subject-graphs`
- **<abbr title="The version indicator (name or identifier) of a resource.">Version</abbr>**: `dev`
- **<abbr title="Indicates that the subject (either a task or a profile) is in benchmark category. This property is functional (each task/profile must be in exactly one benchmark category).">In benchmark category</abbr>**: [stream (dev)](https://w3id.org/riverbench/v/dev/categories/stream)
- **<abbr title="Indicates that this profile's datasets are all in the other profile">Is subset of profile</abbr>**: 
    - [stream-graphs (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs)
    - [stream-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-graphs-rdfstar)
    - [stream-mixed (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed)
    - [stream-mixed-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-mixed-rdfstar)
    - [stream-subject-graphs-rdfstar (dev)](https://w3id.org/riverbench/v/dev/profiles/stream-subject-graphs-rdfstar)
- **<abbr title="Indicates which datasets are included in the profile">Includes dataset</abbr>**: 
    - [digital-agenda-indicators (dev)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev)
    - [linked-spending (dev)](https://w3id.org/riverbench/datasets/linked-spending/dev)
    - [muziekweb (dev)](https://w3id.org/riverbench/datasets/muziekweb/dev)
    - [openaire-lod (dev)](https://w3id.org/riverbench/datasets/openaire-lod/dev)
    - [osm2rdf-denmark (dev)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev)
- **<abbr title="Indicates the benchmark suite to which a dataset or profile belongs">In suite</abbr>**: [RiverBench (dev)](https://w3id.org/riverbench/)

## Technical metadata

- **<abbr title="Specifies the SHACL shape of distributions that are allowed in a given benchmark profile.">Has dataset shape</abbr>**: 
    - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
        - **Property (​1)**    
            - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="An RDF subject graph stream is an RDF graph stream in which every element contains an IRI node (called the subject node) that uniquely identifies the graph in the stream. Every other node in the graph can be reached by traversing triples, starting from the subject node.">RDF subject graph stream</abbr> ([stax:subjectGraphStream](https://w3id.org/stax/ontology#subjectGraphStream))
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
                - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
                - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
        - **Or (​2)**    
            - **<abbr title="Links a shape to its property shapes.">Property</abbr>**:     
                - **<abbr title="Specifies a value that must be among the value nodes.">Has value</abbr>**: <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
                - **<abbr title="Specifies the property path of a property shape.">Path</abbr>**: <abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr> ([rb:hasDistributionType](https://w3id.org/riverbench/schema/metadata#hasDistributionType))
    - **<abbr title="Links a shape to a class, indicating that all instances of the class must conform to the shape.">Target class</abbr>**: <abbr title="A distribution of a dataset in the RiverBench benchmark suite.">RiverBench dataset distribution</abbr> ([rb:Distribution](https://w3id.org/riverbench/schema/metadata#Distribution))


## Download links

Below you will find links to download this profile's datasets in different lengths. The length of the dataset
is measured in stream elements (individual graphs or datasets) and is indicated in the table.
To see the size in statements (triples or quads), hover your mouse over the download link.

!!! warning

    Some datasets are shorter than others and a given fixed-size distribution may not be available for all datasets.

!!! note

    There are two available types of distributions for this profile: plain streaming packages, and the universal distribution in the Jelly format. See the [documentation](../documentation/dataset-release-format.md) for details.

### Plain streaming distributions (Turtle)

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | <abbr title="10,000 stream elements; 82,424 statements">[10K (316.9 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_10K.tar.gz)</abbr> | <abbr title="100,000 stream elements; 811,625 statements">[100K (3.6 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_100K.tar.gz)</abbr> | <abbr title="1,000,000 stream elements; 8,108,967 statements">[1M (32.4 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_1M.tar.gz)</abbr> | <abbr title="1,440,415 stream elements; 11,669,016 statements">[Full (46.2 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/stream_full.tar.gz)</abbr>
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | <abbr title="10,000 stream elements; 158,342 statements">[10K (1.3 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_10K.tar.gz)</abbr> | <abbr title="100,000 stream elements; 1,716,898 statements">[100K (10.0 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_100K.tar.gz)</abbr> | <abbr title="1,000,000 stream elements; 23,371,403 statements">[1M (139.9 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_1M.tar.gz)</abbr> | <abbr title="2,477,552 stream elements; 55,097,866 statements">[Full (346.0 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/stream_full.tar.gz)</abbr>
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | <abbr title="10,000 stream elements; 51,721 statements">[10K (861.0 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_10K.tar.gz)</abbr> | <abbr title="100,000 stream elements; 517,454 statements">[100K (8.4 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_100K.tar.gz)</abbr> | <abbr title="1,000,000 stream elements; 6,916,692 statements">[1M (87.3 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_1M.tar.gz)</abbr> | <abbr title="2,450,357 stream elements; 36,195,263 statements">[Full (251.8 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/stream_full.tar.gz)</abbr>
[openaire-lod](https://w3id.org/riverbench/datasets/openaire-lod/dev) | <abbr title="10,000 stream elements; 193,178 statements">[10K (3.0 MB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_10K.tar.gz)</abbr> | <abbr title="100,000 stream elements; 2,267,185 statements">[100K (43.2 MB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_100K.tar.gz)</abbr> | <abbr title="1,000,000 stream elements; 42,913,544 statements">[1M (1.1 GB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_1M.tar.gz)</abbr> | <abbr title="2,000,000 stream elements; 71,810,467 statements">[Full (1.6 GB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/stream_full.tar.gz)</abbr>
[osm2rdf-denmark](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev) | <abbr title="10,000 stream elements; 300,656 statements">[10K (2.7 MB)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_10K.tar.gz)</abbr> | <abbr title="100,000 stream elements; 2,954,825 statements">[100K (26.7 MB)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_100K.tar.gz)</abbr> | <abbr title="1,000,000 stream elements; 29,770,290 statements">[1M (268.1 MB)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_1M.tar.gz)</abbr> | <abbr title="2,030,923 stream elements; 60,608,642 statements">[Full (545.5 MB)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_full.tar.gz)</abbr>

### Jelly distributions

Dataset | 10K | 100K | 1M | Full
--- | --- | --- | --- | ---
[digital-agenda-indicators](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev) | <abbr title="10,000 stream elements; 82,424 statements">[10K (188.1 KB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 811,625 statements">[100K (1.7 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 8,108,967 statements">[1M (16.4 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="1,440,415 stream elements; 11,669,016 statements">[Full (23.5 MB)](https://w3id.org/riverbench/datasets/digital-agenda-indicators/dev/files/jelly_full.jelly.gz)</abbr>
[linked-spending](https://w3id.org/riverbench/datasets/linked-spending/dev) | <abbr title="10,000 stream elements; 158,342 statements">[10K (1.4 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 1,716,898 statements">[100K (13.4 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 23,371,403 statements">[1M (161.9 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="2,477,552 stream elements; 55,097,866 statements">[Full (398.5 MB)](https://w3id.org/riverbench/datasets/linked-spending/dev/files/jelly_full.jelly.gz)</abbr>
[muziekweb](https://w3id.org/riverbench/datasets/muziekweb/dev) | <abbr title="10,000 stream elements; 51,721 statements">[10K (765.2 KB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 517,454 statements">[100K (7.8 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 6,916,692 statements">[1M (85.5 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="2,450,357 stream elements; 36,195,263 statements">[Full (297.6 MB)](https://w3id.org/riverbench/datasets/muziekweb/dev/files/jelly_full.jelly.gz)</abbr>
[openaire-lod](https://w3id.org/riverbench/datasets/openaire-lod/dev) | <abbr title="10,000 stream elements; 193,178 statements">[10K (3.1 MB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 2,267,185 statements">[100K (45.0 MB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 42,913,544 statements">[1M (1.2 GB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="2,000,000 stream elements; 71,810,467 statements">[Full (1.7 GB)](https://w3id.org/riverbench/datasets/openaire-lod/dev/files/jelly_full.jelly.gz)</abbr>
[osm2rdf-denmark](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev) | <abbr title="10,000 stream elements; 300,656 statements">[10K (2.7 MB)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_10K.jelly.gz)</abbr> | <abbr title="100,000 stream elements; 2,954,825 statements">[100K (27.8 MB)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_100K.jelly.gz)</abbr> | <abbr title="1,000,000 stream elements; 29,770,290 statements">[1M (280.5 MB)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_1M.jelly.gz)</abbr> | <abbr title="2,030,923 stream elements; 60,608,642 statements">[Full (571.1 MB)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_full.jelly.gz)</abbr>