"""
Create mock pipeline data from given mock clinical metadata json. Output file is ready to ingest to CanDIGv1 server
Default input file: mock_clinphen_data.json
"""

import json
import random


def generate_id_string(length):
    range_start = 10**(length-1)
    range_end = (10**length)-1
    return str(random.randint(range_start, range_end))

dataset = dict(pipeline_metadata = [])

def generate_pipeline(sample_ids):

    for i in sample_ids:

        current_entry = dict(
            Extraction = dict(),
            Sequencing = dict(),
            Alignment = dict(),
            VariantCalling = dict(),
            FusionDetection = dict(),
            ExpressionAnalysis = dict()
        )

        # current_entry = dataset["pipeline_metadata"][i]

        sample_id = i

        currExtractionId = generate_id_string(5)
        currSequencingId = generate_id_string(5)
        currAlignmentId = generate_id_string(5)
        currVariantCallingId = generate_id_string(5)
        currFusionDetectionId = generate_id_string(5)
        currExpressionAnalysisId = generate_id_string(5)

        # update patient

        current_entry["Extraction"] = dict(
            sampleId   = sample_id,
            rnaBlood    = random.choice(["QIASymphony", "N/A"]),
            dnaBlood = random.choice(["QIASymphony", "QIAamp DNA Blood Mini Kit on QIAcube"]),
            rnaTissue = random.choice(["Qiagen RNEasy micro kit","Agencourt RNAdvance Tissue Protocol using ALINE EvoPure RNA Isolation Kit reagents automated on Hamilton NIMBUS"]),
            dnaTissue   = random.choice(["QIAmp micro column","Agencourt RNAdvance Tissue Protocol using ALINE EvoPure RNA Isolation Kit reagents automated on Hamilton NIMBUS"]),
            extractionId = currExtractionId,
            site = random.choice(["Vancouver", "Toronto", "Montreal"])
            )


        # update enrollment

        current_entry["Sequencing"] = dict(
            sampleId = sample_id,
            dnaLibraryKit = random.choice(["Illumina TruSeq PCR-free library prep kit","illumina TruSeq Nano DNA library prep kit","Illumina TruSeq PCR-free genomic library construction using custom NEB Paired-End Sample Prep Premix Kit automated on Hamilton NIMBUS (500ng input)"]),
            dnaSeqPlatform = "HiSeq X",
            dnaReadLength = "Paired end, 150-bp",
            rnaLibraryKit = random.choice(["NEBNext Ultra II Directional RNA Library prep kit, input varying from 50 to 1000 ng","NEBNext Poly(A) mRNA Magnetic Isolation followed by Maxima H Minus First Strand cDNA Synthesis. NEB Paired-End Sample Prep Premix Kit automated on Hamilton NIMBUS (500ng input)"]),
            rnaSeqPlatform = random.choice(["HiSeq 2500","HiSeq"]),
            rnaReadLength = "Paired end, 125-bp",
            pcrCycles = random.choice(["10 for samples with more than 200 ng, or 12 if lower","13"]),
            sequencingId = currSequencingId,
            extractionId = currExtractionId,
            site = random.choice(["Vancouver", "Toronto", "Montreal"])
            )

        # update consent

        current_entry["Alignment"] = dict(
            sampleId = sample_id,
            inHousePipeline = random.choice(["run_library_alignment_pipeline.pl /0.03","N/A","N/A"]),
            alignmentTool = random.choice(["BWA-MEM/0.7.8,Samtools/1.5","BWA-MEM/0.7.15","BWA-MEM/0.7.6a,Sambamba/0.5.5"]),
            mergeTool = random.choice(["picard-tools/1.108","Sambamba/0.6.6","Sambamba/0.5.5"]),
            markDuplicates = random.choice(["picard-tools/1.108","Sambamba/0.6.6","Sambamba/0.5.5"]),
            realignerTarget = random.choice(["GATK/2.8.1","GATK/3.7","N/A"]),
            indelRealigner = random.choice(["GATK/2.8.1","GATK/3.7","N/A"]),
            baseRecalibrator = random.choice(["GATK/2.8.1","GATK/3.7","N/A"]),
            printReads = random.choice(["GATK/2.8.1","GATK/3.7","N/A"]),
            idxStats = random.choice(["samtools/0.1.19","Sambamba/0.5.5","N/A"]),
            flagStat = random.choice(["samtools/1.5","samtools/1.8","bamStats (in-house)"]),
            coverage = random.choice(["GATK/2.8.1","GATK/3.7","bamStats (in-house)"]),
            insertSizeMetrics = random.choice(["picard/1.107","picard/2.9.0","custom"]),
            fastqc = random.choice(["fastqc/0.11.5","fastqc/0.11.5","N/A"]),
            reference = random.choice(["hs37d5","GRCh37.p13","GRCh37-1000G"]),
            alignmentId = currAlignmentId,
            sequencingId = currSequencingId,
            site = random.choice(["Vancouver", "Toronto", "Montreal"])
            )

        # update diagnosis

        current_entry["VariantCalling"] = dict(
            sampleId = sample_id,
            inHousePipeline = random.choice(["run_ssm_pipeline.pl/0.01","N/A","N/A"]),
            variantCaller = random.choice(["GATK - MuTect2/3.5.0","GATK - MuTect2/3.7,Varscan/2.4.3,bcftools/1.6,Vardict/1.5.1","Strelka/1.0.6,mutationseq/4.3.5"]),
            tabulate = random.choice(["mutect2annovar.pl/0.02","N/A","N/A"]),
            annotation = random.choice(["Annovar /2013.08.23 Databases: refGene, ensGene, snp132, 1000g2012feb_all, esp6500si_all, cg69, cosmic70, clinvar_20150330, exac03, bed","Gemini 20.1 SNPEff/4.3:GRCh37.75 Database: gnomad, ExAC, 1000G, clinvar_20170130, cosmic68, etc. see gemini docs","SNPEff/4.1a - Databases:GRCh37.69, dbSNP_v137, cosmic_v64, clinvar_20170104"]),
            mergeTool = random.choice(["run_ssm_standard_filters.R R/3.4.0","N/A","N/A"]),
            rdaToTab = random.choice(["convert_mutect2_to_pype.R R/3.4.0","N/A","N/A"]),
            delly = random.choice(["delly/0.5.9","N/A","N/A"]),
            postFilter = random.choice(["run_snv_postfiltering.R R/3.4.0","N/A","N/A"]),
            clipFilter = random.choice(["filter_clips.RR/3.4.0","N/A","N/A"]),
            cosmic = random.choice(["CosmicCodingMuts.vcf.gz cosmic/0.75 grch37","cosmic/0.68","N/A"]),
            dbSnp = random.choice(["dbsnp_138.b37.vcf","dbsnp.b147.b37.vcf","N/A"]),
            variantCallingId = currVariantCallingId,
            alignmentId = currAlignmentId,
            site = random.choice(["Vancouver", "Toronto", "Montreal"])
            )

        # update sample

        current_entry["FusionDetection"] = dict(
            sampleId = sample_id,
            inHousePipeline = random.choice(["Fusion Validator/4.0","MAVIS 2.0"]),
            svDetection = random.choice(["Manta/1.3.2Delly/0.7.7Lumpy/0.2.13WHAM/1.8.0CNVkit/0.8.5svaba/0.2.2scones/2.1.0metasv/0.5.3","Trans-ABySS 1.4.10 Manta 1.0 DELLY 0.7.3"]),
            fusionDetection = random.choice(["Starfusion 0.7.0,Mapsplice 2.1.8,Defuse 0.6.2,Chimerascan 0.4.5","Starfucion, FusionCatcher","Trans-ABySS 1.4.10,Defuse 0.6.2,Chimerascan 0.4.5"]),
            realignment = random.choice(["STAR 2.4.2,Blast 2.2.29,Abyss 1.9.0,Gapfiller V1.10","N/A","N/A"]),
            annotation = random.choice(["GRASS","N/A","ENSEMBL"]),
            genomeReference = random.choice(["Gencode Release 19 (GRCh37.p13)","N/A","N/A"]),
            geneModels = random.choice(["Gencode Release 19 (GRCh37.p13)","N/A","N/A"]),
            fusionDetectionId = currFusionDetectionId,
            alignmentId = currAlignmentId,
            site = random.choice(["Vancouver", "Toronto", "Montreal"])
            )

        # update treatment

        current_entry["ExpressionAnalysis"] = dict(
            sampleId = sample_id,
            readLength = random.choice(["125bp","75bp","75bp"]),
            reference = random.choice(["Gencode Release 19 (GRCh37.p13)","GRCh37 - 1000G, Ens75","hg19, Ens69"]),
            alignmentTool = random.choice(["STAR 2.4.2","STAR 2.4.2", "BWA-mem/JAGuaR"]),
            bamHandling = random.choice(["STAR 2.4.2","PICARD 2.10.7","Sambamba/0.5.5"]),
            expressionEstimation = random.choice(["HTSeq/0.8.0","HTSeq 0.9.0 Cufflinks 2.2.1","custom scripts - duplicate reads included"]),
            expressionAnalysisId = currExpressionAnalysisId,
            sequencingId = currSequencingId,
            site = random.choice(["Vancouver", "Toronto", "Montreal"])
            )

        dataset["pipeline_metadata"].append(current_entry)


