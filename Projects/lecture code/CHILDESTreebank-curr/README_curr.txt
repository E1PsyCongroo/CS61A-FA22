Lisa Pearl & Jon Sprouse
lpearl@uci.edu, jon.sprouse@uconn.edu
University of California, Irvine & University of Connecticut, Storrs
Aug 2020
[UPDATES for this version: 
(1) All *.parsed files cleaned by Alex Clark, focusing on making sure that tree node labels were correct.
]



~~~
README for CHILDES derived corpus: CHILDES Treebank files 
(annotated with phrase structure tree information)
Created with funding from NSF grant BCS-0843896, "Testing the Universal Grammar Hypothesis" and NSF grant BCS-1347028, “An integrated theory of syntactic acquisition — Realistic input, quantitatively defined target states, and computational models of the learning strategy”.
~~~

I. OVERVIEW
The CHILDES Treebank corpus is derived from several corpora from the American English section of CHILDES (MacWhinney, B. 2000. The CHILDES Project: Tools for Analyzing Talk. Mahwah, NJ: Lawrence Erlbaum Associates; http://childes.psy.cmu.edu/). The goal was to annotate child-directed speech utterance transcriptions with phrase structure tree information.  For each corpus included, the following was done:

(1) The selected utterances (either all child-directed speech utterances, or simply those child-directed speech utterances containing wh-words) were first automatically parsed by using the Charniak parser [pre-2012] (available here: ftp://ftp.cs.brown.edu/pub/nlparser/) or the Stanford parser [post-2012] (available here: http://nlp.stanford.edu/software/lex-parser.shtml). 

(2) Then, the output from the parser was hand-checked by an undergraduate annotator who had been trained in syntactic tree structure.

(3) The output from the first annotator was hand-checked by a second undergraduate annotator who had been trained in syntactic tree structure.

(4) In the case of trace, animacy, and thematic role annotation, these annotations were added to the previously corrected versions of the output.

We have additionally benefited from some error-checking from the following researchers:

- Avery Andrews: bates-wh.parsed, bernstein-wh.parsed, brown-adam.parsed, brown-eve.parsed, brown-sarah.parsed, soderstrom.parsed, valian.parsed
- Alandi Bates: valian.parsed, all hslld files
- Bob Berwick & Aline Villavicencio: brown-adam.parsed
- Alex Clark: all .parsed files
- Kyle Gorman: bates.wh.parsed, bernstein.wh.parsed, brown-adam.parsed, brown-eve.parsed, brown-sarah.parsed, suppes.parsed, valian.parsed, vanhouten-threes-wh.parsed, vanhouten-twos-wh.parsed, vankleeck-wh.parsed
- Yohei Oseki: brown-adam.parsed, valian+animacy+theta.parsed
- Abbie Thornton: brown-eve.parsed, brown-eve+animacy+theta.parsed, brown-adam3to4+animacy+theta.parsed, brown-adam4up+animacy+theta.parsed


PLEASE NOTE: The hope was that this process would remove the errors resulting from the automatic parsing process.  However, errors may remain and we strongly suggest that any users of these data review automated extraction results to make sure they are accurate. If you do find syntactic annotation errors, please feel free to email Lisa Pearl (lpearl@uci.edu) what they are and where you found them - we'll happily update the files and release the updates in the next version.

~~~

II. CURRENT CORPORA

The corpora currently included in the CHILDES Treebank are as follows:

All child-directed speech utterances:
NOTE: +animacy+theta = includes trace, animacy, and thematic role annotation (detailed below_

-Brown-Adam (Brown 1973): brown-adam.parsed (also includes trace annotation)
     - brown-adam3to4+animacy_theta.parsed: speech directed at a child between the ages of 3 and 4 (starting at file 20 of the original brown-adam *.cha files from the CHILDES database): [~10,965 utterances, ~56,794 words]
     — brown-adam-4up+animacy+theta.parsed: speech directed at a child age 4 and older (starting at file 42 of the original brown-adam *.cha files from the CHILDES database):[~5724 utterances, ~30,841 words]

-Brown-Eve (Brown 1973): brown-eve+animacy+theta.parsed 

-Brown-Sarah (Brown 1973): brown-sarah.parsed

-HSLLD (Snow & Dickinson 1990): hslld-hv1-er/*.parsed (speech directed at children age three through five at home visit 1, from the elicited report subsection), hslld-hv1-mt/*.parsed (speech directed at children age three through five at home visit 1, from the meal time subsection)

-Soderstrom (Soderstrom, Blossom, Foygel, & Morgan 2008): soderstrom.parsed

-Suppes (Suppes 1974): suppes.parsed

-Valian (Valian 1991): valian+animacy+theta.parsed

Only child-directed speech utterances containing wh-words:
-Bates (Bates et al. 1988): bates-wh.parsed
-Bernstein (Bernstein 1987): bernstein-wh.parsed
-VanHouten-Threes (Van Houten 1986): vanhouten-threes-wh.parsed
-VanHouten-Twos (Van Houten 1986): vanhouten-twos-wh.parsed
-VanKleeck: vankleeck-wh.parsed



Original corpora references:

Bates, E., Bretherton, I., & Snyder, L. (1988). From first words to grammar: Individual differences and dissociable mechanisms. Cambridge, MA: Cambridge University Press.
Bernstein-Ratner, N. (1987). The phonology of parent child speech. In K. Nelson & A. Van Kleeck (Eds.), Children's Language: Vol. 6. Hillsdale, NJ: Lawrence Erlbaum.
Brown, R. (1973). A first language: The early stages. Cambridge, MA: Harvard University Press.
Snow, C.E., & Dickinson, D.K. 1990. Social sources of narrative skills at home and at school. First Language, 10, 87-103.
Soderstrom, M., Blossom, M., Foygel, R., & Morgan, J.L. (2008). Acoustical cues and grammatical units in speech to two preverbal infants. Journal of Child Language, 35(4), 869-902. 
Suppes, P. (1974). The semantics of children's language. American Psychologist, 29, 103-114.
Valian, V. (1991). Syntactic subjects in the early speech of American and Italian children. Cognition, 40, 21-81.
Van Houten, L. (1986). Role of maternal input in the acquisition process: The communicative strategies of adolescent and older mothers with their language learning children. Paper presented at the Boston University Conference on Language Development, Boston.
~~~

Corpus statistics, with number of children in [] and age ranges in ():
All child-directed speech utterances:
**Note: Word counts are approximate**
brown-adam.parsed [1] (2;3-4;10) = 28,780 utterances, ~144,135 words
brown-eve+animacy+theta.parsed [1](1;6-2;3) = 14,222 utterances, ~66,157 words
brown-sarah.parsed [1] (2;3-5;1) = 46,947 utterances, ~202,499 words
hslld-hv1-er/*.parsed [78] (3;6-5;0) = 2,912 utterances, ~14,839 words
hslld-hv1-mt/*.parsed [66] (3;7-4;11) = 15,990 utterances, ~81,246 words
soderstrom.parsed [2] (0;6-1;0)= 24,130 utterances, ~90,608 words
suppes.parsed [1] (1;11-3;11)= 35,904 utterances, ~197,620 words
valian+animacy+theta.parsed [21] (1;9-2;8)= 25,550 utterances, ~131,184 words

Only child-directed speech utterances containing wh-words:
bates-wh.parsed [30] (1;8 and 2;4)= 1,800 utterances, ~8,985 words
bernstein-wh.parsed [9] (1;1-1;11)= 1,724 utterances, ~8,036 words
vanhouten-threes-wh.parsed [27] (3;0-3;11) = 1,415 utterances, ~8,141 words
vanhouten-twos-wh.parsed [21] (2;0-2;11) = 397 utterances, ~1,787 words
vankleeck-wh.parsed [20] (3;0-3;11) = 1,675 utterances, ~8,975 words


Total utterances for all corpora: 201,446
Total words for all corpora: ~964,212

Note: Utterance and approximate word counts retrievable using the Tregex query:
/^\w.*/ <: (/.+/ !< /.+/)
Word counts are approximate, since clitics like ’s and n’t are under their own leaf, and so get counted as separate words.
Many thanks to Avery Andrews for this.


~~~
III. PHRASE STRUCTURE ANNOTATION

The phrase structure tree annotation is similar to the Penn Treebank II notation, described in "Bracketing Guidelines for Treebank II Style Penn Treebank Project": AnnotationLabels.html

There are a few exceptions, which were made to (hopefully) make the labeling more useful to syntactic acquisition researchers:

(1) Complementizers (such as "if", "that", etc.) are labeled with COMP, rather than the preposition label IN.
(2) The contracted forms "gonna" and "wanna" have been expanded into "goING To" and "wanT To" for the corpora listed below.  (This aided the initial automatic parsing for the Charniak parser, and the unusual capitalization patterns can still allow these forms to be retrieved automatically.) brown-adam, brown-eve, brown-sarah, soderstrom, suppes, valian, bates-wh, bernstein-wh, vanhouten-threes-wh, vanhouten-twos-wh, vankleeck-wh.
(3) NOT is used for the negatives "not" and "n't", rather than the adverb label RB.
(4) COP is used for forms of copular "be", rather than the verb labels VB*.
(5) AUX is used for auxiliary verbs, with the VB* reserved for main verbs.
(6) TO is only used for infinitival "to" (e.g., "want to go") while IN is used for prepositional "to" (e.g., "to the store"), as well as other prepositions.

~~~
IV. TRACE ANNOTATION

To aid syntactic acquisition researchers, we have begun adding trace annotation. The trace notation is similar in format to the Switchboard corpus, but uses different categories of traces.

The first distinction is between A-bar traces and A traces, with each of these subdivided into additional categories.

(1) ABAR traces: 
(a) WH = wh-traces (e.g., “How do you feel __?”)
(b) RC = relative clause traces (e.g., “This is the one which I want __.”)
(c) OTHER = other A-bar traces like topicalization (e.g., “When I laugh, I feel good ___”. “Smart though Jack is ___1, he often does silly things ___2.”)

(2) A traces:
(a) PASS = passive (e.g., “Jack was kissed __ by Lily.”)
(b) RAISE = raising (e.g., “Lily seems __ to be happy.”)

Some examples are below of the specific notation:
(1a) “How do you feel?” [ABAR-WH]
(ROOT
   (SBARQ 
	(WHADVP-1 (WRB how))
           (SQ (AUX do) 
                   (NP (PRP you))
                   (VP (VB feel) 
                          (ADVP (-NONE-ABAR-WH- *T*-1))))
    (. ?)))

(1b) “This is the way that I feel.” = “This is the way that I feel __.”

(ROOT
   (S (NP (NN This))
        (VP (COP is)
	    (NP (NP (DT the) (NN way))
		(SBAR (WHNP-1 (WDT that))
			 (S (NP (PRP I))
			      (VP (VBP feel)
				   (NP (-NONE-ABAR-RC- *T*-1)))))))
   (. .)))
 
(1c) “Smart though Jack is, he often does silly things.” [ABAR-OTHER, ABAR-OTHER]
(ROOT
   (S (SBAR-2 (ADJP-1 (JJ Smart))
	         (COMP though)
	         (S (NP (NNP Jack))
		   (VP (COP is)
			(ADJP (-NONE-ABAR-OTHER- *T*-1)))))
        (NP (PRP he))
        (ADVP (RB often))
        (VP (VBZ does)
	    (NP (JJ silly) (NNS things))
               (SBAR (-NONE-ABAR-OTHER- *T*-2)))

   (. .)))	     

(2a) “Jack was kissed by Lily.” [A-PASS]
(ROOT
   (S (NP-1 (NNP Jack))
        (VP (AUX was)
	    (VP (VBN kissed)
		(NP (-NONE-A-PASS- *T*-1))
		(PP (IN by)
		       (NP (NNP Lily)))))
    (. .)))

(2b) RAISE = raising
“Lily seems to be happy.” = “Lily seems __Lily to be happy.”
(ROOT
   (S (NP-1 (NNP Lily))
        (VP (VBP seems)
	     (S (NP (-NONE-A-RAISE- *T*-1))
		(VP (TO to)
		       (VP (VB be)
			    (ADJP (JJ happy))))))
   (. .)))




NOTE 1: Occasionally, a single trace will be indexed with multiple positions. This will be reflected in the labeling. For example:

“What did you see __ and like __?”


(ROOT (SBARQ (WHNP-1 (WP what))
                           (SQ (VP (AUX did)
            		         (NP (PRP you))
			         (VP (VP (VB see)
					 (NP (-NONE-ABAR-WH- *T*1)))
				      (CC and)
				      (VP (VB like)
					  (NP (-NONE-ABAR-WH- *T*1))))))
	   (. ?)))


NOTE 2: Occasionally null pronouns have been added due to traces that are indexed with them. For example: 
 “What’s [that (which/that = WDT) you’re writing]?”
~= “(That which) you’re writing is what”

(ROOT (SBARQ (WHNP-1 (WP what))
     (SQ (VP (COP 's)
	 (NP (NP (NN that))
	         (SBAR (WHNP-2 (WP *NULL*))
	     	         (S (NP (PRP you))
	   	              (VP (AUX 're)
	    	                     (VP (VBG writing)
	    		                  (NP (-NONE-ABAR-RC- *T*-2)))))))
             (NP (-NONE-ABAR-WH- *T*-1))
     (. ?)))

NOTE 3: If it seems like there has been sequential movement, this will be indicated by the traces. For example:
“What got tickled?”
This is both a passive and a wh-trace. We represent this as follows:
 
 (SBARQ 
    (WHNP-2 
      (WP what))
    (SQ
      (NP-1
        (-NONE-ABAR-WH- *T*-2))
      (VP 
        (AUX got) 
	(VP 
	  (VBN tickled)
	  (NP
	    (-NONE-A-PASS- *T*-1)))))) 

~~~
V. ANIMACY ANNOTATION

For corpora with animacy annotation, this is added onto the basic form of the phrase structure trees that already have trace annotation.

Because these are non-linguistic (i.e., conceptual) information, we surround the annotations with angle brackets <…>

There are two distinctions:
+Animate: -<ANIM>
-Animate: -<INANIM>

Notes:
(a) This label should be attached to the NP phrase level.
(b) For both ABAR and A traces, the animacy is marked on the overt position of the NP (not where the trace is).
(c) Animacy is labeled for all NPs associated with verbs. (Others may not be labeled.)
(d) Animacy is labeled with respect to the object itself (is it capably of agency or self-initialized motion, does it have feelings, etc.), no matter what verb is associated with it. So, for “The dolly likes her coat” - “the dolly” is inanimate <INANIM>.

Some examples: 
(1) “I think that was Fraser.”

(ROOT (S (NP-<ANIM> (PRP I))
     (VP (VB think)
      (SBAR (S (NP-<INANIM> (NN that)) 
      	    (VP (COP was)
	     (NP-<ANIM> (NNP Fraser))))))
     (. .)))

(2) “Where’s your cup?”

(ROOT (SBARQ (WHADVP-1 (WRB where))
     (SQ (VP (COP 's)
      (NP-<INANIM> (PRP$ your) (NN cup))
      	  (ADVP (-NONE-ABAR-WH- *T*-1))))
     (. ?)))

(3)  “What is that?”

(ROOT (SBARQ (WHNP-1-<INANIM>- (WP what))
       (SQ (VP (COP is)
        (NP-<INANIM>- (NN that))
	(NP (-NONE-ABAR-WH- *T*-1)))) (. ?)))

~~~
VI. THEMATIC ROLE ANNOTATION

Corpora with thematic role annotation have this information added on top of the trace and animacy information. Because these are non-linguistic (i.e., conceptual) information, we surround the annotations with angle brackets <…>. Each thematic role label also indicates which verb it is associated with, with the verbs themselves indicated by <Vx> (ex: <V1>, <V2>, etc.).

There are 13 roles and some approximate heuristics associated with them:
(1) Agent: -AGENT-Vx
 —> Viewed as bringing about the event (and the event is action-y)
(2) Patient: -PATIENT-Vx 
 —> Viewed as undergoing an event passively (ex:  “penguin” in “I hugged the penguin”) 
(3) Theme: -THEME-Vx 
—> Typically the subject of intransitive verbs or paired with a Possessor. (ex: “The ball rolled.” “He’s coming.” “You’re going.” “He’s sitting.”; Possessor ex: “this belongs to Lisa”: Theme = “this”, Possessor = “Lisa”; “I have a cookie”: Theme = “cookie”, Possessor = “I”) 

(4)Causer: -CAUSER-Vx 
—> Causing perception to Experiencer (“The economy” in “The economy worries him.”) or actual causative subject (“we” in “we made him go” and “we let him go”)
(5) Causee: -CAUSEE-Vx 
—> What’s caused, typically an event: (“him go” in “We let him go”)
(6) Experiencer: -EXPER-Vx 
—> Experiencing the psych/mental state (“him” in “The economy worries him.”)
(7) Subject Matter: -SUBJMATT-Vx 
—> Receives the via psych/mental state (“the economy” in “Jon worries about the economy”)

(8) Location: -LOC-Vx 
—> Where event occurs, no movement (ex: “on the table” in “The book rests on the table.”)
(9) Source: -SOURCE-Vx 
—> Where event comes from (ex: “from Lisa” in “This came from Lisa.”)
(10) Goal: -GOAL-Vx 
—> Where event goes to (also recipients) (ex: “to LA” in “I sent this to LA”, “Lisa” in “I gave a cookie to Lisa”)
(11) Benefactor: -BENEF-Vx 
—> Benefits from event (ex: “Lisa” in “I washed the car for Lisa.”)
(12) Instrument: -INSTR-Vx 
—> Instrument used to accomplish event (ex: “a push” in “I closed it with a push.”)
(13) Possessor: -POSSESS-Vx 
—> Typically with stative verbs (ex: “Lisa” in “This belongs to Lisa.”)

Notes about thematic roles:
(1) There’s usually only one thematic role per NP, unless the NP is the subject of a conjoined VP. If there are multiple thematic roles for a single NP, they’re all put inside a single set of <...> (ex: NP-<ANIM>-<AGENT-V2-AGENT-V3>)
(2) For both A and ABAR traces, the thematic role is marked on the overt (WH)NP (and not on the trace). Exception: Relative clause traces that have a silent *NULL* pronoun will probably have the theta role marked on the silent pronoun.
(3) For COP (copula be verbs), no theta roles are assigned for the surrounding NP(s). 
(4) NP thematic roles are only marked for NPs associated with verbs.
(5) Thematic roles are also marked for S and SBAR as appropriate.
(6) Expletive NPs shouldn’t get thematic roles.
(7) *PRO* is added where necessary (when it takes a thematic role).

Examples:
(1) “I think that was Fraser.”

(ROOT (S (NP-<ANIM>-<EXPER-V1> (PRP I))
     (VP (VBP-<V1> think)
      (SBAR-<SUBJMATT-V1> 
              (S (NP-<INANIM> (NN that)) 
      	    (VP (COP was)
	     (NP-<ANIM> (NNP Fraser))))))
     (. .)))

(2) “You have another cookie right on the table.”

(ROOT (S (NP-<ANIM>-<POSSESS-V1> (PRP you))
     (VP (VBP-<V1> have)
      (NP-<INANIM>-<THEME-V1> (DT another)
      	   (NN cookie))
        (PP (ADVP (RB right))
     	  (IN on)
      	    (NP-<INANIM>-<LOC-V1> (DT the) (NN table))))
     (. .)))

(3) “I’ll give you another.”

(ROOT (S (NP-<ANIM>-<AGENT-V1> (PRP I))
     (VP (MD 'll) 
      (VP (VB-<V1> give)
       (NP-<ANIM>-<GOAL-V1> (PRP you))
        (NP-<INANIM>-<PATIENT-V1> (NN another))))
     (. .)))

(4) “Well, what are you trying to do, huh?”

(ROOT
   (INTJ
      (UH well))
   (, ,)
      (SBARQ
         (WHNP-1-<INANIM>-<PATIENT-V2>
	    (WP what))
         (SQ
	    (VP
	       (AUX are)
               (NP-<ANIM>-<EXPER-V1>
	          (PRP you))
               (VP
	          (VBG-<V1> trying)
                  (S-<SUBJMATT-V1>
		     (NP-<ANIM>-<AGENT-V2> 
 			(-NONE- *PRO*))
		     (VP
		        (TO to) 
                        (VP
			   (VB-<V2> do)
                           (NP
			      (-NONE-ABAR-WH- *T*-1))))))))
   (, ,)
     (INTJ
        (UH huh))
   (. ?)))

(5) “She doesn’t seem to want a bottle.”

(ROOT (S (NP-1-<ANIM>-<EXPER-V1> (PRP she))
     (VP (AUX does)
      (NOT n't)
      (VP (VB seem)
       (S
          (NP (-NONE-A-RAISE- *T*-1))
          (VP (TO to) 
                 (VP (VB-<V1> want)
                        (NP-<INANIM>-<SUBJMATT-V1> (DT a) (NN bottle)))))))
     (. .)))

(6) “Did you get your picture taken?”

(ROOT (SQ (VP (AUX did)
     (NP-<ANIM>-<EXPER-V1> (PRP you))
     (VP (VB-<V1> get) 
     (S-<SUBJMATT-V1> 
        (NP-1-<INANIM>-<PATIENT-V2> (PRP$ your) (NN picture)) 
         (VP (VBN-<V2> taken)
         (NP (-NONE-A-PASS- *T*-1))))))
     (. ?)))

~~~
VII. Tools
A very useful tool for searching through these corpora automatically is the Stanford Natural Language Processing Group's freely available Tregex tool, available at
http://nlp.stanford.edu/software/tregex.shtml#Download


****************************************
NOTE: If using these corpora in published materials, please cite one or more of the following:

Pearl, L. & Sprouse, J. 2013. Syntactic islands and learning biases: Combining experimental syntax and computational modeling to investigate the language acquisition problem. Language Acquisition, 20, 23-68.

Pearl, L. & Sprouse, J. 2013. Computational Models of Acquisition for Islands.  In J. Sprouse & N. Hornstein (eds), Experimental Syntax and Islands Effects. Cambridge University Press, 109-131.

Pearl, L. & Sprouse, J. 2019. Comparing solutions to the linking problem using an integrated quantitative framework of language acquisition.  Language, 95(4), 583-611. lingbuzz: https://ling.auf.net/lingbuzz/003913.
******************************************
