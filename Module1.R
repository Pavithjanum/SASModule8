# 1. Create a vector "Random" which comprises of ten observations, whose:
# . First three observations are normally distributed random numbers with mean '5' and standard deviation '1'
# . Next three observations are normally distributed random numbers with mean '3' and standard deviation '3'
# . Last four observations are normally distributed random numbers with mean '1' and standard deviation '4'
set.seed(12)
a <- rnorm(n=3,mean=5,sd=1) 

set.seed(10)
b <- rnorm(n=3,mean=3,sd=3)  

set.seed(09)
c <- rnorm(n=4,mean=1,sd=4)  

Random <- c(a,b,c)

# 2. Create a vector "LogExpo" which comprises of ten observations, where:
# . First five observations are log values of the first five natural numbers
# . Next five observations are exponentiation values of next five natural numbers

l <- log(c(1:5))

e <- exp(c(6:10))

LogExpo <- c(l,e)

# 3. Add two vectors "Thousand" and "Negative_thousand", where:
# . Vector "Negative_thousand" is a sequence of integers from '-1000' to '0'
# . Vector "Thousand" is a sequence of integers from '0' to '1000'

Thousand <- c(0:1000)

Negative_thousand <- c(-1000:0)

Thousand + Negative_thousand

# 4. Store the above result in a new vector and name it as "Final_Thousand". From this data-set:
# . Select the 500th observation
# . Extract the first hundred observations and store them in a new vector "First_Hundred"
# . Extract the last hundred observations and store them in a new vector
# "Last_Hundred"
# . Extract all the elements from 321st observation to 764th observation and store
# them in a new vector "Weird_Set"

Final_Thousand <- Thousand + Negative_thousand

Final_Thousand[500]

First_Hundred <- Final_Thousand[1:100] 

#or 

First_Hundred <- head(Final_Thousand,100)

Last_Hundred <- tail(Final_Thousand,100)

Weird_Set <- Final_Thousand[321:764]

# 5.Create a list "Book_Details" which comprises of:
# . 'Book_Name'- A character vector of five observations listing the names of books
# . 'Author_Name'- A character vector of five observations listing the names of
# authors
# . 'Book_Cost'- A numeric vector of five observations listing the cost of books

Book_Name <- c('Akbar-Nama','Wealth of Nations','Mein Kampf','Plague','Count of Monte Cristo')

Author_Name <- c('Abul Fazal','Adam Smith','Adolf Hitler','Albert Camus','Alexander Dumas')

Book_Cost <- c(800, 950, 680, 900, 700)

Book_Details <- list(Book_Name,Author_Name,Book_Cost)

names(Book_Details) <- c('Book_Name','Author_Name','Book_Cost')

class(Book_Details)

# 6. From the above list:
# . Extract all the three individual vectors by their name
# . Extract the name of fourth book
# . Extract the name of second author
# . Extract the cost of last book

Book_Details['Book_Name']

#OR

Book_Details$Book_Name

Book_Details['Author_Name']

#OR

Book_Details$Author_Name

Book_Details['Book_Cost']

#OR

Book_Details$Book_Cost

Book_Details$Book_Name[4]

#or

Book_Details[[1]][4]

Book_Details$Author_Name[2]

Book_Details[[3]] [5]

# 7. Load the inbuilt data-set "women" by using the "data()" command
#   . Extract the observation which is present at 6th row, 2nd column
# . Extract the last four rows of the data-set
# . Extract alternate rows from the data-set

#View(women)

data(women)

Women_data <- women

class(Women_data)

Women_data[6,2]

tail(women,4)

odd_number <- seq(1,nrow(women),2)


Women_data[odd_number,]

# 8. Create a "Student" dataset with a minimum of ten rows, which comprises of:
# . 'Name'- Name of the student
# . 'Department'-Department of the student
# . 'CGPA'- CGPA of the student
# . 'Placement'- Is the student placed or not(Boolean values)

Name <- c('Pavi','Jan','Anna','Sandy','Mani','Ulag')

Department <- c('ECE','M.Phil','ECE','EEE','MTECH','ME','PHD','CS','PJ','LO')

CGPA <- c(9.0,9.4,9.5,8.9,8.0,8.9,9.0,9.2,9.3,9.8)

Placement <- c('Y','Y','N','Y','Y','N','N','Y','N','Y')

Student = data.frame(Name,Department,CGPA,Placement)

label <- c('Name','Department','CGPA','Placement')

Student = data.frame(Name,Department,CGPA,Placement)

#ls()
