
---
    Octagon program to count from 0
    counting on most languages starts at 0
---

prog_vars =  
-- This section is where you define variables.
    d/count 0   
-- We have made a variable called count and given it a value of 0
prog_vars.  
-- this ends the variable section

prog_start = 
-- this code runs once when you start the program
    pclear 
-- this clears the print screen
    print "Program Start" 
-- this prints "program start"
prog_start.
-- this ends the start section

prog_loop = 
--This is the main loop of the program it is where you main code goes as it gets run over and over agin
    print "Count /count"
-- this prints Count and then the value of the variable count
    dly 1000
-- this makes the program wait for 1 second
    inc /count
-- this increases the value of count by 1
prog_loop.
-- this ends the loop section

prog_stop = 
-- this code runs when you press stop on the program or if you use prog_stop in you loop somewhere
    print "bye"
-- this prints bye to the print screen
prog_stop.
-- this ends the print section





