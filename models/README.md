# What is Linear Regression?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linear regression is a basic and commonly used type of predictive analysis.
>Regression is used to explain the relationship between one dependent variable and one or more independent variables. The simplest form of the regression equation with one dependent and one independent variable is defined by the formula ***y = b0 * x + b1***, where y = estimated dependent variable score, b0 = regression coefficient, x = score on the independent variable, and b1 - intercept. I.e. linear regression is based on linear function f(x) = x. It's certainly true, cause the plot of linear regression is a line.

On the picture represented below you can see scatter plot of data and fitted line. 

![](https://miro.medium.com/max/642/1*xxxqZtZExBJoxmYKIY-waw.png)

Three major uses for regression analysis:
* Determining the strength of predictors;
* Forecasting an effect;
* And trend forecasting.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Firstly, the regression might be used to identify the strength of the effect that the independent variable(s) have on a dependent variable.  Typical questions are what is the strength of relationship between dose and effect, sales and marketing spending, or age and income.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Secondly, it can be used to forecast effects or impact of changes.  That is, the regression analysis helps us to understand how much the dependent variable changes with a change in one or more independent variables.  A typical question is, “how much additional sales income do I get for each additional $1000 spent on marketing?”

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Thirdly, regression analysis predicts trends and future values.  The regression analysis can be used to get point estimates.  A typical question is, “what will the price of gold be in 6 months?”

## The core idea is to obtain a line that best fits the data.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The best fit line is the one for which total prediction error (all data points) are as small as possible. Error is the distance between the point to the regression line. And usually this error is called 'mead squared error', cause it's the most widely used kind of this error.
The formula of the MSE is looked pretty simple, is not it.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSf71hzM1lRSEMMwV2wQLR1f5LNSIm1dkDIhMi22RpGfVE3Sr0GAw)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The picture below represents the main idea of this approach. The points of scatter plot are actual outputs and the points on the line which the actual outputs connects with are predicted_outputs. So, the approach is to sum up all the squared distances from actual_input to predicted_output.

![](https://uc-r.github.io/public/images/analytics/regression/sq.errors-1.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Moreover, slope and intercept (b0 and b1) are calculated according to the following formulas:

![](https://miro.medium.com/max/243/1*1evY0PuCUENCpDP_QRplig.png)

&nbsp;&nbsp;![](https://miro.medium.com/max/383/1*Cx1Yej9zLVI1O16I3mODqA.png)


# Metrics for model evaluation.

1. Correlation co-efficient (r).                    
It ranges from -1 to 1 and tell us how good two quantitative variables are related. If coefficient is positive, relashionship of veriables is big, if coefficient is negative - it's not.

![](http://www.datasciencemadesimple.com/wp-content/uploads/2017/07/CORRELATION-COEFFICIENT-FORMULA.png)

2. Regression sum of squares (SSR).                                     
This gives information about how far estimated regression line is from the horizontal ‘no relationship’ line (average of actual output).

![](https://miro.medium.com/max/818/1*eXRB9iStTLFtrPkSfbWEHg.png)

3. Sum of Squared error (SSE).                                        
How much the target value varies around the regression line (predicted value).

![](https://miro.medium.com/max/696/1*M7ukJZNTvPd6tQqNXxGGzQ.png)

4. Total sum of squares (SSTO).                                                         
This tells how much the data point move around the mean.

![](http://www.fairlynerdy.com/wp-content/uploads/2017/01/r_squared_6.png)

---

If you haven't experienced this task before, an understandable and well-orginized information can be taken from [HERE](https://www.statisticssolutions.com/what-is-linear-regression/) and [HERE](https://en.wikipedia.org/wiki/Linear_regression).
