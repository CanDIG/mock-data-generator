"""
Usage:
    mock_clinphen.py <num_records>

Options:
    -h --help       Show this screen
    -v --version    Version
    <num_records>   number of records to produce (int)
"""

import json
import random
import time
import datetime
from docopt import docopt

data = dict(metadata = [])
outfile_name = 'mock_clinphen_data.json'

def generate_id_string(length):
    range_start = 10**(length-1)
    range_end = (10**length)-1
    return str(random.randint(range_start, range_end))

def main():
    args = docopt(__doc__, version='0.1')
    n = int(args['<num_records>'])

    # pick a random site to generate data for
    SITE = random.choice(["BC","ON","QC"])
    if SITE == "BC":
        enrollment_treatment_site = "Canada's Michael Smith Genome Sciences Centre"
        res_province = gsc_province
    elif SITE == "ON":
        enrollment_treatment_site = random.choice(['Hospital for Sick Children', 'Princess Margaret Cancer Centre', 'University Health Network'])
        res_province = to_province
    elif SITE == "QC":
        enrollment_treatment_site = 'McGill University and Genome Quebec Innovation Centre'
        res_province = mo_province

    for i in range (n):

        data["metadata"].append(dict(
            Patient = dict(),
            Enrollment = dict(),
            Consent = dict(),
            Diagnosis = dict(),
            Sample = dict(),
            Treatment = dict(),
            Outcome = dict(),
            Complication = dict(),
            Tumourboard = dict()
            ))

        current_entry = data["metadata"][i]

        patient_id = g_id("PATIENT")

        # update patient
        null_fields = random.choice(fnull)

        current_entry["Patient"] = dict(
            patientId   = patient_id,
            otherIds    = "" if null_fields else generate_id_string(5),
            dateOfBirth = "" if null_fields else g_date("1910-01-01","2002-12-31"),
            gender      = "" if null_fields else g_gender(),
            ethnicity   = "" if null_fields else random.choice(ethnicity),
            race        = "" if null_fields else random.choice(race),
            provinceOfResidence = "" if null_fields else random.choice(res_province),
            dateOfDeath = "" if null_fields else g_date("2004-01-01","2017-12-31"),
            causeOfDeath        = "" if null_fields else random.choice(death_cause),
            autopsyTissueForResearch = "" if null_fields else "n/a",
            dateOfPriorMalignancy = "" if null_fields else "n/a",
            familyHistoryAndRiskFactors = "" if null_fields else "n/a",
            familyHistoryOfPredispositionSyndrome = "" if null_fields else "n/a",
            detailsOfPredispositionSyndrome = "n/a",
            geneticCancerSyndrome = "n/a",
            otherGeneticConditionOrSignificantComorbidity = "" if null_fields else "n/a",
            occupationalOrEnvironmentalExposure = "" if null_fields else random.choice(environmental) 
            )


        # update enrollment
        null_fields = random.choice(fnull)

        current_entry["Enrollment"] = dict(
            patientId = patient_id,
            enrollmentInstitution = "" if null_fields else enrollment_treatment_site,
            enrollmentApprovalDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            crossEnrollment = "" if null_fields else "n/a",
            otherPersonalizedMedicineStudyName = "" if null_fields else "n/a",
            otherPersonalizedMedicineStudyId = "" if null_fields else "n/a",
            ageAtEnrollment = "" if null_fields else g_age(),
            eligibilityCategory = "" if null_fields else "n/a",
            statusAtEnrollment = "" if null_fields else "n/a",
            primaryOncologistName = "" if null_fields else random.choice(oncologist),
            primaryOncologistContact = "" if null_fields else "n/a",
            referringPhysicianName = random.choice(physician),
            referringPhysicianContact = "n/a",
            summaryOfIdRequest = "n/a",
            treatingCentreName = "" if null_fields else enrollment_treatment_site,
            treatingCentreProvince = "" if null_fields else SITE
            )

        # update consent
        consent_id = g_id("CONSENT")
        null_fields = random.choice(fnull)

        current_entry["Consent"] = dict(
            patientId = patient_id,
            consentId = consent_id,
            consentDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            consentVersion = g_version(),
            patientConsentedTo = "" if null_fields else "n/a",
            reasonForRejection = "" if null_fields else "n/a",
            wasAssentObtained = "" if null_fields else random.choice(["Yes","No"]),
            dateOfAssent = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            assentFormVersion = "" if null_fields else g_version(),
            ifAssentNotObtainedWhyNot = "n/a",
            reconsentDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            reconsentVersion = "" if null_fields else g_version(),
            consentingCoordinatorName = "" if null_fields else random.choice(coordinator),
            previouslyConsented = "" if null_fields else random.choice(["Yes","No"]),
            nameOfOtherBiobank = "n/a",
            hasConsentBeenWithdrawn = "" if null_fields else random.choice(["Yes","No"]),
            dateOfConsentWithdrawal = "n/a",
            typeOfConsentWithdrawal = "n/a",
            reasonForConsentWithdrawal = "n/a",
            consentFormComplete = "" if null_fields else random.choice(["Yes","No"])
            )

        # update diagnosis
        diagnosis_id = g_id("DIAGNOSIS")
        c_type = random.choice(cancer_type)
        s_type = random.choice(sample_type)
        null_fields = random.choice(fnull)

        current_entry["Diagnosis"] = dict(
            patientId = patient_id,
            diagnosisId = diagnosis_id,
            diagnosisDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            ageAtDiagnosis = "" if null_fields else g_age(),
            cancerType = "" if null_fields else c_type,
            classification = "" if null_fields else random.choice(classification),
            cancerSite = "" if null_fields else random.choice(tissue),
            histology = "n/a",
            methodOfDefinitiveDiagnosis = "" if null_fields else random.choice(diagnosis_method),
            sampleType = "" if null_fields else s_type,
            sampleSite = "" if null_fields else random.choice(tissue),
            tumorGrade = "" if null_fields else random.choice(tumour_grade),
            gradingSystemUsed = 'n/a',
            sitesOfMetastases = "" if null_fields else random.choice(tissue),
            stagingSystem = 'n/a',
            versionOrEditionOfTheStagingSystem = "" if null_fields else g_version(),
            specificTumorStageAtDiagnosis = "" if null_fields else g_tumour_stage(),
            prognosticBiomarkers = "n/a",
            biomarkerQuantification = "n/a",
            additionalMolecularTesting = "" if null_fields else "n/a",
            additionalTestType = "n/a",
            laboratoryName = "n/a",
            laboratoryAddress = "n/a",
            siteOfMetastases = "" if null_fields else random.choice(tissue),
            stagingSystemVersion = "" if null_fields else g_version(),
            specificStage = "" if null_fields else g_tumour_stage(), 
            cancerSpecificBiomarkers = "n/a",
            additionalMolecularDiagnosticTestingPerformed = "n/a",
            additionalTest = "n/a" 
            )

        # update sample
        sample_id = g_id("SAMPLE")
        null_fields = random.choice(fnull)

        current_entry["Sample"] = dict(
            patientId = patient_id,
            sampleId = sample_id,
            diagnosisId = diagnosis_id,
            localBiobankId = "" if null_fields else generate_id_string(4),
            collectionDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            collectionHospital = "" if null_fields else "BCCA",
            sampleType = "" if null_fields else s_type,
            tissueDiseaseState = "n/a",
            anatomicSiteTheSampleObtainedFrom = random.choice(tissue),
            cancerType = "" if null_fields else c_type,
            cancerSubtype = "n/a",
            pathologyReportId = "" if null_fields else generate_id_string(5),
            morphologicalCode = "" if null_fields else generate_id_string(5) ,
            topologicalCode = "" if null_fields else "C"+generate_id_string(3),
            shippingDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            receivedDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            qualityControlPerformed = "n/a",
            estimatedTumorContent = str(random.randint(1,100)),
            quantity = str(random.randint(5,100)),
            units = "mm3",
            associatedBiobank = "n/a",
            otherBiobank = "n/a",
            sopFollowed = random.choice(["Yes","No"]),
            ifNotExplainAnyDeviation = "n/a"
            )

        # update treatment
        null_fields = random.choice(fnull)

        current_entry["Treatment"] = dict(
            patientId = patient_id,
            courseNumber = "" if null_fields else generate_id_string(3),
            therapeuticModality = "" if null_fields else random.choice(modality),
            systematicTherapyAgentName = "n/a",
            treatmentPlanType = "n/a",
            treatmentIntent = "" if null_fields else "n/a",
            startDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            stopDate = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            reasonForEndingTheTreatment = "n/a",
            protocolNumberOrCode = "" if null_fields else g_version(),
            surgeryDetails = "" if null_fields else "n/a",
            radiotherapyDetails = "" if null_fields else "n/a",
            chemotherapyDetails = "n/a",
            hematopoieticCellTransplant = "" if null_fields else "n/a",
            immunotherapyDetails = "n/a",
            responseToTreatment = "" if null_fields else random.choice(tumour_response),
            dateOfRecurrenceOrProgressionAfterThisTreatment = "n/a",
            unexpectedOrUnusualToxicityDuringTreatment = "n/a",
            drugListOrAgent = g_drug_list(),
            drugIdNumbers = "n/a"
            )

        # update outcome
        null_fields = random.choice(fnull)

        current_entry["Outcome"] = dict(
            patientId = patient_id,
            physicalExamId = "" if null_fields else generate_id_string(4),
            dateOfAssessment = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            diseaseResponseOrStatus = "" if null_fields else random.choice(tumour_response),
            otherResponseClassification = "n/a",
            minimalResidualDiseaseAssessment = "n/a",
            methodOfResponseEvaluation = "n/a",
            responseCriteriaUsed = "n/a",
            summaryStage = "n/a",
            sitesOfAnyProgressionOrRecurrence = "n/a",
            vitalStatus = "n/a",
            height = "" if null_fields else str(random.randint(100, 200)),
            weight = "" if null_fields else str(random.randint(40, 130)),
            heightUnits = "" if null_fields else "cm",
            weightUnits = "" if null_fields else "kg",
            performanceStatus = "n/a"
            )

        # update complication
        null_fields = random.choice(fnull)

        current_entry["Complication"] = dict(
            patientId = "" if null_fields else patient_id,
            date = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            lateComplicationOfTherapyDeveloped = "" if null_fields else "n/a",
            lateToxicityDetail = "" if null_fields else "n/a",
            suspectedTreatmentInducedNeoplasmDeveloped = "" if null_fields else "n/a",
            treatmentInducedNeoplasmDetails = "" if null_fields else "n/a" 
            )


        # update tumourboard
        null_fields = random.choice(fnull)

        current_entry["Tumourboard"] = dict(
            patientId = patient_id,
            dateOfMolecularTumorBoard = "" if null_fields else g_date("2004-01-01","2018-03-31"),
            typeOfSampleAnalyzed = "" if null_fields else s_type,
            typeOfTumourSampleAnalyzed = "",
            analysesDiscussed = "",
            somaticSampleType = "" if null_fields else s_type,
            normalExpressionComparator = "",
            diseaseExpressionComparator = "",
            hasAGermlineVariantBeenIdentifiedByProfilingThatMayPredisposeToCancer = "",
            actionableTargetFound = "",
            molecularTumorBoardRecommendation = "",
            germlineDnaSampleId = "" if null_fields else generate_id_string(4),
            tumorDnaSampleId = "" if null_fields else generate_id_string(4),
            tumorRnaSampleId = "" if null_fields else generate_id_string(4),
            germlineSnvDiscussed = "",
            somaticSnvDiscussed = "",
            cnvsDiscussed = "",
            structuralVariantDiscussed = "",
            classificationOfVariants = "",
            clinicalValidationProgress = "",
            typeOfValidation = "",
            agentOrDrugClass = "",
            levelOfEvidenceForExpressionTargetAgentMatch = "",
            didTreatmentPlanChangeBasedOnProfilingResult = "",
            howTreatmentHasAlteredBasedOnProfiling = "",
            reasonTreatmentPlanDidNotChangeBasedOnProfiling = "",
            detailsOfTreatmentPlanImpact = "",
            patientOrFamilyInformedOfGermlineVariant = "",
            patientHasBeenReferredToAHereditaryCancerProgramBasedOnThisMolecularProfiling = "",
            summaryReport = "" 
            )

