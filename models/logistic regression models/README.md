# What is Logistic Regression?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Logistic regression is a statistical model that predicts **binary** outcomes. Its basic form uses the **Sigmoid** function that also called the logistic function gives an ‘S’ shaped curve that can take any real-valued number and map it into a value between 0 and 1.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It is the appropriate regression analysis when the dependent variable is categorical. As a simple example, we can predict sex of person using some data. Like all regression analyses, the logistic regression is a predictive analysis. It is used to describe data and to explain the relationship between one dependent variable and one or more numerical predictors. Actually, we can just consider that logistic regression is some case of linear regression where dependent variable is a categorical.                                                  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Main function on which our model based is placed below. As you can see it takes values from 0 to 1.

![](https://ars.els-cdn.com/content/image/3-s2.0-B9780128154588000074-f07-02-9780128154588.jpg)

# Step by step
&nbsp;&nbsp;&nbsp;As we say, logistic regression is similar to linear regression. So, linear equation:

![](https://miro.medium.com/max/462/0*c28OC-B--sPBd0wG.png)

&nbsp;&nbsp;&nbsp;The graph of the sigmoid function is defined by the following formula:

![](http://res.cloudinary.com/dyd911kmh/image/upload/f_auto,q_auto:best/v1534281880/image4_gw5mmv.png)

&nbsp;&nbsp;&nbsp;All that we have to do is to pass linear equation to **sigmoid function**. We get something like this:

![](https://miro.medium.com/max/395/0*1-TM_M93_cM6xIe1.png)

&nbsp;&nbsp;&nbsp;Main conclusion: if the output of the sigmoid function is more than 0.5, we can classify the outcome as 1 or YES, and if it is less than 0.5, we can classify it like 0 or NO. If the output is 0.75, we can say in terms of probability as: There is a 75 percent chance that patient will suffer from cancer.

## Logistic regression assumptions
* Binary logistic regression requires the dependent variable to be binary.
* Only meaningful variables should be included.
* The independent variables should be independent of each other. That is, the model should have little or no multicollinearity. More about multicollinearity: https://www.statisticssolutions.com/multicollinearity/.
* For a binary regression, the factor level 1 of the dependent variable should represent the desired outcome.
* The independent variables are linearly related to the log odds.
* Logistic regression requires quite large sample sizes.

## Model evaluation
&nbsp;&nbsp;&nbsp;Usually, we can evaluate with such metrics as accuracy, presicion, recall, confusion matrix. Further in details.
* Accuracy is the most standard method to evaluate the model. It's just a num of right predictions divided by total number of data objects.
* Precision is about being precise, i.e., how accurate your model is. In other words, you can say, when a model makes a prediction, how often it is correct. In your prediction case, when your Logistic Regression model predicted customers will buy the magazine 69% of the time.
* If there are customers that bought the magazine in test data and your Logistic Regression model can identify it 85% of the time.
* A confusion matrix is a table that is often used to describe the performance of a classification model on a set of test data for which the true values are known.

![](https://miro.medium.com/max/712/1*Z54JgbS4DUwWSknhDCvNTQ.png)
- True positives (TP): These are cases in which we predicted yes and are actually yes.
- True negatives (TN): We predicted no, and no in actual.
- False positives (FP): We predicted yes, but actual is no. (Type I error)
- False negatives (FN): We predicted no, yes in actual. (Type II error)


                                                                                                              
&nbsp;&nbsp;&nbsp;If you haven't experienced this task before, an understandable and well-orginized information can be taken from [HERE](https://en.wikipedia.org/wiki/Logistic_regression) and [HERE](https://machinelearningmastery.com/logistic-regression-for-machine-learning/).
