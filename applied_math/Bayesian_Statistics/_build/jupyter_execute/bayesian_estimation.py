#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy


# # Bayesian Estimation
# Given a parametric model $P_\theta \in \mathcal{M}_\theta$ and a random sample $X = (X_1,X_2,X_3,...,X_N)$. The goal is to find $p(\theta|x)$, where $x$ is a realisation of $X$. To do this, we use the Bayes formula:
# 
# $$ p(\theta|x) = \dfrac{p(x|\theta) \pi (\theta)}{p_X (x)} $$
# 
# or just:
# 
# $$ p(\theta|x) \propto p(x|\theta) \pi (\theta) $$
# 
# In general, we need 4 steps:
# 
# 1. Find the likelihood function.
# 2. Choose a prior distribution and use the Bayes formula
# 3. Recognise a known distribution from previous result (Or find it numerically)
# 4. Find the posterior probability law.
# 
# ## Bernoulli Experiment
# 
# We will use the Bayesian Estimation to infer the parameter $\theta$ of the Bernoulli trial.
# 
# Let $X = (X_1,X_2,X_3,...,X_N)$ be a i.i.d. random sample such that $X_i \sim \mathcal{B}(\theta), i \in \{1,2,...,N \}$
# 
# We start by the first step:
# 
# ### Find the likelihood function
# 
# Since we are dealing with a i.i.d. random sample:
# $$ P(x|\theta) = \prod_{i = 1}^N P(x_i|\theta) = \prod_{i = 1}^N \theta^{x_i}(1 - \theta)^{1 - x_i} = \large \theta^{\sum_{i = 1}^N x_i} (1 - \theta)^{N - \sum_{i = 1}^N x_i} $$
# 
# Let $S(x) = \sum_{i = 1}^N x_i$, then we would have:
# 
# $$ \large P(x|\theta) = \theta^{S(x)} (N - \theta)^{1 - S(x)} $$
# 
# ### Choose a prior distribution and use the Bayes formula
# 
# Since we do not have anymore information about the system, we cannot think of a special type of prior $\pi (\theta)$, so we will use the uniform distribution $\mathcal{U}([0,1])$ to treat each possible $\theta \in [0,1]$ with the same "importance", then we have:
# 
# $$ p(\theta|x) \propto p(x|\theta) \pi (\theta) = \theta^{S(x)} (1 - \theta)^{N - S(x)}$$
# 
# Recall that $\pi(\theta) = \mathcal{U}([a,b]) \Leftrightarrow \pi(\theta) = \dfrac{1}{b-a}$, in particular, $\pi (\theta) = \mathcal{U}([0,1]) \Leftrightarrow \pi (\theta) = 1$
# 
# ### Recognise a known distribution from previous result
# 
# We found that $ p(\theta|x) $ is proportional to the **Beta distribution** $Beta(S(x) + 1, N - S(x) + 1)$.
# 
# ### Find the posterior probability law
# 
# Since we have a distribution proportional to another distribution, they are equal! Then we have:
# 
# $$ p(\theta|x) = Beta(S(x) + 1, N - S(x) + 1) $$
# 
# Now we are going to see a numerical example with several values for $N$.

# # Decision Theory
# 
# The previous result is very interesting, but we are not just interested in having interval of possible values. We also want to find a value that we could use to make predictions, that is, we want to find the "best" value of $\theta$.
# 
# To find this "best" value, we have to define what do we mean by "best". In fact, we are going to define a **Loss function** $L(\theta,\hat{\theta})$ that will quantify this sense of optimality and hopefuly it will lead us to a single value of $\theta$. As we shall see later, there are certain conditions that our problem must satisfy so we can have only one value for $\theta$, but we will proceed as all the problems will satisfy all these conditions for now.
# 
# The choice of this **Loss function** is what gave birth to the field of **Decision Theory**, which give us the necessary tools to solve our problems.
# 
# To find the best $\hat{\theta}$ we have to solve the following equation:
# 
# $$ \large \hat{\theta} = arg \min _{\delta \in \Theta} \mathbb{E}_{p(\theta|x)}(L(\theta,\delta)) $$
# 
# The choice of this Loss function is up to the problem. Sometimes we want to give different importances to depending of the errors, for example if we are diagnosing a human with a disease, classify someone as healthy while she is sick may be catastrophic and we would try to forbid this to happen.
# 
