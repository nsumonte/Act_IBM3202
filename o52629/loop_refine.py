from modeller import *
from modeller.automodel import *

log.verbose()
env = Environ()

# directories for input atom files

# Create a new class based on 'LoopModel' so that we can redefine
# select_loop_atoms (necessary)
class MyLoop(LoopModel):
    # This routine picks the residues to be refined by loop modeling
    def select_loop_atoms(self):
        # 10 residue insertion 
        return Selection(self.residue_range('90:A', '100:A'),
        		self.residue_range('220:A', '225:A'))
m = MyLoop(env,
           inimodel='target.B99990003.pdb', # initial model of the target
           sequence='target')       # code of the target

m.loop.starting_model= 22           # index of the first loop model 
m.loop.ending_model  = 40          # index of the last loop model
m.loop.md_level = refine.slow      # loop refinement method; this yields
                                   # models quickly but of low quality;
                                   # use refine.slow for better models

m.make()