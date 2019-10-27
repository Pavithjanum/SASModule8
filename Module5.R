#1. 
#Load the required libraries and the data.

library(ggplot2)

setwd(choose.dir())

getwd()

data = read.csv('b0078brlpa.csv')

# 2. 
# Understand the data structure and provide concise summary on the following – 
# • no of observations 
# • total number of variables 
# • number of continuous variables 
# • number of categorical variables 
# • number of variables which have missing values 

str(data)

summary(data)
head(data)

# 3. 
# Create a scatter plot between Credit_Record on x-axis and Income on y-axis.  
# • Is the plot satisfying, if not, what could be the reason? 
# • Change the command executed in the previous line so that Credit_Record is treated as factor.  
# • what is the change in the above two plots?


plot(data$Income ~ data$Credit_Record,xlab='Credit Record',ylab='Income',
     main='Scatter Plot between Income and Credit Record',col='palegreen4')

str(data)

#The Credit_Record is in int that are categorical in nature.
#i.e, the value is either 0 or 1. 


data_new <- data.frame(data, stringsAsFactors = F) 

Credit_Record_infactor <- as.factor(data$Credit_Record)

class(Credit_Record_infactor)

plot(data$Income ~ Credit_Record_infactor,xlab='Credit Record',ylab='Income',
     main='Scatter Plot between Income and Credit Record',col='maroon')

#The Credit_Record is in Factor and hence resulted in a boxplot with values 0 & 1

# 4. 
# Create a scatter plot between Income on x-axis and PropertyValue on y-axis.  
# • In the above plot, add the color argument which should be dependent on the No_kids of the applicant  
# • In the above plot, now add the size argument which should be dependent on the No_kids of the applicant. 
# • Now, in the above plot, please add the smooth line using the geom_smooth() function.

ggplot(data,aes(y=PropertyValue,x=Income))+geom_point()

ggplot(data,aes(y=PropertyValue,x=Income,col=No_kids))+geom_point()

ggplot(data,aes(y=PropertyValue,x=Income,col=No_kids,size=No_kids))+geom_point()

ggplot(data,aes(y=PropertyValue,x=Income,col=No_kids,size=No_kids))+geom_point()+geom_smooth()

ggplot(data,aes(y=PropertyValue,x=Income,col=No_kids,size=No_kids))+geom_point()+geom_smooth(se=F)

# 5. 
# ggplot comparson with Base plot :  
# • Using the base package plot(), make a scatter plot with Income on the x-axis and PropertyValue on the y-axis, 
# colored according to No of kids (use the col argument). 
# • Now, Change No_kids in previous step to a factor 
# • Now, Make the same plot as in the first instruction - 5a 
# • Now, recreate the same plot as above  using the ggplot functon. 

plot(data$PropertyValue~data$Income,col=data$No_kids)

plot(data$PropertyValue~data$Income,col=(as.factor(data$No_kids)))     

plot(data$PropertyValue~data$Income,col=data$No_kids)

ggplot(data,aes(y=PropertyValue,x=Income,col=No_kids))+geom_point()

ggplot(data,aes(y=PropertyValue,x=Income,col=as.factor(No_kids)))+geom_point()

# 6. 
# Aesthetics:  
# • Map Income to x and Property Value to y 
# • Reverse: Map Property Value to x and Income to y 
# • Map Income to x and Property Value to y and No of kids to col 
# • Change shape and size of the points in the above plot. 

ggplot(data,aes(y=PropertyValue,x=Income))+geom_point()

ggplot(data,aes(x=PropertyValue,y=Income))+geom_point()

ggplot(data,aes(y=PropertyValue,x=Income,col=No_kids))+geom_point()

ggplot(data,aes(y=PropertyValue,x=Income,col=No_kids,size=No_kids))+geom_point(shape='*')

# 7. 
# Geometry:  
# • Start with creating a scatter plot mapping Income to x and Property Value to y. 
# • Make a plot With geom_jitter() function 
# • Now, in the above plot, Set width in geom_jitter()
# . Take the width value as 0.1

ggplot(data,aes(y=PropertyValue,x=Income))+geom_point()

ggplot(data,aes(y=PropertyValue,x=Income))+geom_jitter()

ggplot(data,aes(y=PropertyValue,x=Income))+geom_jitter(width = 0.1)


# 8. 
# Histogram:  
# • Make a univariate histogram on Income 
# • In the above plot, add set binwidth to 100 in the geom layer 
# • In the above plot,  MAP ..density.. to the y aesthetic (i.e. in a second aes() function) 
# • Finally, in the above plot, plus SET the fill attribute to "#377EB8". 

ggplot(data,aes(x=Income))+geom_histogram()

ggplot(data,aes(x=Income))+geom_histogram(binwidth = 100)


ggplot(data,aes(x=Income))+geom_histogram(binwidth = 100,fill="#377EB8")

# 
# 9. 
# Bar Plot:  
# • Draw a bar plot of Property_Purchased, filled according to Education 
# • In the above plot, Change the position argument to "stack" 
# • In the above plot, Change the position argument to "fill" 
# • In the above plot, Change the position argument to "dodge"

ggplot(data,aes(x=Property_Purchased,fill=Education))+geom_bar()

ggplot(data,aes(x=Property_Purchased,fill=Education))+geom_bar(position='stack')

ggplot(data,aes(x=Property_Purchased,fill=Education))+geom_bar(position='fill')

ggplot(data,aes(x=Property_Purchased,fill=Education))+geom_bar(position='dodge')


# 10. 
# Overlapping bar plots:  
# • Take the last plot form the previous exercise 
# • In the above plot, Define posn_d with position_dodge(). Take value as 0.7 
# • Change the position argument to posn_d in the last plot made in Step 9(d) 
# • Use posn_d as position and adjust alpha to 0.6 - can you see the overlap in bars. 
# If not, change the value of alpha 
ggplot(data,aes(x=Property_Purchased,fill=Education))+geom_bar(position='dodge')

ggplot(data,aes(x=Property_Purchased,fill=Education))+geom_bar(position=position_dodge(width=0.7))

ggplot(data,aes(x=Property_Purchased,fill=Education))+geom_bar(position = position_dodge())

ggplot(data,aes(x=Property_Purchased,fill=Education))+geom_bar(position = position_dodge(0.7),alpha=.75)

# 11. 
# Overlapping histograms:  
# • A basic histogram, add coloring defined by Income and filled by HasCar, select a suitable binwidth 
# • In the above plot, In the above chart, Change position to identity

ggplot(data,aes(x=Income,fill=HasCar,col=Income))+geom_histogram(binwidth = 100)

ggplot(data,aes(x=Income,fill=HasCar,col=Income))+geom_histogram(binwidth = 100,position = 'identity')

# 12. 
# Faceting:  
# • Now create a basic scatter plot between income and property value variables  
# • In the above plot, Separate rows according to HasCar 
# • In plot made in step 12b, Separate columns according to No of kids 
# • In plot made in step 12b, , Separate by both HasCar and No of kids 

ggplot(data,aes(x=Income,y=PropertyValue))+geom_point()

ggplot(data,aes(x=Income,y=PropertyValue))+geom_point()+facet_grid(.~HasCar)

ggplot(data,aes(x=Income,y=PropertyValue))+geom_point()+facet_grid(.~HasCar)+facet_grid(.~No_kids)

ggplot(data,aes(x=Income,y=PropertyValue))+geom_point()+facet_grid(HasCar~No_kids)

