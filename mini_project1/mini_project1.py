def determine_data_type(value):
    """
    The function takes a string input and determines its data type to be either a float, int, or string. 
    """
    # BEGIN SOLUTION
    try:
        int(value)
        return int
    except ValueError:
        try:
            float(value)
            return float
        except ValueError:
            return str

    # END SOLUTION

def determine_data_type_of_list(values):
    """
    Write a function whose input is a list of strings. 
    This function determines the correct data type of all the elements in the list. 
    For example, ['1', '2', '3'] is int, ['1.1', '2.2', '3.3'] is float, ['1.1', '2', '3.3'] 
    is also float, and ['1.1', '234String', '3.3'] is str. 
    The purpose of this function to figure out what to cast an array of strings to. 
    Some lists might be all ints, in which case the data type is int. 
    Some might be a mixture of ints and floats, in which case the data type will be a float. 
    Some lists might be a mixture of ints, floats, and strings, 
    in which case the data type of the list will be a string.
    NOTE: This function should use "determine_data_type" function you coded previously

    """
    # BEGIN SOLUTION
    types = set()
    for value in values:
        types.add(determine_data_type(value))
    if len(types) == 1:
        return types.pop()
    elif all(t in (int, float) for t in types):
        return float
    else:
        return str

    # END SOLUTION


def format_sample_fields(format_field, sample_field):
    """
    Write a function whose inputs are a format field and sample field. 
    The format field looks like format_field = 'GT:AD:DP:GQ:PGT:PID:PL' and 
    the sample field looks like

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

    Transform the inputs such that the output looks like this:

    output = {
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
    """

    # BEGIN SOLUTION
    formatFieldData= format_field.split(':')
    finalOutputDict = {}

    for id, data in sample_field.items():
        sampleFieldData = data.split(':')
        sample_output = {}
        for tag, value in zip(formatFieldData, sampleFieldData):
            sample_output[tag] = value
        finalOutputDict[id] = sample_output
    return finalOutputDict

    # END SOLUTION


