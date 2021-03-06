#! /usr/bin/env python
from argparse import ArgumentParser, RawTextHelpFormatter
import ROOT
ROOT.SetMemoryPolicy(ROOT.kMemoryStrict)

slim_samples = ["./samples/nanotree.root"]

# samples = [
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/5328123C-B5B1-7240-982C-91C22BFBFF59.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/8633326F-CA38-4446-9629-10B1347ED382.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/4AA64837-7A3A-2C4A-A7FE-CCD5FEFB6775.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/F08E36CF-94D2-0946-BFBE-BBC75FE0AE71.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/BEFED70C-D7E6-994A-8BEA-B526C3B359AD.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/557A957A-E9E5-E246-8229-D0A0AE495B30.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/E80005ED-3698-C446-B3A1-E0FBE7080560.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/B9C94331-05BF-1A45-90E8-06A8A009B159.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/1B6191AA-449D-3A45-9CDF-C0D4202AAF81.root",
#     "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/0B711A4B-9FC6-C84A-A01E-87DAAAF69CCB.root"]
samples = [
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/5328123C-B5B1-7240-982C-91C22BFBFF59.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/8633326F-CA38-4446-9629-10B1347ED382.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/4AA64837-7A3A-2C4A-A7FE-CCD5FEFB6775.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/F08E36CF-94D2-0946-BFBE-BBC75FE0AE71.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/BEFED70C-D7E6-994A-8BEA-B526C3B359AD.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/557A957A-E9E5-E246-8229-D0A0AE495B30.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/E80005ED-3698-C446-B3A1-E0FBE7080560.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/B9C94331-05BF-1A45-90E8-06A8A009B159.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/1B6191AA-449D-3A45-9CDF-C0D4202AAF81.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/0B711A4B-9FC6-C84A-A01E-87DAAAF69CCB.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/0AD64945-42B2-2F43-B41A-FCF1504C7545.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/220567B5-ED66-1243-ABF0-5EB8729568A7.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/54F3FC94-9AD4-2449-A288-64EF3965D04D.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/667864B5-00BD-824E-8027-4AE3890A36BF.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/AF090711-780B-8642-94E1-338103A17F67.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/FC93EBFA-C1D6-6C47-B662-BD18B10F2965.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/D948ED2A-ABEA-1E4F-A98D-D922A009A9B4.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/EF2BE14B-C2F0-1C41-BC59-83990AB4ECFE.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/D960041D-C435-A94E-8D09-6F76DEFF672D.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/848B8154-682D-CE4B-BDF7-B28086C6ACE8.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/B2E1513F-B352-784B-A60C-BE2F9D96E4D7.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/DCE0E5C3-7C9E-F148-92F6-72C76C3CD10D.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/A349BF70-4E19-2D48-96F0-4B0C0CCDE394.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/002DC5D6-3515-D949-BD26-59B897A7E0B4.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/0F9769D4-425A-F94B-AA7B-309179396F0D.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/0858B12E-E3FC-E841-994E-725321AAFA43.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/0092D3B4-722E-214B-9402-C885AD7C6DD8.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/819BA76F-CA87-9340-9AC4-2DDA4D581FD0.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/C2B1234D-724B-C842-B9A1-F302E2689FE7.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/0CEABD0E-3715-3148-8CE3-F862873BF556.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/5A259BBC-8757-0046-88B8-4122052FD74D.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/96005C55-A3C7-3549-B1CF-3709EFEF43A2.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/81EFDA64-5B49-354D-9484-85DE7D05FA2F.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/A0C1F62F-4E50-D64E-90FD-DF4597E80672.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/093A1F81-29A1-B848-9464-E27FF5432FC9.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/673D0556-5988-BA48-8BE8-965B2B36B63E.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/FE7F7C99-F9B1-7F49-A767-193CCAFB4DF7.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/DEF2FBF1-1839-AF48-8922-136706F1FFC9.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/10D46CE8-70CA-494D-BA8E-94E362998DAA.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/D4A65BDD-FB33-D046-A2F5-1E5B8B3D4A85.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/E277E6ED-F3E8-AF45-8C01-A9895DDD5E0E.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/5E83033F-A5CC-7C4D-8736-0E6A7C9DA3E6.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/E08EBF0E-A0DB-2A4F-AD98-0A097EFF8B8B.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/6EE0B929-E374-ED45-8F8D-24D201F928CA.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/5DE0ADD6-4F10-8F40-A396-BD9A1D431642.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/946E1F89-7B57-1E4C-8A71-2AF1F9842B79.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/1BF8E3C7-7247-934D-B135-8C6491CC4E6C.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/9C97DE2B-F887-6343-93BA-480D284758A7.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/22416824-5291-D94E-8475-9A8DDCF25CE6.root",
    "root://cmsxrootd.fnal.gov//store/mc/RunIIFall17NanoAODv6/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/PU2017_12Apr2018_Nano25Oct2019_ext_102X_mc2017_realistic_v7-v1/250000/99E550CD-9057-D948-BDC7-D411E3A8567B.root"]


def doAll(slimmed=False, debug=False, sample=None, nsamples=10):
    if slimmed:
        if not sample:
            sample = 0
        # Make TChain
        mc = ROOT.TChain("Events")
        mc.Add(slim_samples[0])
        # Run ScanChain
        print("Running ScanChain over the following file:")
        print(slim_samples[0])
        ROOT.ScanChain(mc, "output/ttjets_fakes_slim.root")
    else:
        # Load .so files
        ROOT.gROOT.ProcessLine(".L ./NanoCORE/NANO_CORE.so");
        ROOT.gROOT.ProcessLine(".L ./monolep.C+");
        ROOT.gROOT.ProcessLine(".L MonolepChain.C+");
        if not sample:
            for i, sample in enumerate(samples):
                if i <= 29: continue
                # Make TChain
                mc = ROOT.TChain("Events")
                mc.Add(sample)
                # Run ScanChain
                print("Running ScanChain over the following file:")
                print(sample)
                ROOT.MonolepChain(mc, "output/ttbar-monolep_btags_{}.root".format(i))
                if debug:
                    break
        else:
            # Make TChain
            mc = ROOT.TChain("Events")
            mc.Add(samples[sample])
            # Run ScanChain
            print("Running ScanChain over the following file:")
            print(samples[sample])
            ROOT.MonolepChain(mc, "output/ttbar-monolep_btags_{}.root".format(sample))

    return

if __name__ == "__main__":
    # CLI
    argparser = ArgumentParser(description='Run looper',
                               formatter_class=RawTextHelpFormatter)
    # Number of samples
    argparser.add_argument('--nsamples', type=int, default=10,
                           help='Number of samples to parse')
    # Sample index
    argparser.add_argument('--sample', type=int, default=None,
                           help='Which (index) hardcoded sample to run over')
    # Toggle debug
    argparser.add_argument('--debug', dest='debug', action='store_true',
                           help='Run in debug mode')
    # Toggle slimmed files
    argparser.add_argument('--slimmed', dest='slimmed', action='store_true',
                           help='Run over slimmed files')
    args = argparser.parse_args()

    doAll(slimmed=args.slimmed, debug=args.debug, sample=args.sample,
          nsamples=args.nsamples)
