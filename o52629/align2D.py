from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='7f1n', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='7f1n', atom_files='7f1n.pdb')
aln.append(file='target.fasta', align_codes='target', alignment_format='FASTA')
aln.align2d(overhang=0, gap_penalties_1d=(-100, 0),
            gap_penalties_2d=(3.5, 3.5, 3.5, 0.2, 4.0, 6.5, 2.0, 0., 0.),
            )
aln.write(file='aligned.fasta', alignment_format='FASTA')
aln.write(file='aligned.ali', alignment_format='PIR')
aln.write(file='aligned.pap', alignment_format='PAP')