def create_dict_from_line(header, line):
    """
    Given the header and a single line, transform them into dictionary as described above. 
    Header and line input are provided in this cell. 

    Write a function whose inputs are a list containing the vcf header and a variant line. 
    The function should return a dictionary using the header as keys and the variant line as values.
     The function should use the format_sample_fields you wrote previously to format the sample fields. 
     The output of the first line looks like this:

    {'ALT': 'G',
    'CHROM': '4',
    'FILTER': 'PASS',
    'ID': '.',
    'INFO': 'AC=1;AF=0.167;AN=6;BaseQRankSum=-2.542;ClippingRankSum=0;DP=180;ExcessHet=3.0103;FS=0;MLEAC=1;MLEAF=0.167;MQ=52.77;MQRankSum=-4.631;QD=0.39;ReadPosRankSum=1.45;SOR=0.758;VQSLOD=-8.209;culprit=MQ;ANNOVAR_DATE=2018-04-16;Func.refGene=intergenic;Gene.refGene=IL2,IL21;GeneDetail.refGene=dist=38536,dist=117597;ExonicFunc.refGene=.;AAChange.refGene=.;Func.ensGene=intergenic;Gene.ensGene=ENSG00000109471,ENSG00000138684;GeneDetail.ensGene=dist=38306,dist=117597;ExonicFunc.ensGene=.;AAChange.ensGene=.;cytoBand=4q27;gwasCatalog=.;tfbsConsSites=.;wgRna=.;targetScanS=.;Gene_symbol=.;OXPHOS_Complex=.;Ensembl_Gene_ID=.;Ensembl_Protein_ID=.;Uniprot_Name=.;Uniprot_ID=.;NCBI_Gene_ID=.;NCBI_Protein_ID=.;Gene_pos=.;AA_pos=.;AA_sub=.;Codon_sub=.;dbSNP_ID=.;PhyloP_46V=.;PhastCons_46V=.;PhyloP_100V=.;PhastCons_100V=.;SiteVar=.;PolyPhen2_prediction=.;PolyPhen2_score=.;SIFT_prediction=.;SIFT_score=.;FatHmm_prediction=.;FatHmm_score=.;PROVEAN_prediction=.;PROVEAN_score=.;MutAss_prediction=.;MutAss_score=.;EFIN_Swiss_Prot_Score=.;EFIN_Swiss_Prot_Prediction=.;EFIN_HumDiv_Score=.;EFIN_HumDiv_Prediction=.;CADD_score=.;CADD_Phred_score=.;CADD_prediction=.;Carol_prediction=.;Carol_score=.;Condel_score=.;Condel_pred=.;COVEC_WMV=.;COVEC_WMV_prediction=.;PolyPhen2_score_transf=.;PolyPhen2_pred_transf=.;SIFT_score_transf=.;SIFT_pred_transf=.;MutAss_score_transf=.;MutAss_pred_transf=.;Perc_coevo_Sites=.;Mean_MI_score=.;COSMIC_ID=.;Tumor_site=.;Examined_samples=.;Mutation_frequency=.;US=.;Status=.;Associated_disease=.;Presence_in_TD=.;Class_predicted=.;Prob_N=.;Prob_P=.;SIFT_score=.;SIFT_converted_rankscore=.;SIFT_pred=.;Polyphen2_HDIV_score=.;Polyphen2_HDIV_rankscore=.;Polyphen2_HDIV_pred=.;Polyphen2_HVAR_score=.;Polyphen2_HVAR_rankscore=.;Polyphen2_HVAR_pred=.;LRT_score=.;LRT_converted_rankscore=.;LRT_pred=.;MutationTaster_score=.;MutationTaster_converted_rankscore=.;MutationTaster_pred=.;MutationAssessor_score=.;MutationAssessor_score_rankscore=.;MutationAssessor_pred=.;FATHMM_score=.;FATHMM_converted_rankscore=.;FATHMM_pred=.;PROVEAN_score=.;PROVEAN_converted_rankscore=.;PROVEAN_pred=.;VEST3_score=.;VEST3_rankscore=.;MetaSVM_score=.;MetaSVM_rankscore=.;MetaSVM_pred=.;MetaLR_score=.;MetaLR_rankscore=.;MetaLR_pred=.;M-CAP_score=.;M-CAP_rankscore=.;M-CAP_pred=.;CADD_raw=.;CADD_raw_rankscore=.;CADD_phred=.;DANN_score=.;DANN_rankscore=.;fathmm-MKL_coding_score=.;fathmm-MKL_coding_rankscore=.;fathmm-MKL_coding_pred=.;Eigen_coding_or_noncoding=.;Eigen-raw=.;Eigen-PC-raw=.;GenoCanyon_score=.;GenoCanyon_score_rankscore=.;integrated_fitCons_score=.;integrated_fitCons_score_rankscore=.;integrated_confidence_value=.;GERP++_RS=.;GERP++_RS_rankscore=.;phyloP100way_vertebrate=.;phyloP100way_vertebrate_rankscore=.;phyloP20way_mammalian=.;phyloP20way_mammalian_rankscore=.;phastCons100way_vertebrate=.;phastCons100way_vertebrate_rankscore=.;phastCons20way_mammalian=.;phastCons20way_mammalian_rankscore=.;SiPhy_29way_logOdds=.;SiPhy_29way_logOdds_rankscore=.;Interpro_domain=.;GTEx_V6_gene=.;GTEx_V6_tissue=.;esp6500siv2_all=.;esp6500siv2_aa=.;esp6500siv2_ea=.;ExAC_ALL=.;ExAC_AFR=.;ExAC_AMR=.;ExAC_EAS=.;ExAC_FIN=.;ExAC_NFE=.;ExAC_OTH=.;ExAC_SAS=.;ExAC_nontcga_ALL=.;ExAC_nontcga_AFR=.;ExAC_nontcga_AMR=.;ExAC_nontcga_EAS=.;ExAC_nontcga_FIN=.;ExAC_nontcga_NFE=.;ExAC_nontcga_OTH=.;ExAC_nontcga_SAS=.;ExAC_nonpsych_ALL=.;ExAC_nonpsych_AFR=.;ExAC_nonpsych_AMR=.;ExAC_nonpsych_EAS=.;ExAC_nonpsych_FIN=.;ExAC_nonpsych_NFE=.;ExAC_nonpsych_OTH=.;ExAC_nonpsych_SAS=.;1000g2015aug_all=.;1000g2015aug_afr=.;1000g2015aug_amr=.;1000g2015aug_eur=.;1000g2015aug_sas=.;CLNALLELEID=.;CLNDN=.;CLNDISDB=.;CLNREVSTAT=.;CLNSIG=.;dbscSNV_ADA_SCORE=.;dbscSNV_RF_SCORE=.;snp138NonFlagged=.;avsnp150=.;CADD13_RawScore=0.015973;CADD13_PHRED=2.741;Eigen=-0.3239;REVEL=.;MCAP=.;Interpro_domain=.;ICGC_Id=.;ICGC_Occurrence=.;gnomAD_genome_ALL=0.0003;gnomAD_genome_AFR=0.0001;gnomAD_genome_AMR=0;gnomAD_genome_ASJ=0;gnomAD_genome_EAS=0.0007;gnomAD_genome_FIN=0.0009;gnomAD_genome_NFE=0.0002;gnomAD_genome_OTH=0.0011;gerp++gt2=.;cosmic70=.;InterVar_automated=.;PVS1=.;PS1=.;PS2=.;PS3=.;PS4=.;PM1=.;PM2=.;PM3=.;PM4=.;PM5=.;PM6=.;PP1=.;PP2=.;PP3=.;PP4=.;PP5=.;BA1=.;BS1=.;BS2=.;BS3=.;BS4=.;BP1=.;BP2=.;BP3=.;BP4=.;BP5=.;BP6=.;BP7=.;Kaviar_AF=.;Kaviar_AC=.;Kaviar_AN=.;ALLELE_END',
    'POS': '123416186',
    'QUAL': '23.25',
    'REF': 'A',
    'SAMPLE': {'XG102': {'AD': '51,8',
                      'DP': '59',
                      'GQ': '32',
                      'GT': '0/1',
                      'PL': '32,0,1388'},
            'XG103': {'AD': '47,0',
                      'DP': '47',
                      'GQ': '99',
                      'GT': '0/0',
                      'PL': '0,114,1353'},
            'XG104': {'AD': '74,0',
                      'DP': '74',
                      'GQ': '51',
                      'GT': '0/0',
                      'PL': '0,51,1827'},
            'XG202': {'AD': '51,8',
                      'DP': '59',
                      'GQ': '32',
                      'GT': '0/1',
                      'PL': '32,0,1388'},
            'XG203': {'AD': '47,0',
                      'DP': '47',
                      'GQ': '99',
                      'GT': '0/0',
                      'PL': '0,114,1353'},
            'XG204': {'AD': '74,0',
                      'DP': '74',
                      'GQ': '51',
                      'GT': '0/0',
                      'PL': '0,51,1827'},
            'XG302': {'AD': '51,8',
                      'DP': '59',
                      'GQ': '32',
                      'GT': '0/1',
                      'PL': '32,0,1388'},
            'XG303': {'AD': '47,0',
                      'DP': '47',
                      'GQ': '99',
                      'GT': '0/0',
                      'PL': '0,114,1353'},
            'XG304': {'AD': '74,0',
                      'DP': '74',
                      'GQ': '51',
                      'GT': '0/0',
                      'PL': '0,51,1827'},
            'XG402': {'AD': '51,8',
                      'DP': '59',
                      'GQ': '32',
                      'GT': '0/1',
                      'PL': '32,0,1388'},
            'XG403': {'AD': '47,0',
                      'DP': '47',
                      'GQ': '99',
                      'GT': '0/0',
                      'PL': '0,114,1353'},
            'XG404': {'AD': '74,0',
                      'DP': '74',
                      'GQ': '51',
                      'GT': '0/0',
                      'PL': '0,51,1827'}}}
    """
    # BEGIN SOLUTION
    sample_output = {}
    output = {}
    finalOutput = {}
    sample_list = line.split('\t')
    for keys, value in zip(header[9:], sample_list[9:]):
        sample_output[keys] = value
    output = format_sample_fields(sample_list[8], sample_output)
    for keys, values in zip(header[0:8], sample_list[0:8]):
        finalOutput[keys] = values
    finalOutput['SAMPLE'] = output
    return finalOutput


    # END SOLUTION

