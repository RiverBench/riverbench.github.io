# citypulse-traffic-graphs (development version)

This is a variation of the [citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic) dataset that was transformed into a stream of graphs, compliant with the [RSP Data Model](https://streamreasoning.org/RSP-QL/Abstract%20Syntax%20and%20Semantics%20Document/). The dataset is a processed subset of real traffic data published by the [CityPulse EU FP7 project](http://iot.ee.surrey.ac.uk:8080/index.html). The used dataset is '[Road Traffic Data](http://iot.ee.surrey.ac.uk:8080/datasets.html#traffic)', dataset-4. The dataset was processed to fix prefixes without a trailing '#' or '/'. It consists of subsequent chronologically ordered substreams of observations from each sensor. See also [the paper](https://www.researchgate.net/publication/300337751_CityBench_A_Configurable_Benchmark_to_Evaluate_RSP_Engines_Using_Smart_City_Datasets) for more details.

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev.jelly)**
    <br>Source repository: **[citypulse-traffic-graphs](https://github.com/RiverBench/dataset-citypulse-traffic-graphs)**

??? example "Stream preview (click to expand)"

    === "Element 0"

        ```turtle title="0000000000.trig"
        --8<-- "docs/datasets/citypulse-traffic-graphs/data/sample_0000000000.trig"
        ```


    === "Element 10"

        ```turtle title="0000000010.trig"
        --8<-- "docs/datasets/citypulse-traffic-graphs/data/sample_0000000010.trig"
        ```


    === "Element 100"

        ```turtle title="0000000100.trig"
        --8<-- "docs/datasets/citypulse-traffic-graphs/data/sample_0000000100.trig"
        ```


    === "Element 1000"

        ```turtle title="0000001000.trig"
        --8<-- "docs/datasets/citypulse-traffic-graphs/data/sample_0000001000.trig"
        ```


    === "Element 10000"

        ```turtle title="0000010000.trig"
        --8<-- "docs/datasets/citypulse-traffic-graphs/data/sample_0000010000.trig"
        ```


## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: CityPulse traffic (graphs variation) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `citypulse-traffic-graphs`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - Data collection ([eurovoc:6030](http://eurovoc.europa.eu/6030))
    - Internet of Things ([eurovoc:c_b12a760a](http://eurovoc.europa.eu/c_b12a760a))
    - Road traffic ([eurovoc:3127](http://eurovoc.europa.eu/3127))
    - Smart city ([eurovoc:c_d59e7560](http://eurovoc.europa.eu/c_d59e7560))
    - Traffic control ([eurovoc:3107](http://eurovoc.europa.eu/3107))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **CityPulse EU FP7 project (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: CityPulse EU FP7 project
        - **<abbr title="This axiom needed so that Protege loads DCAT2 without errors.">Homepage</abbr>**: [http://iot.ee.surrey.ac.uk:8080/index.html](http://iot.ee.surrey.ac.uk:8080/index.html)
    - **Piotr Sowiński (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="This axiom needed so that Protege loads DCAT2 without errors.">Homepage</abbr>**:     
            -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
            - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Processing the dataset
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0)
- **<abbr title="A related resource from which the described resource is derived.">Source</abbr>**: 
    - [http://dx.doi.org/10.1007/978-3-319-25010-6_25](http://dx.doi.org/10.1007/978-3-319-25010-6_25)
    - [http://iot.ee.surrey.ac.uk:8080/datasets.html#traffic](http://iot.ee.surrey.ac.uk:8080/datasets.html#traffic)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-05-01
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2024-05-30
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

## Technical metadata

- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4,382,599
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**:     
        - <abbr title="The elements correspond to different instants or intervals of time.">Stream elements split by time</abbr> ([rb:TimeStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit))
        - <abbr title="The elements correspond to different topics/subjects in the dataset.">Stream elements split by topic</abbr> ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="The IRI of the property that is used in the stream to denote time at which the event occured.">Has temporal property</abbr>**: [http://purl.org/NET/c4dm/timeline.owl#at](http://purl.org/NET/c4dm/timeline.owl#at)
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each element corresponds to one measurement made by a traffic sensor. _(<abbr title="English">en</abbr>)_
- **<abbr title="A vocabulary that is used in the dataset.">Uses vocabulary</abbr>**: 
    - [http://iot.ee.surrey.ac.uk/citypulse/resources/ontologies/sao.ttl](http://iot.ee.surrey.ac.uk/citypulse/resources/ontologies/sao.ttl)
    - [http://purl.oclc.org/NET/ssnx/ssn](http://purl.oclc.org/NET/ssnx/ssn)
    - [http://purl.org/NET/c4dm/timeline.owl](http://purl.org/NET/c4dm/timeline.owl)
    - [http://purl.org/NET/provenance.owl](http://purl.org/NET/provenance.owl)
    - [http://www.insight-centre.org/citytraffic](http://www.insight-centre.org/citytraffic)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no
- **<abbr title="minimum time period resolvable in a dataset.">Temporal resolution</abbr>**: PT5M

## Distributions

### <a name="stream-full"></a> Full stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_full.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4,382,599
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 898.99 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `8b56c6238c3f8873d018c0f69bfb7079`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5b6feb0d4be82ab90503833f432e2c11abb25bbd`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="jelly-full"></a> Full Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_full.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4,382,599
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.42 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3b93b037e33fb5d6f7dee68d7f7bf12e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7b5c92093c0d6cd92fb2cb780904c48011f81bf2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_full.jelly.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_full.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_full.nq.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4,382,599
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.69 GB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `4ca7f72b002311b5a5ba0c2b34274690`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `dd7279bd35b15cdc5e39d61555f45115290279f5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_full.nq.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_full.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="stream-1m"></a> 1M elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 204.36 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `d5fc9e3bc71e7e333145e0d3211e6762`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `9fd5940665d3134239ec4bde086c686f1e291d14`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)

### <a name="jelly-1m"></a> 1M elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_1M.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 330.27 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `101fa70451ce6882da7829e74d81643b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `de442e218ee7c2ee51e9830a5bb14ee2c83a756a`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_1M.jelly.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_1M.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-1m`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nq.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 395.85 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3b321f7cac699fdad0ccd7e26cd1f747`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `8a4ee663d0ccb7195ae6145467d67b3b3b0fc62f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_1M.nq.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_1M.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-1m](#statistics-1m)

### <a name="stream-100k"></a> 100K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 20.61 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `d6de36bc78e5dc22bc04fc8a0622add5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `51043b72c45e3649d63f37e3fbe33b5d9088d045`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="jelly-100k"></a> 100K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_100K.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 32.91 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `080bed29116649075b7e01db2dff51a6`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `25b3d58975ed8c427bb448b1a1f9d87339ec0c13`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_100K.jelly.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_100K.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nq.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 39.64 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `409e6569e01e79d74537d8e51e3d7c05`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5267c54e0c3033271aec4d5c942b2ce324504277`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_100K.nq.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_100K.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="stream-10k"></a> 10K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2.04 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a98d1ad892c28ae7176ddac783ebcea9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6773b01f0c356a34f0851bbdcc8de43fba858a19`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

### <a name="jelly-10k"></a> 10K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_10K.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to one measurement made by a traffic sensor. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.27 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `05fb76a787d6bcb2a4ca98a313969a10`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c7daa195c3be04851ca72182430d48f3c09a07c9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_10K.jelly.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/jelly_10K.jelly.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `flat-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nq.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.96 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c90666f925ad77b741b058595ff1372d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `15a47dae1d5e44ef39a6568cf7a9200e005e537b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_10K.nq.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_10K.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

## <abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>

### <a name="statistics-full"></a> Statistics for full distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for full distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 100,799,777 | 26,296,686 | 23.00 | 0.00 | 23 | 23 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 21,912,995 | _N/A_ | 5.00 | 0.00 | 5 | 5 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 8,765,198 | _N/A_ | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 162,156,163 | _N/A_ | 37.00 | 0.00 | 37 | 37 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 21,407,125 | 13,222 | 4.88 | 0.46 | 3 | 5 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 17,024,526 | 2,530 | 3.88 | 0.46 | 2 | 4 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 4,382,599 | 10,692 | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 52,591,188 | _N/A_ | 12.00 | 0.00 | 12 | 12 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 39,443,391 | _N/A_ | 9.00 | 0.00 | 9 | 9 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 95,911,308 | _N/A_ | 21.88 | 0.46 | 20 | 22 |

### <a name="statistics-1m"></a> Statistics for 1M distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 1M distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 23,000,000 | 6,000,120 | 23.00 | 0.00 | 23 | 23 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 5,000,000 | _N/A_ | 5.00 | 0.00 | 5 | 5 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 2,000,000 | _N/A_ | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 37,000,000 | _N/A_ | 37.00 | 0.00 | 37 | 37 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 4,794,267 | 11,711 | 4.79 | 0.60 | 3 | 5 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 3,794,267 | 1,047 | 3.79 | 0.60 | 2 | 4 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 1,000,000 | 10,664 | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 12,000,000 | _N/A_ | 12.00 | 0.00 | 12 | 12 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 9,000,000 | _N/A_ | 9.00 | 0.00 | 9 | 9 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 21,794,267 | _N/A_ | 21.79 | 0.60 | 20 | 22 |

### <a name="statistics-100k"></a> Statistics for 100K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 100K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 2,300,000 | 600,028 | 23.00 | 0.00 | 23 | 23 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 500,000 | _N/A_ | 5.00 | 0.00 | 5 | 5 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 200,000 | _N/A_ | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 3,700,000 | _N/A_ | 37.00 | 0.00 | 37 | 37 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 499,366 | 11,112 | 4.99 | 0.08 | 3 | 5 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 399,366 | 450 | 3.99 | 0.08 | 2 | 4 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 100,000 | 10,662 | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 1,200,000 | _N/A_ | 12.00 | 0.00 | 12 | 12 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 900,000 | _N/A_ | 9.00 | 0.00 | 9 | 9 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 2,199,366 | _N/A_ | 21.99 | 0.08 | 20 | 22 |

### <a name="statistics-10k"></a> Statistics for 10K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 10K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 230,000 | 60,021 | 23.00 | 0.00 | 23 | 23 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 50,000 | _N/A_ | 5.00 | 0.00 | 5 | 5 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 20,000 | _N/A_ | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 370,000 | _N/A_ | 37.00 | 0.00 | 37 | 37 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 49,981 | 9,536 | 5.00 | 0.05 | 3 | 5 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 39,981 | 229 | 4.00 | 0.05 | 2 | 4 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 10,000 | 9,307 | 1.00 | 0.00 | 1 | 1 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 120,000 | _N/A_ | 12.00 | 0.00 | 12 | 12 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 90,000 | _N/A_ | 9.00 | 0.00 | 9 | 9 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 219,981 | _N/A_ | 22.00 | 0.05 | 20 | 22 |

