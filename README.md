---
title: "WES analysis"
author: "Bingfang Ruth Xu"
date: "2024-07-31"

---



# Run Exome seek v1.0.3 or XAVIER v2.0 pipeline 

Run on a high-performance computing system. Exome seek/XAVIER pipeline uses Trimmomatic to trim FASTQ files and uses bwa-mem to conduct alignment and generate BAM files. 

```
src/XAVIER_human_mouse.Rmd
```

# Run Dragen v3.10 pipeline

Alternatively, use Dragen v3.10 pipeline to conduct the secondary analysis on a Dragen server.


# Germline and somatic calling

Utilize Exome seek v1.0.3 or XAVIER v2.0 pipeline to conduct germline and somatic calling and generate VCF files.


```
src/XAVIER_human_mouse.Rmd
```



# Annotate variants 

Annotate variants by using Ensembl Variant Effect Predictor (VEP) for mouse WES analysis.


```
src/WES_downstreamAnalysis_workflow_20230517.Rmd
```

Annotate variants by using PCGR, CPSR, MAF for human WES analysis.


```
src/Filter_merge_maf_20240120.Rmd
```
