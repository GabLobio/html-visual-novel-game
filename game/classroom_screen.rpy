




screen lesson_ui():
    image "images/bg_lesson_choices.png" 
    

    imagebutton:
        xpos 436
        ypos 200
        idle "images/interactive_button/btn_lesson_1.png"
        hover "images/interactive_button/hover_lesson_1.png"
        action Jump("lesson_one")


    imagebutton:
        xpos 436
        ypos 330
        idle "images/interactive_button/btn_lesson_2.png"
        hover "images/interactive_button/hover_lesson_2.png"
        action Jump("lesson_two")


    imagebutton:
        xpos 436
        ypos 460
        idle "images/interactive_button/btn_lesson_3.png"
        hover "images/interactive_button/hover_lesson_3.png"
        action Jump("lesson_three")


    imagebutton:
        xpos 436
        ypos 590
        idle "images/interactive_button/btn_lesson_4.png"
        hover "images/interactive_button/hover_lesson_4.png"
        action Jump("lesson_four")


    imagebutton:
        xpos 436
        ypos 720
        idle "images/interactive_button/btn_lesson_5.png"
        hover "images/interactive_button/hover_lesson_5.png"
        action Jump("lesson_five")


    imagebutton:
        xpos 986
        ypos 200
        idle "images/interactive_button/btn_lesson_6.png"
        hover "images/interactive_button/hover_lesson_6.png"
        action Jump("lesson_six")


    imagebutton:
        xpos 986
        ypos 330
        idle "images/interactive_button/btn_lesson_7.png"
        hover "images/interactive_button/hover_lesson_7.png"
        action Jump("lesson_seven")   
    
    
    imagebutton:
        xpos 986
        ypos 460
        idle "images/interactive_button/btn_lesson_8.png"
        hover "images/interactive_button/hover_lesson_8.png"
        action Jump("lesson_eight")


    imagebutton:
        xpos 986
        ypos 590
        idle "images/interactive_button/btn_lesson_9.png"
        hover "images/interactive_button/hover_lesson_9.png"
        action Jump("lesson_nine")


    imagebutton:
        xpos 986
        ypos 720
        idle "images/interactive_button/btn_lesson_10.png"
        hover "images/interactive_button/hover_lesson_10.png"
        action Jump("lesson_ten")         





###########################################################################################################################


screen error_msg_final_test():
    image "images/final_browser_screen.png"
    vbox:
        text "Error" size 24 color "#c00000" xpos 105 ypos 210 xoffset 6 yoffset 6
        text "Please, check every line for any errors or mispelled" size 24 color "#c00000" xpos 105 ypos 210 xoffset 6 yoffset 6

    imagebutton:
        xpos 1770
        ypos 30
        idle "images/interactive_button/reset_button.png"
        hover "images/interactive_button/reset_button_hover.png"
        action Return()


