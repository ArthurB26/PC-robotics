
---
    Jackbord Electronics Control System (Main)
---
prog_vars =
    d/fireinterval 200
    d/gunspeedhigh 25
    d/gunspeedlow 30
    d/ammo 16
    
    d/motorstate 0
prog_vars.

prog_start =
    pclear
    print "ECS on standby"
    
    aoff
    boff
    coff
    
    btp c5 togglemotors
    btp d1 forward
    btp d2 left
    btp d3 right
    btp d4 reverse
    btp d5 fire
prog_start.

prog_loop =

    dly 10

prog_loop.

togglemotors =
    print "Motors toggle"
    tg a1
    tg b1
togglemotors.

forward =
    print "Forward start"
    a2 1
    b2 1
    dly 2000
    print "Forward stop"
    a2 0
    b2 0
forward.

left =
    print "Left start"
    a3 1
    b2 1
    dly 2000
    print "Left stop"
    a3 0
    b2 0
left.

right =
    print "Right start"
    a2 1
    b3 1
    dly 2000
    print "Right stop"
    a2 0
    b3 0
right.

reverse =
    print "Reverse start"
    a3 1
    b3 1
    dly 2000
    print "Reverse stop"
    a3 0
    b3 0
reverse.

fire =
    print "Fire start"
    /ammo 16
    pwm c2 /gunspeedlow
    dly 10000
    
    repeat /ammo ->
        svp c1 90
        dly /fireinterval
        svp c1 0
        dly /fireinterval
        print "Ammo: /ammo"
        dec /ammo
    repeat.
    
    print "Ammo: 0"
    svp c1 0
    c2 0
fire.

prog_stop =
    rstb
    aoff
    boff
    coff
    doff
    print "ECS off"
prog_stop.
