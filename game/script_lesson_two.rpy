label lesson_two:


    
    label lessonTwoIntro:
        show lesson_two_intro
        "Ready to begin the lesson two?"

    label lessonTwoFillone:
        $ ans_f0_was_dropped = False
        scene ltf1
        "{b}Headings{/b} in HTML come in different levels. <h1> defines the most important heading"
        call screen lesson_two_ls1_fill

        label call_t1:
            $ ans_f0_was_dropped = False
            call screen lesson_two_ls1_fill

        label if_lt1_wrong:
            scene ltf1
            "You got it wrong"
            call screen lesson_two_ls1_fill


    label lessonTwoFilltwo:
        $ ans_ft_was_dropped = False
        scene ltf2
        "You can use up to 6 levels of headings in HTML. The tags for these heading elements are <h1>, <h2>,"     
        call screen lesson_two_ls2_fill

        label call_t2:
            $ ans_ft_was_dropped = False
            call screen lesson_two_ls2_fill

        label if_lt2_wrong:
            scene ltf2
            "You got it wrong"
            call screen lesson_two_ls2_fill


    label lessonTwoFillThree:
        scene ltf4
        "You can add different headings to your page to organize the content."
        "In the upcoming section, we'll be entering a {b}Code Playground{/b} to practice writing HTML code."
        "Click the Run button to see what the web browser will display"
        call screen lesson_two_ls4_fill

        label when_run:
            scene lesson_when_run
            "<h1> usually styled with the largest font, and <h6> with the smallest."
            "Let's move on to the next example"
            jump lessonTwoFillFour
    

    label lessonTwoFillFour:
        scene ltf5
        "You can combine headings with other elements."
        "Run the code to see what the web browser will display"
        call screen lesson_two_ls5_fill

        label when_run_two:
            show lesson_when_run_4
            "Let's have another example using the {b}Code playground{/b}"
            jump lessonTwoFillFive

    label lessonTwoFillFive:
        scene ftg_bg
        "Ok, in this example, we will be filling up the gap or completing the tag to make the HTML code work."
        "Before that, let me teach you how to use the {b}Code Playground{/b}."
        "Click on the number or directly on the missing tag if you want to focus the text cursor."
        "Remember that after we code or complete the missing tags, we click the Run button."
        "After that, it will show the working code, or it may display 'Error' when there are code or tag issues."
        "And if you get an error, you could click the 'Return' button to go back"
        scene ltf6
        call screen lesson_two_ls6_fill
        

        label if_lt5_correct:
            show lesson_4_when_run
            "You did a great job, well done!"
            "Moving on..."
            jump lessonTwoFillSeven
    

    label lessonTwoFillSeven:
        $ ans_fs1_was_dropped = False
        $ ans_fs2_was_dropped = False
        scene ltf7
        "h1 is the most important heading."
        call screen lesson_two_ls7_fill

        label call_t7:
            $ ans_fs1_was_dropped = False
            $ ans_fs2_was_dropped = False
            call screen lesson_two_ls7_fill
        
        label if_lt7_wrong:
            scene ltf7
            "Try again"
            call screen lesson_two_ls7_fill


    label lessonTwoFillEight:
        $ ans_fe1_was_dropped = False
        $ ans_fe2_was_dropped = False
        $ ans_fe3_was_dropped = False
        scene ltf8
        "Heading levels need to be used in the correct order (h1, h2, …h6)"
        call screen lesson_two_ls8_fill

        label call_t8:
            $ ans_fe1_was_dropped = False
            $ ans_fe2_was_dropped = False
            $ ans_fe3_was_dropped = False
            call screen lesson_two_ls8_fill
        
        label if_lt8_wrong:
            scene ltf8
            "Try again"
            call screen lesson_two_ls8_fill


    label lessonTwoFillNine:
        scene lesson_8_22 
        "Many HTML elements require both opening and closing tags to contain elements"
        "These tags are also called"

        menu:
            'Empty tag':
                jump if_lth9_wrong
            'Container tag':
                "you are correct"
                jump lessonTwoFillTen
            

        
        label if_lth9_wrong:
            "incorrect"
            jump lessonTwoFillNine 

    
    label lessonTwoFillTen:
        $ ans_ft01_was_dropped = False
        $ ans_ft02_was_dropped = False
        scene ltf10
        "Some HTML elements can be defined with only one tag. They are called {b}empty tags{/b}."
        "The image tag <img> is a good example of an empty tag, it doesn't require a closing tag"
        call screen lesson_two_ls10_fill

        label call_t10:
            $ ans_ft01_was_dropped = False
            $ ans_ft02_was_dropped = False
            call screen lesson_two_ls10_fill
        
        label if_lt10_wrong:
            scene ltf10
            "Try again"
            call screen lesson_two_ls10_fill

    label lessonHeadTakeaways:
        show lesson_head_takeaways
        "Well done! young coders"
        "Next topic will be about Images"
        jump lessonImgIntro

    label lessonImgIntro:
        show lesson_img_intro
        "In this lesson, you'll learn to add images to your pages."
        "Now let's begin"
        jump lessonTwoFillEleven

    label lessonTwoFillEleven:
        scene lesson_8_22 
        "Images only require one tag to be displayed on your web page."
        "What's the HTML tag for the image element?"

        menu:
            '<img>':
                "you are correct"
                jump lessonTwoFillTwelve
            '<img></img>':
                jump if_lth11_wrong
            

        
        label if_lth11_wrong:
            "incorrect"
            jump lessonTwoFillEleven 


    label lessonTwoFillTwelve:
        $ ans_ftw01_was_dropped = False
        scene ltf12
        "Images are not technically inserted into a web page, they are linked. The source ({b}src{/b}) of the image
        needs to be included in the tag."
        call screen lesson_two_ls12_fill

        label call_12:
            $ ans_ftw01_was_dropped = False
            call screen lesson_two_ls12_fill

        
        
        label if_lt12_wrong:
            scene ltf12
            "Try again"
            call screen lesson_two_ls12_fill


    label lessonTwoFillThirteen:
        $ ans_fth01_was_dropped = False
        scene ltf13
        "You need to tell the browser where to find the image. The source ({b}src{/b}) is the location on the Internet
        where the image is stored."
        call screen lesson_two_ls13_fill

        label call_13:
            $ ans_fth01_was_dropped = False
            call screen lesson_two_ls13_fill

        
        
        label if_lt13_wrong:
            scene ltf13
            "Try again"
            call screen lesson_two_ls13_fill


    label lessonTwoFillFourteen:
        scene ltf14
        "Web browsers request information from the Web to put together and display web pages.
        Code, documents and media files such as images and videos are put together by the browser to display
        the resulting web page"
        "Web servers are computers that are always connected to the internet and continuously listening for
        requests of information."
        "Click the Run button to see what the web browser will display"
        call screen lesson_two_ls14_fill

        label when_run_14:
            scene lesson_14_when_run
            "The source (src) in the image tag points to the server where the image can be found."
            jump lessonTwoFillFifteen
    

    label lessonTwoFillFifteen:
        $ ans_ffit01_was_dropped = False
        scene ltf15
        "You need to tell the browser where to find the image. The source (src) is the location on the Internet
        where the image is stored."
        call screen lesson_two_ls15_fill

        label call_15:
            $ ans_ffit01_was_dropped = False
            call screen lesson_two_ls15_fill
        
        label if_lt15_wrong:
            scene ltf15
            "Try again"
            call screen lesson_two_ls15_fill


    label lessonTwoFillSixteen:
        scene ltf16
        "The broken image icon is usually shown in web pages when something is wrong with the image.
        The code below contains an error."
        "Web servers are computers that are always connected to the internet and continuously listening for
        requests of information."
        "Click the Run button to see what the web browser will display"
        call screen lesson_two_ls16_fill

        label when_run_16:
            scene lesson_16_when_run
            "As a result, the image won't be displayed on the page."
            jump lessonTwoFillSeventeen


    label lessonTwoFillSeventeen:
        scene ltf17
        "You can now include 4 different types of elements in your web pages. Let's put this into practice."
        "Click the Run button to see what the web browser will display"
        call screen lesson_two_ls17_fill

        label when_run_17:
            scene lesson_17_when_run
            "Great!"
            jump lessonTwoFillEighteen


    label lessonTwoFillEighteen:
        scene ftg_bg
        "The web browser will struggle to understand your code if there are errors. This can result in missing
        elements."
        "Errors in HTML code can include missing quotation marks, missing tags and typos in general. Can you fix
        the errors?"
        scene ltf18
        call screen lesson_two_ls18_fill
        

        label if_lt18_correct:
            scene lesson_18_when_run
            "You did a great job, well done!"
            jump lessonTwoTakeaways
            
    label lessonTwoTakeaways:
        show lesson_two_takeaways
        "Fantastic work, code explorers! Lesson Two unlocked some cool insights: {b}Headings{/b} bring order with up to {b}6{/b} levels, use those {b}container tags{/b} wisely!"
        "{b}Images{/b}, our visual pals, can be {b}linked or embedded{/b}—just share their online {b}address!{/b}"
        "No {b}closing tags{/b} for images, keep the {b}URLs{/b} flowing for pixel perfection!"





    return


