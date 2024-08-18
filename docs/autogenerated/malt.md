---
name: MALT
urls: ["http://ab.inf.uni-tuebingen.de/software/malt/"]
summary: >
  Aligns of metagenomic reads to a database of reference sequences (such as NR, GenBank or Silva) and outputs a MEGAN RMA file
---

<!--
~~~~~ DO NOT EDIT ~~~~~
This file is autogenerated from the MultiQC module python docstring.
Do not edit the markdown, it will be overwritten.

File path for the source of this content: multiqc/modules/malt/malt.py
~~~~~~~~~~~~~~~~~~~~~~~
-->

The MALT MultiQC module reads the header of the MALT log files and produces three MultiQC sections:

- A MALT summary statistics table
- A Mappability bargraph
- A Taxonomic assignment success bargraph

### File search patterns

```yaml
malt:
  contents: MaltRun - Aligns sequences using MALT (MEGAN alignment tool)
  num_lines: 2
```