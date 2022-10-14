This repository is to provide the code to the article 'A Pilot Study on Identifying Gene Signatures as Markers for Predicting Patient Response to Antiseizure Medications'. Please note that this code is ONLY provided for academic use.

folder list:
  
    1.Identification of Differentially Expressed Genes : The code for identification of differentially expressed genes and box plot used in the article.
    2.Prediction of possible response to ASMs: The code for prediction of possible response to ASMs.
    
 
Note：
- Make sure you have installed:
  + ***pandas***
  + ***numpy***
- Make sure you have installed and started ***docker***

- Stay in folder **demo**
  - run 
  ```
  chmod -R +x ./cmap
  chmod -R +x ./datasets
  ```
  
- Change shell file 'datasets/examples/run_query.sh'
  - Use `vim ./datasets/examples/run_query.sh` and then specify your own path

  - Change paths listed below
    - UP_GENESET
    - DOWN_GENESET
    - SCORE_FILE
    - RANK_fILE
    - SIG_META_FILE
    - RESULTS
- Run `datasets/examples/run_query.sh` in folder **demo**
