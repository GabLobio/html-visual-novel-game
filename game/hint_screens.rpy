




###########################################################################################################################


screen head_hint():
    image "images/empty_board.png"

    imagebutton:
        xpos 1700
        ypos 30
        idle "images/interactive_button/back_button.png"
        hover "images/interactive_button/hover_back_button.png"
        action Return()

    viewport:
            xpos 145
            ypos 141
            xysize (1183,802)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Task:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    hbox:
                        text 'Mrs. Rodriguez`s favorite lessons are Lesson 5 "Attribute," and Lesson 8 "Style Attribute".' size 24 color "#dfdfdf" xoffset 6 yoffset 6