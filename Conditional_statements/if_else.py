''' If...else statement is a control statement that helps in decision-making based on specific condition.
When the if condition is False. If the condition in the if statement is not true, the else block will be executed.'''


# Example :
i = 20
if i >0 :
    print("I is positive")
else :
    print("I is negative")
    
# If_ else in oneline:
# If we need to execute a single shorthand statment inside the 'if' or 'else'block
# then one-line shorthand can be used.


a = -2

res = "positive" if a >= 0 else "negative"
print(res)


# Logical operates with If...else

''' We can combine multiple conditions using logical operators such as and , or and not.'''

age = 25
exp = 10

# using '>' operator & 'and' with if-else
if age > 23 and exp > 8 :
    print("Eligible.")
else:
    print("Not eligible.")
    
    
    
    
# nested if_else conditional statement ;
''' Nested if..else statement occurs when if...else structure is placed inside another if or else
block, Nested if..else allows the execution of specific code blocks based on series of conditional checks.'''



i = 10
if i == 10:



# First if statement
  if i < 15:
      print("i is smaller than 15")
      
  
  # Nested -if statement
  # will only be executed if statement above it is true
  if i < 12 :
    print("i is smaller than 12 too")
  else :
    print("i is greater than 15")
    

else :
    print("i is not eual to 10")
    
    
    
    
# ex2 of nested if... else  conditional statement


age = 70

is_member = True


if age >= 60:
    if is_member:
      print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
    
    
    
    
    
# shorthand if_else statemnt:
''' The shorthand if_else statement allows us to write a single -line-if-else statement.'''

marks = 45
res = "pass" if marks >= 40 else "fail"
print(f"Result:{res}")








# ternary conditional statement:
# A ternary operator is compact way to write an if..else code in a single line. it's sometimes called a "conditional expression"



age = 20
s = 'Adult' if age >=18 else "Minor"
print(s)