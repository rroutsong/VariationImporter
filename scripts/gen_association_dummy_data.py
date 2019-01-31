import json
import random
from pprint import pprint as pp
from math import log10 as log10

# Association Data Bottom Up Approach

"""
    Generate four different location objections,
    with reasonable random latitudes, longitudes, and elevations
    lorem ipsum for description
"""

LI = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis ac orci sollicitudin, interdum felis eget, porta tortor. Vestibulum vitae libero molestie nulla accumsan viverra. Nullam tempor in ipsum ornare sollicitudin. Nullam a elit eget nulla vehicula venenatis. Cras mi dolor, rutrum tincidunt finibus at, eleifend at massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent a ante nisi. Proin aliquet massa in velit volutpat, sed maximus lectus imperdiet. Nam vel pellentesque libero, eget bibendum erat. Aenean purus leo, suscipit in nunc quis, congue porta libero. In sapien diam, sodales sed ligula quis, congue lobortis mi. Sed quis diam sed nibh commodo convallis imperdiet id libero.  
     """.strip()

"""
    Generate four different location objects, put into list
    floats are generated randomly within the natural confines of 
    number, and description is lorem ipsum
"""

locations = [] # hold dummy location values in list object
for x in range(0,3):
    random.seed((x+1)*12345)
    # maximum latitude is 90 degrees, minimum -90 degrees
    dummy_lat = round(random.uniform(-90.00, 90.00),6)
    # maximum longitude 180, minimum -180
    dummy_lon = round(random.uniform(-180.00, 180.00),6)
    """
        rounding to the 6th digit ensures accuracy with 0.1m
                decimal  degrees    distance
                places
                -------------------------------  
                0        1.0        111 km
                1        0.1        11.1 km
                2        0.01       1.11 km
                3        0.001      111 m
                4        0.0001     11.1 m
                5        0.00001    1.11 m
                6        0.000001   0.111 m
                7        0.0000001  1.11 cm
                8        0.00000001 1.11 mm
    """

    # dead sea = -413m below sea level, mt. everest 8850.0m above sea level
    # expressed in meters
    dummy_elev = round(random.uniform(-413.0, 8850.0),1)
    dummy_desc = LI

    dummy_loc = {
        'lat': dummy_lat,
        'lon': dummy_lon,
        'elevation': dummy_elev,
        'description': dummy_desc
    }

    locations.append(dummy_loc)

"""
    Generate four different straininfo objects,
    each containing a location object and a source_id of random text
"""

straininfos = []
for x in range(0,3):
    dummy_sourceid = hash('source_id'+str(x))
    dummy_source_info_loc = locations[x]

    dummy_sid = {
        'source_id': dummy_sourceid,
        'location_info': dummy_source_info_loc
    }

    straininfos.append(dummy_sid)

"""
    Generate one population object containing a list of the four straininfos
    and lorem ipsum for description
"""

population = {
    'strains':  straininfos,
    'description': LI
}

"""
    Generate sixteen different ontology info objects
    With simulated ontology ids and types
