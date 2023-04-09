# Data Governance Schema

## Introduction

This scheme is based on the [Data Beliefs](https://www.linkedin.com/pulse/data-beliefs-eugene-morozov/) I outlined in the LinkedIn article back in 2022. It is formalising Terms, Concepts, Data Containers, Data Elements and Data Ownership.

## Usage

Import the schema into [Confluence](https://www.atlassian.com/software/confluence) with [Taxonomies for Confluence](https://dalstonsemantics.com/services/taxonomies-for-confluence/) add-on and use it to govern your organisation's data.

## References

1. [Data](https://www.isko.org/cyclo/data) and [Information](https://www.isko.org/cyclo/information) entries in the [ISKO Encyclopedia of Knowledge Organization](https://www.isko.org/cyclo/) by Birger Hjørland.
1. [Data and Reality](https://www.goodreads.com/en/book/show/1753248.Data_and_Reality) by William Kent.
1. [Metaphors We Live By](https://www.goodreads.com/book/show/34459.Metaphors_We_Live_By) by George Lakoff and Mark Johnson.
1. [Creating a Structured Vocabulary](https://www.meetup.com/Knowledge-Organisation-London/events/284319067/) by Leonard Will.
1. [Data on the Outside vs. Data on the Inside](https://queue.acm.org/detail.cfm?id=3415014) by Pat Helland.
1. [Why not one big database? Principles for data ownership](https://www.sciencedirect.com/science/article/abs/pii/0167923694000424) by Marshall Van Alstyne, Erik Brynjolfsson, and Stuart Madnick.

## Design Decisions

1. Following schema.org naming convention for properties (e.g. classification rather than hasClassification) to increase readability and adoption.
1. Only using "has" and "is" in property URIs and labels when it helps make the meaning clear (e.g. hasBroaderConcept rather than broader as in SKOS) to increase readability and adoption.
1. Doing away with domain and range and using names of the classes in the UIRs of the properties and, in most cases, in the labels

## Attribution and Disclaimer

Part of this work, "Data Governance Taxonomy", is a derivative of [Prudential Practice Guide CPG 235 - Managing Data Risk (September 2013)](https://www.apra.gov.au/managing-data-risk) by [Australian Prudential Regulation Authority (APRA)](https://www.apra.gov.au/) used under [Creative Commons Attribution 3.0 Australia Licence (CCBY 3.0)](www.creativecommons.org/licenses/by/3.0/au/)

This prudential practice guide is not legal advice and users are encouraged to obtain professional advice about the application of any legislation or prudential standard relevant to their particular circumstances and to exercise their own skill and care in relation to any material contained in this guide.

APRA disclaims any liability for any loss or damage arising out of any use of this prudential practice guide.

APRA do not endorse this derivative work or its author.