additionalModalities = []

def randomDrugListGenerator(numberOfGenerations):
    
    drugList = ['Multivitamins and minerals', 'Risedronate sodium', 'Rosuvastatin', 'Candesartan', 'Hydrochlorothiazide', 'Metoprolol', 'Loperamide', 'Capecitabine', 'Bevacizumab', 'Fluorouracil', 'Oxaliplatin', 'Leucovorin', 'Irinotecan', 'Aait', 'Abiraterone', 'Abraxane', 'Abt-888', 'Accutane', 'Acetazolamide', 'Afatinib', 'Ags67e', 'Alectinib', 'Alemtuzumab', 'Aliskiren', 'Anastrozole', 'Anastrozole/placebo', 'Asa', 'Atezolizumab', 'Atezolizumab/placebo', 'Avelumab', 'Azacitidine', 'Azd1775', 'Azd2171', 'Azd5363', 'Azd8931', 'Azd9291', 'Bay 73-4506', 'Bbi608', 'Bbi608/placebo', 'Bendamustine', 'Bibw2992', 'Bicalutamide', 'Bkm120', 'Bkm120/placebo', 'Bleomycin', 'Bms-936558', 'Bms-986115', 'Bms-986205', 'Bromocriptine', 'Buparlisib', 'Buserelin', 'Busulfan', 'Cabozantinib', 'Carboplatin', 'Carmustine', 'Cediranib', 'Ceritinib', 'Cetuximab', 'Cfi-402257', 'Chlorambucil', 'Chlordiazepoxide', 'Cisplatin', 'Clodronate', 'Co-1686', 'Cobimetinib', 'Copanlisib', 'Cortisone', 'Crizotinib', 'Cx-5461', 'Cyclophosphamide', 'Cytarabine', 'Dabrafenib', 'Dacarbazine', 'Dacarbazine/placebo', 'Dactinomycin', 'Degarelix', 'Demcizumab', 'Demcizumab/placebo', 'Dexamethasone', 'Dexrazoxane', 'Docetaxel', 'Dovitinib', 'Doxorubicin', 'Durvalumab', 'Durvalumab(moind228)', 'Enmd-2076', 'Enzalutamide', 'Epirubicin', 'Eribulin', 'Erlotinib', 'Etoposide', 'Everolimus', 'Exemestane', 'Faslodex', 'Filgrastim', 'Fludarabine', 'Fludarabinepo', 'Fludrocortisone', 'Flutamide', 'Folfiri', 'Fulvestrant', 'Fulvestrant/placebo', 'Ganetesip', 'Gefitinib', 'Gemcitabine', 'Gifirinox', 'Goserelin', 'Hepasphere', 'Herceptin', 'Hydrocortisone', 'Hydroxyurea', 'Ibrutinib', 'Ifosfamide', 'Imatinib', 'Imc-1121b', 'Imgn', 'Imiquimod', 'Immunotherapy', 'Interferon', 'Iodine-131', 'Iph2201', 'Ipilimumab', 'Irbesartan', 'Lambrolizumab', 'Lanreotide', 'Lapatinib', 'Lcl161', 'Ldk378', 'Lee011', 'Lee011/placebo', 'Lenvatinib', 'Letrozole', 'Leuprolide', 'Lomustine', 'Lutetium-177', 'Ly3076226', 'Medi4736', 'Medroxyprogesterone', 'Megestrol', 'Mek162', 'Melphalan', 'Mesna', 'Metformin', 'Metformin/placebo', 'Methotrexate', 'Mgcd265', 'Mitomycin', 'Mitotane', 'Monalizumab', 'Moxr0916', 'Mpdl3280a', 'Mpdl3280a/placebo', 'Napabucasin', 'Naringenin', 'Nilotinib', 'Nintedanib', 'Nintedanib/placebo', 'Niraparib', 'Nivolumab', 'Nktr-102', 'Octreotide', 'Olaparib', 'Olaratumab', 'Olaratumab/placebo', 'Osimertinib', 'Paclitaxel', 'Paclitaxel-nab', 'Palbociclib', 'Pamidronate', 'Panitumumab', 'Pazopanib', 'Pd-0332991', 'Pd-0332991/placebo', 'Pegfilgrastim', 'Pembrolizumab', 'Pemetrexed', 'Pertuzumab', 'Pf-04518600', 'Pki-587', 'Pf-05212384', 'Prednisone', 'Procarbazine', 'Raltitrexed', 'Ramucirumab', 'Ramucirumab/plac', 'Regorafenib', 'Reolysin', 'Ribociclib', 'Ribociclib/placebo', 'Rituximab', 'Rociletinib', 'Romidepsin', 'Rucaparib', 'Sapitinib', 'Selumetinib', 'Slc-0111', 'Sorafenib', 'Streptozocin', 'Sunitinib', 'Talazoparib', 'Tamoxifen', 'Taselisib', 'Taselisib/placebo', 'Telmisartan', 'Temozolomide', 'Temsirolimus', 'Thyrotropin', 'Tipiracil', 'Topotecan', 'Trabectedin', 'Trametinb', 'Trametinib', 'Trastuzumab', 'Tremelimumab', 'Trifluridine', 'Trifluridine-tipiracil', 'Vandetanib', 'Veliparib', 'Vemurafenib', 'Vinblastine', 'Vincristine', 'Vinorelbine', 'Vismodegib', 'Vorinostat', 'Yttrium-90', 'Zactima', 'Zactima/placebo', 'Imgn folate receptor', 'Hyperthermia', 'Bms-936558/placebo', 'Bibw', 'Cytotoxic cells therapy', 'Nk t cells', 'Gedatolisib', 'Sapitinib/placebo', 'Vandetanib/placebo', 'Ramucirumab/placebo', 'Etirinotecan pegol', 'Buparlisib/placebo', 'Palbociclib/placebo', 'Napabucasin/placebo', 'Aspirin', 'Imgn853', 'Istodax', 'Binimetinib', 'Nivolumab/placebo']

    finalDrugList = []

    currNumber = 0

    while currNumber < numberOfGenerations:
        selectedDrug = random.choice(drugList)

        if selectedDrug not in finalDrugList:
            finalDrugList.append(selectedDrug)

        currNumber = currNumber + 1

    return finalDrugList


