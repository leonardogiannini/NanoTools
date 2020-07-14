// C++
#include <iostream>
#include <vector>
// ROOT
#include "TBenchmark.h"
#include "TChain.h"
#include "TDirectory.h"
#include "TFile.h"
#include "TROOT.h"
#include "TTreeCache.h"
#include "TString.h"
// NanoCORE
#include "../NanoCORE/Nano.h"
#include "../NanoCORE/SSSelections.h"
// Header
#include "control.h"

using namespace std;
using namespace tas;

ControlTree::ControlTree(TFile* new_tfile) {
	// TTree and TFile
    ttree = new TTree("tree", "tree");
    tfile = new_tfile;
    // Branches
	b_met = ttree->Branch("met", &met, "met/F");
	b_elec_pt = ttree->Branch("elec_pt", &elec_pt, "elec_pt/F");
	b_elec_eta = ttree->Branch("elec_eta", &elec_eta, "elec_eta/F");
	b_elec_phi = ttree->Branch("elec_phi", &elec_phi, "elec_phi/F");
	b_mu_pt = ttree->Branch("mu_pt", &mu_pt, "mu_pt/F");
	b_mu_eta = ttree->Branch("mu_eta", &mu_eta, "mu_eta/F");
	b_mu_phi = ttree->Branch("mu_phi", &mu_phi, "mu_phi/F");
	b_num_jets = ttree->Branch("num_jets", &num_jets, "num_jets/F");
	b_num_btags_tight = ttree->Branch("num_btags_tight", &num_btags_tight, "num_btags_tight/F");
    b_num_btags_medium = ttree->Branch("num_btags_medium", &num_btags_medium, "num_btags_medium/F");
    b_num_btags_loose = ttree->Branch("num_btags_loose", &num_btags_loose, "num_btags_loose/F");
	b_mc_weight = ttree->Branch("mc_weight", &mc_weight, "mc_weight/F");
}

void ControlTree::resetBranches() {
	// Reset Branches
	met = -999;
	elec_id = -999;
	elec_pt = -999;
	elec_eta = -999;
	elec_phi = -999;
	mu_id = -999;
	mu_pt = -999;
	mu_eta = -999;
	mu_phi = -999;
	num_jets = -999;
	num_btags_tight = -999;
	num_btags_medium = -999;
	num_btags_loose = -999;
	mc_weight = 1;
}

int ControlTree::fillBranches(int nEvents, float xsec, bool isData){
	float mc_weight;
	float int_lum = 7721;
	// Get Leptons
	Leptons leptons = getLeptons();
	// Iter Over Leptons 
	int numElec = 0;
	int numMu = 0;
	Lepton elec;
	Lepton mu;
	for (unsigned int i = 0; i < leptons.size(); i++) {		
		if(leptons[i].is_el() && leptons[i].pt() > 20) {
			elec = leptons[i];
			numElec++; 
		}
		else if(leptons[i].is_mu() && leptons[i].pt() > 20) {
			mu = leptons[i];
			numMu++;
		}
	}
	if (numElec != 1 || numMu != 1){
		return 0;
	} 
		
	if(elec.charge() == mu.charge()) {
		return 0;
	}
	
	float tight_working_point = 0.7221;	
	int num_tagged_b_tight = 0;	
	// Iter Over Jets
	for (unsigned int i = 0; i < nJet(); i++) {
		if(fabs(Jet_eta().at(i)) > 2.5) continue;
		if(Jet_pt().at(i) < 30) continue;
		if(Jet_jetId().at(i) == Electron_jetIdx().at(elec.idx()) || Jet_jetId().at(i) == Muon_jetIdx().at(mu.idx())) continue;
		if(Jet_btagDeepFlavB().at(i) > tight_working_point){
			num_tagged_b_tight++;
		}
	}

 	// Add cut for b tags
	// Assign Branch Values:
	met = MET_pt();
	elec_id = elec.id();
	elec_pt = elec.pt();
	elec_eta = elec.eta();
	elec_phi = elec.phi();
	mu_id = mu.id();
	mu_pt = mu.pt();
	mu_eta = mu.eta();
	mu_phi = mu.phi();
	num_jets = nJet();
	num_btags_tight = num_tagged_b_tight;
	num_btags_medium;
	num_btags_loose;
	if (!isData) {
		mc_weight = xsec * int_lum / nEvents;
	}
	fillTTree();	
	return 0;
}


void ControlTree::fillTTree() {
    ttree->Fill();
	return;
}

void ControlTree::writeTFile() {
    tfile->cd();
    ttree->Write();
    tfile->Close();
	return;
}