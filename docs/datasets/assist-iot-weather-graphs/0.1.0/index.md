# assist-iot-weather-graphs (0.1.0)

This is a timestamped stream of weather data collected with a Davis Vantage Pro 2 weather station installed on the building of the [Systems Research Institute, Polish Academy of Sciences](https://www.ibspan.waw.pl/en/home/). The data was collected during the [ASSIST-IoT Horizon 2020 project](https://assist-iot.eu/). The station measured several different weather parameters and transmitted them in real time at regular intervals. The measurements have rich annotations with the [SOSA/SSN](https://www.w3.org/TR/vocab-ssn/) and [OM 2.0](http://www.ontology-of-units-of-measure.org/page/om-2) ontologies. The stream is very regular and the elements only differ by numeric values and timestamps. This is the graph variant, which is a timestamped graph stream compatible with the RSP Data Model.
    
The dataset is a real application of RDF streaming (originally streamed over MQTT), with much richer annotations than [citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic). On the other hand, it is perfectly regular, with no differences in structure between stream elements.

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0.rdf)**
    <br>Source repository: **[assist-iot-weather-graphs](https://github.com/RiverBench/dataset-assist-iot-weather-graphs)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: ASSIST-IoT weather (graphs variant)
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: assist-iot-weather-graphs
- **<abbr title="Version tag of an artifact">Has version</abbr>**: 0.1.0
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - <abbr title="Datasets with meteorological information.">Meteorological</abbr> ([rbt:meteorological](https://w3id.org/riverbench/schema/theme#meteorological))
    - <abbr title="Datasets with data from sensors, sensor networks, IoT devices, etc.">Sensor data</abbr> ([rbt:sensorData](https://w3id.org/riverbench/schema/theme#sensorData))
    - <abbr title="Datasets with spatial information.">Spatial</abbr> ([rbt:spatial](https://w3id.org/riverbench/schema/theme#spatial))
    - <abbr title="Datasets with temporal information.">Temporal</abbr> ([rbt:temporal](https://w3id.org/riverbench/schema/theme#temporal))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **Piotr Sowiński (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
            -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
            - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
    - **ASSIST-IoT Horizon 2020 project (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: ASSIST-IoT Horizon 2020 project
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://assist-iot.eu/](https://assist-iot.eu/)
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 957258.
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-05-04
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-05-08
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [assist-iot-weather-graphs (0.1.0)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Graph streams are a special case of quad streams, where each element contains exactly one named RDF graph.">Graphs</abbr> ([rb:graphs](https://w3id.org/riverbench/schema/metadata#graphs))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 701,278
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**: <abbr title="The elements correspond to different instants or intervals of time.">Stream elements split by time</abbr> ([rb:TimeStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit))
    - **<abbr title="The IRI of the property that is used in the stream to denote time at which the event occured.">Has temporal property</abbr>**: [http://www.w3.org/ns/prov#atTime](http://www.w3.org/ns/prov#atTime)
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element corresponds to one set of measurements from the weather station. Data was collected every 10 seconds.
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: 
    - [http://www.ontology-of-units-of-measure.org/resource/om-2](http://www.ontology-of-units-of-measure.org/resource/om-2)
    - [http://www.opengis.net/ont/geosparql](http://www.opengis.net/ont/geosparql)
    - [http://www.w3.org/ns/prov](http://www.w3.org/ns/prov)
    - [http://www.w3.org/ns/sosa](http://www.w3.org/ns/sosa)
    - [http://www.w3.org/ns/ssn](http://www.w3.org/ns/ssn)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no
- **<abbr title="minimum time period resolvable in a dataset.">Temporal resolution</abbr>**: PT10S
- **<abbr title="A language of the resource.">Language</abbr>**: en

## Distributions

### <a name="stream-full"></a> Full graph stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full graph stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 701,278
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 91.26 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1df644b933bbe65533ab94f628a3e47c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `04b29f74ff18d7d0d108b93021fca0f296b79b89`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 46,985,626
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 701,333
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 67.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 67
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 67

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 8,516,050
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 704,202
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.14
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.69
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,402,556
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7,113,494
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 704,200
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.14
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.69
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,739,618
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 31
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 31

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9,116,614
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 13.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 13
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 39,372,282
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 56.14
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.69
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 54
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 57

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 701,278
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 81,348,248
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 116.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 116
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 116

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nq.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 701,278
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 354.64 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f0c993ec219424d22aea86aa3ce3fe27`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `11ef5b24a3e8438fed943efe9f80c5c894028814`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/flat_full.nq.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/flat_full.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 46,985,626
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 701,333
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 67.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 67
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 67

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 8,516,050
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 704,202
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.14
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.69
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,402,556
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 7,113,494
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 704,200
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.14
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.69
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 21,739,618
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 31
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 31

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 9,116,614
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 13.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 13
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 39,372,282
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 56.14
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.69
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 54
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 57

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 701,278
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 81,348,248
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 116.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 116
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 116

### <a name="stream-100k"></a> 100K elements graph stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements graph stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 13.01 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f559fc8d6738c6eb6556884ec9013a87`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a89f02dc50cc2dcbbd58d43295084212b1bd0aa9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/stream_100K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 6,700,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 100,071
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 67.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 67
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 67

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,205,786
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 102,024
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.06
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.61
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 200,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,005,786
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 102,022
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.06
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.61
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,100,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 31
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 31

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,300,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 13.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 13
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5,605,786
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 56.06
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.61
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 54
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 57

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 11,600,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 116.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 116
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 116

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-100k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 50.58 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `25612988eac27aad41137bfa86209541`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `8ffa78bd2fb53b004f026b8674b89cfa8d5a2b7c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/flat_100K.nq.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/flat_100K.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 6,700,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 100,071
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 67.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 67
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 67

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,205,786
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 102,024
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.06
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.61
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 200,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,005,786
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 102,022
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.06
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.61
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,100,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 31
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 31

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,300,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 13.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 13
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 5,605,786
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 56.06
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.61
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 54
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 57

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 11,600,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 116.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 116
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 116

### <a name="stream-10k"></a> 10K elements graph stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements graph stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a stream of named RDF graphs.">Graph stream distribution</abbr> ([rb:graphStreamDistribution](https://w3id.org/riverbench/schema/metadata#graphStreamDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.31 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `94cb40e5f4d8c9603284bce05a0a2328`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `e2017740ee136055330b99d61e8cc2ba9299539b`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 670,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 10,066
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 67.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 67
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 67

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 120,737
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 10,801
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,737
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 10,799
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 310,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 31
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 31

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 130,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 13.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 13
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 560,737
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 56.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 54
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 57

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,160,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 116.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 116
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 116

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nq.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 5.07 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `8e37705b9497f80db6a7c0b171ce751d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3792d1f4eff0ede23ef81144dfade598f644e97a`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/flat_10K.nq.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/0.1.0/files/flat_10K.nq.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 670,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 10,066
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 67.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 67
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 67

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 120,737
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 10,801
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 12.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 10
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20,000
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 100,737
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 10,799
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 10.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 11

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Quoted triple count statistics

- **Type**: <abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triple count statistics</abbr> ([rb:QuotedTripleCountStatistics](https://w3id.org/riverbench/schema/metadata#QuotedTripleCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 310,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 31.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 31
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 31

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 130,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 13.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 13
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 560,737
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 56.07
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.60
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 54
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 57

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,160,000
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 116.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 116
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 116