def read_vcf_file(filename):
    """
    Write a function whose input is a filename for a vcf. 
    The function reads the vcf file one variant at a time and transforms it 
    into a dictionary using the create_dict_from_line function. 
    It returns a list containing all the variant dictionaries. 
    NOTE: Your function should be able to handle multiple lines.
    """
    # BEGIN SOLUTION
    variant_dicts = []
    header = None
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('##'):
                continue
            elif line.startswith('#'): 
                header = line[1:].strip().split('\t')
            elif not line.startswith('#'):  
                variant_dict = create_dict_from_line(header, line.strip())
                variant_dicts.append(variant_dict)
    return variant_dicts
    # END SOLUTION


def extract_info_field(data):
    """
    Write a function that extracts the info field from the data dictionary that was 
    created in the previous part. The function should return all the info field dictionaries as list. 
    """
    # BEGIN SOLUTION
    info_dicts = []
    for variant_dict in data:
        if 'INFO' in variant_dict and variant_dict['INFO']:
            info_dicts.append(variant_dict['INFO'])
    return info_dicts

    # END SOLUTION


def create_dictionary_of_info_field_values(data):
    """
    You now need to figure out that data types for each of the info fields. Begin by writing a function that first takes the info fields and turns them into a dictionary. Make sure to skip any fields that do not have a value or are missing a value.

    Note: only return keys that have values! 
    """

    # BEGIN SOLUTION
    info_dict = {}
    for line in data:
        lineSplit = line.split(";")
        for item in lineSplit:
            key_val = item.split("=", 1)
            if len(key_val) == 2 and key_val[1] != ".":
                key = key_val[0]
                if key in info_dict and (key_val[1] in info_dict[key]) == False:
                    info_dict[key].append(key_val[1])
                else:
                    info_dict[key] = [key_val[1]]
    return info_dict

    # END SOLUTION


