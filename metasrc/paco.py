from __future__ import print_function
import sys
from pacolib import *

if len(sys.argv) < 2:
    sys.stderr.write('\nUsage: '+sys.argv[0]+' relsize\n\n')
    sys.exit(1)

n = int(sys.argv[1])

print ('Require Export paconotation pacotacuser.')
print ('Require Import paconotation_internal pacotac pacon.')
print ('Set Implicit Arguments.')
print ('')

print ('Section PACO'+str(n)+'.')
print ('')

for i in range(n):
    print ('Variable T'+str(i)+' : '+ifpstr(i,'forall'),end='')
    for j in range(i):
        print (' (x'+str(j)+': @T'+str(j)+itrstr(" x",j)+')',end='')
    print (ifpstr(i,', ')+'Type.')
print ('')

print ('Record sig'+str(n)+'T :=')
print ('  exist'+str(n)+'T { ')
for i in range(n):
    print ('      proj'+str(n)+'T'+str(i)+': @T'+str(i)+itrstr(' proj'+str(n)+'T', i)+';')
print ('    }.')
print ('')

print ('Definition uncurry'+str(n)+' (R: rel'+str(n)+itrstr(' T',n)+'): rel1 sig'+str(n)+'T := fun x => R'+itrstr(' (proj'+str(n)+'T', n, ' x)')+'.')
print ('')

print ('Definition curry'+str(n)+' (R: rel1 sig'+str(n)+'T): rel'+str(n)+itrstr(' T', n)+' :=')
print ('  '+ifpstr(n, 'fun'+itrstr(' x', n)+' => ')+'R (exist'+str(n)+'T'+ifpstr(n, ' x'+str(n-1))+').')
print ('')

print ('Lemma uncurry_map'+str(n)+' r0 r1 (LE : r0 <'+str(n)+'== r1) : uncurry'+str(n)+' r0 <1== uncurry'+str(n)+' r1.')
print ('Proof. intros [] H. apply LE. apply H. Qed.')
print ('')

print ('Lemma uncurry_map_rev'+str(n)+' r0 r1 (LE: uncurry'+str(n)+' r0 <1== uncurry'+str(n)+' r1) : r0 <'+str(n)+'== r1.')
print ('Proof.')
print ('  repeat_intros '+str(n)+'. intros H. apply (LE (exist'+str(n)+'T'+ifpstr(n, ' x'+str(n-1))+') H).')
print ('Qed.')
print ('')

print ('Lemma curry_map'+str(n)+' r0 r1 (LE: r0 <1== r1) : curry'+str(n)+' r0 <'+str(n)+'== curry'+str(n)+' r1.')
print ('Proof. ')
print ('  repeat_intros '+str(n)+'. intros H. apply (LE (exist'+str(n)+'T'+ifpstr(n, ' x'+str(n-1))+') H).')
print ('Qed.')
print ('')

print ('Lemma curry_map_rev'+str(n)+' r0 r1 (LE: curry'+str(n)+' r0 <'+str(n)+'== curry'+str(n)+' r1) : r0 <1== r1.')
print ('Proof. ')
print ('  intros [] H. apply LE. apply H.')
print ('Qed.')
print ('')

print ('Lemma uncurry_bij1_'+str(n)+' r : curry'+str(n)+' (uncurry'+str(n)+' r) <'+str(n)+'== r.')
print ('Proof. unfold le'+str(n)+'. repeat_intros '+str(n)+'. intros H. apply H. Qed.')
print ('')

print ('Lemma uncurry_bij2_'+str(n)+' r : r <'+str(n)+'== curry'+str(n)+' (uncurry'+str(n)+' r).')
print ('Proof. unfold le'+str(n)+'. repeat_intros '+str(n)+'. intros H. apply H. Qed.')
print ('')

print ('Lemma curry_bij1_'+str(n)+' r : uncurry'+str(n)+' (curry'+str(n)+' r) <1== r.')
print ('Proof. intros []. intro H. apply H. Qed.')
print ('')

