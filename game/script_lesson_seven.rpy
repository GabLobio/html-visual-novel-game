









label lesson_seven:

    #jump lessonSevenFillTwentysix
    if lesson_six_finish:
        jump lessonPageIntro
    else:
        "Please finish lesson 6"
        call screen lesson_ui


    label lessonPageIntro:
        scene lesson_page_intro
        "In this lesson, you`ll learn to apply a layout to your web pages."
        jump lessonSevenFillOne


    label lessonSevenFillOne:
        $ ans_fsv_o1_was_dropped = False
        $ ans_fsv_o2_was_dropped = False
        $ ans_fsv_o3_was_dropped = False
        scene l7f1
        "The body of a web page can be divided into 3 parts."
        call screen lesson_seven_ls1_fill

        label call_sv1:
            $ ans_fsv_o1_was_dropped = False
            $ ans_fsv_o2_was_dropped = False
            $ ans_fsv_o3_was_dropped = False
            call screen lesson_seven_ls1_fill
        
        label if_lsv1_wrong:
            scene l7f1
            "Try again"
            call screen lesson_seven_ls1_fill


    label lessonSevenFillTwo:
        $ ans_fsv_t1_was_dropped = False
        scene l7f2
        "The {b}<header>{/b} container tag usually contains introductory information."
        "You can add several header elements to a web page."
        call screen lesson_seven_ls2_fill

        label call_sv2:
            $ ans_fsv_t1_was_dropped = False
            call screen lesson_seven_ls2_fill
        
        label if_lsv2_wrong:
            scene l7f2
            "Try again"
            call screen lesson_seven_ls2_fill


    label lessonSevenFillThree:
        $ ans_fsv_thr1_was_dropped = False
        $ ans_fsv_thr2_was_dropped = False
        scene l7f3 
        "The {b}header{/b} often contains navigation links, a menu and/or a search bar. Brand elements like logos are usually found in the header too."
        call screen lesson_seven_ls3_fill

        label call_sv3:
            $ ans_fsv_thr1_was_dropped = False
            $ ans_fsv_thr2_was_dropped = False
            call screen lesson_seven_ls3_fill
        
        label if_lsv3_wrong:
            scene l7f3
            "Try again"
            call screen lesson_seven_ls3_fill


    label lessonSevenFillFour:
        $ ans_fsv_fr1_was_dropped = False
        $ ans_fsv_fr2_was_dropped = False
        scene l7f4
        "The {b}<main>{/b} container tag is used to include the main content of a web page."
        "There must not be more than one {b}<main>{/b} element in a document."
        call screen lesson_seven_ls4_fill

        label call_sv4:
            $ ans_fsv_fr1_was_dropped = False
            $ ans_fsv_fr2_was_dropped = False
            call screen lesson_seven_ls4_fill
        
        label if_lsv4_wrong:
            scene l7f4
            "Try again"
            call screen lesson_seven_ls4_fill


    label lessonSevenFillFive:
        $ ans_fsv_fv1_was_dropped = False
        scene l7f5
        "The {b}<footer>{/b} container tag often contains contact and legal information and links."
        "You can have several {b}<footer>{/b} elements in one document."
        call screen lesson_seven_ls5_fill

        label call_sv5:
            $ ans_fsv_fv1_was_dropped = False
            call screen lesson_seven_ls5_fill
        
        label if_lsv5_wrong:
            scene l7f5
            "Try again"
            call screen lesson_seven_ls5_fill


    label lessonSevenFillSix:
        scene lesson_7_6
        "{b}<header>{/b}, {b}<main>{/b} and {b}<footer>{/b} elements are nested inside the <body> container tag"
        jump lessonSevenFillSeven


    label lessonSevenFillSeven:
        scene lesson_7_7 
        "New web designers and developers often confuse <header> with other HTML elements. Let`s practice a bit."
        "Which  elements must be nested inside {b}<body>{/b}?"

        label choices_fs:
        menu:
            "<head>":
                jump if_lsv7_wrong
            "<header>":
                "You are correct"
                jump lessonSevenFillEight
 
        label if_lsv7_wrong:
            "incorrect"
            jump lessonSevenFillSeven


    label lessonSevenFillEight:
        scene lesson_7_7 
        "Which of the following elements is used to include technical information about the page like title, description, author and keywords?"

        label choices_fe:
        menu:
            "<header>":
                jump if_lsv8_wrong
            "<head>":
                "You are correct"
                jump lessonSevenFillNine
 
        label if_lsv8_wrong:
            "incorrect"
            jump choices_fe


    label lessonSevenFillNine:
        scene lesson_7_7 
        "Which of the following elements is {b}not{/b} shown to the visitor by the web browser?"

        label choices_fn:
        menu:
            "<header>":
                jump if_lsv9_wrong
            "<head>":
                "You are correct"
                jump lessonSevenFillTen
 
        label if_lsv9_wrong:
            "incorrect"
            jump choices_fn


    label lessonSevenFillTen:
        $ ans_fsv_ten1_was_dropped = False
        $ ans_fsv_ten2_was_dropped = False
        $ ans_fsv_ten3_was_dropped = False
        scene l7f10 
        call screen lesson_seven_ls10_fill

        label call_sv10:
            $ ans_fsv_ten1_was_dropped = False
            $ ans_fsv_ten2_was_dropped = False
            $ ans_fsv_ten3_was_dropped = False
            call screen lesson_seven_ls10_fill
        
        label if_lsv10_wrong:
            scene l7f10
            "Try again"
            call screen lesson_seven_ls10_fill


    label lessonSevenFillEleven:
        scene lesson_7_7 
        'Where would you add a "back to top of the page" link?'

        label choices_fel:
        menu:
            "<header>":
                jump if_lsv11_wrong
            "<footer>":
                "You are correct"
                jump lessonSevenFillThirteen
            "<head>":
                jump if_lsv11_wrong

        label if_lsv11_wrong:
            "incorrect"
            jump choices_fel


    label lessonSevenFillThirteen:
        scene lesson_page_takeaways
        "In the next lesson, you`ll dive deeper into page layout and structure."


    label lessonLayoutIntro:
        scene lesson_layout_intro 
        "In this lesson, you`ll learn to structure web pages with layouts that improve accessibility and make the content easier to understand for both search engines and users."


    label lessonSevenFillFourteen:
        $ ans_fsv_ft1_was_dropped = False
        scene l7f14
        "{b}<article>{/b} represents an independent, self-contained piece of content."
        call screen lesson_seven_ls14_fill

        label call_sv14:
            $ ans_fsv_ft1_was_dropped = False
            call screen lesson_seven_ls14_fill
        
        label if_lsv14_wrong:
            scene l7f14
            "Try again"
            call screen lesson_seven_ls14_fill


    label lessonSevenFillFifteen:
        $ ans_fsv_fft1_was_dropped = False
        $ ans_fsv_fft2_was_dropped = False
        scene l7f15 
        "An article is content that would make sense on its own."
        call screen lesson_seven_ls15_fill

        label call_sv15:
            $ ans_fsv_fft1_was_dropped = False
            $ ans_fsv_fft2_was_dropped = False
            call screen lesson_seven_ls15_fill
        
        label if_lsv15_wrong:
            scene l7f15
            "Try again"
            call screen lesson_seven_ls15_fill


    label lessonSevenFillSixteen:
        scene lesson_7_7 
        'The {b}<article> tag{/b} clearly indicates the role for its content. It`s used for content like news stories, and blog posts.'
        "So <article> is an example of…"

        label choices_fst:
        menu:
            "an empty tag":
                jump if_lsv16_wrong
            "a semantic tag":
                "You are correct"
                jump lessonSevenFillSeventeen

        label if_lsv16_wrong:
            "incorrect"
            jump choices_fst


    label lessonSevenFillSeventeen:
        scene lesson_7_7 
        "Layout tags like {b}<header>{/b}, {b}<main>{/b}, {b}<footer>{/b} and {b}<article>{/b} are semantic tags because they…"

        label choices_fsvt:
        menu:
            "use angle brackets <>":
                jump if_lsv17_wrong
            "give information about what they contain":
                "You are correct"
                jump lessonSevenFillEighteen

        label if_lsv17_wrong:
            "incorrect"
            jump choices_fsvt


    label lessonSevenFillEighteen:
        $ ans_fsv_et1_was_dropped = False
        scene l7f18 
        "{b}<section>{/b} helps to break down the content into parts."
        call screen lesson_seven_ls18_fill

        label call_sv18:
            $ ans_fsv_et1_was_dropped = False
            call screen lesson_seven_ls18_fill
        
        label if_lsv18_wrong:
            scene l7f18
            "Try again"
            call screen lesson_seven_ls18_fill


    label lessonSevenFillNineteen:
        $ ans_fsv_nt1_was_dropped = False
        $ ans_fsv_nt2_was_dropped = False
        scene l7f19 
        "{b}<section>{/b} helps to break down the content into parts."
        call screen lesson_seven_ls19_fill

        label call_sv19:
            $ ans_fsv_nt1_was_dropped = False
            $ ans_fsv_nt2_was_dropped = False
            call screen lesson_seven_ls19_fill
        
        label if_lsv19_wrong:
            scene l7f19
            "Try again"
            call screen lesson_seven_ls19_fill


    label lessonSevenFillTwenty:
        scene lesson_7_7 
        "A web page could be split into separate sections for introduction, contact information, etc."
        "{b}<section>{/b} is…"

        label choices_ftwt:
        menu:
            "an empty tag":
                jump if_lsv20_wrong
            "a container tag":
                "You are correct"
                jump lessonSevenFillTwentyone

        label if_lsv20_wrong:
            "incorrect"
            jump choices_ftwt


    label lessonSevenFillTwentyone:
        scene lesson_7_7 
        "{b}<section>{/b} can be used to separate each chapter, news item, etc."
        "{b}<section>{/b} is a…"

        label choices_ftwto:
        menu:
            "non-semantic tag":
                "You are correct"
                jump lessonSevenFillTwentytwo
            "semantic tag":
                jump if_lsv21_wrong

        label if_lsv21_wrong:
            "incorrect"
            jump choices_ftwto


    label lessonSevenFillTwentytwo:
        $ ans_fsv_twtt1_was_dropped = False
        $ ans_fsv_twtt2_was_dropped = False
        scene l7f22
        "{b}<aside>{/b} is used for secondary, additional or somehow related content."
        call screen lesson_seven_ls22_fill

        label call_sv22:
            $ ans_fsv_twtt1_was_dropped = False
            $ ans_fsv_twtt2_was_dropped = False
            call screen lesson_seven_ls22_fill
        
        label if_lsv22_wrong:
            scene l7f22
            "Try again"
            call screen lesson_seven_ls22_fill


    label lessonSevenFillTwentythree:
        scene lesson_7_23
        "You can combine these elements to create a well-structured semantic layout for your content."
        jump lessonSevenFillTwentyfour


    label lessonSevenFillTwentyfour:
        scene lesson_7_7 
        "Which element should be used to divide a story into chapters?"

        label choices_ftwfr:
        menu:
            "<article>":
                jump if_lsv24_wrong
            "<section>":
                "You are correct"
                jump lessonSevenFillTwentyfive
            "<main>":
                jump if_lsv24_wrong

        label if_lsv24_wrong:
            "incorrect"
            jump choices_ftwfr


    label lessonSevenFillTwentyfive:
        scene lesson_7_23
        "Semantic tags don`t give any visual effect to the content. You can nest layout elements to create organized and accessible pages."
        jump lessonSevenFillTwentysix


    label lessonSevenFillTwentysix:
        scene lesson_7_7 
        "What would you use <article> for?"

        label choices_ftwsx:
        menu:
            "Today`s news brief":
                "You are correct"
                jump lessonSevenFillTwentyseven
            "Navigation menu":
                jump if_lsv26_wrong
            "Sidebar":
                jump if_lsv26_wrong

        label if_lsv26_wrong:
            "incorrect"
            jump choices_ftwsx



    label lessonSevenFillTwentyseven:
        $ ans_fsv_twts1_was_dropped = False
        $ ans_fsv_twts2_was_dropped = False
        $ ans_fsv_twts3_was_dropped = False
        call screen lesson_seven_ls27_fill

        label call_sv27:
            $ ans_fsv_twts1_was_dropped = False
            $ ans_fsv_twts2_was_dropped = False
            $ ans_fsv_twts3_was_dropped = False
            call screen lesson_seven_ls27_fill
        
        label if_lsv27_wrong:
            scene l7f27
            "Try again"
            call screen lesson_seven_ls27_fill


    label lessonLayoutTakeaways:
        scene lesson_layout_takeaways
        "Take the next lesson to learn even more layout skills."

















    return