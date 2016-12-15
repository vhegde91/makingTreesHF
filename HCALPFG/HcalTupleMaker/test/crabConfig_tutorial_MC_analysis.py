from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'HFTreeMC_800to1000'
config.General.workArea = 'crabMC_800to1000'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'analysis_CollisionData_Noise_Run2SingleMethod_RECO_cfg.py'

#config.Data.inputDataset ='/QCD_Pt_15to30_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v1/GEN-SIM-RECODEBUG'
#config.Data.inputDataset ='/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'
#config.Data.inputDataset ='/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v1/GEN-SIM-RECODEBUG'
#config.Data.inputDataset ='/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'
#config.Data.inputDataset ='/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'
#config.Data.inputDataset ='/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v1/GEN-SIM-RECODEBUG'
#config.Data.inputDataset = '/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'
#config.Data.inputDataset = '/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v1/GEN-SIM-RECODEBUG'
#config.Data.inputDataset = '/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'
config.Data.inputDataset = '/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v3/GEN-SIM-RECODEBUG'
#config.Data.inputDataset = '/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v1/GEN-SIM-RECODEBUG'
#config.Data.inputDataset = '/QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'
#config.Data.inputDataset ='/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'
#config.Data.inputDataset ='/QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'
#config.Data.inputDataset ='/QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt50nsRecodebug_MCRUN2_74_V9A-v2/GEN-SIM-RECODEBUG'

config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = 'CRAB3_HFTreeMC_800to1000'

config.Site.storageSite = 'T2_IN_TIFR'

