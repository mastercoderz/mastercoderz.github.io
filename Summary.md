
The following is a summary of our efforts in the development of this probability analysis program:
    =====================================================================
      1. Get data pools (group1, group2)
      2. Modify data pools using intersectSets with base lib
      3. Establish word counts for each respective group
      4. Loop through each group and calculate prob. of word occurring
           in that group (do this for every word)
      5. Store dict = {word : (prob group, prob overall)}, for each group
      6. determine change in probabilities between groups for every word
           compare this change 
      7. Pick the top 20 words whose delta probability is highest (use pq
           again)
      8. Use log likelihood calculations to determine a better measure of
           the probaiblity of the words appearing
      9. Infer cool things about what caused changes in word appearance
           over time
    ======================================================================