def determine_data_type_of_info_fields(data):
    """
    Write a function whose input is the output from create_dictionary_of_info_field_values 
    and uses the previously written function determine_data_type_of_list to determine 
    the data type of each of the info fields. The output is a dictionary whose 
    keys are the name of the info fields and values are the data type. 
    """
    # BEGIN SOLUTION
    dataType_dict = {}
    for key, value in data.items():
        data_type = determine_data_type_of_list(value)
        dataType_dict[key] = data_type
    return dataType_dict
    # END SOLUTION


def format_data(data, info_field_data_type):
    """
    Write a function whose first input is the data from read_vcf_file and 
    the second input is the output from determine_data_type_of_info_fields. 
    The function converts the info field into a dictionary and uses the data types 
    that you determined to cast each field into the correct data type. 
    Make sure to convert the POS to int and QUAL to float. 
    The output will look something like this (I have removed most of the fields):

    The output will look something like this

    {
            "ALT": "G",
            "CHROM": "4",
            "FILTER": "PASS",
            "ID": ".",
            "INFO": {

                "Gene.ensGene": "ENSG00000109471,ENSG00000138684",
                "Gene.refGene": "IL2,IL21",
                "GeneDetail.ensGene": "dist=38306,dist=117597",
                "GeneDetail.refGene": "dist=38536,dist=117597"
            },
            "POS": 123416186,
            "QUAL" :23.25,
            "REF": "A",
            "SAMPLE": {
                "XG102": {
                    "AD": "51,8",
                    "DP": "59",
                    "GQ": "32",
                    "GT": "0/1",
                    "PL": "32,0,1388"
                }
        }

    Additional hints: The function in part 9 takes in two inputs. 
    input #1 is all the data read from lab1_data.vcf and converted into a 
    list of dictionaries where each dictionary corresponds to a line in the vcf file. 
    input #2 is a dictionary that tells you what the data type of each of the info field is.

    The purpose of part 9 is update each of the fields in "data" input so 
    that the data type matches what you have determined it to be previously.
    POS is an integer and QUAL is a float. For the info fields, you have already 
    created a dictionary called info_field_data_type that contains the information 
    for the data type of each of the info field. Now use this to cast the info field 
    into the correct data types.

    And the info field goes from being a string to a nested dictionary.

    NOTE: You can only test this function in the last part! There are not tests for it    

    """
    # BEGIN SOLUTION
    formatted_data = []
    for line in data:
        line['POS'] = int(line['POS'])
        line['QUAL'] = float(line['QUAL'])
    
        info_fields = line['INFO'].strip().split(';')
        info_dict = {}
        for field in info_fields:
            field_value = field.split('=', 1)
            if len(field_value ) == 2:
                key = field_value[0]
                value = field_value[1]
            if key in info_field_data_type and value != ".":
                data_type = info_field_data_type[key]
                if data_type == int:
                    info_dict[key] = int(float(value))
                elif data_type == float:
                    info_dict[key] = float(value)
                else:
                 info_dict[key]= str(value)
        line['INFO'] = info_dict
        formatted_data.append(line)
    return formatted_data
    # END SOLUTION


