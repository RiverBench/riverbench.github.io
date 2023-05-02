# lod-katrina (development version)

The Katrina dataset from the Linked Observation Data collection by the Kno.e.sis  Center describes weather measurements from many weather stations across the US during the Katrina hurricane. See more details on [LOD Cloud](http://cas.lod-cloud.net/dataset/knoesis-linked-sensor-data) and the [original website (Internet Archive)](https://web.archive.org/web/20200111135659/http://wiki.knoesis.org:80/index.php/LinkedSensorData). See also [the paper](https://ieeexplore.ieee.org/abstract/document/5478492/).

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Linked Observation Data Katrina
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: lod-katrina
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - <abbr title="Datasets with meteorological information.">Meteorological</abbr> ([rbt:meteorological](https://w3id.org/riverbench/schema/theme#meteorological))
    - <abbr title="Datasets with data from sensors, sensor networks, IoT devices, etc.">Sensor data</abbr> ([rbt:sensorData](https://w3id.org/riverbench/schema/theme#sensorData))
    - <abbr title="Datasets with temporal information.">Temporal</abbr> ([rbt:temporal](https://w3id.org/riverbench/schema/theme#temporal))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **MesoWest, a project within the Department of Meterology at the University of Utah (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: MesoWest, a project within the Department of Meterology at the University of Utah
    - **Harshal Patni (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Harshal Patni
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://scholar.google.com/citations?user=SepRItoAAAAJ](https://scholar.google.com/citations?user=SepRItoAAAAJ)
    - **Piotr Sowiński (3)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
            - [https://github.com/Ostrzyciel](https://github.com/Ostrzyciel)
            - [https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461)
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-3.0](https://spdx.org/licenses/CC-BY-3.0)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-05-01
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-05-02
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [lod-katrina (dev)](https://w3id.org/riverbench/datasets/lod-katrina/dev)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: <abbr title="Ontology for describing datasets and profiles in the RiverBench benchmark suite.">RiverBench metadata ontology</abbr> ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://w3id.org/riverbench/schema/metadata#triples))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,893,763
- **Has stream element split**: 
    - **Type**:     
        - Stream elements split by time ([rb:TimeStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit))
        - Stream elements split by topic ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element corresponds to information from one weather station at a given time OR to a weather station-independent piece of information (e.g., time annotation).
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: [http://knoesis.wright.edu/ssw/ont/sensor-observation.owl](http://knoesis.wright.edu/ssw/ont/sensor-observation.owl)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no

## Distributions

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-100k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 15.45 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1ae1da09be65e94f922c3ca77e6e8b5b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `03505d9794ee92dd67eb51637119040910c1bc4c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_100K.nt.gz](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_100K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,877,016
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 18.77
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 16.84
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 58

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 514,855
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.15
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,862,713
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 28.63
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 27.16
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 98

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 717,827
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.18
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.22
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 303,830
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 4,038
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.04
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.22
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,140,372
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 614,462
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.40
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 17.13
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 57

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 303,830
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 4,038
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.04
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.22
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.11 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7c2638487030e993be4172bc8db5da4b927a4db3`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `fca2dfd2bd3b19e89c28c7102f19bc6e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_10K.nt.gz](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_10K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 140,706
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 14.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 12.15
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 52,052
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.21
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.99
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 8

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 198,649
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 19.86
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.39
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 54

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 52,444
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.24
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.26
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 23,317
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 1,979
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.49
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 174,765
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 42,399
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 17.48
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 13.09
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 39

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 23,317
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 1,979
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.49
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="flat-1m"></a> 1M elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_1M.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 163.50 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c9240342b61d43bdbd0ba6b4a1aa0a57830a592d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `d2dd400033cd74800204400d976a13cb`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_1M.nt.gz](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_1M.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20,113,895
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 20.11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.23
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 61

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5,140,098
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.14
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.01
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 30,855,326
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 30.86
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 29.46
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 98

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7,670,021
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.67
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.73
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,366,044
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 9,402
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.55
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 22,409,270
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 6,636,075
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.41
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.19
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 60

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,366,044
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 9,402
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.55
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nt.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,893,763
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 952.14 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `83377938e7a1a4c701c15406fb948c3f`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `d30ea3b9ec86de645fea2763d6957f2dd82ba916`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_full.nt.gz](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/flat_full.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 116,973,143
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 19.85
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.28
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 61

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 30,335,043
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.15
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.02
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 179,128,407
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 30.39
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 29.63
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 98

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 44,616,700
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.57
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.77
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 19,791,285
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 23,948
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.59
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 130,591,793
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 38,478,589
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.16
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.15
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 60

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 19,791,285
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 23,948
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.59
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="stream-100k"></a> 100K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 12.99 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3b37314c690602c6f08377e45c321d400c9460ca`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5c8fc1ea7a5ca6e7d2882f43f27c356e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_100K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,877,016
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 18.77
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 16.84
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 58

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 514,855
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.15
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,862,713
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 28.63
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 27.16
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 98

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 717,827
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.18
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.22
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 303,830
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 4,038
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.04
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.22
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,140,372
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 614,462
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 21.40
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 17.13
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 57

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 303,830
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 4,038
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.04
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.22
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="stream-10k"></a> 10K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.04 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `25a6f94f7618c46bf588c2b6fb331cd0b35b3944`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ae9ab87391c26e364077148d33696210`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 140,706
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 14.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 12.15
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 37

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 52,052
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.21
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.99
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 8

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 198,649
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 19.86
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.39
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 54

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 52,444
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.24
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 4.26
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 23,317
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 1,979
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.49
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 174,765
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 42,399
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 17.48
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 13.09
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 39

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 23,317
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 1,979
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.49
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="stream-1m"></a> 1M elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 1M elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-1m
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_1M.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 1,000,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 135.48 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `74e2f69d970c9e7d0bdf2227d34e535cf015c4d2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `38e30c53cf53c848b13a82ab28993ba7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_1M.tar.gz](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_1M.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20,113,895
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 20.11
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.23
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 61

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5,140,098
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.14
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.01
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 30,855,326
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 30.86
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 29.46
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 98

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7,670,021
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.67
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.73
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,366,044
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 9,402
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.55
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 22,409,270
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 6,636,075
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.41
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.19
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 60

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,366,044
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 9,402
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.37
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.55
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

### <a name="stream-full"></a> Full triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 5,893,763
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 791.12 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b9da362ae5c9e213bad1d6cdf78c5d71e928f3e7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b23ba26bf11e39013a1acf17b875c770`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/lod-katrina/dev/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 116,973,143
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 19.85
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.28
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 61

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 30,335,043
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.15
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.02
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 179,128,407
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 30.39
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 29.63
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 98

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 44,616,700
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 7.57
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.77
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 23

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 19,791,285
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 23,948
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.59
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 130,591,793
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 38,478,589
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 22.16
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 18.15
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 4
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 60

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 19,791,285
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 23,948
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.36
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.59
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:PlainLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#PlainLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

