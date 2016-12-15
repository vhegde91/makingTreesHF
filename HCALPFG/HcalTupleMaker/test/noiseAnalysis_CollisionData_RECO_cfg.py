#------------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------------
import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras
import FWCore.ParameterSet.VarParsing as VarParsing


#------------------------------------------------------------------------------------
# Declare the process and input variables
#------------------------------------------------------------------------------------
#process = cms.Process('NOISE',eras.Run2_50ns)#for 50ns 13 TeV data
process = cms.Process('NOISE',eras.Run2_25ns)#for 25ns 13 TeV data
options = VarParsing.VarParsing ('analysis')
options.register ('skipEvents', 0, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "no of skipped events")
#options.inputFiles = 'root://xrootd-cms.infn.it//store/data/Run2016B/SingleMuon/RECO/PromptReco-v2/000/273/158/00000/00169924-201A-E611-A087-02163E013590.root'
#options.inputFiles = 'root://xrootd-cms.infn.it//store/data/Run2016B/JetHT/RECO/PromptReco-v2/000/273/150/00000/CC80E0AF-DA19-E611-BF0D-02163E014456.root'
#options.inputFiles = 'file:/afs/cern.ch/work/v/vhegde/public/HF2016/CMSSW_8_0_7_patch1/src/HCALPFG/HcalTupleMaker/test/Run2016JetHT_273150_50Events.root'
#options.inputFiles = 'root://xrootd.unl.edu///store/mc/RunIISpring15DR74/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/GEN-SIM-RECODEBUG/Asympt25nsRecodebug_MCRUN2_74_V9-v1/80000/003C3FDF-9302-E511-8BB7-0025902008AC.root'
#options.inputFiles = 'root://xrootd.unl.edu///store/data/Run2015D/JetHT/RECO/PromptReco-v4/000/258/159/00000/6269BC62-D16B-E511-A54D-02163E011A36.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016B/JetHT/RECO/PromptReco-v2/000/273/158/00000/0CD0D922-DF19-E611-AF37-02163E0144DF.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/express/Run2016D/ExpressPhysics/FEVT/Express-v2/000/276/811/00002/FEE81C6C-4E4A-E611-B0BF-02163E011C55.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/mc/RunIISpring16DR80/QCD_Pt-15to7000_TuneCUETP8M1_Flat_13TeV_pythia8/GEN-SIM-RECO/PUSpring16_RECO_NZS_80X_mcRun2_asymptotic_2016_v3-v1/80000/2274BE6B-F633-E611-B1AD-001517E73B50.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016C/JetHT/RECO/PromptReco-v2/000/275/603/00000/16341968-8A3A-E611-A113-02163E01351C.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016B/JetHT/RECO/PromptReco-v2/000/275/376/00001/FCB8DA49-FA39-E611-8B35-02163E013942.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/express/Run2016C/ExpressPhysics/FEVT/Express-v2/000/275/420/00000/1CB6F1B7-AF37-E611-8211-02163E011D5E.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016B/JetHT/AOD/01Jul2016-v1/00000/4EBB55E7-AC42-E611-BC6E-002590495244.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016B/JetHT/RECO/PromptReco-v2/000/275/376/00000/EAB61E1A-C339-E611-83FF-02163E014144.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016C/JetHT/RECO/PromptReco-v2/000/275/656/00000/F636D37A-483B-E611-A7D4-02163E012312.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016E/JetHT/RECO/PromptReco-v2/000/276/831/00000/003659D9-DA4C-E611-8801-02163E012271.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016F/JetHT/RECO/PromptReco-v1/000/278/018/00000/00123117-405A-E611-AC27-02163E013877.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016G/JetHT/RECO/PromptReco-v1/000/278/820/00000/0019DF04-E463-E611-8431-02163E0136E8.root'
options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016H/JetHT/RECO/PromptReco-v3/000/284/036/00000/0AB663D8-039F-E611-90FE-02163E011C68.root'
#options.inputFiles = 'root://xrootd-cms.infn.it///store/data/Run2016B/JetHT/AOD/23Sep2016-v3/00000/003EC773-5797-E611-A173-002590E7D7C2.root'
#options.inputFiles = 'file:24BB20F0-0F9F-E611-95D5-FA163EC77B7C.root'
#options.outputFile = 'results.root'

options.maxEvents = -1 # -1 means all events
#options.skipEvents = 0 # default is 0.


