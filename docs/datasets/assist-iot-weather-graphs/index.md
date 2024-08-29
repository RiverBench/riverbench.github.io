<div markdown class="rb-top-buttons"><div markdown>[:material-link-variant: Permanent URL](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev "Link to the permanent URL of this resource.")</div><div markdown>**[:material-database-edit: Edit this page](https://github.com/RiverBench/dataset-assist-iot-weather-graphs/edit/main/metadata.ttl "Edit this page's source in RDF/Turtle on GitHub.")**</div><div markdown>[:material-help-circle:](../../documentation/editing-docs.md "Need help with editing?")</div></div>

# Dataset: assist-iot-weather-graphs (development version)

This is a timestamped stream of weather data collected with a Davis Vantage Pro 2 weather station installed on the building of the [Systems Research Institute, Polish Academy of Sciences](https://www.ibspan.waw.pl/en/home/). The data was collected during the [ASSIST-IoT Horizon 2020 project](https://assist-iot.eu/). The station measured several different weather parameters and transmitted them in real time at regular intervals. The measurements have rich annotations with the [SOSA/SSN](https://www.w3.org/TR/vocab-ssn/) and [OM 2.0](http://www.ontology-of-units-of-measure.org/page/om-2) ontologies. The stream is very regular and the elements only differ by numeric values and timestamps. This is the graph variant, which is a timestamped graph stream compatible with the RSP Data Model.
    
The dataset is a real application of RDF streaming (originally streamed over MQTT), with much richer annotations than [citypulse-traffic](https://w3id.org/riverbench/datasets/citypulse-traffic). On the other hand, it is perfectly regular, with no differences in structure between stream elements.

!!! info

    :fontawesome-solid-diagram-project: Download this metadata in RDF: **[Turtle](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev.ttl)**, **[N-Triples](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev.nt)**, **[RDF/XML](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev.rdf)**, **[Jelly](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev.jelly)**
    <br>:material-github: Source repository: **[dataset-assist-iot-weather-graphs](https://github.com/RiverBench/dataset-assist-iot-weather-graphs)**
    <br><abbr title="The permanent URL is guaranteed to never change and also allows for retrieving machine-readable metadata in RDF. You should always use permanent URLs to refer to tasks, profiles, or datasets in RiverBench.">:material-link-variant: Permanent URL:</abbr> [`https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev`](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)

    **[:octicons-arrow-down-24: Go to download links](#distributions)**

??? example "Stream preview (click to expand)"

    === "Element 0"

        ```turtle title="0000000000.trig"
        --8<-- "docs/datasets/assist-iot-weather-graphs/data/sample_0000000000.trig"
        ```


    === "Element 10"

        ```turtle title="0000000010.trig"
        --8<-- "docs/datasets/assist-iot-weather-graphs/data/sample_0000000010.trig"
        ```


    === "Element 100"

        ```turtle title="0000000100.trig"
        --8<-- "docs/datasets/assist-iot-weather-graphs/data/sample_0000000100.trig"
        ```


    === "Element 1000"

        ```turtle title="0000001000.trig"
        --8<-- "docs/datasets/assist-iot-weather-graphs/data/sample_0000001000.trig"
        ```


    === "Element 10000"

        ```turtle title="0000010000.trig"
        --8<-- "docs/datasets/assist-iot-weather-graphs/data/sample_0000010000.trig"
        ```


## General information

- **<abbr title="A name given to the resource.">Title</abbr>**: ASSIST-IoT weather (graphs variant) _(<abbr title="English">en</abbr>)_
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `assist-iot-weather-graphs`
- **<abbr title="Version tag of an artifact">Has version</abbr>**: `dev`
- **<abbr title="A main category of the resource. A resource can have multiple themes.">Theme</abbr>**: 
    - Data collection ([eurovoc:6030](http://eurovoc.europa.eu/6030))
    - Internet of Things ([eurovoc:c_b12a760a](http://eurovoc.europa.eu/c_b12a760a))
    - Meteorology ([eurovoc:1892](http://eurovoc.europa.eu/1892))
    - Spatial data ([eurovoc:c_7a168de0](http://eurovoc.europa.eu/c_7a168de0))
- **<abbr title="An entity responsible for making the resource.">Creator</abbr>**: 
    - **Piotr Sowiński (1)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: Piotr Sowiński
        - **<abbr title="A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).">Nickname</abbr>**: Ostrzyciel
        - **<abbr title="This axiom needed so that Protege loads DCAT2 without errors.">Homepage</abbr>**:     
            -  ([https://orcid.org/0000-0002-2543-9461](https://orcid.org/0000-0002-2543-9461))
            - Ostrzyciel ([https://github.com/Ostrzyciel](https://github.com/Ostrzyciel))
    - **ASSIST-IoT Horizon 2020 project (2)**    
        - **<abbr title="A name for some thing.">Name</abbr>**: ASSIST-IoT Horizon 2020 project
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 957258.
        - **<abbr title="This axiom needed so that Protege loads DCAT2 without errors.">Homepage</abbr>**: [https://assist-iot.eu/](https://assist-iot.eu/)
- **<abbr title="A legal document giving official permission to do something with the resource.">License</abbr>**: [https://spdx.org/licenses/CC-BY-4.0](https://spdx.org/licenses/CC-BY-4.0)
- **<abbr title="Date of formal issuance of the resource.">Date Issued</abbr>**: 2023-05-04
- **<abbr title="Date on which the resource was changed.">Date Modified</abbr>**: 2024-08-29
- **<abbr title="A Web page that can be navigated to in a Web browser to gain access to the catalog, a dataset, its distributions and/or additional information.">Landing page</abbr>**: [assist-iot-weather-graphs (dev)](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev)
- **<abbr title="An established standard to which the described resource conforms.">Conforms To</abbr>**: Metadata ([https://w3id.org/riverbench/schema/metadata](https://w3id.org/riverbench/schema/metadata))

## Technical metadata

- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to a set of measurements from the weather station. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 701,278
- **<abbr title="Indicates how the stream was split into elements.">Has stream element split</abbr>**: 
    - **Type**: <abbr title="The elements correspond to different instants or intervals of time.">Stream elements split by time</abbr> ([rb:TimeStreamElementSplit](https://w3id.org/riverbench/schema/metadata#TimeStreamElementSplit))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: Each stream element corresponds to one set of measurements from the weather station. Data was collected every 10 seconds. _(<abbr title="English">en</abbr>)_
    - **<abbr title="The IRI of the property that is used in the stream to denote time at which the event occured.">Has temporal property</abbr>**: [http://www.w3.org/ns/prov#atTime](http://www.w3.org/ns/prov#atTime)
- **<abbr title="A vocabulary that is used in the dataset.">Uses vocabulary</abbr>**: 
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
- **<abbr title="A language of the resource.">Language</abbr>**: `en`

## Distributions


### Download links

The dataset is published in a few size variants, each containing a specific number of stream elements.
For each size, there are three distribution types available: flat (just an N-Triples/N-Quads file),
streaming (a .tar.gz archive with Turtle/TriG files, one file per stream element),
and [Jelly](https://w3id.org/jelly) (a native binary format for streaming RDF).
See the [documentation](../../documentation/dataset-release-format.md) for more details.

Distribution size | Statements | Flat | Streaming | Jelly
--- | --: | --: | --: | --:
<abbr title="10,000 stream elements">10K</abbr> | 1,160,000 | [:octicons-download-24: 5.0 MB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_10K.nq.gz) | [:octicons-download-24: 1.3 MB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_10K.tar.gz) | [:octicons-download-24: 703.3 KB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz)
<abbr title="100,000 stream elements">100K</abbr> | 11,600,000 | [:octicons-download-24: 50.3 MB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_100K.nq.gz) | [:octicons-download-24: 13.4 MB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_100K.tar.gz) | [:octicons-download-24: 6.8 MB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz)
<abbr title="701,278 stream elements">Full</abbr> | 81,348,248 | [:octicons-download-24: 353.0 MB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_full.nq.gz) | [:octicons-download-24: 93.8 MB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz) | [:octicons-download-24: 47.7 MB](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz)


The full metadata of all distributions can be found below.

### <a name="stream-full"></a> Full stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_full.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to a set of measurements from the weather station. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 701,278
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 93.8 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `71d6406ce833fbed4cf191fe8d69d541`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `f46eeac8d64004f3bed410e8a88443b7a6de3002`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_full.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="jelly-full"></a> Full Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: Full Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-full`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_full.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to a set of measurements from the weather station. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A full distribution, including all data in the dataset.">Full distribution</abbr> ([rb:fullDistribution](https://w3id.org/riverbench/schema/metadata#fullDistribution))
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 701,278
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 47.7 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `23e2ab84352a6437f9c729cc21606fd3`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ea3c980a47b598d405e8647fd3936343a7ec3f9c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_full.jelly.gz)
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
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 701,278
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 353.0 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `cc44aff0c32f7b1dfb89fd7e5c2558c1`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `ff71b599c2ddfcd34c2bea710b8de41fc81d463e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_full.nq.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_full.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-full](#statistics-full)

### <a name="stream-100k"></a> 100K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_100K.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to a set of measurements from the weather station. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 13.4 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6c0031a3f653ec3834db7940903cd6f5`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `5db3b576faf42813745122c0d525bca387ba3b5c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_100K.tar.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_100K.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="jelly-100k"></a> 100K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 100K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-100k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_100K.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to a set of measurements from the weather station. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 100,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 6.8 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `efa5f1632c2af4eebe2729a06e75537e`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `6ed0e49c69c59406855e53b0717825d8d3ecaa76`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_100K.jelly.gz)
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
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 50.3 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `25c7625f0cee259f95c7e6635598d72c`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `34b8bd46bf73b95880362f2b796011eeed6bb19d`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_100K.nq.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_100K.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-100k](#statistics-100k)

### <a name="stream-10k"></a> 10K elements stream distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements stream distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `stream-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `stream_10K.tar.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
    - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to a set of measurements from the weather station. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
    - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
    - <abbr title="The dataset is distributed as a stream of RDF datasets or RDF graphs (grouped RDF stream in RDF-STaX).">Stream distribution</abbr> ([rb:streamDistribution](https://w3id.org/riverbench/schema/metadata#streamDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 1.3 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/trig
- **<abbr title="The package format of the distribution in which one or more data files are grouped together, e.g. to enable a set of related files to be downloaded together.">Packaging format</abbr>**: application/tar
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `0adf6a7412e0a6de52156f058cc4a4b7`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `8bf7bf6773866ace13802e3c4744e763d8fb01fe`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_10K.tar.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/stream_10K.tar.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

### <a name="jelly-10k"></a> 10K elements Jelly distribution

- **<abbr title="A name given to the resource.">Title</abbr>**: 10K elements Jelly distribution
- **<abbr title="An unambiguous reference to the resource within a given context.">Identifier</abbr>**: `jelly-10k`
- **<abbr title="Canonical file name of this distribution">Has file name</abbr>**: `jelly_10K.jelly.gz`
- **<abbr title="Inverse of stax:isUsageOf – indicates that the subject is related to a usage of an RDF stream type.  The subject for this property can be for example a published stream on the Web (e.g., vocals:RDFStream) or a scientific publication that discusses a usage of an RDF stream type.">Has stream type usage</abbr>**: 
    - **RDF stream type usage (1)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a stream of RDF datasets, each containing exactly one named graph corresponding to a set of measurements from the weather station. The named graphs are annotated with the timestamp property. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A timestamped named graph is an RDF dataset in which: (1) there is exactly one named RDF graph pair <n, G>, where G is an RDF graph, and n is the graph name; (2) the default graph includes a timestamp triple <n, p, t>, where p is a timestamp predicate that relates t, called the timestamp, and the graph G.  A timestamped RDF named graph stream is an RDF named graph stream in which every element is a timestamped named graph. The elements that share the same timestamp predicate p are ordered by the partial order associated with p.">Timestamped RDF named graph stream</abbr> ([stax:timestampedNamedGraphStream](https://w3id.org/stax/ontology#timestampedNamedGraphStream))
    - **RDF stream type usage (2)**    
        - **Type**: <abbr title="Class for instances of using an RDF stream type, in a program, an academic paper, or elsewhere. This class is suitable for annotating both theoretical uses and practical ones, i.e., real streams or datasets.  Instances of this class should have the stax:hasStreamType property pointing to a concrete stream type. The stax:usedIn property is recommended to indicate where the stream is used – alternatively you can use its inverse (stax:hasStreamTypeUsage). The use of other properties (e.g., rdfs:label, rdfs:comment) is encouraged to give more context about the usage.  Note that 'stream type usage' is a subjective assertion and instances of this class may be annotated with additional provenance properties to explain who made the assertion. There can be multiple views on what type of stream is in use, depending on the involved actor, processing step, etc.">RDF stream type usage</abbr> ([stax:RdfStreamTypeUsage](https://w3id.org/stax/ontology#RdfStreamTypeUsage))
        - **<abbr title="A description of the subject resource.">Comment</abbr>**: The dataset can be viewed as a flattened stream of quads. _(<abbr title="English">en</abbr>)_
        - **<abbr title="For an RDF stream type usage, this property indicates which stream type is used.">Has stream type</abbr>**: <abbr title="A flat RDF quad stream is a flat RDF stream whose elements are quads.">Flat RDF quad stream</abbr> ([stax:flatQuadStream](https://w3id.org/stax/ontology#flatQuadStream))
- **<abbr title="Indicates the type of RiverBench dataset distribution">Has distribution type</abbr>**: 
    - <abbr title="A streaming distribution in the Jelly binary format.">Jelly distribution</abbr> ([rb:jellyDistribution](https://w3id.org/riverbench/schema/metadata#jellyDistribution))
    - <abbr title="A partial distribution, including only a subset of the data in the dataset. The rb:hasStreamElementCount property indicates the length of this distribution.">Partial distribution</abbr> ([rb:partialDistribution](https://w3id.org/riverbench/schema/metadata#partialDistribution))
- **<abbr title="Number of elements in the stream">Has stream element count</abbr>**: 10,000
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 703.3 KB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/x-jelly-rdf
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `1a4d5ab634da20d2869793027e64aa77`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `162f6ef7e4dd2d143aa8921415a6e3c89c4fe671`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/jelly_10K.jelly.gz)
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
- **<abbr title="The size of a distribution in bytes.">Byte size</abbr>**: 5.0 MB
- **<abbr title="The media type of the distribution as defined by IANA">Media type</abbr>**: application/n-quads
- **<abbr title="The compression format of the distribution in which the data is contained in a compressed form, e.g. to reduce the size of the downloadable file.">Compression format</abbr>**: application/gzip
- **<abbr title="The checksum property provides a mechanism that can be used to verify that the contents of a File or Package have not changed.">Checksum</abbr>**: 
    - **Checksum (1)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `8673a4b95245fd8ba0bee87c2e26d054`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was MD5">ChecksumAlgorithm_md5</abbr> ([spdx:checksumAlgorithm_md5](http://spdx.org/rdf/terms#checksumAlgorithm_md5))
    - **Checksum (2)**    
        - **Type**: <abbr title="A Checksum is value that allows the contents of a file to be authenticated. Even small changes to the content of the file will change its checksum. This class allows the results of a variety of checksum and cryptographic message digest algorithms to be represented.">Checksum</abbr> ([spdx:Checksum](http://spdx.org/rdf/terms#Checksum))
        - **<abbr title="The checksumValue property provides a lower case hexidecimal encoded digest value produced using a specific algorithm.">ChecksumValue</abbr>**: `b539baf70f62bc24ff8322dcfe5886f318ed6339`
        - **<abbr title="Identifies the algorithm used to produce the subject Checksum. Currently, SHA-1 is the only supported algorithm. It is anticipated that other algorithms will be supported at a later time.">Algorithm</abbr>**: <abbr title="Indicates the algorithm used was SHA-1">ChecksumAlgorithm_sha1</abbr> ([spdx:checksumAlgorithm_sha1](http://spdx.org/rdf/terms#checksumAlgorithm_sha1))
- **<abbr title="The URL of the downloadable file in a given format. E.g. CSV file or RDF file. The format is indicated by the distribution's dct:format and/or dcat:mediaType.">Download URL</abbr>**: [https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_10K.nq.gz](https://w3id.org/riverbench/datasets/assist-iot-weather-graphs/dev/files/flat_10K.nq.gz)
- **<abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>**: [statistics-10k](#statistics-10k)

## <abbr title="Indicates the grouping (set) of statistics for a given distribution. Multiple distributions can share one set of statistics, but a distribution must have exactly one statistics set.">Statistics</abbr>

### <a name="statistics-full"></a> Statistics for full distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for full distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique (approx.)</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 46,985,626 | 701,333 | 67.00 | 0.00 | 67 | 67 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 1,402,556 | 701,186 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 81,348,248 | _N/A_ | 116.00 | 0.00 | 116 | 116 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 8,516,050 | 704,202 | 12.14 | 0.69 | 10 | 13 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 1,402,556 | 2 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 7,113,494 | 704,200 | 10.14 | 0.69 | 8 | 11 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 21,739,618 | 701,215 | 31.00 | 0.00 | 31 | 31 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 9,116,614 | 13 | 13.00 | 0.00 | 13 | 13 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 39,372,282 | 704,261 | 56.14 | 0.69 | 54 | 57 |

### <a name="statistics-100k"></a> Statistics for 100K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 100K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique (approx.)</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 6,700,000 | 100,071 | 67.00 | 0.00 | 67 | 67 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 200,000 | 100,004 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 11,600,000 | _N/A_ | 116.00 | 0.00 | 116 | 116 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 1,205,786 | 102,024 | 12.06 | 0.61 | 10 | 13 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 200,000 | 2 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 1,005,786 | 102,022 | 10.06 | 0.61 | 8 | 11 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 3,100,000 | 100,033 | 31.00 | 0.00 | 31 | 31 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 1,300,000 | 13 | 13.00 | 0.00 | 13 | 13 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 5,605,786 | 102,082 | 56.06 | 0.61 | 54 | 57 |

### <a name="statistics-10k"></a> Statistics for 10K distributions

- **<abbr title="A name given to the resource.">Title</abbr>**: Statistics for 10K distributions

| | **<abbr title="Sum of all values in the distribution. In statistics about counts, this corresponds to the total number of given elements in the dataset.">Sum</abbr>** | **<abbr title="Only used for count statistics. Indicates how many unique elements are in the entire dataset. The value is estimated with a Bloom filter and is accurate to ~1%.">Unique (approx.)</abbr>** | **<abbr title="Arithmetic mean of a distribution">Mean</abbr>** | **<abbr title="Standard deviation of a distribution">St. dev.</abbr>** | **<abbr title="Minimum value of a distribution">Min.</abbr>** | **<abbr title="Maximum value of a distribution">Max.</abbr>** |
| --- | --: | --: | --: | --: | --: | --: |
| **<abbr title="Statistics about the number of IRIs in the dataset.">IRIs</abbr>** | 670,000 | 10,066 | 67.00 | 0.00 | 67 | 67 |
| **<abbr title="Statistics about the number of blank nodes in the dataset.">Blank nodes</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of RDF graphs in the dataset, including the default graph.">Graphs</abbr>** | 20,000 | 10,002 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of RDF statements in the dataset.">Statements</abbr>** | 1,160,000 | _N/A_ | 116.00 | 0.00 | 116 | 116 |
| **<abbr title="Statistics about the number of literals in the dataset.">Literals</abbr>** | 120,737 | 10,801 | 12.07 | 0.60 | 10 | 13 |
| **<abbr title="Statistics about the number of simple literals (of type xsd:string) in the dataset.">Simple literals</abbr>** | 20,000 | 2 | 2.00 | 0.00 | 2 | 2 |
| **<abbr title="Statistics about the number of datatype literals (NOT of type rdf:langString) in the dataset.">Datatype literals</abbr>** | 100,737 | 10,799 | 10.07 | 0.60 | 8 | 11 |
| **<abbr title="Statistics about the number of language literals in the dataset.">Language literals</abbr>** | 0 | 0 | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of quoted triples in the dataset.">Quoted triples</abbr>** | 0 | _N/A_ | 0.00 | 0.00 | 0 | 0 |
| **<abbr title="Statistics about the number of subjects in the dataset.">Subjects</abbr>** | 310,000 | 10,031 | 31.00 | 0.00 | 31 | 31 |
| **<abbr title="Statistics about the number of predicates in the dataset.">Predicates</abbr>** | 130,000 | 13 | 13.00 | 0.00 | 13 | 13 |
| **<abbr title="Statistics about the number of objects in the dataset.">Objects</abbr>** | 560,737 | 10,845 | 56.07 | 0.60 | 54 | 57 |