def chemoGenerator(numberOfGenerations, patientId, courseNumber, chemoStartDate, chemoEndDate, treatmentIntent, treatingCentreName, treatmentPlanId):

    drugList = randomDrugListGenerator(numberOfGenerations)

    for drug in drugList:

        temp = {}

        temp["Chemotherapy"] = dict(
            patientId = patientId,
            courseNumber = courseNumber,
            startDate = chemoStartDate,
            stopDate = chemoEndDate,
            systematicTherapyAgentName = drug,
            route = random.choice(["By mouth (PO)", "IV"]),
            dose = str(random.randint(0.0, 40.0)),
            doseUnit = "mg",
            doseFrequency = random.choice(["Every morning", "Once everyday", "As Needed", "Once every two days"]),
            daysPerCycle = str(random.randint(6, 10)),
            numberOfCycle = str(random.randint(4, 6)),
            treatmentIntent = treatmentIntent,
            treatingCentreName = treatingCentreName,
            type = random.choice(["Chemotherapy", "Hormonal drug therapy", "Targeted therapy", "Supportive drugs"]),
            protocolCode = str(random.randint(1, 4)),
            recordingDate = g_date("2014-01-01", "2018-01-01"),
            treatmentPlanId = treatmentPlanId
        )

        additionalModalities.append(temp)


