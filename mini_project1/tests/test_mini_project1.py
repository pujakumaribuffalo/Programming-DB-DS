import unittest
import os
import mini_project1

import pprint
pp = pprint.PrettyPrinter(indent=4)

from gradescope_utils.autograder_utils.decorators import (number, visibility,
                                                          weight)


class TestMiniProject1(unittest.TestCase):
    def setUp(self):
        self.mini_project1 = mini_project1

    @weight(3)
    @visibility('visible')
    @number("1.1")
    def test_determine_data_type_1(self):
        value = self.mini_project1.determine_data_type('1.2')
        self.assertEqual(float, value)

    @weight(3)
    @visibility('visible')
    @number("1.2")
    def test_determine_data_type_2(self):
        value = self.mini_project1.determine_data_type('4')
        self.assertEqual(int, value)

    @weight(3)
    @visibility('visible')
    @number("1.3")
    def test_determine_data_type_3(self):
        value = self.mini_project1.determine_data_type('EAS503')
        self.assertEqual(str, value)

    @weight(3)
    @visibility('visible')
    @number("2.1")
    def test_determine_data_type_of_list_1(self):
        value = self.mini_project1.determine_data_type_of_list(['1', '2', '3'])
        self.assertEqual(int, value)

    @weight(3)
    @visibility('visible')
    @number("2.2")
    def test_determine_data_type_of_list_2(self):
        value = self.mini_project1.determine_data_type_of_list(
            ['1.1', '2.2', '3.3'])
        self.assertEqual(float, value)

    @weight(3)
    @visibility('visible')
    @number("2.3")
    def test_determine_data_type_of_list_3(self):
        value = self.mini_project1.determine_data_type_of_list(
            ['1.1', '2', '3.3'])
        self.assertEqual(float, value)

    @weight(3)
    @visibility('visible')
    @number("2.4")
    def test_determine_data_type_of_list_4(self):
        value = self.mini_project1.determine_data_type_of_list(
            ['1.1', '234String', '3.3'])
        self.assertEqual(str, value)

    @weight(6)
    @visibility('visible')
    @number("3.1")
    def test_format_sample_fields_1(self):
        expected_solution = {
            'XG102': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG103': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG104': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG202': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG203': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG204': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG302': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG303': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG304': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG402': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG403': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG404': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'}}

        format_field = "GT:AD:DP:GQ:PGT:PID:PL"
        sample_field = {'XG102': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG103': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG104': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG202': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG203': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG204': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG302': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG303': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG304': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG402': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG403': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG404': '0/1:34,38:72:99:.:.:938,0,796'}

        value = self.mini_project1.format_sample_fields(
            format_field, sample_field)
        self.assertEqual(expected_solution['XG102'], value['XG102'])

    @weight(6)
    @visibility('visible')
    @number("3.2")
    def test_format_sample_fields_2(self):
        expected_solution = {
            'XG102': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG103': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG104': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG202': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG203': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG204': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG302': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG303': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG304': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG402': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG403': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG404': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'}}

        format_field = "GT:AD:DP:GQ:PGT:PID:PL"
        sample_field = {'XG102': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG103': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG104': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG202': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG203': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG204': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG302': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG303': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG304': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG402': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG403': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG404': '0/1:34,38:72:99:.:.:938,0,796'}

        value = self.mini_project1.format_sample_fields(
            format_field, sample_field)
        self.assertEqual(expected_solution['XG302'], value['XG302'])

    @weight(6)
    @visibility('visible')
    @number("3.3")
    def test_format_sample_fields_3(self):
        expected_solution = {
            'XG102': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG103': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG104': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG202': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG203': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG204': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG302': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG303': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG304': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'},
            'XG402': {'AD': '0,76',
                      'DP': '76',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '1|1',
                      'PID': '48306945_C_G',
                      'PL': '3353,229,0'},
            'XG403': {'AD': '0,52',
                      'DP': '52',
                      'GQ': '99',
                      'GT': '1/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '1517,156,0'},
            'XG404': {'AD': '34,38',
                      'DP': '72',
                      'GQ': '99',
                      'GT': '0/1',
                      'PGT': '.',
                      'PID': '.',
                      'PL': '938,0,796'}}

        format_field = "GT:AD:DP:GQ:PGT:PID:PL"
        sample_field = {'XG102': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG103': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG104': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG202': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG203': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG204': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG302': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG303': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG304': '0/1:34,38:72:99:.:.:938,0,796',
                        'XG402': '1/1:0,76:76:99:1|1:48306945_C_G:3353,229,0',
                        'XG403': '1/1:0,52:52:99:.:.:1517,156,0',
                        'XG404': '0/1:34,38:72:99:.:.:938,0,796'}

        value = self.mini_project1.format_sample_fields(
            format_field, sample_field)
        self.assertEqual(expected_solution['XG404'], value['XG404'])

    @weight(10)
    @visibility('visible')
    @number("4")
    def test_create_dict_from_line(self):
        expected_solution = {'CHROM': '4', 'POS': '123416186', 'ID': '.', 'REF': 'A', 'ALT': 'G', 'QUAL': '23.25', 'FILTER': 'PASS', 'INFO': 'AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2,IL21;GeneDetail.refGene=dist=38536,dist=117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471,ENSG00000138684;GeneDetail.ensGene=dist=38306,dist=117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END',
                             'SAMPLE': {'XG102': {'GT': '0/1', 'AD': '51,8', 'DP': '59', 'GQ': '32', 'PL': '32,0,1388'}, 'XG103': {'GT': '0/0', 'AD': '47,0', 'DP': '47', 'GQ': '99', 'PL': '0,114,1353'}, 'XG104': {'GT': '0/0', 'AD': '74,0', 'DP': '74', 'GQ': '51', 'PL': '0,51,1827'}, 'XG202': {'GT': '0/1', 'AD': '51,8', 'DP': '59', 'GQ': '32', 'PL': '32,0,1388'}, 'XG203': {'GT': '0/0', 'AD': '47,0', 'DP': '47', 'GQ': '99', 'PL': '0,114,1353'}, 'XG204': {'GT': '0/0', 'AD': '74,0', 'DP': '74', 'GQ': '51', 'PL': '0,51,1827'}, 'XG302': {'GT': '0/1', 'AD': '51,8', 'DP': '59', 'GQ': '32', 'PL': '32,0,1388'}, 'XG303': {'GT': '0/0', 'AD': '47,0', 'DP': '47', 'GQ': '99', 'PL': '0,114,1353'}, 'XG304': {'GT': '0/0', 'AD': '74,0', 'DP': '74', 'GQ': '51', 'PL': '0,51,1827'}, 'XG402': {'GT': '0/1', 'AD': '51,8', 'DP': '59', 'GQ': '32', 'PL': '32,0,1388'}, 'XG403': {'GT': '0/0', 'AD': '47,0', 'DP': '47', 'GQ': '99', 'PL': '0,114,1353'}, 'XG404': {'GT': '0/0', 'AD': '74,0', 'DP': '74', 'GQ': '51', 'PL': '0,51,1827'}}}

        header = "CHROM	POS	ID	REF	ALT	QUAL	FILTER	INFO	FORMAT	XG102	XG103	XG104	XG202	XG203	XG204	XG302	XG303	XG304	XG402	XG403	XG404".split(
            '\t')
        line = '4	123416186	.	A	G	23.25	PASS	AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2,IL21;GeneDetail.refGene=dist=38536,dist=117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471,ENSG00000138684;GeneDetail.ensGene=dist=38306,dist=117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END	GT:AD:DP:GQ:PL	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827	0/1:51,8:59:32:32,0,1388	0/0:47,0:47:99:0,114,1353	0/0:74,0:74:51:0,51,1827'

        value = self.mini_project1.create_dict_from_line(header, line)
        self.assertEqual(expected_solution, value)

    @weight(10)
    @visibility('visible')
    @number("5")
    def test_read_vcf_file(self):
        expected_solution = [{'CHROM': '4',
                              'POS': '123416186',
                              'ID': '.',
                              'REF': 'A',
                              'ALT': 'G',
                              'QUAL': '23.25',
                              'FILTER': 'PASS',
                              'INFO': 'AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2,IL21;GeneDetail.refGene=dist=38536,dist=117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471,ENSG00000138684;GeneDetail.ensGene=dist=38306,dist=117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END',
                              'SAMPLE': {'XG102': {'GT': '0/1',
                                                   'AD': '51,8',
                                                   'DP': '59',
                                                   'GQ': '32',
                                                   'PL': '32,0,1388'},
                                         'XG103': {'GT': '0/0',
                                                   'AD': '47,0',
                                                   'DP': '47',
                                                   'GQ': '99',
                                                   'PL': '0,114,1353'},
                                         'XG104': {'GT': '0/0',
                                                   'AD': '74,0',
                                                   'DP': '74',
                                                   'GQ': '51',
                                                   'PL': '0,51,1827'},
                                         'XG202': {'GT': '0/1',
                                                   'AD': '51,8',
                                                   'DP': '59',
                                                   'GQ': '32',
                                                   'PL': '32,0,1388'},
                                         'XG203': {'GT': '0/0',
                                                   'AD': '47,0',
                                                   'DP': '47',
                                                   'GQ': '99',
                                                   'PL': '0,114,1353'},
                                         'XG204': {'GT': '0/0',
                                                   'AD': '74,0',
                                                   'DP': '74',
                                                   'GQ': '51',
                                                   'PL': '0,51,1827'},
                                         'XG302': {'GT': '0/1',
                                                   'AD': '51,8',
                                                   'DP': '59',
                                                   'GQ': '32',
                                                   'PL': '32,0,1388'},
                                         'XG303': {'GT': '0/0',
                                                   'AD': '47,0',
                                                   'DP': '47',
                                                   'GQ': '99',
                                                   'PL': '0,114,1353'},
                                         'XG304': {'GT': '0/0',
                                                   'AD': '74,0',
                                                   'DP': '74',
                                                   'GQ': '51',
                                                   'PL': '0,51,1827'},
                                         'XG402': {'GT': '0/1',
                                                   'AD': '51,8',
                                                   'DP': '59',
                                                   'GQ': '32',
                                                   'PL': '32,0,1388'},
                                         'XG403': {'GT': '0/0',
                                                   'AD': '47,0',
                                                   'DP': '47',
                                                   'GQ': '99',
                                                   'PL': '0,114,1353'},
                                         'XG404': {'GT': '0/0',
                                                   'AD': '74,0',
                                                   'DP': '74',
                                                   'GQ': '51',
                                                   'PL': '0,51,1827'}}},
                             {'CHROM': '12',
                              'POS': '81444551',
                              'ID': 'rs10746177',
                              'REF': 'T',
                              'ALT': 'C',
                              'QUAL': '5022.69',
                              'FILTER': 'PASS',
                              'INFO': 'AC=6;AF=1;AN=6;DP=185;ExcessHet=3.0103;FS=0;MLEAC=6;MLEAF=1;MQ=59.95;QD=27.3;SOR=1.042;VQSLOD=4.51;culprit=QD;DB;POSITIVE_TRAIN_SITE;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=LIN7A,ACSS3;GeneDetail.refGene=dist=112857,dist=27258;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intronic;Gene.ensGene=ENSG00000111058;GeneDetail.ensGene=.;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=12q21.31;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=0.9998;1000g2015aug_afr=0.9992;1000g2015aug_amr=1;1000g2015aug_eur=1;1000g2015aug_sas=1;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=rs10746177;avsnp150=rs10746177;CADD13_RawScore=-0.101662;CADD13_PHRED=1.718;Eigen=-0.4730;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.9988;gnomAD_genome_AFR=0.9961;gnomAD_genome_AMR=1;gnomAD_genome_ASJ=1;gnomAD_genome_EAS=1;gnomAD_genome_FIN=1;gnomAD_genome_NFE=0.9998;gnomAD_genome_OTH=1;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=0.953358;Kaviar_AC=24814;Kaviar_AN=26028;ALLELE_END',
                              'SAMPLE': {'XG102': {'GT': '1/1',
                                                   'AD': '0,72',
                                                   'DP': '72',
                                                   'GQ': '99',
                                                   'PL': '1905,214,0'},
                                         'XG103': {'GT': '1/1',
                                                   'AD': '0,56',
                                                   'DP': '56',
                                                   'GQ': '99',
                                                   'PL': '1568,168,0'},
                                         'XG104': {'GT': '1/1',
                                                   'AD': '0,56',
                                                   'DP': '56',
                                                   'GQ': '99',
                                                   'PL': '1563,168,0'},
                                         'XG202': {'GT': '1/1',
                                                   'AD': '0,72',
                                                   'DP': '72',
                                                   'GQ': '99',
                                                   'PL': '1905,214,0'},
                                         'XG203': {'GT': '1/1',
                                                   'AD': '0,56',
                                                   'DP': '56',
                                                   'GQ': '99',
                                                   'PL': '1568,168,0'},
                                         'XG204': {'GT': '1/1',
                                                   'AD': '0,56',
                                                   'DP': '56',
                                                   'GQ': '99',
                                                   'PL': '1563,168,0'},
                                         'XG302': {'GT': '1/1',
                                                   'AD': '0,72',
                                                   'DP': '72',
                                                   'GQ': '99',
                                                   'PL': '1905,214,0'},
                                         'XG303': {'GT': '1/1',
                                                   'AD': '0,56',
                                                   'DP': '56',
                                                   'GQ': '99',
                                                   'PL': '1568,168,0'},
                                         'XG304': {'GT': '1/1',
                                                   'AD': '0,56',
                                                   'DP': '56',
                                                   'GQ': '99',
                                                   'PL': '1563,168,0'},
                                         'XG402': {'GT': '1/1',
                                                   'AD': '0,72',
                                                   'DP': '72',
                                                   'GQ': '99',
                                                   'PL': '1905,214,0'},
                                         'XG403': {'GT': '1/1',
                                                   'AD': '0,56',
                                                   'DP': '56',
                                                   'GQ': '99',
                                                   'PL': '1568,168,0'},
                                         'XG404': {'GT': '1/1',
                                                   'AD': '0,56',
                                                   'DP': '56',
                                                   'GQ': '99',
                                                   'PL': '1563,168,0'}}}]
        value = self.mini_project1.read_vcf_file('two_variants.vcf')
        self.assertEqual(expected_solution, value)

    @weight(6)
    @visibility('visible')
    @number("6")
    def test_extract_info_field(self):
        expected_result = open('info_field.vcf', 'r').readline().strip()
        value = self.mini_project1.extract_info_field(
            self.mini_project1.read_vcf_file('two_variants.vcf'))
        self.assertEqual(expected_result, value[0])

    @weight(10)
    @visibility('visible')
    @number("7")
    def test_create_dictionary_of_info_field_value(self):
        data = self.mini_project1.read_vcf_file('two_variants.vcf')
        info_field = self.mini_project1.extract_info_field(data)
        expected_result = {'AC': ['1', '6'], 'AF': ['0.167', '1'], 'AN': ['6'], 'BaseQRankSum': ['-2.542'], 'ClippingRankSum': ['0'], 'DP': ['180', '185'], 'ExcessHet': ['3.0103'], 'FS': ['0'], 'MLEAC': ['1', '6'], 'MLEAF': ['0.167', '1'], 'MQ': ['52.77', '59.95'], 'MQRankSum': ['-4.631'], 'QD': ['0.39', '27.3'], 'ReadPosRankSum': ['1.45'], 'SOR': ['0.758', '1.042'], 'VQSLOD': ['-8.209', '4.51'], 'culprit': ['MQ', 'QD'], 'ANNOVAR_DATE': ['2018-04-16'], 'Func.refGene': ['intergenic'], 'Gene.refGene': ['IL2,IL21', 'LIN7A,ACSS3'], 'GeneDetail.refGene': ['dist=38536,dist=117597', 'dist=112857,dist=27258'], 'Func.ensGene': ['intergenic', 'intronic'], 'Gene.ensGene': ['ENSG00000109471,ENSG00000138684', 'ENSG00000111058'], 'GeneDetail.ensGene': [
            'dist=38306,dist=117597'], 'cytoBand': ['4q27', '12q21.31'], 'CADD13_RawScore': ['0.015973', '-0.101662'], 'CADD13_PHRED': ['2.741', '1.718'], 'Eigen': ['-0.3239', '-0.4730'], 'gnomAD_genome_ALL': ['0.0003', '0.9988'], 'gnomAD_genome_AFR': ['0.0001', '0.9961'], 'gnomAD_genome_AMR': ['0', '1'], 'gnomAD_genome_ASJ': ['0', '1'], 'gnomAD_genome_EAS': ['0.0007', '1'], 'gnomAD_genome_FIN': ['0.0009', '1'], 'gnomAD_genome_NFE': ['0.0002', '0.9998'], 'gnomAD_genome_OTH': ['0.0011', '1'], '1000g2015aug_all': ['0.9998'], '1000g2015aug_afr': ['0.9992'], '1000g2015aug_amr': ['1'], '1000g2015aug_eur': ['1'], '1000g2015aug_sas': ['1'], 'snp138NonFlagged': ['rs10746177'], 'avsnp150': ['rs10746177'], 'Kaviar_AF': ['0.953358'], 'Kaviar_AC': ['24814'], 'Kaviar_AN': ['26028']}
        value = self.mini_project1.create_dictionary_of_info_field_values(info_field)
        self.assertEqual(expected_result, value)

    @weight(10)
    @visibility('visible')
    @number("8")
    def test_determine_data_type_of_info_fields(self):
        data = {'key1': ['1', '2', '3'], 'key2': ['1.1', '2.2', '3.3'], 'key3': ['1.1', '2', '3.3'], 'key4': ['1.1', '234String', '3.3']}
        expected_result = {'key1': int, 'key2': float, 'key3': float, 'key4': str}
        value = self.mini_project1.determine_data_type_of_info_fields(data)
        self.assertEqual(expected_result, value)

    @weight(10)
    @visibility('visible')
    @number("9")
    def test_load_data_from_json(self):
        expected_result = {'key1': ['1', '2', '3'], 'key2': ['1.1', '2.2', '3.3'], 'key3': ['1.1', '2', '3.3'], 'key4': ['1.1', '234String', '3.3']}
        self.mini_project1.save_data_as_json(expected_result, 'test_save.json')
        value = self.mini_project1.load_data_from_json('test_save.json')
        self.assertEqual(expected_result, value)

    @weight(20)
    @visibility('visible')
    @number("10.1")
    def test_find_variant_1(self):
        filename = 'mini_project1_data.vcf'
        data = self.mini_project1.read_vcf_file(filename)  # read vcf file
        info_field_data = self.mini_project1.extract_info_field(data)  # extract all the info fields
        info_field_list = self.mini_project1.create_dictionary_of_info_field_values(info_field_data)  # create dictionary from info fields
        info_field_data_type = self.mini_project1.determine_data_type_of_info_fields(info_field_list)  # Determine data type of each info field
        data = self.mini_project1.format_data(data, info_field_data_type)  # format the data variable -- from data = read_vcf_file(filename)
        self.mini_project1.save_data_as_json(data, 'mini_project1_data.json')  # save the formatted data

        # Now I will fetch variants using your find_variant function
        # and check that they match my results

        value = self.mini_project1.find_variant("13", "T", "G", 56292303, 'mini_project1_data.json')
        expected_result = [{'ALT': 'G', 'CHROM': '13', 'FILTER': 'PASS', 'ID': 'rs4421887', 'INFO': {'1000g2015aug_afr': 0.8313, '1000g2015aug_all': 0.952676, '1000g2015aug_amr': 0.9841, '1000g2015aug_eur': 1.0, '1000g2015aug_sas': 0.9969, 'AC': 6, 'AF': 1.0, 'AN': 6, 'ANNOVAR_DATE': '2018-04-16', 'BaseQRankSum': 1.77, 'CADD13_PHRED': 3.712, 'CADD13_RawScore': 0.109684, 'ClippingRankSum': 0, 'DP': 176, 'Eigen': -0.7945, 'ExcessHet': 3.0103, 'FS': 0.0, 'Func.ensGene': 'intergenic', 'Func.refGene': 'intergenic', 'Gene.ensGene': 'ENSG00000264387,ENSG00000228611', 'Gene.refGene': 'MIR5007,PRR20D', 'GeneDetail.ensGene': 'dist=543620,dist=281031', 'GeneDetail.refGene': 'dist=543620,dist=1422749', 'Kaviar_AC': 3, 'Kaviar_AF': 0.0001153, 'Kaviar_AN': 26028, 'MLEAC': 6, 'MLEAF': 1.0, 'MQ': 60.0, 'MQRankSum': 0.0, 'QD': 28.95, 'ReadPosRankSum': -0.338, 'SOR': 0.257, 'VQSLOD': 22.53, 'avsnp150': 'rs4421887', 'culprit': 'MQ', 'cytoBand': '13q21.1', 'gnomAD_genome_AFR': 0.8475, 'gnomAD_genome_ALL': 0.9546, 'gnomAD_genome_AMR': 0.9843, 'gnomAD_genome_ASJ': 0.9834, 'gnomAD_genome_EAS': 1.0, 'gnomAD_genome_FIN': 0.9951,
                                                                                                     'gnomAD_genome_NFE': 0.9987, 'gnomAD_genome_OTH': 0.9887, 'snp138NonFlagged': 'rs4421887'}, 'POS': 56292303, 'QUAL': 5037.69, 'REF': 'T', 'SAMPLE': {'XG102': {'AD': '0,62', 'DP': '62', 'GQ': '99', 'GT': '1/1', 'PL': '1796,185,0'}, 'XG103': {'AD': '0,41', 'DP': '41', 'GQ': '99', 'GT': '1/1', 'PL': '1218,122,0'}, 'XG104': {'AD': '1,70', 'DP': '71', 'GQ': '99', 'GT': '1/1', 'PL': '2037,202,0'}, 'XG202': {'AD': '0,62', 'DP': '62', 'GQ': '99', 'GT': '1/1', 'PL': '1796,185,0'}, 'XG203': {'AD': '0,41', 'DP': '41', 'GQ': '99', 'GT': '1/1', 'PL': '1218,122,0'}, 'XG204': {'AD': '1,70', 'DP': '71', 'GQ': '99', 'GT': '1/1', 'PL': '2037,202,0'}, 'XG302': {'AD': '0,62', 'DP': '62', 'GQ': '99', 'GT': '1/1', 'PL': '1796,185,0'}, 'XG303': {'AD': '0,41', 'DP': '41', 'GQ': '99', 'GT': '1/1', 'PL': '1218,122,0'}, 'XG304': {'AD': '1,70', 'DP': '71', 'GQ': '99', 'GT': '1/1', 'PL': '2037,202,0'}, 'XG402': {'AD': '0,62', 'DP': '62', 'GQ': '99', 'GT': '1/1', 'PL': '1796,185,0'}, 'XG403': {'AD': '0,41', 'DP': '41', 'GQ': '99', 'GT': '1/1', 'PL': '1218,122,0'}, 'XG404': {'AD': '1,70', 'DP': '71', 'GQ': '99', 'GT': '1/1', 'PL': '2037,202,0'}}}]
        self.assertEqual(expected_result, value)

    @weight(20)
    @visibility('visible')
    @number("10.2")
    def test_find_variant_2(self):
        filename = 'mini_project1_data.vcf'
        data = self.mini_project1.read_vcf_file(filename)  # read vcf file
        info_field_data = self.mini_project1.extract_info_field(data)  # extract all the info fields
        info_field_list = self.mini_project1.create_dictionary_of_info_field_values(info_field_data)  # create dictionary from info fields
        info_field_data_type = self.mini_project1.determine_data_type_of_info_fields(info_field_list)  # Determine data type of each info field
        data = self.mini_project1.format_data(data, info_field_data_type)  # format the data variable -- from data = read_vcf_file(filename)
        self.mini_project1.save_data_as_json(data, 'mini_project1_data.json')  # save the formatted data

        # Now I will fetch variants using your find_variant function
        # and check that they match my results

        value = self.mini_project1.find_variant("18", "T", "C", 49338409, 'mini_project1_data.json')
        expected_result = [{'ALT': 'C', 'CHROM': '18', 'FILTER': 'PASS', 'ID': 'rs75100641', 'INFO': {'1000g2015aug_afr': 0.0136, '1000g2015aug_all': 0.0461262, '1000g2015aug_amr': 0.0086, '1000g2015aug_eur': 0.0249, '1000g2015aug_sas': 0.0838, 'AC': 2, 'AF': 0.333, 'AN': 6, 'ANNOVAR_DATE': '2018-04-16', 'BaseQRankSum': 0.462, 'CADD13_PHRED': 1.888, 'CADD13_RawScore': -0.079391, 'ClippingRankSum': 0, 'DP': 189, 'Eigen': -0.1036, 'ExcessHet': 3.9794, 'FS': 2.119, 'Func.ensGene': 'intergenic', 'Func.refGene': 'intergenic', 'Gene.ensGene': 'ENSG00000265712,ENSG00000215457', 'Gene.refGene': 'LOC100287225,DCC', 'GeneDetail.ensGene': 'dist=123830,dist=32968', 'GeneDetail.refGene': 'dist=249570,dist=528133', 'Kaviar_AC': 816, 'Kaviar_AF': 0.0313509, 'Kaviar_AN': 26028, 'MLEAC': 2, 'MLEAF': 0.333, 'MQ': 60.0, 'MQRankSum': 0.0, 'QD': 13.33, 'ReadPosRankSum': 0.592, 'SOR': 0.89, 'VQSLOD': 22.2, 'avsnp150': 'rs75100641', 'culprit': 'MQ', 'cytoBand': '18q21.2', 'gnomAD_genome_AFR': 0.0147, 'gnomAD_genome_ALL': 0.0225, 'gnomAD_genome_AMR': 0.0155, 'gnomAD_genome_ASJ': 0.0265, 'gnomAD_genome_EAS': 0.1005, 'gnomAD_genome_FIN': 0.0097,
                                                                                                      'gnomAD_genome_NFE': 0.0217, 'gnomAD_genome_OTH': 0.0255, 'snp138NonFlagged': 'rs75100641'}, 'POS': 49338409, 'QUAL': 1893.12, 'REF': 'T', 'SAMPLE': {'XG102': {'AD': '29,44', 'DP': '73', 'GQ': '99', 'GT': '0/1', 'PL': '1066,0,631'}, 'XG103': {'AD': '35,34', 'DP': '69', 'GQ': '99', 'GT': '0/1', 'PL': '838,0,805'}, 'XG104': {'AD': '47,0', 'DP': '47', 'GQ': '99', 'GT': '0/0', 'PL': '0,113,1504'}, 'XG202': {'AD': '29,44', 'DP': '73', 'GQ': '99', 'GT': '0/1', 'PL': '1066,0,631'}, 'XG203': {'AD': '35,34', 'DP': '69', 'GQ': '99', 'GT': '0/1', 'PL': '838,0,805'}, 'XG204': {'AD': '47,0', 'DP': '47', 'GQ': '99', 'GT': '0/0', 'PL': '0,113,1504'}, 'XG302': {'AD': '29,44', 'DP': '73', 'GQ': '99', 'GT': '0/1', 'PL': '1066,0,631'}, 'XG303': {'AD': '35,34', 'DP': '69', 'GQ': '99', 'GT': '0/1', 'PL': '838,0,805'}, 'XG304': {'AD': '47,0', 'DP': '47', 'GQ': '99', 'GT': '0/0', 'PL': '0,113,1504'}, 'XG402': {'AD': '29,44', 'DP': '73', 'GQ': '99', 'GT': '0/1', 'PL': '1066,0,631'}, 'XG403': {'AD': '35,34', 'DP': '69', 'GQ': '99', 'GT': '0/1', 'PL': '838,0,805'}, 'XG404': {'AD': '47,0', 'DP': '47', 'GQ': '99', 'GT': '0/0', 'PL': '0,113,1504'}}}]
        self.assertEqual(expected_result, value)

    @weight(20)
    @visibility('visible')
    @number("10.3")
    def test_find_variant_3(self):
        filename = 'mini_project1_data.vcf'
        data = self.mini_project1.read_vcf_file(filename)  # read vcf file
        info_field_data = self.mini_project1.extract_info_field(data)  # extract all the info fields
        info_field_list = self.mini_project1.create_dictionary_of_info_field_values(info_field_data)  # create dictionary from info fields
        info_field_data_type = self.mini_project1.determine_data_type_of_info_fields(info_field_list)  # Determine data type of each info field
        data = self.mini_project1.format_data(data, info_field_data_type)  # format the data variable -- from data = read_vcf_file(filename)
        self.mini_project1.save_data_as_json(data, 'mini_project1_data.json')  # save the formatted data

        # Now I will fetch variants using your find_variant function
        # and check that they match my results

        value = self.mini_project1.find_variant("10", "CT", "C", 80242879, 'mini_project1_data.json')
        expected_result = [{'ALT': 'C', 'CHROM': '10', 'FILTER': 'PASS', 'ID': '.', 'INFO': {'AC': 2, 'AF': 0.333, 'AN': 6, 'ANNOVAR_DATE': '2018-04-16', 'BaseQRankSum': 1.99, 'ClippingRankSum': 0, 'DP': 183, 'ExcessHet': 3.9794, 'FS': 2.263, 'Func.ensGene': 'ncRNA_intronic', 'Func.refGene': 'intergenic', 'Gene.ensGene': 'ENSG00000230417', 'Gene.refGene': 'LINC00595,ZMIZ1-AS1', 'GeneDetail.refGene': 'dist=202910,dist=460203', 'Kaviar_AC': 3, 'Kaviar_AF': 0.0001153, 'Kaviar_AN': 26028, 'MLEAC': 2, 'MLEAF': 0.333, 'MQ': 60.0, 'MQRankSum': 0.0, 'QD': 12.24, 'ReadPosRankSum': 1.19, 'SOR': 0.686, 'VQSLOD': 21.46, 'avsnp150': 'rs1046715494', 'culprit': 'MQRankSum', 'cytoBand': '10q22.3', 'gnomAD_genome_AFR': 0.0, 'gnomAD_genome_ALL': 6.471e-05, 'gnomAD_genome_AMR': 0.0, 'gnomAD_genome_ASJ': 0.0033, 'gnomAD_genome_EAS': 0.0, 'gnomAD_genome_FIN': 0.0, 'gnomAD_genome_NFE': 6.676e-05, 'gnomAD_genome_OTH': 0.0}, 'POS': 80242879, 'QUAL': 1567.12, 'REF': 'CT', 'SAMPLE': {'XG102': {
            'AD': '19,41', 'DP': '60', 'GQ': '99', 'GT': '0/1', 'PL': '1231,0,457'}, 'XG103': {'AD': '52,16', 'DP': '68', 'GQ': '99', 'GT': '0/1', 'PL': '347,0,1536'}, 'XG104': {'AD': '54,0', 'DP': '54', 'GQ': '99', 'GT': '0/0', 'PL': '0,120,1800'}, 'XG202': {'AD': '19,41', 'DP': '60', 'GQ': '99', 'GT': '0/1', 'PL': '1231,0,457'}, 'XG203': {'AD': '52,16', 'DP': '68', 'GQ': '99', 'GT': '0/1', 'PL': '347,0,1536'}, 'XG204': {'AD': '54,0', 'DP': '54', 'GQ': '99', 'GT': '0/0', 'PL': '0,120,1800'}, 'XG302': {'AD': '19,41', 'DP': '60', 'GQ': '99', 'GT': '0/1', 'PL': '1231,0,457'}, 'XG303': {'AD': '52,16', 'DP': '68', 'GQ': '99', 'GT': '0/1', 'PL': '347,0,1536'}, 'XG304': {'AD': '54,0', 'DP': '54', 'GQ': '99', 'GT': '0/0', 'PL': '0,120,1800'}, 'XG402': {'AD': '19,41', 'DP': '60', 'GQ': '99', 'GT': '0/1', 'PL': '1231,0,457'}, 'XG403': {'AD': '52,16', 'DP': '68', 'GQ': '99', 'GT': '0/1', 'PL': '347,0,1536'}, 'XG404': {'AD': '54,0', 'DP': '54', 'GQ': '99', 'GT': '0/0', 'PL': '0,120,1800'}}}]
        self.assertEqual(expected_result, value)

    @weight(20)
    @visibility('visible')
    @number("11.1")
    def test_pull_basic_and_predictor_fields(self):
        filename = 'mini_project1_data.json'
        value = self.mini_project1.pull_basic_and_predictor_fields(filename)

        expected_result = [
            {
                "FATHMM_pred": "T",
                "LRT_pred": "D",
                "MetaLR_pred": "D",
                "MetaSVM_pred": "D",
                "MutationAssessor_pred": "H",
                "MutationTaster_pred": "D",
                "PROVEAN_pred": "D",
                "Polyphen2_HDIV_pred": "D",
                "Polyphen2_HVAR_pred": "D",
                "SIFT_pred": "D",
                "sum_predictor_values": 9,
                "CHROM": "7",
                "POS": 87837848,
                "REF": "C",
                "ALT": "A"
            },
            {
                "FATHMM_pred": "T",
                "LRT_pred": "N",
                "MetaLR_pred": "T",
                "MetaSVM_pred": "T",
                "MutationAssessor_pred": "N",
                "MutationTaster_pred": "P",
                "PROVEAN_pred": "N",
                "Polyphen2_HDIV_pred": "B",
                "Polyphen2_HVAR_pred": "B",
                "SIFT_pred": "T",
                "sum_predictor_values": 0,
                "CHROM": "22",
                "POS": 50278568,
                "REF": "A",
                "ALT": "G"
            },
            {
                "FATHMM_pred": "T",
                "LRT_pred": "N",
                "MetaLR_pred": "T",
                "MetaSVM_pred": "T",
                "MutationAssessor_pred": "N",
                "MutationTaster_pred": "N",
                "PROVEAN_pred": "N",
                "Polyphen2_HDIV_pred": "B",
                "Polyphen2_HVAR_pred": "B",
                "SIFT_pred": "T",
                "sum_predictor_values": 0,
                "CHROM": "2",
                "POS": 85843431,
                "REF": "C",
                "ALT": "T"
            }
        ]
        print("expected result and value assert after this line ...")
        print(expected_result)
        self.assertEqual(expected_result, value)


    @weight(40)
    @visibility('visible')
    @number("12.1")
    def test_pull_basic_and_predictor_fields_gzip(self):
        import json
        filename = 'test_4families_annovar.vcf.gz'
        
        if os.path.exists('mini_project1_gzip.json'):
            os.remove('mini_project1_gzip.json')
        self.mini_project1.pull_basic_and_predictor_fields_gzip(filename)
        expected_result = json.load(open('expected_mini_project1_gzip.json'))
        value = json.load(open('mini_project1_gzip.json'))
        self.assertEqual(expected_result, value)


    @weight(20)
    @visibility('visible')
    @number("13.1")
    def test_return_all_non_zero_sum_predictor_values(self):
        import json
        
        if os.path.exists('sum_predictor_values_gt_zero.json'):
            os.remove('sum_predictor_values_gt_zero.json')
        self.mini_project1.return_all_non_zero_sum_predictor_values()
        expected_result = json.load(open('expected_sum_predictor_values_gt_zero.json'))
        value = json.load(open('sum_predictor_values_gt_zero.json'))
        
        self.assertEqual(expected_result, value)