print ('Lemma curry_bij2_'+str(n)+' r : r <1== uncurry'+str(n)+' (curry'+str(n)+' r).')
print ('Proof. intros []. intro H. apply H. Qed.')
print ('')

print ('Lemma uncurry_adjoint1_'+str(n)+' r0 r1 (LE: uncurry'+str(n)+' r0 <1== r1) : r0 <'+str(n)+'== curry'+str(n)+' r1.')
print ('Proof.')
print ('  apply uncurry_map_rev'+str(n)+'. eapply le1_trans; [apply LE|]. apply curry_bij2_'+str(n)+'.')
print ('Qed.')
print ('')

print ('Lemma uncurry_adjoint2_'+str(n)+' r0 r1 (LE: r0 <'+str(n)+'== curry'+str(n)+' r1) : uncurry'+str(n)+' r0 <1== r1.')
print ('Proof.')
print ('  apply curry_map_rev'+str(n)+'. eapply le'+str(n)+'_trans; [|apply LE]. apply uncurry_bij2_'+str(n)+'.')
print ('Qed.')
print ('')

print ('Lemma curry_adjoint1_'+str(n)+' r0 r1 (LE: curry'+str(n)+' r0 <'+str(n)+'== r1) : r0 <1== uncurry'+str(n)+' r1.')
print ('Proof.')
print ('  apply curry_map_rev'+str(n)+'. eapply le'+str(n)+'_trans; [apply LE|]. apply uncurry_bij2_'+str(n)+'.')
print ('Qed.')
print ('')

print ('Lemma curry_adjoint2_'+str(n)+' r0 r1 (LE: r0 <1== uncurry'+str(n)+' r1) : curry'+str(n)+' r0 <'+str(n)+'== r1.')
print ('Proof.')
print ('  apply uncurry_map_rev'+str(n)+'. eapply le1_trans; [|apply LE]. apply curry_bij1_'+str(n)+'.')
print ('Qed.')
print ('')

print ('(** ** Predicates of Arity '+str(n))
print ('*)')
print ('')

print ('Definition ',end='')
print ('paco'+str(n)+"(gf"+' : '+'rel'+str(n)+itrstr(" T",n)+' -> '+'rel'+str(n)+itrstr(" T",n)+")"+'('+'r'+': rel'+str(n)+itrstr(' T',n)+')'+' : rel'+str(n)+itrstr(' T',n)+' :=')
print ('  curry'+str(n)+' (paco', end='')
print (' (fun'+' R0'+' => uncurry'+str(n)+' (gf'+' (curry'+str(n)+' R0)'+'))', end='')
print (' (uncurry'+str(n)+' r)'+').')
print ('')

print ('Definition ',end='')
print ('upaco'+str(n)+"(gf"+' : '+'rel'+str(n)+itrstr(" T",n)+' -> '+'rel'+str(n)+itrstr(" T",n)+")"+'('+'r'+': rel'+str(n)+itrstr(' T',n)+')'+' := '+'paco'+str(n)+' gf'+' r'+' \\'+str(n)+'/ r.')
print ('Arguments paco'+str(n)+' : clear implicits.')
print ('Arguments upaco'+str(n)+' : clear implicits.')
print ('Hint Unfold upaco'+str(n)+'.')
print ('')