def insert_labkey_tables():

    for current_entry in data["metadata"]:

        currPatientId = current_entry["Patient"]["patientId"]
        currSampleId = current_entry["Sample"]["sampleId"]
        currDiagnosisId = current_entry["Diagnosis"]["diagnosisId"]
        currTreatmentPlanId = currPatientId + "_" + generate_id_string(5)

        current_entry["Treatment"]["diagnosisId"] = currDiagnosisId
        current_entry["Treatment"]["treatmentPlanId"] = currTreatmentPlanId
        current_entry["Treatment"]["responseCriteriaUsed"] = random.choice(["RECIST", "Other", "RECIST"])

        modalities = ["Chemotherapy"]*5 + ["Radiotherapy", "Immunotherapy", "Celltransplant", "Surgery"]
        selectedModality = random.choice(modalities)

        current_entry["Treatment"]["therapeuticModality"] = selectedModality

        if selectedModality == "Chemotherapy":

            numberOfGenerations = random.randint(1, 3)

            chemoStartDate = g_date("2014-01-01", "2018-01-01")
            chemoEndDate = g_date(chemoStartDate, "2019-01-01")

            current_entry["Chemotherapy"] = dict(
                patientId = currPatientId,
                courseNumber = "1",
                startDate = chemoStartDate,
                stopDate = chemoEndDate,
                systematicTherapyAgentName = random.choice(['Synthroid', 'Amlodipine', 'Hydrochlorthiazide (avalide)', 'Irbesartan (avalide)', 'Multivitamin and mineral', 'Percocet', 'Rivaroxaban', 'Candesartan cilexetil', 'Ferrous gluconate']),
                route = random.choice(["By mouth (PO)", "IV"]),
                dose = str(random.randint(0.0, 40.0)),
                doseUnit = "mg",
                doseFrequency = random.choice(["Every morning", "Once everyday", "As Needed", "Once every two days"]),
                daysPerCycle = str(random.randint(6, 10)),
                numberOfCycle = str(random.randint(4, 6)),
                treatmentIntent = current_entry["Treatment"]["treatmentIntent"],
                treatingCentreName = current_entry["Enrollment"]["treatingCentreName"],
                type = random.choice(["Chemotherapy", "Hormonal drug therapy", "Targeted therapy", "Supportive drugs"]),
                protocolCode = str(random.randint(1, 4)),
                recordingDate = g_date("2014-01-01", "2018-01-01"),
                treatmentPlanId = currTreatmentPlanId
            )

            chemoGenerator(numberOfGenerations, currPatientId, "1", chemoStartDate, chemoEndDate, current_entry["Treatment"]["treatmentIntent"], current_entry["Enrollment"]["treatingCentreName"], currTreatmentPlanId)


        # update enrollment

        if selectedModality == "Radiotherapy":

            radioStartDate = g_date("2014-01-01", "2018-01-01")

            current_entry["Radiotherapy"] = dict(
                patientId = currPatientId,
                courseNumber = "1",
                radiationType = random.choice(["Conformal", "Electron", "Proton", "Systemic", "Other", "IMRT", "Conventional External Beam", "Brachytherapy"]),
                radiationSite = random.choice(["Oral and Pharyngeal", "Lymphoid and Hematopoietic", "Trachea", "Lung", "Bones, Joints", "Nervous system", "GU", "Other"]),
                totalDose = str(random.randint(1, 40)) + " cGy",
                boostSite = random.choice(["Oral and Pharyngeal", "Lymphoid and Hematopoietic", "Trachea", "Lung", "Bones, Joints", "Nervous system", "GU", "Other"]),
                boostDose = str(random.randint(1, 40)) + " cGy",
                therapeuticModality = random.choice(["Three-Dimensional Treatment Planning", "GliaSite Brachytherapy", "Low Dose Rate Brachytherapy", "SIR-Spheres Microspheres treatment", "TomoTherapy", "Intensity Modulated Radiation Therapy (IMRT)", "Total Skin Electron Beam Therapy"]),
                baseline = str(random.randint(1, 20)),
                testResult = str(random.randint(1, 20)),
                testResultStd = str(random.randint(1, 10)),
                treatingCentreName = current_entry["Enrollment"]["treatingCentreName"],
                startIntervalRad = str(random.randint(1, 20)),
                startIntervalRadRaw = str(random.randint(1, 20)),
                recordingDate = g_date("2014-01-01", "2018-01-01"),
                adjacentFields = random.choice(["muscle", "epithelial", "connective", "nervous"]),
                adjacentFractions = str(random.random()),
                complete = random.choice(["Yes", "No"]),
                brachytherapyDose = str(random.randint(0, 40)),
                radiotherapyDose = str(random.randint(0, 40)),
                siteNumber = str(random.randint(1, 20)),
                startDate = radioStartDate,
                stopDate = g_date(radioStartDate, "2018-01-01"),
                technique = random.choice(["02", "08", str(random.randint(10, 99))]) + random.choice("ABCDEFGHIJKLMSFSDNFYUIERHDSFLKDF"),
                treatedRegion = random.choice(["Oral and Pharyngeal", "Lymphoid and Hematopoietic", "Trachea", "Lung", "Bones, Joints", "Nervous system", "GU", "Other"]),
                treatmentPlanId = currTreatmentPlanId
            )

        if selectedModality == "Immunotherapy":

            current_entry["Immunotherapy"] = dict(
                patientId = currPatientId,
                treatmentPlanId = currTreatmentPlanId,
                startDate = g_date("2014-01-01", "2018-01-01"),
                immunotherapyType = random.choice(["CAR-T", "Vaccine", "Antibody", "Other"]),
                immunotherapyTarget = "N/A",
                immunotherapyDetail = "N/A",
                courseNumber = "1"
            )

        if selectedModality == "Celltransplant":

            current_entry["Celltransplant"] = dict(
                patientId = currPatientId,
                treatmentPlanId = currTreatmentPlanId,
                startDate = g_date("2014-01-01", "2018-01-01"),
                cellSource = random.choice(["Bone Marrow", "Cord Blood", "Peripheral blood stem cells"]),
                donorType = random.choice(["Allogeneic", "Sysgeneic", "N/A", "Other", "Unknown"]),
                courseNumber = "1"
            )

        if selectedModality == "Surgery":

            SurgeryStartDate = g_date("2014-01-01", "2018-01-01")

            current_entry["Surgery"] = dict(
                patientId = currPatientId,
                sampleId = currSampleId,
                treatmentPlanId = currTreatmentPlanId,
                startDate = SurgeryStartDate,
                stopDate = g_date(SurgeryStartDate, "2019-01-01"),
                site = random.choice(["Primary lesion", "Metastatic liver lesion", "Normal liver tissue"]),
                type = random.choice(["Liver metastectomy", "Right hemicolectomy", "Low anterior resection"]),
                collectionTimePoint = random.choice(["Liver Metastectomy", "Archival", "Montreal"]),
                diagnosisDate = g_date("2014-01-01", "2018-01-01"),
                recordingDate = g_date("2014-01-01", "2018-01-01"),
                courseNumber = "1"
            )


        current_entry["Slide"] = dict(
            patientId = currPatientId,
            sampleId = currSampleId,
            slideId = generate_id_string(5),
            slideOtherId = generate_id_string(5),
            lymphocyteInfiltrationPercent = str(random.randint(0, 100)) + "%",
            monocyteInfiltrationPercent = str(random.randint(0, 100)) + "%",
            normalCellsPercent = str(random.randint(0, 100)) + "%",
            tumorCellsPercent = str(random.randint(0, 100)) + "%",
            stromalCellsPercent = str(random.randint(0, 100)) + "%",
            eosinophilInfiltrationPercent = str(random.randint(0, 100)) + "%",
            neutrophilInfiltrationPercent = str(random.randint(0, 100)) + "%",
            granulocyteInfiltrationPercent = str(random.randint(0, 100)) + "%",
            necrosisPercent = str(random.randint(0, 100)) + "%",
            inflammatoryInfiltrationPercent = str(random.randint(0, 100)) + "%",
            proliferatingCellsNumber = str(random.randint(0, 100)) + "%",
            sectionLocation = "",
            tumorNucleiPercent = str(random.randint(0, 100)) + "%"
        )


        studyStartDate = g_date("2014-01-01", "2018-01-01")

        current_entry["Study"] = dict(
            patientId = currPatientId,
            startDate = studyStartDate,
            endDate = g_date(studyStartDate, "2019-01-01"),
            status = random.choice(["Enrolled"]*10 + ["In Progress"]*5 +["Completed", "Rejected", "Withdrawn"]),
            recordingDate = g_date("2014-01-01", "2018-01-01")
        )


        LabtestStartDate = g_date("2014-01-01", "2018-01-01")

        current_entry["Labtest"] = dict(
            patientId = currPatientId,
            startDate = LabtestStartDate,
            collectionDate = g_date("2014-01-01", "2018-01-01"),
            endDate = g_date(LabtestStartDate, "2019-01-01"),
            eventType = random.choice(["CTDNA BLOOD DRAW"]),
            testResults = random.choice(["N/A"]),
            timePoint = random.choice(["Baseline", "Post-Op"]),
            recordingDate = g_date("2014-01-01", "2018-01-01")
        )

    print("labkey tables inserted.")


