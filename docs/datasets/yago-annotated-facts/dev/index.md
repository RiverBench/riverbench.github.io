# yago-annotated-facts (development version)

This is a subset of the [YAGO 4 knowledge base](https://yago-knowledge.org/downloads/yago-4) ([paper](https://suchanek.name/work/publications/eswc-2020-yago.pdf)), based on Wikidata, [version from February 24, 2020](https://yago-knowledge.org/data/yago4/full/2020-02-24/). This dataset includes only the fact annotations in RDF-star, that is facts about facts. Each stream element corresponds to one item in Wikidata.

!!! info

    Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev.rdf)**
    <br>Source repository: **[yago-annotated-facts](https://github.com/RiverBench/dataset-yago-annotated-facts)**



## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: YAGO annotated facts
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: yago-annotated-facts
- **<abbr title="Version tag of an artifact">Has version</abbr>**: dev
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: <abbr title="Datasets with encyclopedic information.">Encyclopedic</abbr> ([rbt:encyclopedic](https://w3id.org/riverbench/schema/theme#encyclopedic))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **The creators and contributors of Wikidata (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: The creators and contributors of Wikidata
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://www.wikidata.org/](https://www.wikidata.org/)
    - **The YAGO team of Télécom Paris and the Max Planck Institute for Informatics (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: The YAGO team of Télécom Paris and the Max Planck Institute for Informatics
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**: [https://yago-knowledge.org/contributors](https://yago-knowledge.org/contributors)
    - **Piotr Sowiński (3)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="A homepage for some thing.">Homepage</abbr>**:     
            -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
            - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-SA-3.0](https://spdx.org/licenses/CC-BY-SA-3.0)
- **<abbr title="A related resource from which the described resource is derived.">Source</abbr>**: 
    - [https://doi.org/10.1007%2F978-3-030-49461-2_34](https://doi.org/10.1007%2F978-3-030-49461-2_34)
    - [https://yago-knowledge.org/downloads/yago-4](https://yago-knowledge.org/downloads/yago-4)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-04-30
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2023-05-08
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [yago-annotated-facts (dev)](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

## Technical metadata

- **<abbr title="Indicates the type of contents of each stream element">Has stream element type</abbr>**: <abbr title="Triple streams consist of elements, where each element is an RDF graph.">Triples</abbr> ([rb:triples](https://w3id.org/riverbench/schema/metadata#triples))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 617,768
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**: <abbr title="The elements correspond to different topics/subjects in the dataset.">Stream elements split by topic</abbr> ([rb:TopicStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TopicStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Every stream element corresponds to one Wikidata item.
- **<abbr title="Indicates that the dataset uses an ontology. The object must be a resource, but it doesn't neccesarily have to be an OWL ontology.">Uses ontology</abbr>**: [http://schema.org/](http://schema.org/)
- **<abbr title="Whether the dataset is RDF 1.1-compliant, i.e., does not use any non-standard features, like generalized triples.">Conforms to W3C RDF 1.1 specification</abbr>**: no
- **<abbr title="Whether the dataset is RDF-star compliant, i.e., does not use any non-standard features. Note that all standard RDF 1.1 datasets also qualify, as RDF-star is a superset of RDF 1.1.">Conforms to W3C RDF-star draft specification as of December 17, 2021</abbr>**: yes
- **<abbr title="Whether the dataset uses the non-standard generalized triples feature">Uses generalized triples</abbr>**: no
- **<abbr title="Whether the dataset uses the non-standard generalized datasets feature. A 'dataset' here is used in the same meaning as in the RDF 1.1 specification.">Uses generalized RDF datasets</abbr>**: no
- **<abbr title="Whether the dataset uses RDF-star features.">Uses RDF-star</abbr>**: yes

## Distributions

### <a name="stream-full"></a> Full triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: stream_full.tar.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 617,768
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 36.16 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `c9e06af6b58ed50dd1a5a7a4b778849c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b21f2846fab96a6054f813de27e992efe38404c8`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_full.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,631,687
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 594,855
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.88
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.22
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 853

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,736,327
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 57,578
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.81
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.50
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 66

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 211
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 174
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.02
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,736,116
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 57,405
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.81
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.50
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 66

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
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,484,547
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.02
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.10
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,455

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,009,932
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.25
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.04
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 850

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,622,855
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.63
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.48
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,127,393
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.06
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.06
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 853

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,484,547
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.02
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.10
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,455

### <a name="flat-full"></a> Full flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-full
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: flat_full.nt.gz
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 617,768
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 28.75 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5cebabe22bfa4e4ee2cd0f1b2502547a`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f70d95958960eb247ecbe6df159a642abbb77152`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_full.nt.gz](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_full.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,631,687
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 594,855
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.88
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.22
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 853

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,736,327
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 57,578
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.81
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.50
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 66

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 211
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 174
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.02
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,736,116
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 57,405
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.81
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 2.50
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 66

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
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,484,547
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.02
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.10
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,455

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,009,932
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.25
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 3.04
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 850

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 1,622,855
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.63
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.48
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 3,127,393
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.06
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.06
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 853

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 2,484,547
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.02
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 6.10
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,455

### <a name="stream-100k"></a> 100K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 3.57 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `93db75a276ca63541bfb58f85dd1a4cb`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ae652aa0df32689cb6b31ab652149c3fabe95216`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_100K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 502,972
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 102,657
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.03
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.30
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 853

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 187,612
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 37,329
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.88
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.98
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 49

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 66
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 66
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.03
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 187,546
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 37,263
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.88
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.97
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 49

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
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 226,648
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.27
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 9.28
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,455

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 246,103
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.46
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.24
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 850

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 257,646
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.58
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.49
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 332,939
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.46
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 853

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 226,648
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.27
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 9.28
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,455

### <a name="flat-100k"></a> 100K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-100k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_100K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 2.38 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `459fcc6e818aba459271874ba7c01515`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ba8de0be6ca49a118aed54ca674c67e3947fcdec`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_100K.nt.gz](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_100K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 502,972
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 102,657
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 5.03
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.30
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 853

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 187,612
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 37,329
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.88
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.98
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 49

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 66
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 66
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.03
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 187,546
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 37,263
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.88
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.97
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 49

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
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 226,648
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.27
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 9.28
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,455

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 246,103
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.46
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.24
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 850

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 257,646
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.58
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.49
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 332,939
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.33
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 5.46
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 853

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 226,648
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.27
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 9.28
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 1,455

### <a name="stream-10k"></a> 10K elements triple stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements triple stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: stream-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF triples.">Triple stream distribution</abbr> ([rb:tripleStreamDistribution](https://w3id.org/riverbench/schema/metadata#tripleStreamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 376.46 KB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: text/turtle
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `7e304d69042c206d4db615a9886e5db0`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `3f32b11ba612cc400ba7e95973e69318d729d2e2`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/stream_10K.tar.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49,533
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 10,233
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.95
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.93
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 19,576
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 7,332
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.96
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.90
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 8

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 19,576
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 7,332
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.96
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.90
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 8

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
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 22,977
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.30
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.34
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 23,762
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.38
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.53
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 26,100
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.61
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.49
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 33,009
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.30
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.39
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 22,977
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.30
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.34
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

### <a name="flat-10k"></a> 10K elements flat distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements flat distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: flat-10k
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `flat_10K.nt.gz`
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="The dataset is distributed as a single flat file.">Flat distribution</abbr> ([rb:flatDistribution](https://w3id.org/riverbench/schema/metadata#flatDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 256.83 KB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-triples
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `edaa110cde79d3c57846c39ea1ec7827`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `82db849d4410765888daba032cea8d635b6f0be6`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_10K.nt.gz](https://w3id.org/riverbench/datasets/yago-annotated-facts/dev/files/flat_10K.nt.gz)

#### <abbr title="Has a dataset statistics object">Has statistics</abbr>

##### IRI count statistics

- **Type**: <abbr title="Statistics about the number of IRIs in the dataset.">IRI count statistics</abbr> ([rb:IriCountStatistics](https://w3id.org/riverbench/schema/metadata#IriCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 49,533
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 10,233
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 4.95
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.93
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 3
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Blank node count statistics

- **Type**: <abbr title="Statistics about the number of blank nodes in the dataset.">Blank node count statistics</abbr> ([rb:BlankNodeCountStatistics](https://w3id.org/riverbench/schema/metadata#BlankNodeCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Literal count statistics

- **Type**: <abbr title="Statistics about the number of literals in the dataset.">Literal count statistics</abbr> ([rb:LiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#LiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 19,576
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 7,332
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.96
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.90
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 8

##### Simple literal count statistics

- **Type**: <abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literal count statistics</abbr> ([rb:SimpleLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#SimpleLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Datatype literal count statistics

- **Type**: <abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literal count statistics</abbr> ([rb:DatatypeLiteralCountStatistics](https://w3id.org/riverbench/schema/metadata#DatatypeLiteralCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 19,576
- **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique count (estimated)</abbr>**: 7,332
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 1.96
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.90
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 8

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
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 22,977
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.30
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.34
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

##### Subject count statistics

- **Type**: <abbr title="Statistics about the number of subjects in the dataset.">Subject count statistics</abbr> ([rb:SubjectCountStatistics](https://w3id.org/riverbench/schema/metadata#SubjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 23,762
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.38
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.53
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 7

##### Predicate count statistics

- **Type**: <abbr title="Statistics about the number of predicates in the dataset.">Predicate count statistics</abbr> ([rb:PredicateCountStatistics](https://w3id.org/riverbench/schema/metadata#PredicateCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 26,100
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.61
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.49
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 2
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 3

##### Object count statistics

- **Type**: <abbr title="Statistics about the number of objects in the dataset.">Object count statistics</abbr> ([rb:ObjectCountStatistics](https://w3id.org/riverbench/schema/metadata#ObjectCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 33,009
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 3.30
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.39
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 13

##### Graph count statistics

- **Type**: <abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graph count statistics</abbr> ([rb:GraphCountStatistics](https://w3id.org/riverbench/schema/metadata#GraphCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 0
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 0.00
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 0.00
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 0
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 0

##### Statement count statistics

- **Type**: <abbr title="Statistics about the number of RDF statements in the dataset.">Statement count statistics</abbr> ([rb:StatementCountStatistics](https://w3id.org/riverbench/schema/metadata#StatementCountStatistics))
- **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>**: 22,977
- **<abbr title="Arithmetic mean of a distribution">Mean</abbr>**: 2.30
- **<abbr title="Standard deviation of a distribution">Standard deviation</abbr>**: 1.34
- **<abbr title="Minimum value of a distribution">Minimum</abbr>**: 1
- **<abbr title="Maximum value of a distribution">Maximum</abbr>**: 10

