
*The following is a summary of our goals in the development of this probability analysis program:*

Basically, we wanted to take two pools of data - each representing the newspapers in a given year - and get the words whose use varied the most between these two data pools. We didn't get to implement this final portion to to time and some error constraints, though the foundation is here. We were encouraged to use a "log likelihood" calculation to improve the models predictive accuracy. We also worked on graphical analysis given a specific word, over the entire data set. Our idea was to take words returned through our probability analysis calculations and use them as input for this more specific analysis. Thus, we could see a pool of words whose use varied greatly (above a certain user dictated threshold) over time, and then we could graph the incidence of these words and use the results to infer broadly about things like social issues or current events. 

Part 1: establish a base collection of words:
      - User can choose a collection of text files 
      - The collection will be established based on the most possible n words (user may choose), we used 5,000
      - This collection establishes a basis for comparison with our two data pools, so we only need to look at words in a 
            pool that are also in the library
            
Part 2: establish some sort of probability comparison:

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

Our end goal was to create a program that took as input two time periods and returned the top 20 words that saw the most change in use over this time period. Although we weren't able to produce our final output, we felt that we 