def newIdGenerator(oldId):

    newId = generate_id_string(5)

    if newId != oldId:
        return newId
    else:
        return newIdGenerator(oldId)


deleted_treatment_fields = ["systematicTherapyAgentName", "protocolNumberOrCode", "surgeryDetails", "radiotherapyDetails", "chemotherapyDetails", "hematopoieticCellTransplant", "immunotherapyDetails", "drugListOrAgent", "drugIdNumbers"]


def remove_deleted_fields():
    for entry in data["metadata"]:
        for key in deleted_treatment_fields:
            entry["Treatment"].pop(key)

            #tierKey = key + "Tier"
            #entry["Treatment"].pop(tierKey)


def add_sample_outcome_fields():
    for entry in data["metadata"]:
        entry["Sample"]["recordingDate"] = g_date("2014-01-01", "2018-01-01")
        entry["Sample"]["startInterval"] = str(random.randint(1, 20))

        entry["Outcome"]["overallSurvivalInMonths"] = str(random.randint(1, 240))
        entry["Outcome"]["diseaseFreeSurvivalInMonths"] = str(random.randint(1, 120))

    print("modified data with sample and outcome added")


def modify_dates():
    for entry in data["metadata"]:
        entry["Sample"]["receivedDate"] = date_format_transformer(entry["Sample"]["receivedDate"])
        entry["Sample"]["shippingDate"] = date_format_transformer(entry["Sample"]["shippingDate"])
        entry["Sample"]["collectionDate"] = date_format_transformer(entry["Sample"]["collectionDate"])

        # The following field is newly populated, should be OK
        # entry["Sample"]["recordingDate"] = date_format_transformer(entry["Sample"]["recordingDate"])

        entry["Complication"]["date"] = date_format_transformer(entry["Complication"]["date"])

        entry["Patient"]["dateOfBirth"] = date_format_transformer(entry["Patient"]["dateOfBirth"])
        entry["Patient"]["dateOfDeath"] = date_format_transformer(entry["Patient"]["dateOfDeath"])

        entry["Tumourboard"]["dateOfMolecularTumorBoard"] = date_format_transformer(entry["Tumourboard"]["dateOfMolecularTumorBoard"])

        entry["Consent"]["reconsentDate"] = date_format_transformer(entry["Consent"]["reconsentDate"])
        entry["Consent"]["consentDate"] = date_format_transformer(entry["Consent"]["consentDate"])
        entry["Consent"]["dateOfAssent"] = date_format_transformer(entry["Consent"]["dateOfAssent"])
        entry["Consent"]["dateOfConsentWithdrawal"] = date_format_transformer(entry["Consent"]["dateOfConsentWithdrawal"])


        entry["Enrollment"]["enrollmentApprovalDate"] = date_format_transformer(entry["Enrollment"]["enrollmentApprovalDate"])

        entry["Treatment"]["startDate"] = date_format_transformer(entry["Treatment"]["startDate"])
        entry["Treatment"]["stopDate"] = date_format_transformer(entry["Treatment"]["stopDate"])
        entry["Treatment"]["dateOfRecurrenceOrProgressionAfterThisTreatment"] = date_format_transformer(entry["Treatment"]["dateOfRecurrenceOrProgressionAfterThisTreatment"])

        entry["Diagnosis"]["diagnosisDate"] = date_format_transformer(entry["Diagnosis"]["diagnosisDate"])

        entry["Outcome"]["dateOfAssessment"] = date_format_transformer(entry["Outcome"]["dateOfAssessment"])


