
---
    Jackbord Fire Control System (Deprecated)
---

prog_vars =
    d/fireinterval 200
    d/gunspeedhigh 25
    d/gunspeedlow 30
    d/ammo 16
prog_vars.

prog_start =
    pclear
    print "Program Start"
    pwm c2 /gunspeedhigh
    dly 10000
prog_start.

prog_loop =
    svp c1 90
    dly /fireinterval
    svp c1 0
    dly /fireinterval
    print "Ammo: /ammo"
    dec /ammo
    any /ammo < 0 -> exitprog
prog_loop.
	    
prog_stop =
    svp c1 0
    dly 1000
    c2 0
    print "Program End"
prog_stop.
