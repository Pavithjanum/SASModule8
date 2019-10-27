
#1
# Load the required libraries and the data and call the dataframe ‘tweets’

library(tm)
library(qdap)

getwd()

setwd(choose.dir())

tweets <- read.csv('tweets.CSV',stringsAsFactors = FALSE)

#2
# Understand the data structure and provide concise summary on the following – 
#• no of observations 
#• total number of variables 
#• structure of the variables

str(tweets)

View(tweets)

summary(tweets)

head(tweets)

tail(tweets)

#3
#Setting up before text processing. Run the following lines of codes  
#r1 = as.character(tweets$Tweet) 
#set.seed(100) 
#sample = sample(r1, (length(r1))) 

r1=as.character(tweets$Tweet)

str(r1)
set.seed(100)

sample = sample(r1,length(r1))

str(sample)

#4
# Data Preprocessing using Bag of Words Technique 
#• Create a Corpus - which, in simple terms, is nothing but a collection of text documents. 
#• Now, remove punctuations 
#• Next, change the case of the word to lowercase so that same words are not counted as different because of lower or upper case. 
#• Next, remove numbers 
#• Next, remove whitespaces 
#• Now, remove unhelpful terms, also referred as stopwords 
#• Now, please carry out the process of stemming, motivated by the desire to represent words with different endings as the same word. 
#• create a document term matrix from the corpus 
#• now create the data frame from the output of the above line 


tweets_for_mining <- VectorSource(tweets$Tweet)

tweets_for_mining

tweets_for_mining[1]

str(tweets_for_mining)

class(tweets_for_mining)

tweets_corpus <- VCorpus(tweets_for_mining)

tweets_corpus[[1]][1]


tweets_without_punctuations <- tm_map(tweets_corpus,removePunctuation)

tweets_without_punctuations[[1]][1]

tweets_inlower_Case <- tm_map(tweets_without_punctuations,content_transformer(tolower))

tweets_inlower_Case[[1]][1]

tweets_without_numbers <- tm_map(tweets_inlower_Case,removeNumbers)

tweets_without_spaces <- tm_map(tweets_without_numbers,stripWhitespace)

tweets_without_spaces[[9]]

tweets_without_stopword <- paste(c(tweets_without_spaces))

#rm(stopwords_regex)
stopwords_regex = paste(stopwords('en'), collapse = '\\b|\\b')

stopwords_regex = paste0('\\b', stopwords_regex, '\\b')

library(stringr)

tweets_without_stopword <- str_replace_all(tweets_without_stopword,stopwords_regex,'')

tweets_without_stopword[1]

tweets_wt_stopword <- tm_map(tweets_without_spaces,removeWords,stopwords('en'))

tweets_wt_stopword[[1]]

a <- c('apple','applee','appl')

stem_doc <- stemDocument(r1)

comp_dict <- 'apple'

V1 <- DocumentTermMatrix(tweets_wt_stopword)

V2 <- as.matrix(V1)
dim(V2)


V3 <- as.data.frame(V2)
str(V3)

V4<-t(V3)

tweets_freq <- colSums(V2)

head(tweets_freq)


#5
#Now, create three different wordclouds using the following arguments  
#  • Create a word cloud and set random.order = TRUE: 
#  • Create a word cloud and set random.order = FALSE: 
#  • In the above word cloud, adjust the frequency level with min.freq parameter set at 5  

library(wordcloud2)

library(wordcloud)
tweets_word_freqs <- data.frame(
  term = names(tweets_freq),
  num = tweets_freq
)

head(tweets_word_freqs)

wordcloud(tweets_word_freqs$term,tweets_word_freqs$num,shape = 'star',size = 0.7)


df <- data.frame(term=c(1,4,8,9,2),num=c(9,0,4,6,8))

install.packages('wordcloud')

library(wordcloud)
wordcloud(df$term,
          df$num,
          max.words = 100, 
          colors = c("grey80","darkgoldenrod1", "tomato",size=1.9)
)


V5 <- as.data.frame(V4)

wordcloud2(tweets_word_freqs)


install.packages("RColorBrewer")
