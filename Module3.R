#1. 
#Load the required packages 

library(R6)

#2.
# Create a new class template/object generator with the name “Football_Generator”, 
# it should comprise of these components: • Three private data members:”Player_Name”, “Player_Club” & 
# “Player_Salary” • Three public functions: “set_name()”, “set_club()” and “set_salary()” 

Football_Generator <- R6Class('Football_Generator',private = list(Player_Name=NA,Player_Club=NA,Player_Salary=NA),
                              public = list(set_name = function(x) {private$Player_Name=x},
                                            set_club = function(y) {private$Player_Club=y},
                                            set_salary = function(z) {private$Player_Salary=z} 
                                            ))

# 3. 
# For the above class template create two new objects and assign values to the private data members 
# with the public functions

player1 <- Football_Generator$new()
player1
player1$set_name('Henry')
player1$set_club('California')
player1$set_salary(55000)
player1

player2 <- Football_Generator$new()
player2
player2$set_name('Michalle')
player2$set_club('London')
player2$set_salary(78000)
player2
 

# 4. 
# Create a new class generator with the name “Movie_Generator”, it should comprise of these components: 
#   • Three private data members: “Movie_Name”, “Protagonist_Name”, “Movie_Budget”

Movie_Generator <- R6Class('Movie_Generator',private = list(Movie_Name=NA,Protagonist_Name=NA,Movie_Budget=NA))
Movie_Generator

# 5. 
# For the above class template, assign values to the private data members using initialize method.

Movie_Generator <- R6Class('Movie_Generator',private = list(Movie_Name=NA,Protagonist_Name=NA,Movie_Budget=NA),
                           public = list(initialize = function(x,y,z)
                            {private$Movie_Name=x
                             private$Protagonist_Name=y
                             private$Movie_Budget=z})
                           
                           )


Movie1 <- Movie_Generator$new('Titan','Smith','900000')
Movie1


# 6. 
# Create a new class generator with the name “Vegetable_Generator”, it should comprise of these components: 
#   • Two private data members: “Vegetable_Name”, “Vegetable_Cost”


Vegetable_Generator <- R6Class('Vegetable_Generator',private = list(Vegetable_Name=NA,Vegetable_Cost=NA))

#7
# For the above class template, create two new objects and assign values to the private data members by 
# using Active Bindings

Vegetable_Generator <- R6Class('Vegetable_Generator',private = list(..Vegetable_Name=NA,..Vegetable_Cost=NA),
                               
                               active = list(Vegetable_Name = function(x) {private$..Vegetable_Name = x},
                                             Vegetable_Cost = function(y) {private$..Vegetable_Cost = y}
                               ))

Veg1 <- Vegetable_Generator$new()
Veg1$Vegetable_Name <- 'Tomato'
Veg1$Vegetable_Cost <- 78

Veg1
