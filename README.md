# ChookEggCount
This project will count the number of chicken eggs found in an input image file.

I have uploaded a number of image files and associated "truth" tables to allow you to check your own detection approaches:
- RAW_images_Set1_16July2016.zip - (Set of 48) 1385 × 569 pixel JPEG images of the laying boxes at various times of the day
- RAW_images_Set2_16July2016.zip - (Set of 57) 1385 × 569 pixel JPEG images of the laying boxes at various times of the day
- RAW_images_Set3_16July2016.zip - (Set of 33) 1385 × 569 pixel JPEG images of the laying boxes at various times of the day

- truthtable_new_16July2016.csv - Comma-separated-value file: 
          - "filename" - name of the image file
          - "num_eggs" - number of eggs visible in the image (TRUTH)
          - "visible_hens" - Binary (0 or 1) indicating whether there were any hens visible in the image (TRUTH)

- OUTPUT_images_Set1_26July2016.zip - (Set of 48) 1385 × 569 pixel JPEG images - showing where eggs have been detected.

- RESULTS_Summary_26July2016.csv - Comma-separated-value file:
          - "detected_eggs" - number of eggs DETECTED in the image
          - "detected_hens" - binary (0 or 1) indicating whether there were are any hens DETECTED in the image
          - "filename" - name of the image file
          - "num_eggs" - number of eggs visible in the image (TRUTH)
          - "visible_hens" - Binary (0 or 1) indicating whether there were any hens visible in the image (TRUTH)
