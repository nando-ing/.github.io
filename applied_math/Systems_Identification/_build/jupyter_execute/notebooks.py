#!/usr/bin/env python
# coding: utf-8

# # Introduction to Systems Identification
# 
# In this notebook, I will explain how can we use data to find a model that 
# describes somehow the process which generated that same data. For example, 
# suppose we have a DC(Direct Current) Motor, but we don't know the parameters
# which characterizes it, such as coupling factor, coil resistance and Inertial
# moment.
# 
# We would like to know how the motor behaves as we change its inputs, that is,
# the voltage on its coils. In other words, we can say we are interested in 
# describing the motor dynamics.
# 
# In order to achieve this goal, we could do the following approach to obtain a 
# model describing the motor behavior:
# 
# 1. Put an encoder sensor in the motors rotor, so we can know the angular
# velocity in which the rotor turns.
# 
# 2. Put a sensor to measure the motor input voltage 
# $u:\mathbb{R}^+ \to I$, where $I = [V_{min}, V_{max}]$, so we can know the input
# at each given time.
# 
# 3. Use the input and output captured to infer the system dynamics. In other words,
# to find the transformation.
# $\mathcal{T}: \mathcal{F}(\mathbb{R}^+,I) \to \mathcal{F}(\mathbb{R}^+,\mathbb{R})$
# 
# There are several ways one can proceed to achieve our goal.
# 
# For example, we could just try to fit a linear model of order $n$, and if the system
# is nonlinear, we could try a generic nonlinear method. However, in this case, 
# we can proceed differently, incorporating more prior knowledge to our model.
# 
# Note that we already know from the eletromecanical equations that we have a
# second order differential equation, so we can just fit our model to a second
# order differential equations, finding the parameters that best suits our system.
# 
# This approach I just described is called _parameter estimation_, since we have
# already a prior structure to the model and we just want to find its best 
# parameters.
