# Seneca
This repository contains code and data for the paper "Morphological Segmentation for Seneca", to appear in AmericasNLP 2021

## Data set construction when evaluating with a development set##
There are two data sources: a grammar book (Bardeau 2007), and words collected from transcribed informal recordings.

To constuct data sets for the grammar book, do:
```python3 code/segmentation_data.py --input resources/all-forms-from-spreadsheet.txt --output OUTPUT_PATH --lang grammar```

The data generated this way in our experiments is in 1/grammar/:
  1. baseline contains data used to train the Naive baseline
  2. tuning contains data used to train the Less naive baseline
  3. domain contains data for a series of cross-domain training experiments
    a. 
