# tjsp_data_treatment

Collection of relevant terms and cleaning of TJSP judgments

Before using the provided functions, it is necessary to have scraped data from TJSP according to a specific list of terms. These functions aim to facilitate the analysis and visualization of the scraped decisions.

The file **"cleaning.py"** contains a program that removes white spaces and repetitive terms from the judgments.

The code in **"collection.py"** allocates, in a new column of the spreadsheets, the excerpts from each judgment that contain the searched term, and also highlights mentions between different cases.

Finally, with **"mark_new_results.py"**, the scraping spreadsheets are compared with their previous versions, and the new found cases are marked with the "*" character.

In all files, it is necessary to change the directory paths for opening and saving spreadsheets.





