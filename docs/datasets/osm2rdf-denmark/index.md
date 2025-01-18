<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev "Link to the permanent URL of this resource.")</div><div markdown>**[:material-database-edit: Edit this page](https://github.com/RiverBench/dataset-osm2rdf-denmark/edit/main/metadata.ttl "Edit this page's source in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../../documentation/editing-docs.md "Need help with editing?")</div></div>

# Dataset: osm2rdf-denmark (development version)

The dataset is based on datasets that were derived from OpenStreetMap data using the osm2rdf tool. It includes information about each element which is of type node (osm:node), way (osm:way) or relation (osm:relation). Nodes are a core concept in OSM and they represent a single point in space defined by geographic coordinates. A node itself can describe for example a city, town, road junction, post box etc.. A way is line, represents linear features on the ground - like a road. It consist of an ordered node list. A relation is a colection of the three core elements: nodes, ways and relations. Each element contains all atributes associated with it.

!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev.jelly)**
    <br>:material-github: Source repository: **[dataset-osm2rdf-denmark](https://github.com/RiverBench/dataset-osm2rdf-denmark)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev`](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev)

    **[:octicons-arrow-down-24: Go to download links](#distributions)**

??? example "Stream preview (click to expand)"

    === "Element 0"

        ```turtle title="0000000000.ttl"
        --8<-- "docs/datasets/osm2rdf-denmark/data/sample_0000000000.ttl"
        ```


    === "Element 10"

        ```turtle title="0000000010.ttl"
        --8<-- "docs/datasets/osm2rdf-denmark/data/sample_0000000010.ttl"
        ```


    === "Element 100"

        ```turtle title="0000000100.ttl"
        --8<-- "docs/datasets/osm2rdf-denmark/data/sample_0000000100.ttl"
        ```


    === "Element 1000"

        ```turtle title="0000001000.ttl"
        --8<-- "docs/datasets/osm2rdf-denmark/data/sample_0000001000.ttl"
        ```


    === "Element 10000"

        ```turtle title="0000010000.ttl"
        --8<-- "docs/datasets/osm2rdf-denmark/data/sample_0000010000.ttl"
        ```


## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: osm2rdf-denmark _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `osm2rdf-denmark`
- **<abbr title="The version indicator (name or identifier) of a resource.">Version</abbr>**: `dev`
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - Data collection ([eurovoc:6030](http://eurovoc.europa.eu/6030))
    - Geography ([eurovoc:1148](http://eurovoc.europa.eu/1148))
    - Spatial data ([eurovoc:c_7a168de0](http://eurovoc.europa.eu/c_7a168de0))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **<abbr title="A name for some thing.">Name</abbr>**: Karol Nowiński
    - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: `karol-nowinski`
    - **<abbr title="This axiom needed so that Protege loads DCAT 3 without errors.">Homepage</abbr>**: [https://github.com/karol-nowinski](https://github.com/karol-nowinski)
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/ODbL-1.0](https://spdx.org/licenses/ODbL-1.0)
- **<abbr title="A related resource from which the described resource is derived.">Source</abbr>**: [https://osm2rdf.cs.uni-freiburg.de/](https://osm2rdf.cs.uni-freiburg.de/)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2025-01-18
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2025-01-18
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [osm2rdf-denmark (dev)](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev)

## Technical metadata

- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 2,030,923
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**: <abbr title="The elements correspond to different topics/subjects in the dataset.">Stream elements split by topic</abbr> ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element corresponds to one basic component of OpenStreetMap: node, way or relation. _(<abbr title="English">en</abbr>)_
    - **<abbr title="Indicates the subject node in an RDF subject graph stream, using SHACL. The value of this property should be a SHACL sh:NodeShape with a specified target (e.g., sh:targetSubjectsOf). Only the target will be considered, restrictions on the shape will be ignored.  This property is required for RDF subject graph streams. Only sh:targetClass, sh:targetSubjectsOf, and sh:targetObjectsOf are allowed as the target specification.  This property can be specified multiple times. The different target specifications will then be treated as alternatives.">Has subject shape</abbr>**:     
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Target instances of any class. _(<abbr title="English">en</abbr>)_
        - **<abbr title="Links a shape to a property, indicating that all subjects of triples that have the given property as their predicate must conform to the shape.">Target subjects of</abbr>**: Type ([rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type))
- **<abbr title="A vocabulary that is used in the dataset.">Uses vocabulary</abbr>**: 
    - [http://www.opengis.net/ont/geosparql#](http://www.opengis.net/ont/geosparql#)
    - [http://www.opengis.net/rdf#](http://www.opengis.net/rdf#)
    - [http://www.w3.org/2001/XMLSchema#](http://www.w3.org/2001/XMLSchema#)
    - [https://osm2rdf.cs.uni-freiburg.de/rdf#](https://osm2rdf.cs.uni-freiburg.de/rdf#)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no

## Distributions


### Download links

The dataset is published in a few size variants, each containing a specific number of stream elements.
For each size, there are three distribution types available: flat (just an N-Triples/N-Quads file),
streaming (a .tar.gz archive with Turtle/TriG files, one file per stream element),
and [Jelly](https://w3id.org/jelly) (a native binary format for streaming RDF).
See the [documentation](../../documentation/dataset-release-format.md) for more details.

Distribution size | Statements | Flat | Streaming | Jelly
--- | --: | --: | --: | --:
<abbr title="10,000 stream elements">10K</abbr> | 300,656 | [:octicons-download-24: 3.0 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_10K.nt.gz) | [:octicons-download-24: 2.7 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_10K.tar.gz) | [:octicons-download-24: 2.7 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_10K.jelly.gz)
<abbr title="100,000 stream elements">100K</abbr> | 2,954,825 | [:octicons-download-24: 30.3 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_100K.nt.gz) | [:octicons-download-24: 26.7 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_100K.tar.gz) | [:octicons-download-24: 27.8 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_100K.jelly.gz)
<abbr title="1,000,000 stream elements">1M</abbr> | 29,770,290 | [:octicons-download-24: 304.8 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_1M.nt.gz) | [:octicons-download-24: 268.1 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_1M.tar.gz) | [:octicons-download-24: 280.5 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_1M.jelly.gz)
<abbr title="2,030,923 stream elements">Full</abbr> | 60,608,642 | [:octicons-download-24: 620.1 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_full.nt.gz) | [:octicons-download-24: 545.5 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_full.tar.gz) | [:octicons-download-24: 571.1 MB](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_full.jelly.gz)


The full metadata of all distributions can be found below.

### <a name="jelly-100k"></a> 100K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_100K.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 27.8 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e83ed0bee9642ca07690590fe04b8601`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `d7d6d4524f346b40f1352bcb89eb3d1a72feed8f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_100K.jelly.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_100K.jelly.gz)

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 30.3 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `49312b6ee168dd080ac0ee1f44ad1ec1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `84346f24152f42159ff1e1f5169a8a9d70cde2fa`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_100K.nt.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_100K.nt.gz)

### <a name="jelly-10k"></a> 10K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_10K.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2.7 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `08ed4be600341e860cbbe73ece414e6f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5671ac6248072908537c48d001fb67a0ff1873d0`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_10K.jelly.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_10K.jelly.gz)

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.0 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c784d6a279c98b3f1852be9e6cd24a4f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e7dd7c1a7ce3adbb69d2ccbb3f2b63524a33d070`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_10K.nt.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_10K.nt.gz)

### <a name="jelly-1m"></a> 1M elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_1M.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 280.5 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `cd4f9c504031bad0c940f0cd0ecf96af`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `69fc5996a0d0eb092b3d9ef258a5fbbf3346b86b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_1M.jelly.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_1M.jelly.gz)

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 304.8 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `84f4857ac5eff93fb721fde6db4d45fb`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c592e054d4c19c109ebf40ffff46d712847c160b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_1M.nt.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_1M.nt.gz)

### <a name="jelly-full"></a> Full Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_full.jelly.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 2,030,923
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 571.1 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `685ec262ff2f055aef4b563c3c48abce`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `af72eb22a67d1498195e73e6ac81809c3f58ae86`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_full.jelly.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/jelly_full.jelly.gz)

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_full.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of triples. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF triple stream is a flat RDF stream whose elements are triples.">Flat RDF triple stream</abbr> ([stax:flatTripleStream](https://w3id.org/stax/ontology#flatTripleStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 2,030,923
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 620.1 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3a5956d5fc8096512a9f50e7020e2162`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `261224c4b7fd3b391d4b7678393efdd372f7a1bd`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_full.nt.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/flat_full.nt.gz)

### <a name="stream-100k"></a> 100K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 26.7 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `2033999a539f8fb661af564d694b8ab9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `cc12896c489ad1bbfa63fb37de95f1e9f85bb69e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_100K.tar.gz)

### <a name="stream-10k"></a> 10K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2.7 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ff404728e970757aadb0dce1fec6bf80`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e92e255873bf387bc93230947eef4a54fa23ddd1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_10K.tar.gz)

### <a name="stream-1m"></a> 1M elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 268.1 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a7c1cf8da79b63192d62d691ae835358`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `8f09820dc32914e797eab74cca51fdb8c817b1d2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_1M.tar.gz)

### <a name="stream-full"></a> Full stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_full.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of graphs. Each graph corresponds to one core element of OpenStreetMap: node, way or relation _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="An RDF graph stream is a grouped RDF stream whose elements are unnamed (default) RDF graphs.">RDF graph stream</abbr> ([stax:graphStream](https://w3id.org/stax/ontology#graphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 2,030,923
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 545.5 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7de76815f6d3f08fe719c3fbb845c55d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `80944fdd9370fc652cb304b35eb7e686e6184b58`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dcterms:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/osm2rdf-denmark/dev/files/stream_full.tar.gz)

## <abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>

### <a name="statistics-100k"></a> Statistics for 100K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 100K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 3,007,866 | <abbr title="Estimated value. Lower bound: 585,590, upper bound: 593,257 (95% confidence).">~589,399</abbr> | 30.08 | 33.19 | 6 | 3,014 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 19,045 | _N/A_ | 0.19 | 6.59 | 0 | 1,334 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 1,045,980 | <abbr title="Estimated value. Lower bound: 554,174, upper bound: 561,430 (95% confidence).">~557,778</abbr> | 10.46 | 7.29 | 3 | 1,354 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 348,584 | <abbr title="Estimated value. Lower bound: 54,974, upper bound: 55,694 (95% confidence).">~55,332</abbr> | 3.49 | 2.99 | 0 | 29 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 697,396 | <abbr title="Estimated value. Lower bound: 499,579, upper bound: 506,121 (95% confidence).">~502,829</abbr> | 6.97 | 6.82 | 3 | 1,340 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.">Datatypes</abbr>** | 349,893 | 7 | 3.50 | 0.50 | 2 | 5 |
| **<abbr title="Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page 'Dataset compatibility notes' for more details.">ASCII control chars</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 318,339 | <abbr title="Estimated value. Lower bound: 315,155, upper bound: 319,282 (95% confidence).">~317,205</abbr> | 3.18 | 6.59 | 1 | 1,337 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 1,515,858 | <abbr title="Estimated value. Lower bound: 1,516, upper bound: 1,516 (95% confidence).">~1,516</abbr> | 15.16 | 3.08 | 4 | 79 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 2,457,033 | <abbr title="Estimated value. Lower bound: 1,061,360, upper bound: 1,075,258 (95% confidence).">~1,068,264</abbr> | 24.57 | 42.14 | 4 | 4,459 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 100,000 | <abbr title="Estimated value. Lower bound: 1, upper bound: 1 (95% confidence).">~1</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 2,954,825 | _N/A_ | 29.55 | 96.76 | 4 | 8,899 |
| **<abbr title="Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much 'information' is in an average statement in the dataset when it is uncompressed.">Bytes per statement</abbr>** | _N/A_ | _N/A_ | 160.10 | 12.26 | 125.64 | 1,870.06 |

### <a name="statistics-10k"></a> Statistics for 10K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 10K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 302,440 | <abbr title="Estimated value. Lower bound: 67,630, upper bound: 68,516 (95% confidence).">~68,070</abbr> | 30.24 | 43.88 | 6 | 3,014 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 1,500 | _N/A_ | 0.15 | 4.39 | 0 | 268 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 103,847 | <abbr title="Estimated value. Lower bound: 62,751, upper bound: 63,573 (95% confidence).">~63,159</abbr> | 10.38 | 5.41 | 3 | 292 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 34,517 | <abbr title="Estimated value. Lower bound: 8,536, upper bound: 8,647 (95% confidence).">~8,591</abbr> | 3.45 | 3.03 | 0 | 29 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 69,330 | <abbr title="Estimated value. Lower bound: 54,327, upper bound: 55,038 (95% confidence).">~54,680</abbr> | 6.93 | 4.74 | 3 | 274 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.">Datatypes</abbr>** | 34,974 | 7 | 3.50 | 0.50 | 2 | 5 |
| **<abbr title="Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page 'Dataset compatibility notes' for more details.">ASCII control chars</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 31,444 | <abbr title="Estimated value. Lower bound: 31,319, upper bound: 31,729 (95% confidence).">~31,522</abbr> | 3.14 | 4.39 | 1 | 271 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 151,194 | <abbr title="Estimated value. Lower bound: 724, upper bound: 724 (95% confidence).">~724</abbr> | 15.12 | 3.10 | 4 | 50 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 246,593 | <abbr title="Estimated value. Lower bound: 121,225, upper bound: 122,812 (95% confidence).">~122,013</abbr> | 24.66 | 48.38 | 4 | 3,006 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 10,000 | <abbr title="Estimated value. Lower bound: 1, upper bound: 1 (95% confidence).">~1</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 300,656 | _N/A_ | 30.07 | 127.56 | 4 | 8,899 |
| **<abbr title="Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much 'information' is in an average statement in the dataset when it is uncompressed.">Bytes per statement</abbr>** | _N/A_ | _N/A_ | 160.22 | 10.62 | 127.68 | 320.77 |

### <a name="statistics-1m"></a> Statistics for 1M distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 1M distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 30,152,324 | <abbr title="Estimated value. Lower bound: 4,629,089, upper bound: 4,689,702 (95% confidence).">~4,659,198</abbr> | 30.15 | 37.50 | 6 | 3,558 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 197,001 | _N/A_ | 0.20 | 6.74 | 0 | 1,639 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 10,456,873 | <abbr title="Estimated value. Lower bound: 4,929,707, upper bound: 4,994,256 (95% confidence).">~4,961,771</abbr> | 10.46 | 7.48 | 3 | 1,807 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 3,478,487 | <abbr title="Estimated value. Lower bound: 381,543, upper bound: 386,538 (95% confidence).">~384,024</abbr> | 3.48 | 3.00 | 0 | 233 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 6,978,386 | <abbr title="Estimated value. Lower bound: 4,555,725, upper bound: 4,615,377 (95% confidence).">~4,585,357</abbr> | 6.98 | 6.96 | 3 | 1,645 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.">Datatypes</abbr>** | 3,498,625 | 7 | 3.50 | 0.50 | 2 | 6 |
| **<abbr title="Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page 'Dataset compatibility notes' for more details.">ASCII control chars</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 3,189,527 | <abbr title="Estimated value. Lower bound: 3,171,268, upper bound: 3,212,792 (95% confidence).">~3,191,895</abbr> | 3.19 | 6.74 | 1 | 1,642 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 15,150,181 | <abbr title="Estimated value. Lower bound: 3,349, upper bound: 3,349 (95% confidence).">~3,349</abbr> | 15.15 | 3.11 | 4 | 341 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 24,656,017 | <abbr title="Estimated value. Lower bound: 9,067,518, upper bound: 9,186,247 (95% confidence).">~9,126,496</abbr> | 24.66 | 46.52 | 4 | 6,212 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 1,000,000 | <abbr title="Estimated value. Lower bound: 1, upper bound: 1 (95% confidence).">~1</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 29,770,290 | _N/A_ | 29.77 | 108.21 | 4 | 9,890 |
| **<abbr title="Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much 'information' is in an average statement in the dataset when it is uncompressed.">Bytes per statement</abbr>** | _N/A_ | _N/A_ | 160.09 | 11.90 | 120.00 | 2,245.28 |

### <a name="statistics-full"></a> Statistics for full distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for full distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value may be estimated using a HyperLogLog sketch. In that case, rb:uniqueCountLowerBound and rb:uniqueCountLowerBound properties are also set on the subject.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 61,286,682 | <abbr title="Estimated value. Lower bound: 8,306,687, upper bound: 8,415,454 (95% confidence).">~8,360,717</abbr> | 30.18 | 37.92 | 6 | 3,558 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 402,621 | _N/A_ | 0.20 | 6.73 | 0 | 1,639 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 21,240,094 | <abbr title="Estimated value. Lower bound: 9,695,351, upper bound: 9,822,300 (95% confidence).">~9,758,413</abbr> | 10.46 | 7.45 | 3 | 1,807 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 7,064,444 | <abbr title="Estimated value. Lower bound: 720,297, upper bound: 729,728 (95% confidence).">~724,982</abbr> | 3.48 | 3.00 | 0 | 233 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 14,175,650 | <abbr title="Estimated value. Lower bound: 8,982,598, upper bound: 9,100,215 (95% confidence).">~9,041,024</abbr> | 6.98 | 6.95 | 3 | 1,645 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | <abbr title="Estimated value. Lower bound: 0, upper bound: 0 (95% confidence).">~0</abbr> | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the count of datatypes (NOT datatype literals) in the dataset. This statistic does not include rdf:langString and xsd:string.">Datatypes</abbr>** | 7,105,442 | 7 | 3.50 | 0.50 | 2 | 6 |
| **<abbr title="Statistics about the number of ASCII control characters except HT, LF, and CR (0x00-0x08, 0x0B, 0x0C, 0x0E-0x1F) in literals. These characters are allowed in RDF literals, but some serializations (e.g., RDF/XML) may not be able to encode them. See the documentation page 'Dataset compatibility notes' for more details.">ASCII control chars</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 6,480,228 | <abbr title="Estimated value. Lower bound: 6,462,864, upper bound: 6,547,488 (95% confidence).">~6,504,901</abbr> | 3.19 | 6.73 | 1 | 1,642 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 30,768,122 | <abbr title="Estimated value. Lower bound: 4,186, upper bound: 4,186 (95% confidence).">~4,186</abbr> | 15.15 | 3.10 | 4 | 341 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 50,130,352 | <abbr title="Estimated value. Lower bound: 17,280,769, upper bound: 17,507,040 (95% confidence).">~17,393,168</abbr> | 24.68 | 46.88 | 4 | 6,212 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 2,030,923 | <abbr title="Estimated value. Lower bound: 1, upper bound: 1 (95% confidence).">~1</abbr> | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 60,608,642 | _N/A_ | 29.84 | 109.53 | 4 | 9,890 |
| **<abbr title="Statistics about the number of bytes needed to encode a single statement in the N-Triples/N-Quads formats. One newline character is included for each statement.  This statistic can be used as a proxy to estimate how much 'information' is in an average statement in the dataset when it is uncompressed.">Bytes per statement</abbr>** | _N/A_ | _N/A_ | 160.09 | 11.70 | 120.00 | 2,245.28 |

