#!/usr/bin/env python3
# Filename: my_tmw.py

"""
# Topic Modeling Pipeline for todays particular project.
"""

### Usage ###
# 0. Make sure you have Python3, TreeTagger and Mallet installed.
# 1. Make sure all necessary files are in the working directory
# 2. Set working directory below
# 3. Select series of functions below by un-commenting them as needed
# 4. Set parameters for each function.
# 5. Run the workflow.

# Note: one possible workflow is: 2,3,6,7,8,9,10,11,12,14.
# Now also working, more or less: 1,5,6,7,8,9,10,11,13,14.


import tmw
#print(help(topmod))

### Set the general working directory.
wdir = "/home/christof/Repos/cligs/toolbox/tmw/demo/"


### 1 tei4reader_scenes (reads text and splits plays at scene boundaries)
inpath = wdir + "0_tei_test/*.xml"
outfolder = wdir + "2_scenes/"
#tmw.tei4reader_scenes(inpath,outfolder)


### 2 tei4reader_fulldocs (standard option)
inpath = wdir + "0_tei_test/*.xml"
outfolder = wdir + "1_txt/"
#tmw.tei4reader_fulldocs(inpath,outfolder)


### 3 - segmenter
inpath = wdir + "1_txt/*.txt"
outpath = wdir + "2_segments/"
segment_length = 5000
#tmw.segmenter(inpath,outpath,segment_length)


### 4 - segments_to_bins: inpath, outfile
inpath = wdir + "2_segments/*.txt"
outfile = wdir + "segments-and-bins.csv"
#tmw.segments_to_bins(inpath,outfile)


### 5 - scenes_to_bins
inpath = wdir + "2_scenes/*.txt"
outfolder = wdir + "2_scenes_bins/"
outfile = wdir + "scenes-and-bins.csv"
#tmw.scenes_to_bins(inpath,outfolder,outfile)


### 6 - pretokenize
inpath = wdir + "2_scenes/*.txt"
outfolder = wdir + "3_tokenized/"
#tmw.pretokenize(inpath,outfolder)


### 7 - call_treetagger
infolder = wdir + "3_tokenized/"
outfolder = wdir + "4_tagged/"
tagger = "/home/christof/Programs/TreeTagger/cmd/tree-tagger-french"
#tmw.call_treetagger(infolder, outfolder, tagger) 


### 8 - make_lemmatext
inpath = wdir + "4_tagged/*.trt"
outfolder = wdir + "5_lemmata/"
#tmw.make_lemmatext(inpath,outfolder)


### 9 - call_mallet_import
infolder = wdir + "5_lemmata/"
outfolder = wdir + "6_mallet/" 
outfile = outfolder + "tc30.mallet"
stoplist = wdir + "fr-lem.txt"
#tmw.call_mallet_import(infolder,outfolder,outfile,stoplist)


### 10 - call_mallet_model
inputfile = wdir + "6_mallet/tc30.mallet"
outfolder = wdir + "6_mallet/"
num_topics = "20"
optimize_interval = "100"
num_iterations = "2000" # for demo purposes
num_top_words = "20"
doc_topics_max = "20"
num_threads = "4"
#tmw.call_mallet_modeling(inputfile,outfolder,num_topics,optimize_interval,num_iterations,num_top_words,doc_topics_max)


### 11 - generate_wordlescores
word_weights_file = wdir + "6_mallet/" + "word-weights.txt"
wordlescores_file = wdir + "6_mallet/" + "wordle-scores.txt"
topics = 30
words = 100
#tmw.generate_wordlescores(word_weights_file,wordlescores_file,topics,words)


### 12 - aggregate_using_metadata
corpuspath = wdir + "5_lemmata"
outfolder = wdir + "7_aggregates/"
topics_in_texts = wdir + "6_mallet/topics-in-texts.txt"
metadatafile = wdir + "tc30-metadata.csv"
targets = ["author","decade","genre","insp-type","insp-region"] # USER: set depending on available metadata
#tmw.aggregate_using_metadata(corpuspath,outfolder,topics_in_texts,metadatafile,targets)


### 13 - aggregate_using_bins_and_metadata
corpuspath = wdir + "5_lemmata"
outfolder = wdir + "7_aggregates/"
topics_in_texts = wdir + "6_mallet/" + "topics-in-texts.txt"
metadatafile = wdir + "tc30-metadata.csv"
bindatafile = wdir + "scenes-and-bins.csv" # USER: segments or scenes?
target = "genre"
#tmw.aggregate_using_bins_and_metadata(corpuspath,outfolder,topics_in_texts,metadatafile,bindatafile,target)


### 14 - create_topicscores_heatmap
inpath = wdir + "7_aggregates/*hm.csv"
outfolder = wdir + "8_visuals/"
rows_shown = 16
dpi = 200
#tmw.create_topicscores_heatmap(inpath,outfolder,rows_shown,dpi)


### 15 - create_topicscores_lineplot
inpath = wdir + "7_aggregates/*lp.csv"
outfolder = wdir + "8_visuals/"
topicwordfile = wdir + "6_mallet/topics-with-words.txt"
dpi = 200
height = 0.100
genres = ["comedy","tragedy"] # User: set depending on metadata.
tmw.create_topicscores_lineplot(inpath,outfolder,topicwordfile,dpi,height,genres)





