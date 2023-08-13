#classes do a function 
#from itertools import permutations
#cause of conversion
class PhenoConversion(object):
    def __init__(self,condition,medicine,enzyme,geno):
        self.condition=condition #will have to address if age,inflammation, type of cancer(advanced or myeloma), pregnant
        self.medicine=medicine
        self.enzyme=enzyme
        self.geno=geno
        
          
    def check_disease(self):
    #age
        #self.disease=disease
        #disease=["age", "inflammation", "cancer"]
        disease = self.condition
        if disease=="age":
            while True:
                age=input("please provide age of patient, valid/studied ranges are 21-36 and 66-85:"+ "\n")
                age=int(age)
                if age >=21 and age <=36:
                    disease=age
                    return disease
                elif age >=66 and age <=85:
                    disease=age
                    return disease
                else:
                    print("please provide a valid number for age between 21-36 or 66-85"+ "\n")
    # #cancer
        if disease=="cancer":
            cancer=input("please provide type of cancer. "+"\n"+"Options are: advanced cancer or multiple myeloma"+"\n")
            cancer.islower()
            if cancer=="advanced cancer" or cancer=="advanced":
                return cancer
            elif cancer=="multiple myeloma" or cancer =="multiple":
               return cancer
            else:
                print("not a valid input, please state if advanced cancer or multiple myeloma")
        # return self.disease[:] #returns a copy

# #drug or agent phenoconverting
    def drug(self):
        drug=self.medicine
        drug.lower()
        drug_list=["omeprazole", "proguanil", "losartan", "voriconazole", "dextromethorphan", "paroxetine"]
        while True:
            if drug in drug_list:
                return drug
            else:
                print("drug is not in the repertoire, available drugs are: Omeprazole, Proguanil, Losartan, Voriconazole, Dextromethorphan, Paroxetine"+ "\n")
                drug=input("please provide drug in question, options are: omeprazole, proguanil, losartan, voriconazole, dextromethorphan, paroxetine"+ "\n")
                break
# genotype:
    def genotype(self):
        genotype =self.geno
        #genotype=genotype.split()
        enzyme =self.enzyme
        enzyme=enzyme.upper()
        enzyme.upper()
        strlist=[]
        if enzyme=="CYP2C19":
            genotype_listC19 = ["*1","*2","*3","*17"]
            genotype_CYP2C19=[]
            for i in range(len(genotype_listC19)):
                for a in genotype_listC19:
                    strlist.append(a)
                    strlist.append(genotype_listC19[i])
                    strlist="/".join(strlist) #*1*/1
                    genotype_CYP2C19.append(strlist)
                    strlist=[]      
            if genotype in genotype_CYP2C19:
                return genotype
        
        elif enzyme=="CYP2C9":
            genotype_listC9 = ["*1","*2","*3"]
            genotype_CYP2C9=[]
            for i in range(len(genotype_listC9)):
                for a in genotype_listC9:
                    strlist.append(a)
                    strlist.append(genotype_listC9[i])
                    strlist="/".join(strlist) #*1*/1
                    genotype_CYP2C9.append(strlist)
                    strlist=[]      
            while True:
                #gene_split=genotype.split('/')
                if genotype in genotype_CYP2C9:
                    return genotype
                elif genotype in genotype_listC9:
                    return genotype 
                else: 
                    print("genotype not referenced")
                    genotype=input("genotype available for CYP2C9: *1/*2/*3" +'\n')
                    
        elif enzyme =="CYP2D6":
            genotype_listD6=["*1, *3, *4, *5, *6, *9, *10, *41"]        

            #perm = permutations(genotype_list, 2) #I might have to modify this in the future to have duplicates ie *1/*1
#             for i in perm:
#                 i="/".join(i)
#                 genotype_CYP2C19.append(i)
#             if genotype in genotype_list:
#                 return genotype
# #                 elif genotype == a or b:
# #                             return genotype
        else:
            print("Gene and Genotype was not referenced in this study.")
                                  
# # #genotype assessment
    def assessment(self):
        genotype=self.geno
        genotype=genotype.split("/")
        print(genotype)
        disease=self.check_disease()
        drug=self.drug()
        
        while True:
            #enzyme_list=["CYP2C19","CYP2C9","CYP2D6"]
            # if enzyme=="CYP2C19":
            #     if genotype == 
            if drug=="omeprazole":
                if disease == "advanced cancer" or disease == "advanced":
                    if "*17" not in genotype:
                            print("\n"+"Patient will phenoconvert to a poor metabolizer"+"\n" + "Initiate standard starting daily dose."+"\n"+"For chronic therapy (>12 weeks) and efficacy achieved," +"\n" + "consider 50% reduction in daily dose and monitor for continued efficacy.")
                            break
                    else: 
                        print("available genotypes in this category are: CYP2C19*1/*2/*3" + '\n')
                        genotype = input("please enter a valid genotype (options are: *1 or *2 or *3 or a combination): ")
                        genotype=genotype.split("/")
                        print(genotype)
                
                elif type(disease) == int:
                    print("\n"+ "Patient will phenoconvert to a poor metabolizer"+"\n" + "Initiate standard starting daily dose."+"\n"+"For chronic therapy (>12 weeks) and efficacy achieved," +"\n" + "consider 50% reduction in daily dose and monitor for continued efficacy.")
                    break
                
                
            elif drug =="proguanil":
                if disease == "multiple myeloma" or disease =="multiple":
                    print("\n"+ "Patient will phenoconvert to a poor metabolizer."+"\n" + "Monitor Proguanil levels or discontinue medication")
                    break
                        
                    
