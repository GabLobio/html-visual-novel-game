image html_peter = Movie(play="images/html_peter.webm")
#image main_menu = Movie(play="html_peter.webm")

screen final_browser():
    image "images/final_browser_screen.png"
    

    hbox:
        xpos 105
        ypos 160    
        text "{b}HTML Lesson{/b}" size 24 color "#3A3A3A"

    viewport:
            xpos 105
            ypos 210
            xysize (1710,790)   
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"



            hbox:
                    
                vbox:

                    #textbutton "Scroll Down" action Function(scroll_viewport, 50)  # Adjust the scrolling amount as needed
                    #textbutton "Scroll Up" action Function(scroll_viewport, -50)  # Adjust the scrolling amount as needed

                    hbox:
                        ############### INPUTS ###############
                        text "{b}HTML{/b}" size 42 color "#3A3A3A"
                    
                    hbox:
                        text "\n " size 20 color "#3A3A3A"

                    hbox:
                        image "images/mrs_rodriguez.png" xysize (111,188)

                
                    hbox:
                        text "\nTeacher Rodriguez" size 20 color "#3A3A3A"
                    
                    hbox:
                        text "\nMy two favorite lesson:" size 20 color "#3A3A3A"
                    
                    hbox:
                        text "\n    • {u}Lesson 5{/u}" size 20 color "#551AA9"
                    hbox:
                        text "    • {u}Lesson 8{/u}" size 20 color "#551AA9"

                    hbox:
                        text "\n{b}Lesson 5: Attribute{/b}" size 28 color "#3A3A3A"
                    
                    hbox:
                        text "\nAttribute concept adds depth to their comprehension of HTML, contributing to a well-rounded understanding of web development." size 20 color "#0000FF"

                    hbox:
                        text "\n{b}Lesson 8: Style Attribute{/b}" size 28 color "#3A3A3A"
                    
                    hbox:
                        text "\nStyle Attribute because they offer practical insights into manipulating webpage aesthetics, allowing students to create visually appealing designs." size 20 color "#FF0000"

                    hbox:
                        text "\nThese are my favorite element tag" size 20 color "#3A3A3A"
                        frame:
                            background Solid("#bdbdbdff")  
                            xoffset 6 
                            yoffset 25
                            padding (1, 1)
                            image "images/dropdown.png" xysize (90,55)
                    
                    hbox:
                        text "\n" size 20 color "#3A3A3A"
                        add "html_peter"