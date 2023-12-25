label lesson_four:

    #jump lessonFourFillTwentyThree
    if lesson_three_finish:
        jump lessonFourFillOne
    else:
        "Please finish lesson 3"
        call screen lesson_ui  

    
    label lessonFourFillOne:
        scene lesson_text_intro
        "Ready to start Text Formatting Lesson?"
        jump lessonFourFillTwo


    label lessonFourFillTwo:
        $ ans_ff_o1_was_dropped = False
        scene l4f2
        "HTML {b}formatting tags{/b} are used to change how text is displayed."
        call screen lesson_four_ls2_fill

        label call_fr2:
            $ ans_ff_o1_was_dropped = False
            call screen lesson_four_ls2_fill
        
        label if_lf2_wrong:
            scene l4f2
            "Try again"
            call screen lesson_four_ls2_fill


    label lessonFourFillThree:
        $ ans_ff_th01_was_dropped = False
        $ ans_ff_th02_was_dropped = False
        scene l4f3
        "Formatting tags are container tags. This means that both opening and closing tags are required."
        call screen lesson_four_ls3_fill

        label call_fr3:
            $ ans_ff_th01_was_dropped = False
            $ ans_ff_th02_was_dropped = False
            call screen lesson_four_ls3_fill
        
        label if_lf3_wrong:
            scene l4f3
            "Try again"
            call screen lesson_four_ls3_fill


    label lessonFourFillFour:
        $ ans_ff_fr01_was_dropped = False
        $ ans_ff_fr02_was_dropped = False
        scene l4f4
        "The {b}italic tags <i>{/b} is used to display text in italics."
        call screen lesson_four_ls4_fill

        label call_fr4:
            $ ans_ff_fr01_was_dropped = False
            $ ans_ff_fr02_was_dropped = False
            call screen lesson_four_ls4_fill
        
        label if_lf4_wrong:
            scene l4f4
            "Try again"
            call screen lesson_four_ls4_fill


    label lessonFourFillFive:
        $ ans_ff_fv01_was_dropped = False
        $ ans_ff_fv02_was_dropped = False
        scene l4f5
        "The {b}underline tags <u>{/b} is used to underline text"
        call screen lesson_four_ls5_fill

        label call_fr5:
            $ ans_ff_fv01_was_dropped = False
            $ ans_ff_fv02_was_dropped = False
            call screen lesson_four_ls5_fill
        
        label if_lf5_wrong:
            scene l4f5
            "Try again"
            call screen lesson_four_ls5_fill


    label lessonFourFillSix:
        $ ans_ff_sx01_was_dropped = False
        $ ans_ff_sx02_was_dropped = False
        scene l4f6
        "Formatting tags are applied to text and are {b}nested{/b} inside {b}elements{/b}."
        call screen lesson_four_ls6_fill

        label call_fr6:
            $ ans_ff_sx01_was_dropped = False
            $ ans_ff_sx02_was_dropped = False
            call screen lesson_four_ls6_fill
        
        label if_lf6_wrong:
            scene l4f6
            "Try again"
            call screen lesson_four_ls6_fill


    label lessonFourFillSeven:
        scene l4f7
        "The code above shows how the formatting tags are nested inside the paragraph element."
        "Run the code to see what the web browser will display"
        call screen lesson_four_ls7_fill

        label when_run_four_seven:
            scene lesson_4_7_run
            "Well done!"
            jump lessonFourFillEight


    label lessonFourFillEight:
        scene lesson_intro_9
        "You are getting better at this. Let's go to the next one"
        jump lessonFourFillNine

    
    label lessonFourFillNine:
        $ ans_ff_nn01_was_dropped = False
        $ ans_ff_nn02_was_dropped = False
        scene l4f9
        "There are some HTML formatting tags that you can use to make your web pages more accessible."
        call screen lesson_four_ls9_fill

        label call_fr9:
            $ ans_ff_nn01_was_dropped = False
            $ ans_ff_nn02_was_dropped = False
            call screen lesson_four_ls9_fill
        
        label if_lf9_wrong:
            scene l4f9
            "Try again"
            call screen lesson_four_ls9_fill


    label lessonFourFillTen:
        scene l4f10
        "{b}Strong{/b} text is displayed in bold, just like when you use the {b}<b>{/b} tag." 
        "Run the code to see what the web browser will display"
        call screen lesson_four_ls10_fill

        label when_run_four_ten:
            scene lesson_4_10_run
            "The difference is that the {b}<strong>{/b} tag also has meaning and is used by screen readers."
            jump lessonFourFillEleven
        

    label lessonFourFillEleven:
        $ ans_ff_el01_was_dropped = False
        $ ans_ff_el02_was_dropped = False
        scene l4f11
        "The {b}emphasis tag <em>{/b} is used to define emphasized text."
        call screen lesson_four_ls11_fill

        label call_fr11:
            $ ans_ff_el01_was_dropped = False
            $ ans_ff_el02_was_dropped = False
            call screen lesson_four_ls11_fill
        
        label if_lf11_wrong:
            scene l4f11
            "Try again"
            call screen lesson_four_ls11_fill


    label lessonFourFillTwelve:
        scene l4f12
        "Emphasized text is displayed in Italic, just like when you use the <i> tag. The difference is that the screen reader will verbally stress the words."
        "Run the code to see what the web browser will display"
        call screen lesson_four_ls12_fill

        label when_run_four_twelve:
            scene lesson_4_12_run
            "It almost look the same but still different"
            jump lessonFourFillThirteen
        

        label lessonFourFillThirteen:
        $ ans_ff_tt01_was_dropped = False
        $ ans_ff_tt02_was_dropped = False
        $ ans_ff_tt03_was_dropped = False
        scene l4f13
        "The <strong> and <em> tags are considered {b}semantic formatting tags{/b} because they add meaning to the content."
        "They can serve as an indication of emphasis to a screen reader."
        call screen lesson_four_ls13_fill

        label call_fr13:
            $ ans_ff_tt01_was_dropped = False
            $ ans_ff_tt02_was_dropped = False
            $ ans_ff_tt03_was_dropped = False
            call screen lesson_four_ls13_fill
        
        label if_lf13_wrong:
            scene l4f13
            "Try again"
            call screen lesson_four_ls13_fill


    label lessonFourFillFourteen:
        $ ans_ff_ft01_was_dropped = False
        $ ans_ff_ft02_was_dropped = False
        scene l4f14
        call screen lesson_four_ls14_fill

        label call_fr14:
            $ ans_ff_ft01_was_dropped = False
            $ ans_ff_ft02_was_dropped = False
            call screen lesson_four_ls14_fill
        
        label if_lf14_wrong:
            scene l4f14
            "Try again"
            call screen lesson_four_ls14_fill



    label lessonFourTakewaysText:
        scene lesson_text_takeaways
        "Ready to start HyperText Lesson?"
        jump lessonFourIntroHypertext


    label lessonFourIntroHypertext:
        scene lesson_intro_link
        "In this lesson, you`ll learn to connect web pages with {b}hyperlinks{/b}."
        jump lessonFourFillFifteen    


    label lessonFourFillFifteen:
        scene lesson_8_22 
        "{b}Hypertext{/b} is text that contains a link to another page. "
        "Web pages are called {b}Hypertext{/b} documents because they are connect by?"

        menu:
            'field (column) named "radio"':
                jump if_lf15_wrong
            'field (column) named "pay"':
                jump if_lf15_wrong
            'HyperText links (or hyperlinks)':
                "you are correct"
                jump lessonFourFillSixteen
 
        label if_lf15_wrong:
            "incorrect"
            jump lessonFourFillFifteen   


    label lessonFourFillSixteen:
        $ ans_ff_st01_was_dropped = False
        $ ans_ff_st02_was_dropped = False
        scene l4f16
        "{b}Hyperlinks{/b} allows users to…"
        call screen lesson_four_ls16_fill

        label call_fr16:
            $ ans_ff_st01_was_dropped = False
            $ ans_ff_st02_was_dropped = False
            call screen lesson_four_ls16_fill
        
        label if_lf16_wrong:
            scene l4f16
            "Try again"
            call screen lesson_four_ls16_fill


    label lessonFourFillSeventeen:
        scene lesson_8_22 
        "The {b}anchor tag <a>{/b} is used to create hyperlink on a web page."
        "The {b}<a> tag{/b} is a container tag."
        "What does this mean?"

        menu:
            'It requires both opening and closing tags':
                "you are correct"
                jump lessonFourFillEighteen
            'It requires an opening tag only':
                jump if_lf17_wrong
            'It’s an empty tag':
                jump if_lf17_wrong
            
 
        label if_lf17_wrong:
            "incorrect"
            jump lessonFourFillSeventeen   


    label lessonFourFillEighteen:
        $ ans_ff_egt01_was_dropped = False
        scene l4f18
        "Hyperlinks are used to link from one web page to others. To create a link, you need {b}'href'{/b} to add the destination URL ."
        call screen lesson_four_ls18_fill

        label call_fr18:
            $ ans_ff_egt01_was_dropped = False
            call screen lesson_four_ls18_fill
        
        label if_lf18_wrong:
            scene l4f18
            "Try again"
            call screen lesson_four_ls18_fill


    label lessonFourFillNineteen:
        $ ans_ff_nt01_was_dropped = False
        scene l4f19
        call screen lesson_four_ls19_fill

        label call_fr19:
            $ ans_ff_nt01_was_dropped = False
            call screen lesson_four_ls19_fill
        
        label if_lf19_wrong:
            scene l4f19
            "Try again"
            call screen lesson_four_ls19_fill


    label lessonFourFillTwenty:
        $ ans_ff_tw01_was_dropped = False
        $ ans_ff_tw02_was_dropped = False
        scene l4f20
        call screen lesson_four_ls20_fill

        label call_fr20:
            $ ans_ff_tw01_was_dropped = False
            $ ans_ff_tw02_was_dropped = False
            call screen lesson_four_ls20_fill
        
        label if_lf20_wrong:
            scene l4f20
            "Try again"
            call screen lesson_four_ls20_fill


    label lessonFourFillTwentyOne:
        $ ans_ff_two01_was_dropped = False
        $ ans_ff_two02_was_dropped = False
        scene l4f21
        "The URL needs to be enclosed in quotes to work without errors. If you forget to add {b}href{/b} or the {b}quotes{/b}, the <a> tag won't create a hyperlink ."
        call screen lesson_four_ls21_fill

        label call_fr21:
            $ ans_ff_two01_was_dropped = False
            $ ans_ff_two02_was_dropped = False
            call screen lesson_four_ls21_fill
        
        label if_lf21_wrong:
            scene l4f21
            "Try again"
            call screen lesson_four_ls21_fill
    

    label lessonFourFillTwentyTwo:
        scene lesson_4_22 
        "What’s wrong with this line of code?"

        menu:
            'Matching single quotes are needed to avoid errors':
                jump if_lf22_wrong
            'The quotation marks don’t match':
                jump if_lf22_wrong
            'The href is missing':
                "you are correct"
                jump lessonFourFillTwentyThree
            
            
 
        label if_lf22_wrong:
            "incorrect"
            jump lessonFourFillTwentyTwo 


    label lessonFourFillTwentyThree:
        scene ftg_bg
        "Something is wrong with this code. Can you fix it?"
        "Hint: Try checking each line or number"
        call screen lesson_four_ls23_fill
        

        label if_lf23_correct:
            show lesson_4_23_run
            "You did a great job, well done!"
            "We will be having a lot of this next lesson"
            jump lessonFourFillTwentyFour


    label lessonFourFillTwentyFour:
        scene l4f24
        "You can nest hyperlinks inside other text elements "
        "Run the code to see what the web browser will display"
        call screen lesson_four_ls24_fill

        label when_run_four_TwentyFour:
            scene lesson_4_24_run
            "As you can see it can be used inside <p> tag"
            jump lessonIntrFor25


    label lessonIntrFor25:
        scene lesson_intro_25
        "You can also use hyperlinks to connect pages of the same website."
        jump lessonFourFillTwentyFive

    
    label lessonFourFillTwentyFive:
        $ ans_ff_tf01_was_dropped = False
        $ ans_ff_tf02_was_dropped = False
        $ ans_ff_tf03_was_dropped = False
        scene l4f25
        "HTML stands for {b}HyperText Markup Language{/b}."
        call screen lesson_four_ls25_fill

        label call_fr25:
            $ ans_ff_tf01_was_dropped = False
            $ ans_ff_tf02_was_dropped = False
            $ ans_ff_tf03_was_dropped = False
            call screen lesson_four_ls25_fill
        
        label if_lf25_wrong:
            scene l4f25
            "Try again"
            call screen lesson_four_ls25_fill


    label lessonFourFillTwentySix:
        $ ans_ff_ts01_was_dropped = False
        $ ans_ff_ts02_was_dropped = False
        $ ans_ff_ts03_was_dropped = False
        scene l4f26
        call screen lesson_four_ls26_fill

        label call_fr26:
            $ ans_ff_ts01_was_dropped = False
            $ ans_ff_ts02_was_dropped = False
            $ ans_ff_ts03_was_dropped = False
            call screen lesson_four_ls26_fill
        
        label if_lf26_wrong:
            scene l4f26
            "Try again"
            call screen lesson_four_ls26_fill


    label lessonLinkTakeaways:
        scene lesson_link_takeaways
        "Awesome job, young coders! You've just finished learning how to make your words stand out and create clickable links on the web."
        "Your websites are going to look super cool now! Keep up the great work, and soon you'll be web design experts."
        "Way to go and happy coding, little tech wizards!"
        jump lessonListIntro


    label lessonListIntro:
        scene lesson_intro_list
        "Hello, coding enthusiasts! Today, we're diving into the world of HTML lists. We'll explore how to organize content using ordered lists, unordered lists, and the art of nesting." 
        "Get ready to level up your web development skills as we delve into the adventure of list-making!"
        jump lessonFourTwentySeven

    
    label lessonFourTwentySeven:
        $ ans_ff_twts01_was_dropped = False
        scene l4f27
        "A list consists of {b}list items <li>{/b}."
        call screen lesson_four_ls27_fill

        label call_fr27:
            $ ans_ff_twts01_was_dropped = False
            call screen lesson_four_ls27_fill
        
        label if_lf27_wrong:
            scene l4f27
            "Try again"
            call screen lesson_four_ls27_fill
               

    label lessonFourTwentyEight:
        $ ans_ff_twte01_was_dropped = False
        $ ans_ff_twte02_was_dropped = False
        $ ans_ff_twte03_was_dropped = False
        scene l4f28
        "{b}List items{/b} are container tags."
        call screen lesson_four_ls28_fill

        label call_fr28:
            $ ans_ff_twte01_was_dropped = False
            $ ans_ff_twte02_was_dropped = False
            $ ans_ff_twte03_was_dropped = False
            call screen lesson_four_ls28_fill
        
        label if_lf28_wrong:
            scene l4f28
            "Try again"
            call screen lesson_four_ls28_fill


    label lessonOrderedList:
        scene lesson_ordered_list
        "{b}Ordered lists <ol>{/b} show with numbers (1,2,3…) instead of bullet points. Use <ol> when the points have a certain order, like step by step instructions."
        jump lessonFourTwentyNine


    label lessonFourTwentyNine:
        $ ans_ff_twtn01_was_dropped = False
        scene l4f29
        call screen lesson_four_ls29_fill

        label call_fr29:
            $ ans_ff_twtn01_was_dropped = False
            call screen lesson_four_ls29_fill
        
        label if_lf29_wrong:
            scene l4f29
            "Try again"
            call screen lesson_four_ls29_fill


    label lessonFourThirty:
        $ ans_ff_tht01_was_dropped = False
        $ ans_ff_tht02_was_dropped = False
        $ ans_ff_tht03_was_dropped = False
        $ ans_ff_tht04_was_dropped = False
        $ ans_ff_tht05_was_dropped = False
        scene l4f30
        "Lists are also container tags, with the list items nested inside"
        call screen lesson_four_ls30_fill

        label call_fr30:
            $ ans_ff_twt01_was_dropped = False
            $ ans_ff_twt02_was_dropped = False
            $ ans_ff_twt03_was_dropped = False
            $ ans_ff_tht04_was_dropped = False
            $ ans_ff_tht05_was_dropped = False
            call screen lesson_four_ls30_fill
        
        label if_lf30_wrong:
            scene l4f30
            "Try again"
            call screen lesson_four_ls30_fill

            
    label lessonFourThirtyOne:
        $ ans_ff_thto01_was_dropped = False
        $ ans_ff_thto02_was_dropped = False
        scene l4f31
        "Use {b}unordered lists <ul>{/b} when the order of the items is not important. They are shown with bullet points"
        call screen lesson_four_ls31_fill

        label call_fr31:
            $ ans_ff_twto01_was_dropped = False
            $ ans_ff_twto02_was_dropped = False
            call screen lesson_four_ls31_fill
        
        label if_lf31_wrong:
            scene l4f31
            "Try again"
            call screen lesson_four_ls31_fill



    label lessonFourThirtyTwo:
        scene l4f32
        "You can nest a list inside another list"
        "Run the code to see what the web browser will display"
        call screen lesson_four_ls32_fill

        label when_run_four_32:
            scene lesson_4_32_run
            "Remember the indention so you won't be confused when you change a list items."
            jump lessonFourThirtyThree


    label lessonFourThirtyThree:
        $ ans_ff_thtt01_was_dropped = False
        $ ans_ff_thtt02_was_dropped = False
        $ ans_ff_thtt03_was_dropped = False
        $ ans_ff_thtt04_was_dropped = False
        scene l4f33
        "A list can contain any number of items."
        call screen lesson_four_ls33_fill

        label call_fr33:
            $ ans_ff_thtt01_was_dropped = False
            $ ans_ff_thtt02_was_dropped = False
            $ ans_ff_thtt03_was_dropped = False
            $ ans_ff_thtt04_was_dropped = False
            call screen lesson_four_ls33_fill
        
        label if_lf33_wrong:
            scene l4f33
            "Try again"
            call screen lesson_four_ls33_fill

    
    label lessonFourThirtyFour:
        $ ans_ff_thtf01_was_dropped = False
        $ ans_ff_thtf02_was_dropped = False
        $ ans_ff_thtf03_was_dropped = False
        $ ans_ff_thtf04_was_dropped = False
        scene l4f34
        call screen lesson_four_ls34_fill

        label call_fr34:
            $ ans_ff_thtf01_was_dropped = False
            $ ans_ff_thtf02_was_dropped = False
            $ ans_ff_thtf03_was_dropped = False
            $ ans_ff_thtf04_was_dropped = False
            call screen lesson_four_ls34_fill
        
        label if_lf34_wrong:
            scene l4f34
            "Try again"
            call screen lesson_four_ls34_fill


    label lessonFourThirtyFive:
        scene lesson_4_35 
        "Indentation is used to show nested elements."
        "What's the code showing?"

        menu:
            'An ordered list nested inside an unordered list':
                "you are correct"
                jump lessonFourThirtySix
            'An unordered list nested inside an ordered list':
                jump if_lf35_wrong
            
 
        label if_lf35_wrong:
            "incorrect"
            jump lessonFourThirtyFive 


    label lessonFourThirtySix:
        scene lesson_4_36 
        "Remember the web browser will ignore line breaks and white spaces in HTML code."
        "What will the web browser display?"

        menu:
            '1 big paragraph element with all the text':
                jump if_lf36_wrong
            '3 separate paragraphs':
                "you are correct"
                jump lessonFourThirtySeven
            '2 paragraphs':
                jump if_lf36_wrong
            
 
        label if_lf36_wrong:
            "incorrect"
            jump lessonFourThirtySix 


    label lessonFourThirtySeven:
        scene lesson_4_37 
        "Each list item will be displayed on a new line."
        "What will the web browser display?"

        menu:
            '2 unordered list items (A and B) in different lines':
                "you are correct"
                jump lessonFourThirtyEight
            'Nothing due to errors':
                jump if_lf37_wrong
            '2 unordered list items (A and B) in the same line':
                jump if_lf37_wrong
            
 
        label if_lf37_wrong:
            "incorrect"
            jump lessonFourThirtySeven 


    label lessonFourThirtyEight:
        scene lesson_4_38 
        "What will the web browser display?"

        menu:
            '2 ordered list items, 2 lines':
                jump if_lf38_wrong
            '3 ordered list item, 2 lines':
                jump if_lf38_wrong
            '3 ordered list items, 3 lines':
                "you are correct"
                jump lessonListOutro
            
            
 
        label if_lf38_wrong:
            "incorrect"
            jump lessonFourThirtyEight 

    
    label lessonListOutro:
        scene lesson_list_takeaways
        "Well done, coding trailblazers! In our coding odyssey, you've mastered {b}text formatting{/b} to make your content pop, discovered the magic of {b}hyperlinks{/b} to connect your pages, and delved into the art of {b}lists for organized content{/b}"
        "Bravo! Keep weaving these HTML tags, and your web development journey will continue to shine brightly. Onward to more coding adventures!"








    return

















label good_job:
    show bg_classroom
    "good"
    return