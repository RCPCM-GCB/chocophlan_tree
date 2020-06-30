import os, glob

mp_genomes_dir = '/data11/bio/databases/metaphlan2/mp_genomes'

genomes = [f.replace('.fna.gz', '.fna') for f in glob.glob(os.path.join(mp_genomes_dir, '*/*'))]

genomes = ['/data11/bio/databases/metaphlan2/mp_genomes/GCA_001434655/GCA_001434655.1_ASM143465v1_genomic.fna',
 '/data11/bio/databases/metaphlan2/mp_genomes/GCA_002953935/GCA_002953935.1_ASM295393v1_genomic.fna',
 '/data11/bio/databases/metaphlan2/mp_genomes/GCA_900114345/GCA_900114345.1_IMG-taxon_2609459760_annotated_assembly_genomic.fna',
 '/data11/bio/databases/metaphlan2/mp_genomes/GCA_000317655/GCA_000317655.1_ASM31765v1_genomic.fna',
 '/data11/bio/databases/metaphlan2/mp_genomes/GCA_000239775/GCA_000239775.2_ASM23977v2_genomic.fna',
 '/data11/bio/databases/metaphlan2/mp_genomes/GCA_001189345/GCA_001189345.1_ASM118934v1_genomic.fna',
 '/data11/bio/databases/metaphlan2/mp_genomes/GCA_900099815/GCA_900099815.1_IMG-taxon_2622736510_annotated_assembly_genomic.fna']

rule run_all:
    input: genomes

rule ungz_fna:
    input:  os.path.join(mp_genomes_dir, '{GCA_id}/{fna_file_name}.fna.gz')
    output: os.path.join(mp_genomes_dir, '{GCA_id}/{fna_file_name}.fna')
    shell: 'gunzip -k {input}'