def save_data_as_json2(data, filename):
    """
    Write a function whose inputs are a Python dictionary and filename. 
    The function will saves the dictionary as a json file using the filename given. 
    Use the json library. 
    Use these options to correctly format your JSON -- 
    sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False. 
    Use this function to save your parsed data as a json file.
    """
    # BEGIN SOLUTION
    import json
    with open(filename, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=2, separators=(',', ': '), ensure_ascii=False)

    # END SOLUTION

def save_data_as_json(data, filename):
    """
    Write a function whose inputs are a Python dictionary and filename. 
    The function will saves the dictionary as a json file using the filename given. 
    Use the json library. 
    Use these options to correctly format your JSON -- 
    sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False. 
    Use this function to save your parsed data as a json file.
    """
    # BEGIN SOLUTION
    import json
    with open(filename, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)

    # END SOLUTION


def load_data_from_json(filename):
    """
    Write a function whose input is a filename for a json file. 
    The function should use the filename to read the JSON file in 
    which you saved your final parsed data. 
    """
    # BEGIN SOLUTION
    import json
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
    # END SOLUTION


def find_variant(CHROM, REF, ALT, POS, filename):
    """
    Write a function whose inputs are CHROM, REF, ALT, POS, and filename. 
    Using these inputs, the function should load a JSON file using the given 
    filename and return a list of variants that match the given CHROM, REF, ALT, and POS. 
    """
    # BEGIN SOLUTION
    data = load_data_from_json(filename)
    variants = []
    for variant in data:
        if variant['CHROM'] == CHROM and variant['REF'] == REF and variant['ALT'] == ALT and variant['POS'] == POS:
            variants.append(variant)
    return variants
    # END SOLUTION