def date_format_transformer(date):
    try:
        return datetime.datetime.strptime(date, '%m/%d/%Y').strftime('%Y-%m-%d')
    except ValueError:
        #print("Encountered non-transformable date: " + date)
        return date


def append_additional_modalities():

    for item in additionalModalities:
        data["metadata"].append(item)


def output_file():
    with open(outfile_name, 'w') as outfile:
        json.dump(data, outfile)

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def g_date(start, end):
    return strTimeProp(start, end, '%Y-%m-%d', random.random())

def g_id(group='PATIENT'):
    return '{0}_{1}'.format(group, random.randint(10000,99999))

def g_gender():
    return ['male', 'female'][random.randint(0,1)]

def g_age():
    return str(random.randint(15,80))

def g_version():
    return str(random.randint(1,5))

def g_tumour_stage():
    return str(random.randint(1,4))

def g_drug_list():
    count = random.randint(1,5)
    sample = random.sample(drug_list,count)
    return ', '.join(sample)


ethnicity = [
        "Abkhaz", "Acholi", "Afar", "Agbagyi", "Akan", "Albanians", "Ambundu", 
        "Amhara", "Armenians", "Assamese", "Assyrians", "Aymara", "Azerbaijanis", 
        "Bakongo", "Balochis", "Bamars", "Bambara", "Bashkirs", "Basques", 
        "Belarusians", "Bemba", "Bengalis", "Berbers", "Beti-Pahuin", "Bosniaks", 
        "Brahui", "Bulgarians", "Catalans", "Chechens", "Chuvash", "Circassians", 
        "Chewa", "Cornish", "Corsicans", "Cree", "Croats", "Czechs", "Danes", 
        "Dinka", "Dutch", "English", "Estonians", "Ewe", "Finns", "Fon", "French", 
        "Frisians", "Fula", "Ga-Adangbe", "Gagauz", "Ganda", "Georgians", "Germans", 
        "Greeks", "Guaranis", "Gujarati", "Hadiya", "Han Chinese", "Hausa", "Herero", 
        "Hmong", "Hui", "Hungarians", "Ibibio", "Icelanders", "Igbo", "Ijaw", 
        "Irish", "Italians", "Japanese", "Javanese", "Jews", "Kannadigas", "Kanuri", 
        "Karakalpaks", "Karen", "Kashmiris", "Kazakhs", "Khas", "Khmer", "Kikuyu", 
        "Konkani", "Koreans", "Kukis", "Kurds", "Kyrgyz", "Lango", "Lao", "Latvians", 
        "Lithuanians", "Laz", "Luba", "Luo", "Lurs", "Macedonians", "Malays", "Malayali", 
        "Maldivians", "Maltese", "Manchu", "Mandinka", "Mapuche", "Marathi", "Mayans", 
        "Minangkabau", "Mongo", "Mongols", "Montenegrins", "Naga", "Norwegians", 
        "Nubians", "Nuer", "Nuristanis", "Odia", "Oromo", "Ossetians", "Ovambo", 
        "Ovimbundu", "Pashtuns", "Persians", "Poles", "Portuguese", "Punjabis", 
        "Pedi", "Rohingyas", "Romanians", "Romani", "Russians", "Samoans", 
        "Sara", "Sardinians", "Scottish", "Serbs", "Shan", "Shona", "Sindhis", 
        "Sinhalese", "Slovaks", "Slovenes", "Soga", "Somalis", "Songhai", 
        "Soninke", "Sotho", "Sundanese", "Sukuma", "Swazi", "Swedes", 
        "Tagalogs", "Tamils", "Thais", "Tatars", "Telugu", "Temne", "Tibetans", 
        "Tigrayans/Tigrinyas", "Tswana", "Turks", "Turkmens", "Ukrainians", 
        "Uyghur", "Uzbeks", "Vietnamese", "Welsh", "Wolof", "Xhosa", "Yakuts", 
        "Yoruba", "Zhuang", "Zulu"] + ["Canadian"]*200 + ["French"]*20 + ["Chinese"]*30 + ["English"]*20

race = ["Caucasian", "Aboriginal", "Black/African American", "Asian"]

province = ["Ontario", "Quebec", "British Columbia", "Alberta", "Manitoba", "Saskatchewan", "Nova Scotia", "New Brunswick", "Newfoundland and Labrador", "Prince Edward Island", "Northwest Territories", "Yukon", "Navanut"]

# account for site province likelihood
gsc_province = province + ["British Columbia"] * 40
to_province = province + ['Ontario'] * 40
mo_province = province + ['Quebec'] * 40