screen scrollable_screen():
    image "images/final_screen.png" 

    default input_one_value = "?"
    default input_two_value = "?"
    default input_three_value = "?"

    default active_input = 0

    imagebutton:
        xpos 50
        ypos 30
        idle "images/interactive_button/exit_button.png"
        hover "images/interactive_button/exit_button_hover.png"
        action Jump("start")

    imagebutton:
        xpos 1770
        ypos 30
        #text_color "#ff9900"  # Set the text color here\
        #text_hover_color "#ffffff"
        #text_selected_color "#ff9900"
        #text_size 46
        idle "images/interactive_button/run_button.png"
        hover "images/interactive_button/run_button_hover.png"
        if input_one_value == "" and input_two_value == "" and input_three_value == "":
            action ShowMenu("error_msg_final_test")
        elif input_one_value == "style" and input_two_value == "black" and input_three_value == "color":
            action Jump("start")
        else:
            action ShowMenu("error_msg_final_test")
 
    viewport:
            xpos 105
            ypos 210
            xysize (1710,790)
            mousewheel True
            arrowkeys True 
            scrollbars "vertical"
            


            

            
           

            hbox:
                    
                vbox:
                    ############### INPUTS ###############
                    text "{b}Complete the code{/b}\n\n" 

                    hbox:
                        textbutton "  1": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 1)
                        text "<html>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  2": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 2)
                        text "<head>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  3": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 3)
                        text "      <title></title>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  4": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 4)
                        text "</head>" size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "  5": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 5)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  6": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 6)
                        text "<body>" size 24 color "#cecece" xoffset 6 yoffset 6




                    hbox:
                        textbutton "  7": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 7)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "  8": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 8)
                        text "      <div>" size 24 color "#cecece" xoffset 6 yoffset 6


                    hbox:
                        textbutton "  9": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 9)
                        text "          <h1>HTML</h1>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "10": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 10)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "11": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 11)
                        text '          <img src="images/mrs_rodriguez_button.png" alt="Adventure Image">' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "12": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 12)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "13": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 13)
                        text '          <p>This is my teacher Rodriguez</p>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "14": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 14)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "15": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 15)
                        text '          <p>My favorite lesson:</p>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "16": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 16)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "17": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 17)
                        text "          <ul>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "18": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 18)
                        text '              <li><a href="#section1">Lesson 1</a></li>' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "19": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 19)
                        text '              <li><a href="#section2">Lesson 5</a></li>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "20": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 20)
                        text "          </ul>" size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "21": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 21)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "22": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 22)
                        text '          <div id="section1">' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "23": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 23)
                        text '              <h2>Lesson Number: Lesson Name</h2>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "24": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 24)
                        text '              <p style="color:blue">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Magnam, illum?</p>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "25": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 25)
                        text '          </div' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "26": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 26)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "27": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 27)
                        text '          <div id="section2">' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "28": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 28)
                        text '              <h2>Lesson Number: Lesson Name</h2>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "29": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 29)
                        text '              <p style="color:red">Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae architecto et reprehenderit!</p>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "30": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 30)
                        text '          </div' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    
                    hbox:
                        textbutton "31": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 31)
                        text "      </div>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "32": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 32)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6



                    hbox:
                        textbutton "33": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 33)
                        text "      <div>" size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "34": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 34)
                        text '          <label for="select-adventure">These are my favorite tag</label>' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "35": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 35)
                        text '          <select id="select-adventure" name="select-adventure">' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "36": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 36)
                        text '              <option value="forest">"The img tag"</option>' size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "37": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 37)
                        text '              <option value="ocean">The </option>' size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "38": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 38)
                        text '          </select>' size 24 color "#cecece" xoffset 6 yoffset 6




                    hbox:
                        textbutton "39": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 39)
                        text "      </div>" size 24 color "#cecece" xoffset 6 yoffset 6
                    
                    hbox:
                        textbutton "40": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 40)
                        text "       " size 24 color "#cecece" xoffset 6 yoffset 6


                    
                    
                    hbox:
                        textbutton "41": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 41)
                        text "</body>" size 24 color "#cecece" xoffset 6 yoffset 6

                    hbox:
                        textbutton "42": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 42)
                        textbutton "  1": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 1)
                        text "</html>" size 24 color "#cecece" xoffset 6 yoffset 6

                    















                    hbox:
                        textbutton "10": 
                            style_prefix "my"   
                            action SetScreenVariable("active_input", 1)

                        text "<button " size 24 color "#ffffff" xoffset 6 yoffset 6

                        if active_input == 1:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 5
                                value ScreenVariableInputValue("input_one_value")
                                    
                        else:
                            textbutton '[input_one_value]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 1)

                        text '="background-color:' size 24 color "#ffffff" xoffset 6 yoffset 6

                        if active_input == 2:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 5
                                value ScreenVariableInputValue("input_two_value")
                                    
                        else:
                            textbutton '[input_two_value]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 2)
                        
                        text '; ' size 24 color "#ffffff" xoffset 6 yoffset 6
                        
                        if active_input == 3:
                            input:
                                xoffset 6
                                yoffset 6
                                size 24
                                length 5
                                value ScreenVariableInputValue("input_three_value")
                                    
                        else:
                            textbutton '[input_three_value]':
                                style_prefix "my"
                                action SetScreenVariable("active_input", 3)
                        
                        text ':white"> OK </button>' size 24 color "#ffffff" xoffset 6 yoffset 6