"""

ontology_infos = []

ontology_infos.append({ 'ontology_id': 'TO:0000315', 'ontology_type': 'trait ontology' })
ontology_infos.append({ 'ontology_id': 'PO:0000014', 'ontology_type': 'plant anatomy ontology' })
ontology_infos.append({ 'ontology_id': 'GO:9993940', 'ontology_type': 'gene ontology' })
ontology_infos.append({ 'ontology_id': 'ENVO_1000745', 'ontology_type': 'environment ontology' })
ontology_infos.append({ 'ontology_id': 'TO:0000315', 'ontology_type': 'trait ontology' })
ontology_infos.append({ 'ontology_id': 'PO:0000014', 'ontology_type': 'plant anatomy ontology' })
ontology_infos.append({ 'ontology_id': 'GO:9993940', 'ontology_type': 'gene ontology' })
ontology_infos.append({ 'ontology_id': 'ENVO_1000745', 'ontology_type': 'environment ontology' })
ontology_infos.append({ 'ontology_id': 'TO:0000315', 'ontology_type': 'trait ontology' })
ontology_infos.append({ 'ontology_id': 'PO:0000014', 'ontology_type': 'plant anatomy ontology' })
ontology_infos.append({ 'ontology_id': 'GO:9993940', 'ontology_type': 'gene ontology' })
ontology_infos.append({ 'ontology_id': 'ENVO_1000745', 'ontology_type': 'environment ontology' })
ontology_infos.append({ 'ontology_id': 'TO:0000315', 'ontology_type': 'trait ontology' })
ontology_infos.append({ 'ontology_id': 'PO:0000014', 'ontology_type': 'plant anatomy ontology' })
ontology_infos.append({ 'ontology_id': 'GO:9993940', 'ontology_type': 'gene ontology' })
ontology_infos.append({ 'ontology_id': 'ENVO_1000745', 'ontology_type': 'environment ontology' })


"""

    Generate sixteen different traitinfo objects,
    
    originator - random text - PI, lab or institution doing phenotype analysis
    trait_id - random FID (int between 4-5 characters - id of trait
    trait_ontology_id - string "TO" + random 7 numbers - trait ontology of trait
    trait_name - string "extraitname + #" - short trait name
    unit_of_measure - random of ["MEAN", "COUNT", "NUMDAYS"] unit of measurement of trait eg. MEAN, COUNT, NUMDAYS
    protocol - string LI - a brief protocol describing trait measurement
    comment - string LI - Comments or any other information related to the trait
    trait_measurements - list of values for each ecotype for a trait;
    
"""

def random_trait_id():
    range_start = 10**(5-1)
    range_end = (10**5)-1
    return "TO"+str(random.randint(range_start, range_end))

traitinfos = []
for x in range(0, 15):
    dummy_trait_id = random_trait_id()
    dummy_ontology_id = ontology_infos[0]['ontology_id']

    dummy_traitinfo = {
        'originator': "UT_ORNL",
        'trait_id': dummy_trait_id,
        "trait_ontology_id": dummy_ontology_id,
        "trait_name": "extraitname"+str(x),
        "unit_of_measure": str(random.choice(["MEAN", "COUNT", "NUMDAYS"])),
        "protocol": LI,
        "trait_measurements": [("MEASURE A", "VALUE A"), ("MEASURE B", "VALUE B"), ("MEASURE C", "VALUE C")],
        "comment": LI,
        "ontology": [ontology_infos[x]]
    }

    traitinfos.append(dummy_traitinfo)

"""

    Generate four different traits objects,
    
    genome - fake kbase reference - string genome;
    population - one of four fake population structures - Population population;
    Trait - list containing four of sixteen traitinfo structures - list<Traitinfo> Trait;


"""

traits = []
for x in range(0,3):
    if x == 0:
        traitlist = [traitinfos[0], traitinfos[1], traitinfos[2], traitinfos[3]]
    elif x == 1:
        traitlist = [traitinfos[4], traitinfos[5], traitinfos[6], traitinfos[7]]
    elif x == 2:
        traitlist = [traitinfos[8], traitinfos[9], traitinfos[10], traitinfos[11]]
    else:
        traitlist = [traitinfos[12], traitinfos[13], traitinfos[14], traitinfos[15]]


    dummy_traits = {
        'genome': '1/fake/3',
        'population': population,
        'Trait:': traitlist
    }

"""
    Create Traits json data
"""

with open('traits.json', 'w') as t:
    json.dump(traits, t)
    t.close()

"""

    Generate sixteen different snp_to_gene objects,

    gene_id - gene close to the snp - string "GO"+5 random numbers
    distance_from_snp - minimum distance of gene from the snp - int 10
    snp_relative_location - inside_gene, 5', 3'

"""

def random_gene_id():
    range_start = 10**(5-1)
    range_end = (10**5)-1
    return random.randint(range_start, range_end)

snptogenes = []
for x in range(0, 15):
    dummy_gene_id = random_gene_id()

    dummy_snp_to_gene = {
        'gene_id': dummy_gene_id,
        'distance_from_snp': 10,
        'snp_relative_location': "5'"
    }

    snptogenes.append(dummy_snp_to_gene)

"""

    Generate four different associated_variation_details objects,

    contig_id - id of contig
    position - base position of snp
    pvalue - pvalue of association in GWAS analysis
    rank - rank of association
    pvalue_adjusted - adjusted p-value
    reference_allele - Nucleotide in reference genome assembly
    alternate_allele - Nucleotide(s) in ecotype / germplasm
    variation_type - SNP/Indel
    variation_effect - Upstream, non-synonymous, Intron, synonymous,
    variation_impact - High, medium, low
    gene_id - genes in vicinity of SNP
    distance_from_snp - distance between SNP and gene
    is_significant - boolean value to indicate if this SNP is significant based on FDR    
    snp_to_gene - SNP to gene relationship.    

"""

associated_variation_details = []
for x in range(0,3):
    dummy_pval = float(random.uniform(0.0000000001,0.9999999))

    if x == 0:
        dummy_snp_to_gene_list = [snptogenes[0], snptogenes[1], snptogenes[2], snptogenes[3]]
    elif x == 1:
        dummy_snp_to_gene_list = [snptogenes[4], snptogenes[5], snptogenes[6], snptogenes[7]]
    elif x == 2:
        dummy_snp_to_gene_list = [snptogenes[8], snptogenes[9], snptogenes[10], snptogenes[11]]
    else:
        dummy_snp_to_gene_list = [snptogenes[12], snptogenes[13], snptogenes[14], snptogenes[15]]

    dummy_assoc_var_detail = {
        'contig_id': 'contig_'+str(x),
        'position': int(random.uniform(0,900000)),
        'pvalue': dummy_pval,
        'pvalue_adjusted': (-1)*log10(dummy_pval),
        'rank': int(random.choice([1,2,3,4])),
        'reference_allele': str(random.choice(['A','C','T','G'])),
        'alternate_allele': str(random.choice(['A','C','T','G'])),
        'variation_type': str(random.choice(['SNP','INDEL'])),
        'variation_effect': str(random.choice(['upstream','non-synonymous','intron','synonymous'])),
        'variation_impact': str(random.choice(['high', 'medium', 'low'])),
        'is_significant': random.choice([True, False]),
        'gene_details': dummy_snp_to_gene_list
    }

    associated_variation_details.append(dummy_assoc_var_detail)

"""

    Generate two different association_infos objects,

    trait_id - id of trait - string from traitinfos
    variation_id - id of variation - random string
    associated_variations - list of associated_variation_details

"""

association_infos = []
for x in range(0,1):
    if x == 0:
        dummy_assoc_vars = [associated_variation_details[0], associated_variation_details[1]]
    else:
        dummy_assoc_vars = [associated_variation_details[2], associated_variation_details[3]]

    dummy_assoc_info = {
        'trait_id': traitinfos[x]['trait_id'],
        'variation_id': 'var'+str(random.uniform(10000,90000)),
        'associated_variations': dummy_assoc_vars
    }

    association_infos.append(dummy_assoc_info)

"""

    Generate a top-level associations object
    
    description - string lorem ipsum
    Association_result - list of association_infos
"""

associations = [{'description': LI, 'Association_result': association_infos}]

"""
    Create Associations json data
"""

with open('associations.json', 'w') as a:
    json.dump(associations, a)
    a.close()

"""

    Generate one kinship object

    Kinship coefficient is a coefficient to assess the genetic resemblance between individuals.
    For N subjects, these coefficient can be assembled in a N x N matrix termed kinship matrix,
    can be used to model the covariance between individuals in quantitative genetics.

    Kinship matrix will be calculated within KBase as part of value addition to variation data

    The kinship matrix is represented as A simple 2D matrix of floating point numbers with labels/ids for rows and
     columns.  The matrix is stored as a list of lists, with the outer list
     containing rows, and the inner lists containing values for each column of
     that row.  Row/Col ids should be unique.
     row_ids - unique ids for rows.
     col_ids - unique ids for columns.
     kinship_coefficients - two dimensional array indexed as: values[row][col] - all coefficients are random floats between 0.0001 and 0.9999

"""
def kinship_coefs(n):
    top_list = []

    for x in range(0,n-1):
        new_list = []
        for x in range(0,n-1):
            new_list.append(float(random.uniform(0.0001,0.9999)))
        top_list.append(new_list)

    return top_list


kinship = {
    'row_ids': ['1','2','3','4','5','6','7','8','9','10'],
    'col_ids': ['1','2','3','4','5','6','7','8','9','10'],
    'kinship_coefficients': kinship_coefs(10)
}


"""

    Generate one variations object
    
    genome - genome_details
    population - Population
    assay - The assay method for genotyping or identifying SNPs
    originator - PI / LAB
    variation_file_reference - variation file handle
    kinship_info - kinship matrix info
    
"""

variations = {
    'population': population,
    'comment': LI,
    'assay': 'genotyping methodology',
    'originator': 'UT&ORNL',
    'genome': 'details about genome',
    'pubmed_id': 'PMID1234567',
    'contigs': ['contig1','contig2','contig3','contig4','contig5','contig6'],
    'variation_file_reference': 'SHID123456',
    'kinship_info': kinship
}

with open('variations.json', 'w') as v:
    json.dump(variations, v)
    v.close()