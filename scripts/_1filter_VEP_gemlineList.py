#!/usr/local/bin/python3.6
from operator import itemgetter
import vep
import glob

def main():
    ## enter one VEP file for analysis
    for name in glob.glob("../dragen_germline/germline_joint_genotyping/Ontarget*nonRPZ113.vep.vcf"):
        inputfile=str(name)
        with open (inputfile,"r") as f:
            data=f.read().rstrip().split('\n')
        print("input lines:", len(data))    
        ## enter first filter condition   
        AF_min=float(input("Enter minimal AF: "))
        DP_min=float(input("Enter minimal DP: "))
        
        Unique,high,moderate, head_line=filter(data,AF_min, DP_min)
        print("header line number:", head_line)
        print("Total passed filter:",len(Unique), "\nHigh impact:",len(high), "\nmoderate impact deleterious:", len(moderate))       

        high = sort_sites(high)
        moderate = sort_sites(moderate)
        with open ("../dragen_germline/germline_joint_genotyping/germline_hardfFiltered_total.txt","w") as f:
            f.write("GENE" + "\t" + data[head_line]+ "\t" + "AF" + "\tIMPACT\tMUTATION\tAMINO ACID CHANGE\n")
            for item in high:
                line='\t'.join(item)
                f.write(line+'\n')
            for item in moderate:
                line='\t'.join(item)
                f.write(line+'\n')

## filter by minimal AF and DP, extract gene information, and divide to two groups (high, moderate)
def filter(data,AF_min, DP_min):
    vepA=vep.Vep(data) #build a Vep instance
    Unique, head_line = vepA.filter_AF_DP(AF_min, DP_min) #filter Vep instance
    vepB=vep.Vep(Unique) #build a Vep instance
    high,moderate=vepB.get_gene_list() # extract high and moderate deleterious gene list
    return Unique,high,moderate, head_line

## sort by AF    
def sort_sites(vep_list_set):
    list_list=[]
    for line in vep_list_set:
        l = line.split('\t') # itemgetter only work for list of list.
        if l[0] not in ["Skint6","Skint5","Sfi1","Mrgpra3","Mrgpra9","Mrgpra5","Skint11","Mrgprb5","Nlrp1b","Gm10110","Ighg2c", "Gm8909"]:
            list_list.append(l)
    list_list=sorted(list_list, key=itemgetter(0)) # sorted by gene name 
    return list_list      
    
main()    

       

        
         
