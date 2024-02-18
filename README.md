<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# WinAIry

Final project for the Building AI course

## Summary

My AI project aims to identify the quality of wine based on the chemical attributes in a data set. It will try to do this using the Nearest Neighbour algorithm; at least that is the idea from the start.

From the given attributes it will choose a quality value to describe how good the wine is. The higher the value the better the wine. The value range from 1 to 10, but this could change.

## Background

<!-- Which problems does your idea solve? How common or frequent is this problem? What is your personal motivation? Why is this topic important or interesting? -->

I think it would not solve any specific problem more just aid people who want to make their own wine, and maybe see how good it is based on these characteristics. This project could also be used by people who have their own winery, who maybe do not want to spend money on expert to check how good the wine is. It might not be a specific or frequent problem, however for people who might need it the solution could be very useful.

My dad has a winery, or will start making wine soon, maybe I could test how well it predicts the quality with his wine. 

## How is it used?

<!--Describe the process of using the solution. In what kind situations is the solution needed (environment, time, etc.)? Who are the users, what kinds of needs should be taken into account?-->

I think in the begininng, it will just be a simple input of values in the console. But maybe, after the programming is done, I could make an application out of it. Then maybe place it here for people to use. But for now, I think the correct method of predicting will need to be chosen then making it accessible to others will be the next step. If we get that far :). 

