import FWCore.ParameterSet.Config as cms
from SimCalorimetry.HcalSimProducers.hcalSimParameters_cfi import *

# make a block so other modules, such as the data mixing module, can
# also run simulation

hcalSimBlock = cms.PSet(    
    hcalSimParameters,
    # whether cells with MC signal get noise added
    doNoise = cms.bool(True),
    # whether cells with no MC signal get an empty signal created
    # These empty signals can get noise via the doNoise flag
    doEmpty = cms.bool(True),
    doHPDNoise = cms.bool(False),
    doIonFeedback = cms.bool(True),
    doThermalNoise = cms.bool(True),
    HBTuningParameter = cms.double(0.65),
    HETuningParameter = cms.double(0.65),
    HFTuningParameter = cms.double(0.65),
    HOTuningParameter = cms.double(0.65),
    #HPDNoiseLibrary = cms.PSet(
    #   FileName = cms.FileInPath("SimCalorimetry/HcalSimAlgos/data/hpdNoiseLibrary.root"),
    #   HPDName = cms.untracked.string("HPD")
    #),
    doTimeSlew = cms.bool(True),
    doHFWindow = cms.bool(True),
    hitsProducer = cms.string('g4SimHits'),
    injectTestHits = cms.bool(False)
)


simHcalUnsuppressedDigis = cms.EDProducer("HcalDigiProducer",
    hcalSimBlock
)



