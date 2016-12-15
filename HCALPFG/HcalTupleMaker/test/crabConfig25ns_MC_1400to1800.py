from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HFTree25nsMC_v2_1400to1800'
config.General.workArea = 'crab25nsMC_v2_1400to1800'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'noiseAnalysis_CollisionData_RECO_cfg.py'

config.Data.inputDataset = '/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25nsRecodebug_MCRUN2_74_V9-v1/GEN-SIM-RECODEBUG'                     

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_HFTree25nsMC_v2_1400to1800'

config.Site.storageSite = 'T2_IN_TIFR'
