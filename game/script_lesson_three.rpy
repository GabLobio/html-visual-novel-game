label lesson_three:

    #jump lessonThreeFillTwentyFour

    label lessonThreeIntro:
        scene lesson_three_intro
        "Are you ready to take lesson Three? CLICK!!!"
        jump lessonThreeFillOne

    label lessonThreeFillOne:
        $ ans_f3o01_was_dropped = False
        scene l3f1
        "{b}Comments{/b} help other humans to read your code."
        "You can add notes or explanations to your code with the comment tag: {b}<!--...-->{/b}"
        call screen lesson_three_ls1_fill

        label call_th1:
            $ ans_f3o01_was_dropped = False
            call screen lesson_three_ls1_fill

        
        
        label if_lth1_wrong:
            scene l3f1
            "Try again"
            call screen lesson_three_ls1_fill


    label lessonThreeFillTwo:
        $ ans_f3t01_was_dropped = False
        $ ans_f3t02_was_dropped = False
        scene l3f2
        "It's a good practice to use comments in your HTML code. They explain what the code does."
        call screen lesson_three_ls2_fill

        label call_th2:
            $ ans_f3t01_was_dropped = False
            $ ans_f3t02_was_dropped = False
            call screen lesson_three_ls2_fill

        
        
        label if_lth2_wrong:
            scene l3f2
            "Try again"
            call screen lesson_three_ls2_fill


    label lessonThreeFillThree:
        scene l3f3
        "It's a good practice to use comments in your HTML code. They explain what the code does."
        "Comments are ignored by browsers and not displayed on the web page."
        "Click the Run button to see what the web browser will display"
        call screen lesson_three_ls3_fill

        label llt_when_run:
            scene lesson_th_3_when_run
            "As you can see, it didn't show up on the browser."
            "The purpose of comment is to give label or description of the code line"
            "Comments in code are for the humans working on the HTML file"
            jump lessonThreeFillFour
    
    
    label lessonThreeFillFour:
        $ ans_f3f01_was_dropped = False
        $ ans_f3f02_was_dropped = False
        scene l3f4
        "You can use comments to temporarily disable part of your code so its not displayed by the browser."
        "Enclose the whole tag with comment"
        call screen lesson_three_ls4_fill

        label call_th4:
            $ ans_f3f01_was_dropped = False
            $ ans_f3f02_was_dropped = False
            call screen lesson_three_ls4_fill

        
        
        label if_lth4_wrong:
            scene l3f4
            "Try again"
            call screen lesson_three_ls4_fill


    label lessonThreeFillFive:
        scene l3f5
        "HTML is a case - insensitive language. This means that the web browser will understand the tags in both upper and lowercase form."
        "Click the Run button to see what the web browser will display"
        call screen lesson_three_ls5_fill

        label lthf_when_run:
            scene lesson_th_5_when_run
            "It still works"
            "But its good practice to use lowercase, to make your code consistent and easy to read."
            jump lessonThreeFillSix


    label lessonThreeFillSix:
        scene l3f6
        "The web browser will ignore white spaces and line breaks in your code. Still, its a good practice to organize your code into different lines so it's easier to read by humans."
        "Click the Run button to see what the web browser will display"
        call screen lesson_three_ls6_fill

        label lths_when_run:
            scene lesson_th_6_when_run
            "It still works"
            jump lessonThreeFillSeven


    label lessonThreeFillSeven:
        scene lesson_3_7 
        "Line breaks in elements like the paragraph are ignored by the browser."
        "How many line will the browser display"

        menu:
            '1':
                "you are correct"
                jump lessonThreeFillEight
            '2':
                jump if_lth7_wrong
        
        label if_lth7_wrong:
            "incorrect"
            jump lessonThreeFillSeven 

    
    label lessonThreeFillEight:
        $ ans_f3e01_was_dropped = False
        scene l3f8
        "If you need to create a line break you can use the <br> tag. <br> will force a line break."
        call screen lesson_three_ls8_fill

        label call_th8:
            $ ans_f3e01_was_dropped = False
            call screen lesson_three_ls8_fill

        
        
        label if_lth8_wrong:
            scene l3f8
            "Try again"
            call screen lesson_three_ls8_fill


    label lessonThreeFillNine:
        scene l3f9
        "Elements like headings and paragraphs automatically start on a new line when you create them."
        "Click the Run button to see what the web browser will display"
        call screen lesson_three_ls9_fill

        label lthn_when_run:
            scene lesson_th_9_when_run
            "However, other elements like the <button> require the use of <br> to be separated into different lines."
            "It behaves like an inline element, meaning that it will flow within the content of a line and won't start on a new line."
            jump lessonThreeFillTen


    label lessonThreeFillTen:
        scene lesson_3_10 
        "How many lines do you think this code will display"

        menu:
            '1':
                jump if_lth10_wrong
            '4':
                "you are correct"
                jump lessonThreeFillTwelve
            '2':
                jump if_lth10_wrong
            
        
        label if_lth10_wrong:
            "incorrect"
            jump lessonThreeFillTen 



    label lessonThreeFillTwelve:
        $ ans_f3tw01_was_dropped = False
        scene l3f12
        call screen lesson_three_ls12_fill

        label call_th12:
            $ ans_f3tw01_was_dropped = False
            call screen lesson_three_ls12_fill

        
        
        label if_lth12_wrong:
            scene l3f12
            "Try again"
            call screen lesson_three_ls12_fill


    label lessonCommentTakeaways:
        scene lesson_comment_takeaways
        "Well done, make sure you review this section"
        "Next topic will be the standards and best practices"
        jump lessonThreeFillThirteen


    label lessonThreeFillThirteen:
        $ ans_f3th01_was_dropped = False
        $ ans_f3th02_was_dropped = False
        scene l3f13
        "In this lesson you'll start applying some of the standards and best practices used in the web industry."
        call screen lesson_three_ls13_fill

        label call_th13:
            $ ans_f3th01_was_dropped = False
            $ ans_f3th02_was_dropped = False
            call screen lesson_three_ls13_fill

        
        
        label if_lth13_wrong:
            scene l3f13
            "Try again"
            call screen lesson_three_ls13_fill


    label lessonThreeFillFourteen:
        $ ans_f3ft01_was_dropped = False
        scene l3f14
        "The {b}<body> container tag{/b} is used to group everything that gets displayed on a page when loaded in a browser."
        call screen lesson_three_ls14_fill

        label call_th14:
            $ ans_f3ft01_was_dropped = False
            call screen lesson_three_ls14_fill

        
        
        label if_lth14_wrong:
            scene l3f14
            "Try again"
            call screen lesson_three_ls14_fill


    label lessonThreeFillFifteen:
        $ ans_f3fit01_was_dropped = False
        $ ans_f3fit02_was_dropped = False
        scene l3f15
        "{b}Body tags{/b} are needed for your page to be compatible with {b}all{/b} web browsers."
        "A web page can contain only {b}one body element{/b}"
        call screen lesson_three_ls15_fill
        
        label call_th15:
            $ ans_f3fit01_was_dropped = False
            $ ans_f3fit02_was_dropped = False
            call screen lesson_three_ls15_fill

        
        
        label if_lth15_wrong:
            scene l3f15
            "Try again"
            call screen lesson_three_ls15_fill


    label lessonThreeFillSixteen:
        $ ans_f3sit01_was_dropped = False
        $ ans_f3sit02_was_dropped = False
        $ ans_f3sit03_was_dropped = False
        scene l3f16
        "All the content elements that you need to display (like paragraphs, headings, buttons, and images) need to be inside the {b}<body> container bag{/b}."
        call screen lesson_three_ls16_fill
        
        label call_th16:
            $ ans_f3sit01_was_dropped = False
            $ ans_f3sit02_was_dropped = False
            $ ans_f3sit03_was_dropped = False
            call screen lesson_three_ls16_fill

        
        
        label if_lth16_wrong:
            scene l3f16
            "Try again"
            call screen lesson_three_ls16_fill


    label lessonThreeFillSeventeen:
        $ ans_f3set01_was_dropped = False
        scene l3f17
        "The <body> container tags needs to surround all the elements displayed on the page. When some HTML tags go inside others, this is called {b}nesting{/b}."
        call screen lesson_three_ls17_fill

        label call_th17:
            $ ans_f3set01_was_dropped = False
            call screen lesson_three_ls17_fill

        
        
        label if_lth17_wrong:
            scene l3f17
            "Try again"
            call screen lesson_three_ls17_fill
    

    label lessonThreeFillEighteen:
        scene lesson_8_22 
        "Some HTML tags need to be placed inside others. This is called?"

        menu:
            'Feathering':
                jump if_lth18_wrong
            'Egging':
                jump if_lth18_wrong
            'Nesting':
                "you are correct"
                jump lessonThreeFillNineteen
            

        
        label if_lth18_wrong:
            "incorrect"
            jump lessonThreeFillEighteen 


    label lessonThreeFillNineteen:
        $ ans_f3nit01_was_dropped = False
        $ ans_f3nit02_was_dropped = False
        scene l3f19
        "Websites do more than just display content. The {b}<head> container tag{/b} is used to include technical information about the page."
        call screen lesson_three_ls19_fill
        
        label call_th19:
            $ ans_f3nit01_was_dropped = False
            $ ans_f3nit02_was_dropped = False
            call screen lesson_three_ls19_fill

        
        
        label if_lth19_wrong:
            scene l3f19
            "Try again"
            call screen lesson_three_ls19_fill
    

    label lessonThreeFillTwenty:
        $ ans_f3twt01_was_dropped = False
        $ ans_f3twt02_was_dropped = False
        scene l3f20
        "You can use the head to help increase visibility and traffic from search engines like Google."
        call screen lesson_three_ls20_fill

        label call_th20:
            $ ans_f3twt01_was_dropped = False
            $ ans_f3twt02_was_dropped = False
            call screen lesson_three_ls20_fill

        
        
        label if_lth20_wrong:
            scene l3f20
            "Try again"
            call screen lesson_three_ls20_fill


    label lessonThreeFillTwentyOne:
        $ ans_f3twet01_was_dropped = False
        $ ans_f3twet02_was_dropped = False
        scene l3f21
        "The head needs to be placed before the body."
        call screen lesson_three_ls21_fill
        
        label call_th21:
            $ ans_f3twet01_was_dropped = False
            $ ans_f3twet02_was_dropped = False
            call screen lesson_three_ls21_fill

        
        
        label if_lth21_wrong:
            scene l3f21
            "Try again"
            call screen lesson_three_ls21_fill


    label lessonThreeFillTwentyTwo:
        scene l3f22
        "The information in the head is not displayed on the web page. Only the title is shown, in search engine results (e.g. Google) and in the browser tab."
        "Click the Run button to see what the web browser will display"
        call screen lesson_three_ls22_fill

        label lth22_when_run:
            scene lesson_th_22_when_run
            "As you can see it changes the browser tab title into 'Title of the page'"
            "Next, we will be talking about code indention"
            jump lessonThreeFillTwentyThree


    label lessonThreeFillTwentyThree:
        scene l3f23
        "Today, the majority of web professionals always wrap their HTML code in <html> tags. The {b}<html> tag{/b} is a container tag." 
        "{b}Head{/b} and {b}body{/b} are {b}nested{/b} inside the {b}<html> tags{/b}."
        "{b}Indentation{/b} is considered a very good practice to improve code readability. Indentation is the spaces at the beginning of lines."
        "To show what HTML code can be produced if indentation is used, click the Run button."
        call screen lesson_three_ls23_fill

        label lth23_when_run:
            scene lesson_th_23_when_run
            "Different levels of indentation are used to show nesting."
            jump lessonThreeFillTwentyFour


    label lessonThreeFillTwentyFour:
        $ ans_f3twef01_was_dropped = False
        $ ans_f3twef02_was_dropped = False
        scene l3f24
        "Select all correct answers."
        call screen lesson_three_ls24_fill

        label call_th24:
            $ ans_f3twef01_was_dropped = False
            $ ans_f3twef02_was_dropped = False
            call screen lesson_three_ls24_fill

        
        
        label if_lth24_wrong:
            scene l3f24
            "Try again"
            call screen lesson_three_ls24_fill    


    label lessoThreeOutro:
        scene lesson_three_outro
        "Bravo, coding champions! In this lesson, you harnessed the power of {b}comments{/b} for clarity, wielded the {b}<!--...--> tag{/b} as a code whisperer, mastered the {b}<br> ta{/b}g for line breaks"
        "Organized HTML into {b}head{/b} and {b}body{/b} realms, invoked {b}<html>{/b} for universal harmony, and embraced the art of {b}indentation{/b} for readable collaborations."
        "Your coding journey is flourishing—keep up the great work, young {b}coders{/b}! "



    return


