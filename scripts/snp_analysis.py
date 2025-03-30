# scripts/snp_analysis.py
import pandas as pd
vcf = pd.read_csv("data/raw/test_snps.vcf", sep="\t", comment="#")
print(vcf["POS"].describe())  # Basic stats
rule all:
    input: "results/delirious_snps.csv"

rule annotate:
    input: "data/raw/snps.vcf"
    output: "results/annotated.csv"
    shell: "snpEff -csvStats {output} GRCh38.99 {input}"