class Inflammation(PhenoConversion): #I think that whatever definition is in children, cannot be used for parent
    '''checks the type of inflammation if condition is inflammation. 
    Types of inflammations reported in literature are: Behçet’s disase, cirrhosis, hepatitis C'''
    
    def __init__(self,condition,medicine,enzyme,geno):
        PhenoConversion.__init__(self,condition,medicine,enzyme,geno)
    
     
    def stateOfInflammation(self):
    ##inflammation
        condition=self.condition
        drug = self.drug()
        genotype=self.genotype()
        
        #gene_split=genotype.split("/")
        genotype_list = ["*1","*2","*3"]
        if condition == "inflammation":
            typeOfInflammation=input("Does patient have Behçet’s disase? ")
            typeOfInflammation=typeOfInflammation.lower()
            if typeOfInflammation=="yes" or typeOfInflammation =="y":
                if drug=="losartan":
                    if genotype == "*1/*1":
                        return "Patient shows signs of poor metabolizer for Losartan. Higher urinary metabolic ratio seen for this drug. Monitor blood pressure"
                    else:
                        return "Higher urinary metabolic ratio of Losartan seen for these patients than in healthy subjects. Monitor blood pressure"
                else: 
                    print("only Losartan has been studied with this condition")
            elif typeOfInflammation =="no" or typeOfInflammation =="n":
                answer=input("Please choose a, b, or c from the following: "+'\n'+"Does patient have a. cirrhosis/chronic hepatitis? or b. Hepatitis C? or c. C-reactive protein >10mg/L? ")
                answer=answer.lower()
                if answer =="a":
                    if drug =="omeprazole":
                        affected_genotypes=['*1/*1','*1/*2','*1/*3','*2/*2','*2/*3','*3/*3']
                        if genotype in affected_genotypes:
                                return "Patient will phenoconvert to a poor metabolizer"+"\n" + "Initiate standard starting daily dose."+"\n"+"For chronic therapy (>12 weeks) and efficacy achieved," +"\n" + "consider 50% reduction in daily dose and monitor for continued efficacy."
                        elif genotype in genotype_list:
                            return "Patient will phenoconvert to a poor metabolizer"+"\n" + "Initiate standard starting daily dose."+"\n"+"For chronic therapy (>12 weeks) and efficacy achieved," +"\n" + "consider 50% reduction in daily dose and monitor for continued efficacy."
                    else:
                        "no other drugs or enzymes were reported for this condition"  #may need to ask for another drug
                elif answer=="b":
                    if drug=="dextromethorphan" and enzyme == "CYP2D6":
                        return "CYP2D6 metabolic activity is reduced by average 80% due to Liver kidney microsomal type 1 (LKM-1) antibodies in patient with chronic hepatitis C infection."
                    elif drug =="omeprazole":
                        affected_genotypes=['*1/*1','*1/*2','*1/*3','*2/*2','*2/*3','*3/*3']
                        if genotype in affected_genotypes:
                                return "Patient will phenoconvert to a poor metabolizer"+"\n" + "Initiate standard starting daily dose."+"\n"+"For chronic therapy (>12 weeks) and efficacy achieved," +"\n" + "consider 50% reduction in daily dose and monitor for continued efficacy."
                        elif genotype in genotype_list:
                            return "Patient will phenoconvert to a poor metabolizer"+"\n" + "Initiate standard starting daily dose."+"\n"+"For chronic therapy (>12 weeks) and efficacy achieved," +"\n" + "consider 50% reduction in daily dose and monitor for continued efficacy."
                    else:
                        return "no other drugs or enzymes were reported for this condition"
                    
                elif answer == "c":
                    genotypesVoriconazole=['*1/*17','*1/*1','*1/*2','*1/*3','*2/*3','*2/*2','*3/*3']
                    genotype_listC19 = ["*1","*2","*3","*17"]
                    if drug =="voriconazole":
                        if genotype in genotypesVoriconazole:
                            return "Frequent monitoring of Voriconazole serum concentration during Voriconazole treatment is recommended during and after severe inflammation"
                        elif genotype in genotype_listC19:
                            return "Frequent monitoring of Voriconazole serum concentration during Voriconazole treatment is recommended during and after severe inflammation"
                        else:
                            return "no other enzyme/genotype reported"
                    else:
                        return "no other drug reported with this disease"

      
class Pregnancy(PhenoConversion):
    '''checks if pregnancy phenoconverts an enzyme given genes and drug'''
    
    def __init__(self,condition,medicine,enzyme,geno):
        PhenoConversion.__init__(self,condition,medicine,enzyme,geno)      


  #have to do a while loop in case input is invalid
                     
#        elif enzyme == "CYP2C9":
#         #check if *1/*2/*3 genotypes & age normal/intermediate metabolizer-->poor metabolizer:
#         if genotype == "*1" or "*2" or "*3":
#             if 
#             print("Initiate standard starting daily dose. For chronic therapy (>12 weeks) and efficacy achieved, consider 50% reduction in daily dose and monitor for continued efficacy.")
        
# #result, suggestion
disease="cancer"
drug="omeprazole"
enzyme="cyp2c19"
genotype="*1/*17"
result=PhenoConversion(disease,drug,enzyme,genotype)
print(result.assessment())
#print(result.drug())
#result2=Inflammation(disease,drug,enzyme,genotype)
#print(result2.genotype_inflammation())
#print(result2.stateOfInflammation())


# disease="inflammation"
# drug="omeprazole"
# enzyme="cyp2c19"
# genotype="*1/*17"
# result=PhenoConversion(disease,drug,enzyme,genotype)

# print(result.assessment())