print ("Definition monotone"+str(n)+" (gf: "+"rel"+str(n)+itrstr(" T",n)+" -> "+"rel"+str(n)+itrstr(" T",n)+") :=")
print ("  forall"+itrstr(" x",n)+" r"+" r'"+" (IN: gf"+" r"+itrstr(" x",n)+") ",end='')
print ("(LE"+": r"+" <"+str(n)+"= r'"+")",end='')
print (", gf"+" r'"+itrstr(" x",n)+".")
print ('')
print ("Definition _monotone"+str(n)+" (gf: "+"rel"+str(n)+itrstr(" T",n)+" -> "+"rel"+str(n)+itrstr(" T",n)+") :=")
print ("  forall"+" r"+" r'",end='')
print ("(LE"+": r"+" <"+str(n)+"= r'"+")",end='')
print (", gf"+" r"+' <'+str(n)+'== gf'+" r'"+'.')
print ('')
print ("Lemma monotone"+str(n)+'_eq'+" (gf: "+"rel"+str(n)+itrstr(" T",n)+" -> "+"rel"+str(n)+itrstr(" T",n)+") :")
print ("  monotone"+str(n)+' gf <-> _monotone'+str(n)+' gf.')
print ("Proof. unfold monotone"+str(n)+', _monotone'+str(n)+', le'+str(n)+'. split; intros; eapply H; eassumption. Qed.')
print ('')
print ("Lemma monotone"+str(n)+'_map'+" (gf: "+"rel"+str(n)+itrstr(" T",n)+" -> "+"rel"+str(n)+itrstr(" T",n)+")")
print ("      (MON: _monotone"+str(n)+' gf) :')
print ("  _monotone"+' (fun'+' R0'+' => uncurry'+str(n)+' (gf'+' (curry'+str(n)+' R0)'+')).')
print ('Proof.')
print ('  repeat_intros '+str(3)+'. apply uncurry_map'+str(n)+'. apply MON; apply curry_map'+str(n)+'; assumption.')
print ('Qed.')
print ('')

print ("Lemma _paco"+str(n)+"_mon_gen (gf gf': "+"rel"+str(n)+itrstr(" T",n)+" -> "+"rel"+str(n)+itrstr(" T",n)+") r r'")
print ("    (LEgf: gf <"+str(n+1)+"= gf')")
print ("    (LEr: r <"+str(n)+"= r'):")
print ("  paco"+str(n)+" gf r <"+str(n)+"== paco"+str(n)+" gf' r'.")
print ("Proof.")
print ("  apply curry_map"+str(n)+". red; intros. eapply paco_mon_gen. apply PR.")
print ("  - intros. apply LEgf, PR0.")
print ("  - intros. apply LEr, PR0.")
print ("Qed.")
print ('')

print ("Lemma paco"+str(n)+"_mon_gen (gf gf': "+"rel"+str(n)+itrstr(" T",n)+" -> "+"rel"+str(n)+itrstr(" T",n)+") r r'"+itrstr(' x', n))
print ("    (REL: paco"+str(n)+" gf r"+itrstr(' x', n)+")")
print ("    (LEgf: gf <"+str(n+1)+"= gf')")
print ("    (LEr: r <"+str(n)+"= r'):")
print ("  paco"+str(n)+" gf' r'"+itrstr(' x', n)+".")
print ("Proof.")
print ("  eapply _paco"+str(n)+"_mon_gen; [apply LEgf | apply LEr | apply REL].")
print ("Qed.")
print ('')

print ("Lemma upaco"+str(n)+"_mon_gen (gf gf': "+"rel"+str(n)+itrstr(" T",n)+" -> "+"rel"+str(n)+itrstr(" T",n)+") r r'"+itrstr(' x', n))
print ("    (REL: upaco"+str(n)+" gf r"+itrstr(' x', n)+")")
print ("    (LEgf: gf <"+str(n+1)+"= gf')")
print ("    (LEr: r <"+str(n)+"= r'):")
print ("  upaco"+str(n)+" gf' r'"+itrstr(' x', n)+".")
print ("Proof.")
print ("  destruct REL.")
print ("  - left. eapply paco"+str(n)+"_mon_gen; [apply H | apply LEgf | apply LEr].")
print ("  - right. apply LEr, H.")
print ("Qed.")
print ('')

print ('Section Arg'+str(n)+'.')
print ('')
print ('Variable'+" gf"+' : '+'rel'+str(n)+itrstr(" T",n)+' -> '+'rel'+str(n)+itrstr(" T",n)+'.')
print ('Arguments gf'+' : clear implicits.')
print ('')

