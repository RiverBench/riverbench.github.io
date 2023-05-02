# citypulse-traffic-graphs (development version)

This is a variation of the [citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic) dataset that was transformed into a stream of graphs, compliant with the [RSP Data Model](https://streamreasoning.org/RSP-QL/Abstract%20Syntax%20and%20Semantics%20Document/). The dataset is a processed subset of real traffic data published by the [CityPulse EU FP7 project](http://iot.ee.surrey.ac.uk:8080/index.html). The used dataset is '[Road Traffic Data](http://iot.ee.surrey.ac.uk:8080/datasets.html#traffic)', dataset-4. The dataset was processed to fix prefixes without a trailing '#' or '/'. It consists of subsequent chronologically ordered substreams of observations from each sensor. See also [the paper](https://www.researchgate.net/publication/300337751_CityBench_A_Configurable_Benchmark_to_Evaluate_RSP_Engines_Using_Smart_City_Datasets) for more details.

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: CityPulse traffic (graphs variation)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: citypulse-traffic-graphs
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - <abbr title="Datasets with data from sensors, sensor networks, IoT devices, etc.">Sensor data</abbr> ([rbt:sensorData](https://w3id.org/riverbench/schema/theme#sensorData))
    - <abbr title="Datasets with temporal information.">Temporal</abbr> ([rbt:temporal](https://w3id.org/riverbench/schema/theme#temporal))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **CityPulse EU FP7 project (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: CityPulse EU FP7 project
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [http://iot.ee.surrey.ac.uk:8080/index.html](http://iot.ee.surrey.ac.uk:8080/index.html)
    - **Piotr Sowiński (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
            - [https://github.com/Ostrzyciel](https://github.com/Ostrzyciel)
            - [https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461)
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Processing the dataset
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-05-01
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-05-02
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [citypulse-traffic-graphs (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev)

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Graph streams are a special case of quad streams, where each element contains exactly one named RDF graph.">Graphs</abbr> ([rb:graphs](https://w3id.org/riverbench/schema/metadata#graphs))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4,382,599
- **Has stream element split**: 
    - **Type**:     
        - Stream elements split by time ([rb:TimeStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit))
        - Stream elements split by topic ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="The IRI of the property that is used in the stream to denote time at which the event occured.">Has temporal property</abbr>**: [http://purl.org/NET/c4dm/timeline.owl#at](http://purl.org/NET/c4dm/timeline.owl#at)
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each element corresponds to one measurement made by a traffic sensor.
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: 
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

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-100k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 39.69 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a71a02d3080dccc3b74e651ad0d2d076`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `2b5e737c5a34c78b0b80a56e049cfe9c39f0c37e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_100K.nq.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_100K.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 500,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11,112
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 499,366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.99

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 600,028
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,300,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 23
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.00

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11,112
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 499,366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.99

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,199,366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.99

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 900,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.00

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,700,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 37
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 37.00

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,200,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.00

### <a name="stream-100k"></a> 100K elements graph stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements graph stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 20.35 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `19ad0b25cd19d98fc55dc612719e60c9fe8094e9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `67298b348a63c404cf78aa2b15fc92ad`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_100K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 500,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11,112
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 499,366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.99

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 600,028
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,300,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 23
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.00

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11,112
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 499,366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.99

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,199,366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.99

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 900,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.00

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,700,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 37
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 37.00

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,200,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.00

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nq.gz`
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
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1f3133a352c459d71baaa35ffc53bd5d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a681149930d6469442b50cf1d4f284c71e532dc7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_10K.nq.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_10K.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 50,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9,536
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49,981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 60,021
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 230,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 23
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.00

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9,536
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49,981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 219,981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.00

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 90,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.00

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 370,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 37
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 37.00

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 120,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.00

### <a name="stream-10k"></a> 10K elements graph stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements graph stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2.06 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5ab962bd6fff8238285b566bb08b3f8133fc83b7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3091279a185b7105f071a631a7239bc3`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 50,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9,536
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49,981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 60,021
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 230,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 23
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.00

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9,536
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49,981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 219,981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.00

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 90,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.00

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 370,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 37
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 37.00

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 120,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.00

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 395.98 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b99e931ef47387afe638736bbf63b2b9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `93356858586fa23593300b5438ac9f583176cca5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_1M.nq.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_1M.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11,711
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,794,267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.79

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 6,000,120
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 23,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 23
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.00

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11,711
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,794,267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.79

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,794,267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.79

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.00

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 37,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 37
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 37.00

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 12,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.00

### <a name="stream-1m"></a> 1M elements graph stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements graph stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 205.29 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ad1582bc4521bf7cd77e69123f0c39b2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c4783089e53a5b492bddafb8f7fdcc7c47d553d1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_1M.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11,711
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,794,267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.79

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 6,000,120
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 23,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 23
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.00

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11,711
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,794,267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.79

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,794,267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.79

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.00

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 37,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 37
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 37.00

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 12,000,000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.00

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nq.gz
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
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `988de978ab630845c9b7b3fa9a22a77b631c6c2b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6d66a3d4cdfa94af4939446c846f502b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_full.nq.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/flat_full.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,912,995
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 13,222
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.46
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,407,125
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.88

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,382,599
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 26,296,686
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,799,777
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 23
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.00

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 13,222
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.46
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,407,125
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.88

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.46
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 95,911,308
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.88

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 39,443,391
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.00

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 162,156,163
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 37
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 37.00

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 52,591,188
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.00

### <a name="stream-full"></a> Full graph stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full graph stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4,382,599
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 902.25 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5a467715580ca40361f37c53db99df162e3d4878`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `72a5914ef226ca84af601d14280aaf6a`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic-graphs/dev/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,912,995
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.00

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 13,222
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.46
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,407,125
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.88

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4,382,599
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 26,296,686
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,799,777
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 23
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 23.00

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 13,222
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.46
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,407,125
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.88

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.46
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 95,911,308
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.88

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 39,443,391
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.00

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 162,156,163
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 37
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 37.00

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 52,591,188
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 12
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.00