tissue = ["Gut/ alimentary canal", "Mouth", "Teeth / jaw", "Tongue samples/ whole", "Salivary glands samples/ whole", "Parotid glands samples/ whole", "Submandibular glands samples/ whole", "Sublingual glands samples/ whole", "Pharynx whole", "Esophagus samples/ whole", "Stomach samples/ whole", "Small intestine samples/ whole", "Duodenum samples/ whole", "Jejunum samples/ whole", "Ileum samples/ whole", "Large intestine samples/ whole", "Liver samples/ whole", "Gallbladder samples/ whole", "Pancreas samples/ whole", "Nose samples/ whole", "Pharynx whole", "Larynx wholeglandular vertical", "Trachea whole", "Bronchi samples/ whole", "Lung tissue samples/ lung lobe/ whole lung", "Diaphragm", "Kidney tissue samples/ renal samples", "Ureters samples/ whole", "Bladder samples/ whole", "Urethra samples/ whole", "Pituitary gland whole", "Pineal gland whole", "Thyroid gland samples/ whole", "Parathyroid glands whole", "Adrenal glands whole", "Pancreas samples/ whole", "Cardiovascular", "vertical kidney rhsHeart samples/whole", "Artery samples", "Vein samples", "Capillaries", "Blood, serum, plasma, buffy coat samples", "Lymphatic vessel samples/ whole", "Lymph node samples/ whole", "Bone marrow samples", "Thymus samples/ whole", "Spleen samples/ whole", "Central nervous system", "Brain samples/ whole", "Cerebral hemispheres samples/ whole", "Diencephalon", "Brainstem whole", "Midbrain whole", "Pons whole", "Medulla oblongata whole", "Cerebellum samples/ whole", "Spinal cord samples/ whole", "Ventricular system-", "Choroid plexus", "Eye", "Cornea", "Iris ", "Ciliary body", "Lens", "Retina ", "Ear", "Skin", "Subcutaneous tissue", "Mammary glands", "Musculoskeletal system:", "Muscles samples/ whole", "Tendons samples/ whole", "Ligaments samples/ whole", "Joints samples/ whole", "Bones samples/ whole", "Skull", "Spine samples/ whole", "Fallopian tubes", "Uterus samples/ whole", "Vagina", "Vulva", "Clitoris", "Placenta samples/ whole", "Testes samples/ whole", "Epididymis", "Vas deferens", "Seminal vesicles", "Prostate samples/ whole", "Bulbourethral glands", "External sex organs", "Penis", "Scrotum"]
risk_factor = ["High blood pressure", "Tobacco use", "High blood glucose", "Physical inactivity", "Overweight and obesity", "High cholesterol", "Unprotected sex", "Alcohol use", "Childhood underweight", "Indoor smoke from solid fuels"]
predisposition = ["Hereditary Breast & Ovarian Cancer Syndrome", "Cowden Syndrome", "Hereditary Non-polyposis Colorectal Cancer Syndrome (Lynch Syndrome)", "Familial Adenomatous Polyposis (FAP)", "Li-Fraumeni Syndrome", "Von Hippel-Lindau Disease", "Multiple Endocrine Neoplasias"]
environmental = ["Acrylamide", "Air Pollution", "Allergens & Irritants", "Cigarette Smoke", "Cockroaches", "Dust Mites", "Pets & Animals", "Pollen", "Aloe Vera", "Arsenic", "Bisphenol A (BPA)", "Cell Phones", "Climate Change", "Dioxins", "Electric & Magnetic Fields", "Endocrine Disruptors", "Essential Oils", "Flame Retardants", "Formaldehyde", "Ginkgo", "Harmful Algal Blooms", "Hazardous Material/Waste", "Hexavalent Chromium", "Hydraulic Fracturing & Health", "Lead", "Mercury", "Mold", "Nanomaterials", "Ozone", "Perfluorinated Chemicals (PFCs)", "Pesticides", "Radon", "Soy Infant Formula", "Styrene", "Water Pollution", "Weather Extremes"]

hospital = ['Hospital for Sick Children', 'Princess Margaret Cancer Centre', 'University Health Network', "Canada's Michael Smith Genome Sciences Centre", 'McGill University and Genome Quebec Innovation Centre']
oncologist = ["Dr. Shuaib Callahan", "Dr. Chelsey Cornish", "Dr. Veer Moses", "Dr. Hendrix Ryan", "Dr. Nora Hussain", "Dr. Kaya Hall", "Dr. Lisa-Marie Schwartz", "Dr. Kristopher Buckley", "Dr. Favour Needham", "Dr. Abel Adam"]
physician = ["Dr. Darcey Davila", "Dr. Katie Cruz", "Dr. Ubaid Walsh", "Dr. Abdullahi Horne", "Dr. Calum Leach", "Dr. Yannis Cooper", "Dr. Elicia Peters", "Dr. Ellie-May Bass", "Dr. Zohaib Bennett", "Dr. Mai Alfaro"]
coordinator = ["Dr. Gracey Shepherd", "Dr. Kady Hahn", "Dr. Lucinda Bishop", "Dr. Coco Mcbride", "Dr. Md Hardin", "Dr. Zayyan Barrett", "Dr. Florrie Keeling", "Dr. Brooklyn Herrera", "Dr. Alara Piper", "Dr. Kester Ali"]
cancer_type = ["Bladder cancer", "Lung cancer", "Brain cancer", "Melanoma", "Breast cancer", "Non-Hodgkin lymphoma", "Cervical cancer", "Ovarian cancer", "Colorectal cancer", "Pancreatic cancer", "Esophageal cancer", "Prostate cancer", "Kidney cancer", "Skin cancer", "Leukemia", "Thyroid cancer", "Liver cancer", "Uterine cancer"]

tumour_grade = ["GX: Grade cannot be assessed (undetermined grade)", "G1: Well differentiated (low grade)", "G2: Moderately differentiated (intermediate grade)", "G3: Poorly differentiated (high grade)", "G4: Undifferentiated (high grade)"]
sample_type = ['peripheral blood', 'primary solid tumour', 'recurrent solid tumour', 'bone marrow', 'metastatic']


death_cause = ['Disease','Infection','Cardiovascular disease','Cancer','Stroke','Complication','Diabetes mellitus','Myocardial infarction','Acute disease','Cardiac arrest','Bleeding','Pneumonia','Coronary artery disease','Hypertension','Brain death','Heart failure','Brainstem death','Sepsis','Dementias','Depression','Lung cancer','Tuberculosis','Chronic Obstructive Pulmonary Disease','Breast cancer']

# weighted for biopsy
diagnosis_method = ['biopsy', 'bone scan', 'blood test', 'x-ray', 'MRI', 'CT Scan', 'PET Scan'] + ['biopsy'] *10

tumour_response = ['Complete Response', 'Partial Response', 'Stable Disease', 'Progressive Disease']

