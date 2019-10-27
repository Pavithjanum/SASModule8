#1 Load the required libraries and the data.

library(shiny)

library(DT)

library(dplyr)

data = read.csv('C:\\Users\\376020\\Datasets\\app2data.csv')


#2 Understand the data structure and provide concise summary on the following -
# . no of observations
# . total number of variables
# . number of continuous variables
# . number of categorical variables
# . number of variables which have missing values

str(data)
summary(data)

#3 Create separate UI and server files and save it in a separate folder where you have kept the data as well.

ui = fluidPage(title='Basic Data Table',
               
               fluidRow( column (4,
                                 
                                 selectInput(inputId = 's1',label = 'Manufacturer',choices = c('All','BMW','Honda','Maruti','Tata Motors'))),
                         
                         column (4,
                                 
                                 selectInput(inputId = 's2',label = 'Transmission',choices=c('All','Auto','Manual'))),
                         
                         column (4,
                                 
                                 selectInput(inputId = 's3',label = 'Cylinders',choices = c('All',4,5,6)))),
               
               #               fluidRow( 
               
               #               column (4,
               
               #               selectInput(inputId = 's4',label = 'how many entries',choices = c(1:nrow(data)),selected=10)),
               
               #                       column (8,
               
               #               textInput(inputId = 's5',label = 'Search'),align='right')),
               
               fluidRow(
                 
                 
                 
                 DT::dataTableOutput(outputId = 'o1')
                 
                 #                 textOutput(outputId = 'o2')
                 
               )
               
)


server = function(input,output){
  
  
  
  #  output$o1 <- renderTable((filter(data,manufacturer==  (if (input$s1 == 'All') {manufacturer} else {input$s1}) & 
  
  #                                    trans == (if (input$s2 == 'All') {trans} else {input$s2}) & 
  
  #                                    cyl == (if (input$s3 == 'All') {cyl} else {input$s3}))) %>% head(as.numeric(input$s4)))
  
  #  output$o2 <- renderText(paste('showing 1 to ',as.numeric(input$s4),' entries'))
  
  
  
  output$o1 <- DT::renderDataTable((filter(data,manufacturer==  (if (input$s1 == 'All') {manufacturer} else {input$s1}) & 
                                             
                                             trans == (if (input$s2 == 'All') {trans} else {input$s2}) & 
                                             
                                             cyl == (if (input$s3 == 'All') {cyl} else {input$s3}))))
  
  
  
}


shinyApp(ui=ui,server=server)

top_n(data,1)

#1

library(shiny)
library(DT)
library(dplyr)
data = read.csv('C:\\Users\\376020\\Desktop\\Masters\\R_Module7\\Datasets\\app2data.csv')

#2

str(data)
summary(data)

#3

source('C:\\Users\\376020\\Desktop\\Masters\\R_Module7\\UI.R')

#4
source('C:\\Users\\376020\\Desktop\\Masters\\R_Module7\\server.R')
shinyApp(ui=ui,server=server)

top_n(data,1)
