# Introduction 
Being the third son in my family, I wanted to answer some childhood questions using data science and econometrics.

1. To what extent does having two kids of the same sex impact a couples probability to have more than two kids? 
2. How does having more kids affect a mother's likelihood to return to work?
3. How does having a larger number of children impact family earnings?

![joint](https://github.com/WinsonTruong/3rdson/blob/master/images/logearnings_joint.png)


# Notion Page
There is a dedicated Notion page that narrates the results, work-flow, and model descriptions to much greater extent.
[Check it out here](https://www.notion.so/winsontruong/Investigations-of-the-3rd-Son-98b818c3aa0d4f6d817c125f8d244f47)


# Data
Found in the 'data' folder, our data comes from the 2010 Census and it contains information about 236,459 married couples*. Each row represents one member of a couple. All couples have:

* at least 2 children
* a traditional mother and father
* an age between 21 and 35
* a father that worked in the past year

Read about the metadata for [all 42 features here](https://www.notion.so/winsontruong/Metadata-3a70fb580c6041f582956374ba8e67a0). Thank you to David Card and his class Econometrics C142 for providing sample.csv file. 


# Models
The modeling work and intermediate results can be found in the 'notebooks' folder where there are 4 Python notebooks. Here's a quick overview of what I did:

- Linear Probability Models
- Logit Models
- Instrumental Variables / 2-Stage Least Squares

### What's my statistic?
**The odds-ratio**. Why? The odds-ratio is simple to understand and can be used to compare the feature sets!


# Results

1. The odds of having more than two children increases by ~98% for every additional year Asian and Pacific Islander-identifying mothers age.
2. Having more than two children decreases the probability of the mother returning to work by about 13% (sorry Mom?)
3. Having more than two children decreases earnings much more for the mother than it does the father.


# Further Work
This folder contains a notebook that builds on findings in the original project scope by looking at earnings by state.
