















label lesson_nine:
    scene bg_classroom
    #jump lessonNineFillFive
    if lesson_eight_finish:
        jump lessonDivideIntro
    else:
        "Please finish lesson 8"
        call screen lesson_ui


    label lessonDivideIntro:
        scene lesson_divide_intro
        "In this lesson, you`ll learn to group related elements."
        jump lessonNineFillOne


    label lessonNineFillOne:
        $ ans_fnn_o1_was_dropped = False
        scene l9f1
        "The {b}<div>{/b} element is a container for HTML elements that keeps your pages organized"
        call screen lesson_nine_ls1_fill

        label call_nn1:
            $ ans_fnn_o1_was_dropped = False
            call screen lesson_nine_ls1_fill
        
        label if_lnn1_wrong:
            scene l9f1
            "Try again"
            call screen lesson_nine_ls1_fill


    label lessonNineFillTwo:
        scene lesson_8_22 
        "The {b}<div>{/b} element always takes up the full width available. This means the <div> element is …"

        label choices_n2:
        menu:
            "an inline element":
                jump if_ln2_wrong
            "a block-level element":
                "You are correct"
                jump lessonNineFillThree
 
        label if_ln2_wrong:
            "incorrect"
            jump choices_n2


    label lessonNineFillThree:
        scene lesson_8_22 
        "{b}<div>{/b} is a block-level element. This means it…"

        label choices_n3:
        menu:
            "doesn`t start on a new line":
                jump if_ln3_wrong
            "starts on a new line":
                "You are correct"
                jump lessonNineFillFour
 
        label if_ln3_wrong:
            "incorrect"
            jump choices_n3


    label lessonNineFillFour:
        scene l9f4
        "Elements grouped in a {b}<div>{/b} can be styled quicker, all at once."
        "Run the code to see the div tag styled"
        call screen lesson_nine_ls4_fill

        label when_run_nn_four:
            scene lesson_9_4_run 
            "As you can see the style was applied to all element tag inside a {b}div tag{/b}"
            jump lessonNineFillFive


    label lessonNineFillFive:
        scene l9f5
        "Let's practice again"
        call screen lesson_nine_ls5_fill

        label if_ln5_correct:
            scene lesson_8_22
            "Great job"
            jump lessonNineFillSix


    label lessonNineFillSix:
        scene lesson_9_6
        "because it’s a what...?"

        label choices_n6:
        menu:
            "non-semantic tag":
                "You are correct"
                jump lessonNineFillSeven
            "semantic tag":
                jump if_ln6_wrong
 
        label if_ln6_wrong:
            "incorrect"
            jump choices_n6


    label lessonNineFillSeven:
        scene l9f7
        "<div> doesn't add any visual effect unless you add a style to it. It’s often used by web developers to group and style HTML elements."
        "Run the code to see the div tag styled"
        call screen lesson_nine_ls7_fill

        label when_run_nn_seven:
            scene lesson_9_7_run 
            "As you can see the style was applied to all element tag inside a {b}div tag{/b}"
            jump lessonNineFillEight


    label lessonNineFillEight:
        scene lesson_8_22    
        "You can use <div> to apply the same style to a group of elements"

        label choices_n8:
        menu:
            "False":
                jump if_ln8_wrong
            "True":
                "You are correct"
                jump lessonNineFillTen
 
        label if_ln8_wrong:
            "incorrect"
            jump choices_n8


    label lessonNineFillTen:
        scene lesson_9_10
        "In which color will the paragraph element be displayed?"

        label choices_n10:
        menu:
            "red":
                "You are correct"
                jump lessonNineFillEleven
            "green":
                jump if_ln10_wrong
            "black":
                jump if_ln10_wrong

        label if_ln10_wrong:
            "incorrect"
            jump choices_n10


    label lessonNineFillEleven:
        scene l9f11
        "The style in a <div> container will apply to all its nested elements unless you give them their own."
        "Run the code to see the div tag styled"
        call screen lesson_nine_ls11_fill

        label when_run_nn_eleven:
            scene lesson_9_11_run 
            "It will always prioritize the inline style"
            jump lessonNineFillTweleve


    label lessonNineFillTweleve:
        $ ans_fnn_twv1_was_dropped = False
        $ ans_fnn_twv2_was_dropped = False
        scene l9f12
        "Complete the code to make the text in the paragraph blue"
        call screen lesson_nine_ls12_fill

        label call_nn12:
            $ ans_fnn_twv1_was_dropped = False
            $ ans_fnn_twv2_was_dropped = False
            call screen lesson_nine_ls12_fill
        
        label if_lnn12_wrong:
            scene l9f12
            "Try again"
            call screen lesson_nine_ls12_fill


    label lessonNineFillThirteen:
        scene lesson_9_13
        "In which color will the level-3 heading be displayed?"

        label choices_n13:
        menu:
            "black":
                jump if_ln13_wrong
            "green":
                "You are correct"
                jump lessonNineFillFourteen
            "red":
                jump if_ln13_wrong

        label if_ln13_wrong:
            "incorrect"
            jump choices_n13


    label lessonNineFillFourteen:
        scene lesson_9_14
        "In which color will {b}Heading{/b} 2 be displayed?"

        label choices_n14:
        menu:
            "black":
                jump if_ln14_wrong
            "green":
                jump if_ln14_wrong
            "red":
                "You are correct"
                jump lessonNineFillFifteen

        label if_ln14_wrong:
            "incorrect"
            jump choices_n14


    label lessonNineFillFifteen:
        scene lesson_9_15
        "Remember black is the default color for text. In which color will the {b}Heading{/b} 2 element be displayed?"

        label choices_n15:
        menu:
            "black":
                "You are correct"
                jump lessonNineFillSixteen
            "green":
                jump if_ln15_wrong
            "red":
                jump if_ln15_wrong

        label if_ln15_wrong:
            "incorrect"
            jump choices_n15


    label lessonNineFillSixteen:
        scene lesson_9_16
        "Which element will be displayed in blue?"

        label choices_n16:
        menu:
            "Heading 4":
                "You are correct"
                jump lessonNineFillSeventeen
            "Paragraph":
                jump if_ln16_wrong
            "Heading 5":
                jump if_ln16_wrong

        label if_ln16_wrong:
            "incorrect"
            jump choices_n16


    label lessonNineFillSeventeen:
        scene l9f17
        "Complete the code to group and align the elements to the center"
        call screen lesson_nine_ls17_fill

        label if_ln17_correct:
            scene lesson_8_22
            "Great job"
            jump lessonDivideTakeaways


    label lessonDivideTakeaways:
        scene lesson_divide_takeaways
        "In the next lesson, you’ll learn to create tables."







































    return