print ('Theorem _paco'+str(n)+'_mon: _monotone'+str(n)+' (paco'+str(n)+" gf"+').')
print ('Proof.')
print ('  repeat_intros '+str(3)+'. eapply curry_map'+str(n)+', _paco'+'_mon; apply uncurry_map'+str(n)+'; assumption.')
print ('Qed.')
print ('')

print ('Theorem _paco'+str(n)+'_acc: forall')
print ('  l'+' r'+' (OBG: forall rr (INC: r'+' <'+str(n)+'== rr) (CIH: l <'+str(n)+'== rr), l <'+str(n)+'== paco'+str(n)+" gf",end='')
print (' rr',end='')
print ('),')
print ('  l <'+str(n)+'== paco'+str(n)+" gf"+' r'+'.')
print ('Proof.')
print ('  intros. apply uncurry_adjoint1_'+str(n)+'.')
print ('  eapply _paco'+'_acc. intros.')
print ('  apply uncurry_adjoint1_'+str(n)+' in INC. apply uncurry_adjoint1_'+str(n)+' in CIH.')
print ('  apply uncurry_adjoint2_'+str(n)+'.')
print ('  eapply le'+str(n)+'_trans. eapply (OBG _ INC CIH).')
print ('  apply curry_map'+str(n)+'.')
print ('  apply _paco'+'_mon; try apply le1_refl; apply curry_bij1_'+str(n)+'.')
print ('Qed.')
print ('')
    
print ('Theorem _paco'+str(n)+'_mult_strong: forall'+' r'+',')
print ('  paco'+str(n)+" gf",end='')
print (' (upaco'+str(n)+" gf"+' r'+')',end='')
print (' <'+str(n)+'== paco'+str(n)+" gf"+' r'+'.')
print ('Proof.')
print ('  intros. apply curry_map'+str(n)+'.')
print ('  eapply le1_trans; [| eapply _paco'+'_mult_strong].')
print ('  apply _paco'+'_mon; intros []; intros H; apply H.')
print ('Qed.')
print ('')

print ('Theorem _paco'+str(n)+'_fold: forall'+' r'+',')
print ('  gf',end='')
print (' (upaco'+str(n)+" gf"+' r'+')',end='')
print (' <'+str(n)+'== paco'+str(n)+" gf"+' r'+'.')
print ('Proof.')
print ('  intros. apply uncurry_adjoint1_'+str(n)+'.')
print ('  eapply le1_trans; [| apply _paco'+'_fold]. apply le1_refl.')
print ('Qed.')
print ('')
    
print ('Theorem _paco'+str(n)+'_unfold: forall'+' (MON: _monotone'+str(n)+' gf)'+' r'+',')
print ('  paco'+str(n)+" gf"+' r'+' <'+str(n)+'== gf',end='')
print (' (upaco'+str(n)+" gf"+' r'+')',end='')
print ('.')
print ('Proof.')
print ('  intros. apply curry_adjoint2_'+str(n)+'.')
print ('  eapply _paco'+'_unfold; apply monotone'+str(n)+'_map; assumption.')
print ('Qed.')
print ('')

print ('Theorem paco'+str(n)+'_acc: forall')
print ('  l'+' r'+' (OBG: forall rr (INC: r'+' <'+str(n)+'= rr) (CIH: l <'+str(n)+'= rr), l <'+str(n)+'= paco'+str(n)+" gf",end='')
print (' rr',end='')
print ('),')
print ('  l <'+str(n)+'= paco'+str(n)+" gf"+' r'+'.')
print ('Proof.')
print ('  apply _paco'+str(n)+'_acc.')
print ('Qed.')
print ('')
    
print ('Theorem paco'+str(n)+'_mon: monotone'+str(n)+' (paco'+str(n)+" gf"+').')
print ('Proof.')
print ('  apply monotone'+str(n)+'_eq.')
print ('  apply _paco'+str(n)+'_mon.')
print ('Qed.')
print ('')
    
