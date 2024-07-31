#!/usr/bin/bash



for i in {28..61}
do 
  cp ./somatic_variant_calling/Pair_$i*/*.hard-filtered.vep.vcf.gz ./
done


for i in {28..61}
do 
  gunzip $i*.hard-filtered.vep.vcf.gz
done



