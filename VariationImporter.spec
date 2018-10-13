/*
A KBase module: VariationImporter
*/

module VariationImporter {
    /* A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int boolean;

    /* An X/Y/Z style reference
    */
    typedef string obj_ref;

    /*
        required params:
            genome_ref: KBaseGenomes.Genome object reference
            staging_file_subdir_path: path to VCF in staging area
            location_file_subdir_path: path to location data associated with samples
        optional params:
            *** Visualization ***
                plot_maf: generate histogram of minor allele frequencies
                plot_hwe: generate histogram of Hardy-Weinberg Equilibrium p-values
    
            additional_output_type: generate files necessary for particular analysis.
    */
    
    typedef structure {
        string workspace_name;
        obj_ref genome_ref;
        string staging_file_subdir_path;
        string location_file_subdir_path;
        string additional_output_type;
    } import_variation_params;

    typedef structure {
        string report_name;
        string report_ref;
        obj_ref variation_ref;
    } import_variation_results;


    funcdef import_variation(import_variation_params) 
        returns (import_variation_results) authentication required;
};
