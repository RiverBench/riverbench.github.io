# politiquices (development version)

Support and opposition relations extracted from news articles archived in Arquivo.pt. The dataset describes news articles in Portuguese and the presented political stances. [Dataset source](https://data.europa.eu/data/datasets/6130e331078190fd0c6c3819?locale=en), [more information about the project (Portuguese)](https://www.politiquices.pt/about).

## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: Politiquices
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: politiquices
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - <abbr title="Datasets with news information.">News</abbr> ([rbt:news](https://w3id.org/riverbench/schema/theme#news))
    - <abbr title="Datasets with political information.">Political</abbr> ([rbt:political](https://w3id.org/riverbench/schema/theme#political))
    - <abbr title="Datasets with temporal information.">Temporal</abbr> ([rbt:temporal](https://w3id.org/riverbench/schema/theme#temporal))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **David Soares Batista (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: David Soares Batista
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://www.politiquices.pt/about](https://www.politiquices.pt/about)
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: Dataset creator
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
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [politiquices (dev)](https://w3id.org/riverbench/datasets/politiquices/dev)

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://w3id.org/riverbench/schema/metadata#triples))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 17773
- **Has stream element split**: 
    - **Type**: Stream elements split by topic ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element corresponds to one news article.
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: 
    - <abbr title="Ontology for describing datasets and profiles in the RiverBench benchmark suite.">RiverBench metadata ontology</abbr> ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))
    - [http://purl.org/dc/elements/1.1/](http://purl.org/dc/elements/1.1/)
    - [http://www.politiquices.pt/](http://www.politiquices.pt/)
    - [http://www.wikidata.org/entity/](http://www.wikidata.org/entity/)
    - [http://www.wikidata.org/prop/direct/](http://www.wikidata.org/prop/direct/)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: yes
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: no

## Distributions

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2111255
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `168f589f925c1d1cccab067689fb4c95`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `abd6499900be9965c0090fab3f46017e4e5ec37e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_10K.nt.gz](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_10K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 12311
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 50000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 10681
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.014140721338563603
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 119998
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.9998

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9954
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 22263
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 60000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 6.0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.014140721339066081
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 89998
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 8.9998

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
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 90000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0

### <a name="stream-10k"></a> 10K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1908438
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `14af600de27b4ba10549b372ae9c6113`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `a71ae1ad309ee1866ca73d31316731e24643fd6c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 12311
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 50000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 10681
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.014140721338563603
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 119998
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.9998

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 9954
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 10000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 22263
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 60000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 6.0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.014140721339066081
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 89998
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 8.9998

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
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 90000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 20000
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nt.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 17773
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3754132
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `91ae87c5ffd09c0b070a2d975793c4d5107efda5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5bb07c48cf352bc30c1dfbfe6bbb35bd`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_full.nt.gz](https://w3id.org/riverbench/datasets/politiquices/dev/files/flat_full.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 17773
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 18601
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 88865
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 18557
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.010607430387436936
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 213274
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.999887469757498

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 17594
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 17773
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 36172
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 106638
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 6.0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.010607430387436936
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159955
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 8.999887469757498

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159957
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
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159957
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 35546
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0

### <a name="stream-full"></a> Full triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 17773
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3392798
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `2fdae03b6e2c102cadcd67a095aff1c9`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f9d05650d5daadbcfacabc18b0e5d6475b6e37fa`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/politiquices/dev/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 17773
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 18601
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 5
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 88865
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 5
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.0

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.0

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 18557
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 12
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.010607430387436936
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 213274
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 11
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 11.999887469757498

##### Language string count statistics

- **Type**: <abbr title="Statistics about the number of language literals in the dataset.">Language string count statistics</abbr> ([rb:LanguageLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LanguageLiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 17594
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 17773
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset.">Unique count</abbr>**: 36172
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 6
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 106638
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 6
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 6.0

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.010607430387436936
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159955
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 8
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 8.999887469757498

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159957
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
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 9
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 159957
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 9
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 9.0

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 2
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.0
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 35546
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.0