def newIdGenerator(oldId):

    newId = generate_id_string(5)

    if newId != oldId:
        return newId
    else:
        return newIdGenerator(oldId)


def insertSequencing(dataset):

    i = 0;
    selected = []

    while i < 80:
        selectedEntry = random.choice(dataset["pipeline_metadata"])["Sequencing"]

        if selectedEntry not in selected:
            selected.append(selectedEntry)

            current_entry = dict(
                Sequencing = dict()
            )

            newSequencingId = newIdGenerator(selectedEntry["sequencingId"])

            current_entry["Sequencing"] = dict(
                sampleId = selectedEntry["sampleId"],
                dnaLibraryKit = random.choice(["Illumina TruSeq PCR-free library prep kit","illumina TruSeq Nano DNA library prep kit","Illumina TruSeq PCR-free genomic library construction using custom NEB Paired-End Sample Prep Premix Kit automated on Hamilton NIMBUS (500ng input)"]),
                dnaSeqPlatform = "HiSeq X",
                dnaReadLength = "Paired end, 150-bp",
                rnaLibraryKit = random.choice(["NEBNext Ultra II Directional RNA Library prep kit, input varying from 50 to 1000 ng","NEBNext Poly(A) mRNA Magnetic Isolation followed by Maxima H Minus First Strand cDNA Synthesis. NEB Paired-End Sample Prep Premix Kit automated on Hamilton NIMBUS (500ng input)"]),
                rnaSeqPlatform = random.choice(["HiSeq 2500","HiSeq"]),
                rnaReadLength = "Paired end, 125-bp",
                pcrCycles = random.choice(["10 for samples with more than 200 ng, or 12 if lower","13"]),
                sequencingId = newSequencingId,
                extractionId = selectedEntry["extractionId"],
                site = random.choice(["Vancouver", "Toronto", "Montreal"])
            )

            dataset["pipeline_metadata"].append(current_entry)

            i = i + 1

def output_file(outfile_name):
    with open(outfile_name, 'w') as outfile:
        json.dump(dataset, outfile)


def get_sample_ids():
    with open('mock_clinphen_data.json') as f:
        data = json.load(f)

    sampleIds = []

    for entry in data["metadata"]:
        sample = entry.get("Sample")

        if sample is not None:
            sampleId = sample.get("sampleId")

        if sampleId is not None:
            sampleIds.append(sampleId)

    return sampleIds


if __name__ == "__main__":
    print("Creating pipeline data from clinical samples...")
    outfile_name = 'mock_pipeline_data.json'
    sample_ids = get_sample_ids()
    generate_pipeline(sample_ids)
    insertSequencing(dataset)
    output_file(outfile_name)
    print(">>> {} generated.".format(outfile_name))