#------------------------------------------------------------------------------------
# Get and parse the command line arguments
#------------------------------------------------------------------------------------
options.parseArguments()
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.source = cms.Source("PoolSource",
    fileNames  = cms.untracked.vstring(options.inputFiles),
    skipEvents = cms.untracked.uint32(options.skipEvents) # default is 0.
)

process.TFileService = cms.Service("TFileService",
#      fileName = cms.string('HF2016B_MC.root')
      fileName = cms.string('HF_2016.root')
#     fileName = cms.string(options.outputFile)
)


#------------------------------------------------------------------------------------
# import of standard configurations
#------------------------------------------------------------------------------------
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
#process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
#vvvprocess.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')


#------------------------------------------------------------------------------------
# Set up L1 Jet digis #Disabled 
#------------------------------------------------------------------------------------
#process.load("HCALPFG.HcalTupleMaker.HcalL1JetDigisProducer_cfi")


#------------------------------------------------------------------------------------
# Set up our analyzer
#------------------------------------------------------------------------------------
#process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_cfi") # Dont want to use this, load modules individually
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Tree_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Event_cfi")
#vvvprocess.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HBHEDigis_cfi")
#vvvprocess.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HBHERecHits_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HFRecHits_cfi")
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_Trigger_cfi")


#------------------------------------------------------------------------------------
# Set up noise filters
#------------------------------------------------------------------------------------
#vvvprocess.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HcalNoiseFilters_cfi") # This is over-ridden below to remove Method0-Method2 dual reco.
#------------------------------------------------------------------------------------
# Set up iso noise filter parameters, used for iso-noise filter study in 25ns.
#------------------------------------------------------------------------------------
#vvvprocess.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_HcalIsoNoiseFilterParameters_cfi")
#------------------------------------------------------------------------------------
# Set up CaloJetMet quantities 
#------------------------------------------------------------------------------------
process.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_CaloJetMet_cfi") # This is over-ridden below to remove Method0-Method2 dual reco.
#------------------------------------------------------------------------------------
# Set up MuonTrack quantities 
#------------------------------------------------------------------------------------
#vvvprocess.load("HCALPFG.HcalTupleMaker.HcalTupleMaker_MuonTrack_cfi")


#------------------------------------------------------------------------------------
# Specify Global Tag
#------------------------------------------------------------------------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v4'
#process.GlobalTag.globaltag = '76X_dataRun2_v16'
#process.GlobalTag.globaltag = '80X_dataRun2_Prompt_v8'
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag = autoCond['run2_data']


############################################# Changes made by vinay for filtering events based on triggers ##########################################
#------------------------------------------------------------------------------------
# Disabled since we dont deal with HLT
#------------------------------------------------------------------------------------
process.my_hlt = cms.EDFilter("HLTHighLevel",
     TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
#     HLTPaths = cms.vstring("HLT_L1SingleJet16*"), # provide list of HLT paths (or patterns) you want
                              HLTPaths = cms.vstring("HLT_CaloJet500_NoJetID_*",
                                                     "HLT_DiPFJetAve500_*",
                                                     "HLT_PFHT750_4JetPt50_*",
                                                     "HLT_PFHT800_*",
                                                     "HLT_PFJet450_*"),
#                              HLTPaths = cms.vstring("HLT_IsoTkMu22_*",
#                                                     "HLT_IsoMu22_*"
#                                                     "HLT_Mu50_*"),
    eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
    andOr = cms.bool(True),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
    throw = cms.bool(False)    # throw exception on unknown path names
)
############################################# Changes made by vinay end here ##### (by default all these were commneted ############################# 

#------------------------------------------------------------------------------------
#Remove Method 0, Rename Method 2 as "default" where necessary:
#------------------------------------------------------------------------------------
process.hcalTupleCaloJetMet = cms.EDProducer("HcalTupleMaker_CaloJetMet",
         recoInputTag         = cms.untracked.string("hbhereco"),
         Prefix = cms.untracked.string(""),
         Suffix = cms.untracked.string("")
)
process.hcalTupleHcalNoiseFilters = cms.EDProducer("HcalTupleMaker_HcalNoiseFilters",
         noiseSummaryInputTag = cms.untracked.InputTag("hcalnoise"),
         noiseResultInputTag  = cms.untracked.string("HBHENoiseFilterResultProducer"),
         recoInputTag         = cms.untracked.string("hbhereco"),
         isRAW  = cms.untracked.bool(False), # new Flag necessary for HcalNoiseFilters to run on RECO data
         isRECO = cms.untracked.bool(True), 
         Prefix = cms.untracked.string(""),
         Suffix = cms.untracked.string("")
)


