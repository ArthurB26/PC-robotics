
---
    Jackbord Motor Control System (Deprecated)
---

prog_start =
    pclear
    print "Program Start"

    --  Enable Motors
    a1 1
    b1 1
    print "Motors Enabled"
    dly 500
    
    --  Drive Forward
    aoff
    boff
    a1 1
    b1 1
    dly 500
    
    a2 1
    b2 1
    print "Driving Forward"
    dly 2000
    
    --  Drive Backward
    aoff
    boff
    a1 1
    b1 1
    dly 500
    
    a3 1
    b3 1
    print "Driving Backward"
    dly 2000
    
    --  Turn Left
    aoff
    boff
    a1 1
    b1 1
    dly 500
    
    a3 1
    b2 1
    print "Turning Left"
    dly 2000
    
    --  Turn Right
    aoff
    boff
    a1 1
    b1 1
    dly 500
    
    a2 1
    b3 1
    print "Turning Right"
    dly 2000
    
prog_start.
	    
prog_stop =
    aoff
    boff
    print "Motors Disabled"
    print "Program End"
prog_stop.