<!-- 
Images will make your README look nice!
Once you upload an image to your repository, you can link link to it like this (replace the URL with file path, if you've uploaded an image to Github.)
![Cat](https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg)

If you need to resize images, you have to use an HTML tag, like this:
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg" width="300">

This is how you create code examples:
```
def main():
   countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
   pop = [5615000, 5439000, 324000, 5080000, 9609000]   # not actually needed in this exercise...
   fishers = [1891, 2652, 3800, 11611, 1757]

   totPop = sum(pop)
   totFish = sum(fishers)

   # write your solution here

   for i in range(len(countries)):
      print("%s %.2f%%" % (countries[i], 100.0))    # current just prints 100%

main()
```
-->

## Data sources and AI methods
Where does your data come from? Do you collect it yourself or do you use data collected by someone else?
The data that I will use comes from here:
Cortez,Paulo, Cerdeira,A., Almeida,F., Matos,T., and Reis,J.. (2009). Wine Quality. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T.

Like I said in the summary, I will try and use the Nearest Neighbour method to try and classify the input and predict. There are maybe better ways of doing this, but as I did not feel confident using this I wanted to practice. I could try others later. 

<!-- If you need to use links, here's an example:
[Twitter API](https://developer.twitter.com/en/docs) -->

#### The data summary for the red data set

|             | Fixed Acidity   | Volatile Acidity   | Citric Acid   | Residual Sugar   | Chlorides   | Free Sulfur Dioxide   | Total Sulfur Dioxide   | Density   | pH   | Sulphates   | Alcohol   | Quality   |
|:-----------:|:---------------:|:-------------------:|:-------------:|:-----------------:|:-----------:|:----------------------:|:-----------------------:|:---------:|:---:|:-----------:|:---------:|:---------:|
| Count       | 1599            | 1599                | 1599          | 1599              | 1599        | 1599                 | 1599                  | 1599      | 1599| 1599        | 1599      | 1599      |
| Mean        | 8.31964         | 0.527821            | 0.270976      | 2.53881           | 0.0874665   | 15.8749              | 46.4678               | 0.996747 | 3.31111| 0.658149   | 10.423    | 5.63602   |
| Std         | 1.7411          | 0.17906             | 0.194801      | 1.40993           | 0.0470653   | 10.4602              | 32.8953               | 0.00188733| 0.154386| 0.169507   | 1.06567   | 0.807569  |
| Min         | 4.6             | 0.12                | 0             | 0.9               | 0.012       | 1                   | 6                     | 0.99007  | 2.74    | 0.33       | 8.4       | 3         |
| 25%         | 7.1             | 0.39                | 0.09          | 1.9               | 0.07        | 7                   | 22                    | 0.9956   | 3.21    | 0.55       | 9.5       | 5         |
| 50%         | 7.9             | 0.52                | 0.26          | 2.2               | 0.079       | 14                  | 38                    | 0.99675  | 3.31    | 0.62       | 10.2      | 6         |
| 75%         | 9.2             | 0.64                | 0.42          | 2.6               | 0.09        | 21                  | 62                    | 0.997835 | 3.4     | 0.73       | 11.1      | 6         |
| Max         | 15.9            | 1.58               | 1             | 15.5              | 0.611       | 72                  | 289                   | 1.00369  | 4.01    | 2          | 14.9      | 8         |


<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# WinAIry

Final project for the Building AI course

## Summary

My AI project aims to identify the quality of wine based on the chemical attributes in a data set. It will try to do this using the Nearest Neighbour algorithm; at least that is the idea from the start.

From the given attributes it will choose a quality value to describe how good the wine is. The higher the value the better the wine. The value range from 1 to 10, but this could change.

## Background

<!-- Which problems does your idea solve? How common or frequent is this problem? What is your personal motivation? Why is this topic important or interesting? -->

I think it would not solve any specific problem more just aid people who want to make their own wine, and maybe see how good it is based on these characteristics. This project could also be used by people who have their own winery, who maybe do not want to spend money on expert to check how good the wine is. It might not be a specific or frequent problem, however for people who might need it the solution could be very useful.

My dad has a winery, or will start making wine soon, maybe I could test how well it predicts the quality with his wine. 

## How is it used?

<!--Describe the process of using the solution. In what kind situations is the solution needed (environment, time, etc.)? Who are the users, what kinds of needs should be taken into account?-->

I think in the begininng, it will just be a simple input of values in the console. But maybe, after the programming is done, I could make an application out of it. Then maybe place it here for people to use. But for now, I think the correct method of predicting will need to be chosen then making it accessible to others will be the next step. If we get that far :). 

<!-- 
Images will make your README look nice!
Once you upload an image to your repository, you can link link to it like this (replace the URL with file path, if you've uploaded an image to Github.)
![Cat](https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg)

If you need to resize images, you have to use an HTML tag, like this:
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg" width="300">

This is how you create code examples:
```
def main():
   countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
   pop = [5615000, 5439000, 324000, 5080000, 9609000]   # not actually needed in this exercise...
   fishers = [1891, 2652, 3800, 11611, 1757]

   totPop = sum(pop)
   totFish = sum(fishers)

   # write your solution here

   for i in range(len(countries)):
      print("%s %.2f%%" % (countries[i], 100.0))    # current just prints 100%

main()
```
-->

## Data sources and AI methods
Where does your data come from? Do you collect it yourself or do you use data collected by someone else?
The data that I will use comes from here:
Cortez,Paulo, Cerdeira,A., Almeida,F., Matos,T., and Reis,J.. (2009). Wine Quality. UCI Machine Learning Repository. https://doi.org/10.24432/C56S3T.

Like I said in the summary, I will try and use the Nearest Neighbour method to try and classify the input and predict. There are maybe better ways of doing this, but as I did not feel confident using this I wanted to practice. I could try others later. 

<!-- If you need to use links, here's an example:
[Twitter API](https://developer.twitter.com/en/docs) -->

#### The data summary for the red data set

|             | Fixed Acidity   | Volatile Acidity   | Citric Acid   | Residual Sugar   | Chlorides   | Free Sulfur Dioxide   | Total Sulfur Dioxide   | Density   | pH   | Sulphates   | Alcohol   | Quality   |
|:-----------:|:---------------:|:-------------------:|:-------------:|:-----------------:|:-----------:|:----------------------:|:-----------------------:|:---------:|:---:|:-----------:|:---------:|:---------:|
| Count       | 1599            | 1599                | 1599          | 1599              | 1599        | 1599                 | 1599                  | 1599      | 1599| 1599        | 1599      | 1599      |
| Mean        | 8.31964         | 0.527821            | 0.270976      | 2.53881           | 0.0874665   | 15.8749              | 46.4678               | 0.996747 | 3.31111| 0.658149   | 10.423    | 5.63602   |
| Std         | 1.7411          | 0.17906             | 0.194801      | 1.40993           | 0.0470653   | 10.4602              | 32.8953               | 0.00188733| 0.154386| 0.169507   | 1.06567   | 0.807569  |
| Min         | 4.6             | 0.12                | 0             | 0.9               | 0.012       | 1                   | 6                     | 0.99007  | 2.74    | 0.33       | 8.4       | 3         |
| 25%         | 7.1             | 0.39                | 0.09          | 1.9               | 0.07        | 7                   | 22                    | 0.9956   | 3.21    | 0.55       | 9.5       | 5         |
| 50%         | 7.9             | 0.52                | 0.26          | 2.2               | 0.079       | 14                  | 38                    | 0.99675  | 3.31    | 0.62       | 10.2      | 6         |
| 75%         | 9.2             | 0.64                | 0.42          | 2.6               | 0.09        | 21                  | 62                    | 0.997835 | 3.4     | 0.73       | 11.1      | 6         |
| Max         | 15.9            | 1.58               | 1             | 15.5              | 0.611       | 72                  | 289                   | 1.00369  | 4.01    | 2          | 14.9      | 8         |


#### The data summary for the white data set

|             | Fixed Acidity   | Volatile Acidity   | Citric Acid   | Residual Sugar   | Chlorides   | Free Sulfur Dioxide   | Total Sulfur Dioxide   | Density   | pH   | Sulphates   | Alcohol   | Quality   |
|:-----------:|:---------------:|:-------------------:|:-------------:|:-----------------:|:-----------:|:----------------------:|:-----------------------:|:---------:|:---:|:-----------:|:---------:|:---------:|
| Count       | 4898            | 4898                | 4898          | 4898              | 4898        | 4898                 | 4898                  | 4898      | 4898| 4898        | 4898      | 4898      |
| Mean        | 6.85479         | 0.278241            | 0.334192      | 6.39141           | 0.0457724   | 35.3081              | 138.361               | 0.994027 | 3.18827| 0.489847   | 10.5143   | 5.87791   |
| Std         | 0.843868        | 0.100795            | 0.12102       | 5.07206           | 0.021848    | 17.0071              | 42.4981               | 0.00299091| 0.151001| 0.114126   | 1.23062   | 0.885639  |
| Min         | 3.8             | 0.08                | 0             | 0.6               | 0.009       | 2                   | 9                     | 0.98711  | 2.72    | 0.22       | 8         | 3         |
| 25%         | 6.3             | 0.21                | 0.27          | 1.7               | 0.036       | 23                  | 108                   | 0.991723 | 3.09    | 0.41       | 9.5       | 5         |
| 50%         | 6.8             | 0.26                | 0.32          | 5.2               | 0.043       | 34                  | 134                   | 0.99374  | 3.18    | 0.47       | 10.4      | 6         |
| 75%         | 7.3             | 0.32                | 0.39          | 9.9               | 0.05        | 46                  | 167                   | 0.9961   | 3.28    | 0.55       | 11.4      | 6         |
| Max         | 14.2            | 1.1                 | 1.66          | 65.8              | 0.346       | 289                 | 440                   | 1.03898  | 3.82    | 1.08       | 14.2      | 9         |




## Challenges

<!-- What does your project _not_ solve? Which limitations and ethical considerations should be taken into account when deploying a solution like this? -->

I guess, it would not give suggestions for what to add or change when the predition is calculated, that might could be added later maybe. In the beginning at least hat will not be the plan. I am not sure what the ethical considerations may be but there is always the issue with using some else's data, I have given the source though. 

## What next?

<!-- How could your project grow and become something even more? What kind of skills, what kind of assistance would you  need to move on? -->

This could grow in many different ways, for example being an assistent in the production of wines, but for now it is just a classifier. We shall see if it leads anywhere. I will probably need to improve my data cleaning skills. My programming skills will have to be better as well. That is a part of the process. We shall see how far I get with this. 

## Acknowledgments

<!-- * list here the sources of inspiration 
* do not use code, images, data etc. from others without permission
* when you have permission to use other people's materials, always mention the original creator and the open source / Creative Commons licence they've used
  <br>For example: [Sleeping Cat on Her Back by Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
* etc -->
I would like to thank the professors at Linköping and Helsinki for the chance to do these two courses. They have been educational, fun and easy to understand.
If I have used anything without giving the credit, please let me know and I will add your name at the appropriate place. 