#------------------------------------------------------------------------------------
# Place-holder for applying HBHE noise filter:
#------------------------------------------------------------------------------------
#process.ApplyBaselineHBHENoiseFilter = cms.EDFilter('BooleanFlagFilter',
#    inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),    
#    #inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResultRun1'),
#    #inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResultRun2Loose'),
#    #inputLabel = cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResultRun2Tight'),
#    reverseDecision = cms.bool(False)
#)


#------------------------------------------------------------------------------------
# This enables NEF flagging, but needs reconstruction of RAW data.
# This is not needed for datasets reconstructed with >=CMSSW748:
# i.e. 2015C Prompt-reco has NEF flags computed out-of-the-box.
#------------------------------------------------------------------------------------
#process.hbheprereco.setNegativeFlags          = cms.bool(True)

process.goodOfflinePrimaryVertices = cms.EDFilter("VertexSelector",
#process.VertexCollection = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof >= 4.0 && abs(z) <= 24.0 && abs(position.Rho) <= 2.0"),
    filter = cms.bool(False)
)

#------------------------------------------------------------------------------------
# HcalTupleMaker sequence definition
#------------------------------------------------------------------------------------
process.tuple_step = cms.Sequence(
#    process.VertexCollection*
    process.goodOfflinePrimaryVertices*
    # Make HCAL tuples: Event, run, ls number
    process.hcalTupleEvent*
    # Make HCAL tuples: FED info
    #    process.hcalTupleFEDs*
    #    # Make HCAL tuples: digi info
    #raw# process.hcalTupleHBHEDigis*
    #    process.hcalTupleHODigis*
    #    process.hcalTupleHFDigis*
    #    process.hcalTupleTriggerPrimitives*
    #    # Make HCAL tuples: digi info
    #    process.hcalTupleHBHECosmicsDigis*
    #    process.hcalTupleHOCosmicsDigis*
    #    # Make HCAL tuples: digi info
    #    process.hcalTupleHBHEL1JetsDigis*
    #    process.hcalTupleHFL1JetsDigis*
    #    process.hcalTupleL1JetTriggerPrimitives*
    #    # Make HCAL tuples: reco info
#vvv    process.hcalTupleHBHERecHits*
    process.hcalTupleHFRecHits*
#vvv    process.hcalTupleHcalNoiseFilters*
#vvv    process.hcalTupleHcalIsoNoiseFilterParameters* #for studying iso-noise-filter
    process.hcalTupleCaloJetMet*
#vvv    process.hcalTupleMuonTrack*
    #
    #process.hcalTupleHBHERecHitsMethod0*
    #process.hcalTupleHcalNoiseFiltersMethod0*
    #process.hcalTupleCaloJetMetMethod0*
    #    process.hcalTupleHORecHits*
    #    process.hcalTupleHFRecHits*
    #    # Trigger info
    process.hcalTupleTrigger*
    
    #    process.hcalTupleTriggerObjects*
    #    # L1 jet info
    #    process.hcalTupleL1Jets*
    #    # Make HCAL tuples: cosmic muon info
    #    process.hcalTupleCosmicMuons*
    #    # Package everything into a tree
    #
    process.hcalTupleTree
)


#-----------------------------------------------------------------------------------
# Path and EndPath definitions
#-----------------------------------------------------------------------------------
process.preparation = cms.Path(
    process.my_hlt *
    #process.RawToDigi * #needed for RAW files
    #process.L1Reco *
    #rprocess.reconstruction * #needed for RAW files
    #process.caloglobalreco *
    #process.reconstructionCosmics *
    #
    #process.horeco *
    #process.hfreco *
    #
    #process.hbheprerecoMethod0 *
    #process.hbheprerecoMethod2 *
    #process.hbherecoMethod0 *
    #process.hbherecoMethod2 *
    #
    #process.towerMakerMethod0 *
    #process.towerMakerMethod2 *
    #
    #process.hcalnoiseMethod0 *
    #process.hcalnoiseMethod2 *
    #
    #process.HBHENoiseFilterResultProducerMethod0 *
    #process.HBHENoiseFilterResultProducerMethod2 *
    #
    #
    #process.hcalCosmicDigis *
    #process.hcalL1JetDigis *
    #
    #process.hcalnoise *  #needed for RAW files
#vvv    process.HBHENoiseFilterResultProducer *
    #process.ApplyBaselineHBHENoiseFilter *
    #
    process.tuple_step
)
