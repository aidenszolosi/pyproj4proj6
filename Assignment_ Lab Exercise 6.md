pAssignment: Lab Exercise 6

6:02 Estimated 1267 Words EN Language

**Assignment: Lab Exercise 6**  
Python: Exercise calculator with BMI & Karvonen formulas

\>

The objectives of this lab assignment are as follows:

*   Input data from user
*   Perform several different calculations
*   Process data within a loop
*   Make output choices based on conditional logic
*   Output information to user

Skills Required
---------------

To properly complete this assignment you will need to apply the following skills:

*   Read string input from the console and convert input to required numeric data-types
*   Convert math formulas to Python code
*   Research and apply correct conversion formulas
*   Understand the if / elif / else construct
*   Output numeric data to specific decimal places

Assignment User Story
---------------------

As a user I want an application that will allow me to calculate a person's Body Mass Index (BMI) as well as to apply the Karvonen formula in calculating the user's heart rate at varying levels of exercise intensity.  

In this application we are calculating two different values: the first is the Body Mass Index (BMI) and the second is a series of maximum heart rate values at specific exercise intensity percentages calculated using the Karvonen formula.

Building on the work that you have already done or begun thinking about this application must be protected against invalid numeric data entry. Therefore, you must use _while_ loops to prompt the user for each requested value until the value entered is valid—until the user enters acceptable numeric data.

Furthermore, as this assignment is coming after your reading about functions, it is expected that you will define at least two functions in your program. The first function will calculate and return the BMI value based on the height (inches) and weight (pounds) passed into the function. And the second function will calculate and return the Karvonen maximum heart rate given the intensity, resting heart rate, and age passed into the function.

When complete, your output should be as pictured below:

![Image example output](https://softchalkcloud.com/lesson/files/njUvRZqCb1mDIH/HealthCalculator%20output.png)

**Note** : The example output provided above is simply an example. You do not need to format your output to look exactly like mine. You simply need to ensure that you have met the technical requirements for this application and ensure your output is neat and professional looking.

BMI
---

BMI is a calculation of body fat based on an individual's height and weight.

To calculate BMI you need two different values: height in inches and weight in pounds. Once you have obtained these values you will then need to convert the height from inches to height in meters squared, and the weight in pounds to the weight in kilograms. I am not going to provide these conversion formulas to you; you have to do a little online research to find them. In the case of converting inches to meters squared you need to convert inches to meters and then square that value.

The formula for calculating BMI is as follows:

where:

*   weight is value in kilograms
*   height is value in meters squared -- note, one way to obtain the square of a number is to multiply that number by itself

The value for bmi will be a decimal from zero (dead) to a high number indicating high body fatness. Based on the BMI value a person is categorized according to their body fat as follows:

*   Underweight = <18.5
*   Normal weight = 18.5–24.9
*   Overweight = 25–29.9
*   Obese = BMI of 30 or greater

In addition to calculating the user's BMI you will determine which of the above categories the user falls into based on their BMI.

There are many online calculators that you can use to check your BMI results, one such can be found at the National Institute of Health. (Link to website here.)

Karvonen Formula
----------------

The Karvonen formula is used to calculate a target heart rate at specific workout intensities. It can be used to calculate ideal heart rate ranges for specific kinds of workout intensities. What I wish to do is to calculate what the maximum heart rate will be based on exercise intensity that begins at 50% and increases by 5% to a maximum intensity of 95%. This, of course, implies using a loop. We want to construct a loop that will iterate this calculation for the maximum heart rate for each of our exercise intensity percentages.

To calculate maximum heart rate according to the Karvonen formula you need two different values: age and resting heart rate.

The formula for calculating the maximum heart rate is as follows:

This is an exercise in mathematic order of operations.

Another way to think about the fomula above is to break it down like . . .

where:

1.  mhr is maximum heart rate calculated as 220 minus your age
2.  hrr is heart rate reserve calculated by taking maximum heart rate (from step 1) minus resting heart rate
3.  mtz is maximum target zone calculating by taking heart rate reserve (from step 2) multiplied by intensity percent
4.  ttz is target training zone calculated by taking mtz (from step 3) and adding resting heart rate

example:

Suppose you have a resting heart rate of **70** beats per minute and your age is **35**, and let's suppose we want to know what the maximum heart rate should be at **60%** intensity workout:

220 - **35** = 185 (this results in the maximum heart rate -- **mhr**)  
185 (**mhr**) - **70** = 115 (this results in the heart rate reserve -- **hrr**)  
115 (**hrr**) \* **.60** = 69 (this results in the maximum target zone -- **mtz**)  
69 (**mtz**) + **70** = **139** (this is the result that will be output for 60% exercise intensity)

Therefore, **139** is the maximum heart rate for someone who is **35** years of age, has a resting heart rate of **70**, and is exercising at a **60%** intensity level.

We want to perform this calculation for each exercise intensity level from 50% to 95%, with each level incremented by 5%

There are many online calculators that you can use to check your Karvonen results, one such is from this website (Link to website here.)

You must ensure that the application you submit meets all technical/grading requirements. Your grade will be based on how well your application follows the application requirements plus the following:

*   The name of the application with be LastName-HealthCalculator.py (i.e. pagura-HealthCalculator.py)
*   You must have a set of comments at the top of the program that identifies the programmer, date, and name of the program file. Each of these must be on individual lines. In addition, you must also provide a short description of what this program is doing
*   The following four pieces of data will be entered by the user: height in inches, weight in pounds, age, and resting heart rate
*   Using the entered data the BMI value along with the BMI Category will be determined
*   Displaying exercise intensities from 50% (.55) to 95% (.95) the maximum heart rate at each exercise intensity will be calculated and displayed
*   The BMI value will be displayed to two decimals
*   The intensity value will be displayed as a percentage with no decimal value
*   The max heart rates will be displayed as a numeric value with no decimals
*   All numeric values will be formatted as indicated above
*   All numeric values will be validated to ensure the user has keyed appropriate entry into the application.
*   You must demonstrate your knowledge of functions by creating at least two functions: one to calculate the BMI and the second to calculate the maximum heart rate given a specific workout intensity.

How the application looks and how it presents its information to the user is up to you. But it must meet the minimum requirements noted above.

**Important**: Your output must include all of the following: BMI value, BMI category, one row for each exercise intensity from 50% to 95% in 5% increments (performed in a loop) and each row must include the intensity value as a percent and the maximum heart rate at that intensity.
> Generated by [Clearly Reader](https://clearlyreader.com)