classification = ['Adenocarcinoma', 'Blastoma', 'Carcinoma', 'Leukemia', 'Lymphoma', 'Myeloma', 'Sarcoma']

modality = ['Surgery', 'Chemotherapy', 'Radiation therapy', 'Immunotherapy', 'Hormonal therapy']

fnull = [True, False] + [False]*65

drug_list = ['Aait', 'Abiraterone', 'Abraxane', 'Abt-888', 'Accutane', 'Acetazolamide', 'Afatinib', 'Ags67e', 'Alectinib', 'Alemtuzumab', 'Aliskiren', 'Anastrozole', 'Anastrozole/placebo', 'Asa', 'Atezolizumab', 'Atezolizumab/placebo', 'Avelumab', 'Azacitidine', 'Azd1775', 'Azd2171', 'Azd5363', 'Azd8931', 'Azd9291', 'Bay 73-4506', 'Bbi608', 'Bbi608/placebo', 'Bendamustine', 'Bevacizumab', 'Bibw2992', 'Bicalutamide', 'Bkm120', 'Bkm120/placebo', 'Bleomycin', 'Bms-936558', 'Bms-986115', 'Bms-986205', 'Bromocriptine', 'Buparlisib', 'Buserelin', 'Busulfan', 'Cabozantinib', 'Candesartan', 'Capecitabine', 'Carboplatin', 'Carmustine', 'Cediranib', 'Ceritinib', 'Cetuximab', 'Cfi-402257', 'Chlorambucil', 'Chlordiazepoxide', 'Cisplatin', 'Clodronate', 'Co-1686', 'Cobimetinib', 'Copanlisib', 'Cortisone', 'Crizotinib', 'Cx-5461', 'Cyclophosphamide', 'Cytarabine', 'Dabrafenib', 'Dacarbazine', 'Dacarbazine/placebo', 'Dactinomycin', 'Degarelix', 'Demcizumab', 'Demcizumab/placebo', 'Dexamethasone', 'Dexrazoxane', 'Docetaxel', 'Dovitinib', 'Doxorubicin', 'Durvalumab', 'Durvalumab(moind228)', 'Enmd-2076', 'Enzalutamide', 'Epirubicin', 'Eribulin', 'Erlotinib', 'Etoposide', 'Everolimus', 'Exemestane', 'Faslodex', 'Filgrastim', 'Fludarabine', 'Fludarabinepo', 'Fludrocortisone', 'Fluorouracil', 'Flutamide', 'Folfiri', 'Fulvestrant', 'Fulvestrant/placebo', 'Ganetesip', 'Gefitinib', 'Gemcitabine', 'Gifirinox', 'Goserelin', 'Hepasphere', 'Herceptin', 'Hydrocortisone', 'Hydroxyurea', 'Ibrutinib', 'Ifosfamide', 'Imatinib', 'Imc-1121b', 'Imgn', 'Imiquimod', 'Immunotherapy', 'Interferon', 'Iodine-131', 'Iph2201', 'Ipilimumab', 'Irbesartan', 'Irinotecan', 'Lambrolizumab', 'Lanreotide', 'Lapatinib', 'Lcl161', 'Ldk378', 'Lee011', 'Lee011/placebo', 'Lenvatinib', 'Letrozole', 'Leucovorin', 'Leuprolide', 'Lomustine', 'Lutetium-177', 'Ly3076226', 'Medi4736', 'Medroxyprogesterone', 'Megestrol', 'Mek162', 'Melphalan', 'Mesna', 'Metformin', 'Metformin/placebo', 'Methotrexate', 'Mgcd265', 'Mitomycin', 'Mitotane', 'Monalizumab', 'Moxr0916', 'Mpdl3280a', 'Mpdl3280a/placebo', 'Napabucasin', 'Naringenin', 'Nilotinib', 'Nintedanib', 'Nintedanib/placebo', 'Niraparib', 'Nivolumab', 'Nktr-102', 'Octreotide', 'Olaparib', 'Olaratumab', 'Olaratumab/placebo', 'Osimertinib', 'Oxaliplatin', 'Paclitaxel', 'Paclitaxel-nab', 'Palbociclib', 'Pamidronate', 'Panitumumab', 'Pazopanib', 'Pd-0332991', 'Pd-0332991/placebo', 'Pegfilgrastim', 'Pembrolizumab', 'Pemetrexed', 'Pertuzumab', 'Pf-04518600', 'Pki-587', 'Pf-05212384', 'Prednisone', 'Procarbazine', 'Raltitrexed', 'Ramucirumab', 'Ramucirumab/plac', 'Regorafenib', 'Reolysin', 'Ribociclib', 'Ribociclib/placebo', 'Rituximab', 'Rociletinib', 'Romidepsin', 'Rucaparib', 'Sapitinib', 'Selumetinib', 'Slc-0111', 'Sorafenib', 'Streptozocin', 'Sunitinib', 'Talazoparib', 'Tamoxifen', 'Taselisib', 'Taselisib/placebo', 'Telmisartan', 'Temozolomide', 'Temsirolimus', 'Thyrotropin', 'Tipiracil', 'Topotecan', 'Trabectedin', 'Trametinb', 'Trametinib', 'Trastuzumab', 'Tremelimumab', 'Trifluridine', 'Trifluridine-tipiracil', 'Vandetanib', 'Veliparib', 'Vemurafenib', 'Vinblastine', 'Vincristine', 'Vinorelbine', 'Vismodegib', 'Vorinostat', 'Yttrium-90', 'Zactima', 'Zactima/placebo', 'Imgn folate receptor', 'Hyperthermia', 'Bms-936558/placebo', 'Bibw', 'Cytotoxic cells therapy', 'Nk t cells', 'Gedatolisib', 'Sapitinib/placebo', 'Vandetanib/placebo', 'Ramucirumab/placebo', 'Etirinotecan pegol', 'Buparlisib/placebo', 'Palbociclib/placebo', 'Napabucasin/placebo', 'Aspirin', 'Imgn853', 'Istodax', 'Binimetinib', 'Nivolumab/placebo']

if __name__ == "__main__":
    print("Running main...")
    main()
    print("Inserting labkey tables...")
    insert_labkey_tables()
    print("Cleaning up data...")
    remove_deleted_fields()
    modify_dates()
    print("Inserting supporting records...")
    append_additional_modalities()
    output_file()
    print(">>> {} generated.".format(outfile_name))