print ('Theorem upaco'+str(n)+'_mon: monotone'+str(n)+' (upaco'+str(n)+" gf"+').')
print ('Proof.')
print ('  repeat_intros '+str(n+2)+'. intros R '+" LE0"+'.')
print ('  destruct R.')
print ('  - left. eapply paco'+str(n)+'_mon. apply H.'+" apply LE0.")
print ('  - right. apply LE0, H.')
print ('Qed.')
print ('')

print ('Theorem paco'+str(n)+'_mult_strong: forall'+' r'+',')
print ('  paco'+str(n)+" gf",end='')
print (' (upaco'+str(n)+" gf"+' r'+')',end='')
print (' <'+str(n)+'= paco'+str(n)+" gf"+' r'+'.')
print ('Proof.')
print ('  apply _paco'+str(n)+'_mult_strong.')
print ('Qed.')
print ('')

print ('Corollary paco'+str(n)+'_mult: forall'+' r'+',')
print ('  paco'+str(n)+" gf"+' (paco'+str(n)+" gf"+' r'+')'+' <'+str(n)+'= paco'+str(n)+" gf"+' r'+'.')
print ('Proof. intros; eapply paco'+str(n)+'_mult_strong, paco'+str(n)+'_mon; [apply PR|..]; intros; left; assumption. Qed.')
print ('')
    
print ('Theorem paco'+str(n)+'_fold: forall'+' r'+',')
print ('  gf',end='')
print (' (upaco'+str(n)+" gf"+' r'+')',end='')
print (' <'+str(n)+'= paco'+str(n)+" gf"+' r'+'.')
print ('Proof.')
print ('  apply _paco'+str(n)+'_fold.')
print ('Qed.')
print ('')
    
print ('Theorem paco'+str(n)+'_unfold: forall'+' (MON: monotone'+str(n)+' gf)'+' r'+',')
print ('  paco'+str(n)+" gf"+' r'+' <'+str(n)+'= gf',end='')
print (' (upaco'+str(n)+" gf"+' r'+')',end='')
print ('.')
print ('Proof.')
print ('  repeat_intros 1. eapply _paco'+str(n)+'_unfold; apply monotone'+str(n)+'_eq; assumption.')
print ('Qed.')
print ('')

print ('End Arg'+str(n)+'.')
print ('')

print ('Arguments paco'+str(n)+'_acc'+" : clear implicits.")
print ('Arguments paco'+str(n)+'_mon'+" : clear implicits.")
print ('Arguments upaco'+str(n)+'_mon'+" : clear implicits.")
print ('Arguments paco'+str(n)+'_mult_strong'+" : clear implicits.")
print ('Arguments paco'+str(n)+'_mult'+" : clear implicits.")
print ('Arguments paco'+str(n)+'_fold'+" : clear implicits.")
print ('Arguments paco'+str(n)+'_unfold'+" : clear implicits.")
print ('')

print ("Global Instance paco"+str(n)+"_inst "+" ("+"gf "+": rel"+str(n)+itrstr(" T",n)+"->_)"+" r"+itrstr(" x",n)+" : paco_class (paco"+str(n)+" gf"+" r"+itrstr(" x",n)+") :=")
print ("{ pacoacc    := paco"+str(n)+"_acc"+" gf"+";")
print ("  pacomult   := paco"+str(n)+"_mult"+" gf"+";")
print ("  pacofold   := paco"+str(n)+"_fold"+" gf"+";")
print ("  pacounfold := paco"+str(n)+"_unfold"+" gf"+" }.")
print ('')

print ('End PACO'+str(n)+'.')
print ('')

print ('Global Opaque paco'+str(n)+'.')
print ('')

print ('Hint Unfold upaco'+str(n)+'.')
print ('Hint Resolve paco'+str(n)+'_fold.')
print ('Hint Unfold monotone'+str(n)+'.')
print ('')
