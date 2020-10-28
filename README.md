# Higher moments

If we are given a set of random variables we can estimate the __rth moment__ by using:

![](https://render.githubusercontent.com/render/math?math=\widehat{\mu_r}=\frac{1}{n}\sum_{i=1}^{n}X_i^r)

The first moment is nothing more than the mean that we saw in the last exercise.  We can thus examine how the rth moment of the distribution depends on the number of random variables it is computed from by writing a code that is simlar to the code that we wrote to calculate how the mean depended on the number of random variables in the previous exercsie.  With this in mind I would like you to modify the code in `main.py` so that a graph is generated in which:

1. The red points indicate how the first moment (the sample mean) changes as n increases.
2. The blue points indicate how the second moment changes as n increases
3. The green points indicate how the third moment changes as n increases
4. The black points indicate how the square of the first moment (the square of the sample mean) changes as the number of point from which it is computed increases.

Notice that all these statistics appear to converge as the sample size increases.  Importantly, however, the second moment __does not__ converge to the value the square of the sample mean converges to.  The square of the sample mean is a __biased estimator__ for the second moment.  We will investigate these biased estimators further in the exercises next week.

You can use the variables called `ssum1`, `ssum2` and `ssum3` to accumulate the numerator in the expression above with r=1, r=2 and r=3 respectively.  The elements of the NumPy array `indices` should be set equal to 1, 2, 3, ...