# pull_basic_and_predictor_fields('mini_project1_data.json') to process variant/record with at least one predictor
def pull_basic_and_predictor_fields(filename):
    """
    Load mini_project1_data.json and pull out all the variants that have  atleast one of the following predictor with value
    """
    # BEGIN SOLUTION
    predictors = ['FATHMM_pred', 'LRT_pred', 'MetaLR_pred', 'MetaSVM_pred', 'MutationAssessor_pred', 'MutationTaster_pred', 'PROVEAN_pred', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_pred', 'SIFT_pred']

    predictors_field = {
        'FATHMM_pred': {'T': 0, 'D': 1},
        'LRT_pred': {'D': 1, 'N': 0, 'U': 0},
        'MetaLR_pred': {'T': 0, 'D': 1},
        'MetaSVM_pred': {'T': 0, 'D': 1},
        'MutationAssessor_pred': {'H': 1, 'N': 0, 'L': 0.25, 'M': 0.5},
        'MutationTaster_pred': {'D': 1, 'P': 0, 'N': 0, 'A': 1},
        'PROVEAN_pred': {'D': 1, 'N': 0},
        'Polyphen2_HDIV_pred': {'D': 1, 'B': 0, 'P': 0.5},
        'Polyphen2_HVAR_pred': {'D': 1, 'B': 0, 'P': 0.5},
        'SIFT_pred': {'D': 1, 'T': 0}
    }
    additional_fields = ["CHROM", "POS", "REF", "ALT"]
    out = []
    data = load_data_from_json(filename)

    for d in data:
        is_all_predictors_present = True

        for predictor in predictors_field.keys():
            # check if predictor is present in the record and have a valid value
            if predictor not in d['INFO'] or d['INFO'].get(predictor) == '.':
                is_all_predictors_present = False
                # discard this data as all the predictors are not present
                break

        # if all the predictors are present, then add the data to the output
        if is_all_predictors_present:
            out_dict = {k:d['INFO'][k] for k in predictors}
            out_dict |= {"sum_predictor_values": sum([predictors_field[k][d['INFO'][k]] for k in predictors])}
            out_dict |= {k:d[k] for k in additional_fields}
            out.append(out_dict)
       
    return out
    # END SOLUTION

# pull_basic_and_predictor_fields('mini_project1_data.json') to process variant/record with all predictors
def pull_basic_and_predictor_fields_2(filename):
    """
    Load mini_project1_data.json and pull out all the variants that have  atleast one of the following predictor with value
    """
    # BEGIN SOLUTION
    predictors_field = {
        'FATHMM_pred': {'T': 0, 'D': 1},
        'LRT_pred': {'D': 1, 'N': 0, 'U': 0},
        'MetaLR_pred': {'T': 0, 'D': 1},
        'MetaSVM_pred': {'T': 0, 'D': 1},
        'MutationAssessor_pred': {'H': 1, 'N': 0, 'L': 0.25, 'M': 0.5},
        'MutationTaster_pred': {'D': 1, 'P': 0, 'N': 0, 'A': 1},
        'PROVEAN_pred': {'D': 1, 'N': 0},
        'Polyphen2_HDIV_pred': {'D': 1, 'B': 0, 'P': 0.5},
        'Polyphen2_HVAR_pred': {'D': 1, 'B': 0, 'P': 0.5},
        'SIFT_pred': {'D': 1, 'T': 0}
         
    }
    additional_fields = ["CHROM", "POS", "REF", "ALT"]
    # Return a list of dictionaries as final output
    out = []
    # Load the data from the json file
    data = load_data_from_json(filename)

    for d in data:
        predictor_list = []
        for predictor in predictors_field.keys():
            if predictor not in d['INFO'] or d['INFO'].get(predictor) == '.':
                continue
            predictor_list.append(predictor)
        # If no predictors found, skip this variant/data/record
        if not len(predictor_list):
            continue

        out_dict = {k:d['INFO'][k] for k in predictor_list}
        out_dict |= {"sum_predictor_values": sum([predictors_field[k][d['INFO'][k]] for k in predictor_list])}
        out_dict |= {k:d[k] for k in additional_fields}
        out_dict['POS'] = str(out_dict['POS'])
        out.append(out_dict)
       
    return out

    

def pull_basic_and_predictor_fields_gzip(filename):
#     # BEGIN SOLUTION
#     """
#     Load mini_project1_data.json.gz and pull out all the variants that have at least one predictor with value
#     """
    import gzip
    """
    Load test_4families_annovar.vcf.gz and pull out all the variants that have  atleast one of the following predictor with value
    """

    header = None
    header_line = []
    intermediate_transformed_file = 'intermediate_transformed_file.json'

    # Read the compressed file line by line and process it.
    with gzip.open(filename,'rt') as fp:
        for line in fp:
            line = line.strip()
            if(not line) or line.startswith('##'): continue
            elif(line.startswith('#')) and not header:
                header = line[1:].split('\t')
                continue

            header_line.append(create_dict_from_line(header, line))
    
    

    info_field_data = extract_info_field(header_line)
    info_field_values = create_dictionary_of_info_field_values(info_field_data)
    info_field_data_type = determine_data_type_of_info_fields(info_field_values)
    data = format_data(header_line, info_field_data_type)
    save_data_as_json(data, intermediate_transformed_file)

    # using other variant of pull_basic_and_predictor_fields which process data with at least one predictor
    output = pull_basic_and_predictor_fields_2(intermediate_transformed_file)

    out_file = 'mini_project1_gzip.json'
    save_data_as_json2(output, out_file)
    # END SOLUTION



def return_all_non_zero_sum_predictor_values():
    # BEGIN SOLUTION
    import json
    data = load_data_from_json('mini_project1_gzip.json')
    out_list = []
    for d in data:
        if d['sum_predictor_values'] != 0:
            out_list.append(d)

    # Save the output to a file named sum_predictor_values_gt_zero.json with indent=2 and sort_keys=True
    with open('sum_predictor_values_gt_zero.json', 'w') as f_out:
        json.dump(out_list, f_out, indent=2, sort_keys=True)

    # END SOLUTION
