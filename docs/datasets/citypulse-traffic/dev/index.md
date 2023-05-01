# citypulse-traffic (development version)

This is a processed subset of real traffic data published by the [CityPulse EU FP7 project](http://iot.ee.surrey.ac.uk:8080/index.html). The used dataset is '[Road Traffic Data](http://iot.ee.surrey.ac.uk:8080/datasets.html#traffic)', dataset-4. The dataset was processed to fix prefixes without a trailing '#' or '/'. The dataset consists of subsequent chronologically ordered substreams of observations from each sensor. See also [the paper](https://www.researchgate.net/publication/300337751_CityBench_A_Configurable_Benchmark_to_Evaluate_RSP_Engines_Using_Smart_City_Datasets) for more details.

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: CityPulse traffic
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: citypulse-traffic
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
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-05-01
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [citypulse-traffic (dev)](https://w3id.org/riverbench/datasets/citypulse-traffic/dev)

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://w3id.org/riverbench/schema/metadata#triples))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4382599
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
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 39412029
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f99f2d378489f5216b5fe018f5d7ab38e8cab3d7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5835f21352d6a7c71751ff62c36206ea`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_100K.nt.gz](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_100K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 500000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11112
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08437893338978922
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 499366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.99366

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 500027
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2200000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 22
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11112
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08437893338978922
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 499366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.99366

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08437893339025236
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2199366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.99366

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 900000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3600000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 36
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 36.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1100000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0

### <a name="stream-100k"></a> 100K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 19637834
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6109cc15de2dbdc8e80d03987229bbe0`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `334e6f86d4809f5970c98fce854be8b65a4c42ec`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_100K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 500000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11112
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08437893338978922
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 499366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.99366

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 500027
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2200000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 22
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11112
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08437893338978922
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 499366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.99366

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.08437893339025236
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2199366
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.99366

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 900000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3600000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 36
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 36.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1100000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3942822
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e0a29293a1e58cd173e17b8b162674af`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `776f409994b71f916de8ac7985d6437ea0a4111f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_10K.nt.gz](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_10K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 50000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9536
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05192677536686202
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.9981

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 50022
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 220000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 22
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9536
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05192677536686202
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.9981

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05192677536669097
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 219981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.9981

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 90000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 360000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 36
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 36.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 110000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0

### <a name="stream-10k"></a> 10K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1981259
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `326265ef9e78517ddf9c745df087c0fe`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ddfb63c7a21349f59c8448ebf657d034d4e9bf65`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 50000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9536
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05192677536686202
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.9981

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 50022
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 220000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 22
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9536
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05192677536686202
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.9981

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.05192677536669097
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 219981
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.9981

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 90000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 360000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 36
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 36.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 110000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1000000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 394084242
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `30deb0b248be53524e93f8e647b0c3ff`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `d00fc04dda5b05e7cabb1f97ed0ad169573353f1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_1M.nt.gz](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_1M.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11711
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.6003256888648048
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4794267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.794267

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 5000037
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 22000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 22
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11711
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.6003256888648048
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4794267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.794267

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.6003256888647308
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21794267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.794267

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 36000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 36
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 36.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 11000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0

### <a name="stream-1m"></a> 1M elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1000000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 196451988
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `2d91cd96ca48712ed40ced88dc86fa1b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `0f20d6b5c5ea3662269e8243a41a26d78f7d4d80`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_1M.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11711
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.6003256888648048
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4794267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.794267

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 5000037
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 22000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 22
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 11711
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.6003256888648048
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 4794267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.794267

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.6003256888647308
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21794267
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.794267

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 36000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 36
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 36.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 11000000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nt.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4382599
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1723667182
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1df304bcf5eb737d3eb5067236b3b368a0d68ce1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a4554e0dea334298b87366cf0ff530a7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_full.nt.gz](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/flat_full.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21912995
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 13222
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.4591835555246114
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21407125
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.884573058132856

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 21914265
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 96417178
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 22
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 13222
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.4591835555246114
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21407125
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.884573058132856

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.45918355552454176
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 95911308
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.884573058132858

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 39443391
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 157773564
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 36
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 36.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 48208589
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0

### <a name="stream-full"></a> Full triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 4382599
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 860539269
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `af64c9ada420ed9aa9a6b795af4c5ab4`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b108fd2a0ef9062e7d9961e72053d2603546b7da`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/citypulse-traffic/dev/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21912995
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 13222
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.4591835555246114
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21407125
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.884573058132856

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 21914265
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 96417178
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 22
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.0

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 13222
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.4591835555246114
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21407125
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.884573058132856

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 22
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.45918355552454176
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 95911308
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 20
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.884573058132858

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 39443391
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 157773564
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 36
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 36.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 48208589
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.0

