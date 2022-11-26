# PP5 - Vape City

Vape City is an e-commerce site that allows users to order vaping products and paraphernalia as a one off purchase and also subscribe to receive products on a regular basis with a discount for subscribing. As an avid vaper I struggle to find vaping e-commerce platforms with good UX and subscription models that are reliable. This is a problem in the vaping industry as retail vaping products are generally supplied by very small businesses that cannot afford good developers. They also cannot use popular self-build platforms such as Shopify as most ban the setup of vape shops due to the lack of regulation in the vaping space. My goal with this site is to use the skills and knowledge I have learning throughout this course to solve this real-world problem with an e-commerce site that could become a trusted brand with good UX and a reliable subscription model.

[The live project can be viewed here.]()

![](docs/images/ismysiteresponsive_screenshot.png)

# Planning

I started this project by setting up a project in GitHub and using agile methodologies to define user stories that would guide me in the development of site. This allowed me to develop the site in small sprints by focusing on one user story at a time. The goal with using this agile methodology was to prevent me becoming overwhelmed with several developments at once. In the past I have tended to flip between front-end UX and back-end application and get lost or overwhelmed trying to code too many things at once.

Please see my initial GitHub issues:

![](docs/images/plan-flow-diagram.png)


# How to use Vape City

# Features

## Existing Features

## Future Features

# Custom Models
I decided to use Google Sheets as my data model rather than storing data in data model classes. I felt this was more realistic for my imagined purpose as the imagined user is not a programmer. There is possibility with future development that I could take data from the Google Sheet and store that in classes. I would use this especially to be able to develop the functionality for multiple Dealer ID's and sales inputs.

I have used other objects as temporary data storage such as a dictionary to store the dealer name in a function. This dictionary is then used in the function to access dealer names across multiple functions.

I have also used pandas to create a dataframe to access and manipulated data when pulling previous sales data from the pay worksheet

# Testing

I have manually tested Pay Calculator in the following ways:

* Pass the code through PEP8 linter and confirmed there are no errors
* Inputted different types of incorrect data into the input fields, i.e. special characters, strings where there should have been integers, negative numbers in sales data, empty inputs etc. And have confirmed no unexpected error messages.
* Tested the programme in both my GitPod terminal and Code Institute instance of Heroku and the programme runs exactly as expected.

## Bugs

Solved bugs:

* Float error 1:

In my original function for getting sales data, I hadn't accounted for float values as sales - sales may not always be a integer. I was receiving errors such as:

![](docs/images/float-error.png)

To fix the issue I created a function to check and pass the value if it was a float or an integer and pass an error if it is not:

![](docs/images/sales-data-validation-function.png)

* Float error 2

Once I allowed floats to be passed into the programme, I then had to account for them in the functions that calculate dealer and house pay. I did this by getting the function to run a different sum based on int() and float() methods depending on which value was passed. For example in calculating dealer pay, I used the following:

![](docs/images/dealer-pay-ifs.png)

## Remaining Bugs

* No known bugs outstanding in programme

## Validator Testing

I validated the code in PEP8 and no errors were returned:

![](docs/images/pep8-results.png)

# Deployment

I followed the following steps to deploy Pay Calculator to Code Institute's instance of Heroku:

* Update requirements.txt to include gspread library, Google Auth, pandas and datetime
* Push requirements.txt to GutHub repository
* Create new Heroku app
* Create a config var in app settings for credentials for my Google Sheet
* Create a config var for PORT 8000 as requested by Code Institute in README.md and lessons
* Add heroku/python buildpack
* Add heroku/nodejs buildpack
* In app deploy tab deploy main branch from GitHub repository manually to check there are no build errors
* In app deploy deploy main branch to automatic once programme is complete

The programme is live [here](https://pp3-pay-calculator.herokuapp.com/).

# Technologies Used

I used the following technologies:

* Hardware: MacBook Pro
* GitHub
* GitPod
* Google Chrome, Firefox and Safari web browsers
* Gspread library
* Datatime python module
* Pandas dataframe library
* Heroku

# Credits

* Code Institute for the Heroku deployment terminal
* Code Institute for the instructions and SCOPE details to wire up Google Sheets and gspread
* Code Institute for various inspirations in functions as commented in function multiline strings in run.py










