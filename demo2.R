#arithmetic operator
a<-10
b<-3
print(a+b)
a<-c(1,0.1)
b<-c(2,4)
print(a+b)
print(a-b)
print(a^b)
print(a%%b)
cat("addition of a and b:", a+b)
#logical operator
a<-0
b<-1
c<-(a>1) &(b<1)
print(c)
c<-(a<1)|(b=0)  
print(c)
a=TRUE
b=FALSE
c<-(!a)
print(c)
#relational operators
a<-"apple"
b<-"cat"
print(a<b)
print(a>b)
