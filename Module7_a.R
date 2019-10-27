#1 Load the required libraries and the data

library(shiny)

data = read.csv('C:\\Users\\376020\\Desktop\\Masters\\R_Module7\\Datasets\\app2data.csv')

#2 Understand the data structure and provide concise summary on the following -
# . no of observations
# . total number of variables
# . number of continuous variables
# . number of categorical variables
# . number of variables which have missing values

str(data)

summary(data)

#3 Create separate UI and server files and save it in a separate folder where you
# have kept the data as well.


ui = fluidPage(titlePanel('Basic Data Table'),
               
               fluidRow(
                 
                 column(4,selectInput(inputId = 'i1',label='Manufacturer',choices = c('BMW','HONDA','Maruti','Tata Motors'))),
                 
                 column(4,selectInput(inputId = 'i2',label='Transmission',choices = c('Auto','Manual'))),
                 
                 column(4,selectInput(inputId = 'i3',label='Cylinders',choices = c(4,5,6))),
                 
                 fluidRow(
                   
                   column(5,selectInput(inputId = 'i4',label='how',choices = c('BMW','HONDA','Maruti','Tata Motors'))),
                   
                   column(5,textInput(inputId = 'i5',label='Search'))
                   
                 )))

server = function(input,output){
}

shinyApp(ui=ui,server=server)
