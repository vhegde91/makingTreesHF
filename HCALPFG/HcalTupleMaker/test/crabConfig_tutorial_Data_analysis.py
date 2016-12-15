from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HF2016H_v2_V2_JetHT'
config.General.workArea = 'crab_projectRun_2016H_v2_V2_JetHT'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'noiseAnalysis_CollisionData_RECO_cfg.py'

#config.Data.inputDataset = '/JetHT/Run2016B-PromptReco-v2/RECO'
#config.Data.inputDataset = '/JetHT/Run2016C-PromptReco-v2/RECO'
#config.Data.inputDataset = '/ExpressPhysics/Run2016D-Express-v2/FEVT'
#config.Data.inputDataset = '/SingleMuon/Run2016B-PromptReco-v2/RECO'
#config.Data.inputDataset = '/JetHT/Run2016E-PromptReco-v2/RECO'
#config.Data.inputDataset = '/JetHT/Run2016F-PromptReco-v1/RECO'
#config.Data.inputDataset = '/JetHT/Run2016G-PromptReco-v1/RECO'
config.Data.inputDataset = '/JetHT/Run2016H-PromptReco-v2/RECO'
#config.Data.inputDataset = '/JetHT/Run2016H-PromptReco-v3/RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.lumiMask = '/afs/cern.ch/work/v/vhegde/public/HF_new/CMSSW_8_0_14/src/HCALPFG/HcalTupleMaker/test/crab_projectRun_2016H_v2_JetHT/crab_HF2016H_v2_JetHT/results/notFinishedLumis.json'
config.Data.runRange = '273158-284044'#'273158-280385'#'273158-279931'#'273158-277148'#'275375-276384' #'274241-274387'#'273448,273492-273728'
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_HF2016H_v2_V2_JetHT'
#config.Data.ignoreLocality = True
#config.Data.allowNonValidInputDataset = True

config.Site.storageSite = 'T2_IN_TIFR'
