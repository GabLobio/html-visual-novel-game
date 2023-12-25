image lof1 = "images/lesson_one/Lesson 1.1.png"
image lof2 = "images/lesson_one/Lesson 1.2.png"
image lof3 = "images/lesson_one/Lesson 1.3.png"
image lof4 = "images/lesson_one/Lesson 1.4.png"
image lof5 = "images/lesson_one/Lesson 1.5.png"
image lof6 = "images/lesson_one/Lesson 1.6.png"
image lof7 = "images/lesson_one/Lesson 1.7.png"
image lof8 = "images/lesson_one/Lesson 1.8.png"
image lof9 = "images/lesson_one/Lesson 1.9.png"
image lof10 = "images/lesson_one/Lesson 1.10.png"
image lof12 = "images/lesson_one/Lesson 1.12.png"


label lesson_one:



    label tutorial:
        scene dnd_tutorial
        "Before we start the lesson, let's discuss what drag-and-drop is."
        'Your task is to drag HTML elements from the choices below and drop them onto the corresponding blanks space'
        scene dnd_tutorial_two
        '"Simply click, hold, and drag the element you think fits, then release it over the blank space. If correct, it`ll snap into place. If not, try again!"'
        scene dnd_tutorial_three
        'Let`s get started! Match the choices to the correct blanks below by dragging and dropping. Have fun learning HTML through this hands-on experience!'

    #The Core Web Technology
    label coreWebTechnology:
        scene the_core_web_technology
        "Every website you’ve ever visited is built with {b}HTML code{/b}."
        "With this lesson you’ll be able to {b}build your own web page{/b}."    

    label lessonOneFillOne:
        $ ans_button_lt_dropped = False

        scene lof1 
        show mom
        e "HTML code is based on tags like <button> tag"
        e "Tags use angle brackets (<>)"
        call screen lesson_one_fill

        label call_o1:
            $ ans_button_lt_dropped = False
            call screen lesson_one_fill

        label if_wrong:
            scene lof1
            e "Try again"
            call screen lesson_one_fill


    label lessonOneFillTwo:
        $ ans_button_was_dropped = False
        $ ans_gt_was_dropped = False
        scene lof2 
        e "The angle brackets <> surround the name of the element you want to add to the page"
        e "Elements like buttons, text and images are added to web pages with different tags."
        call screen lesson_two_fill

        label call_o2:
            $ ans_button_was_dropped = False
            $ ans_gt_was_dropped = False
            call screen lesson_two_fill

        label if_wrong_l2:
            scene lof2
            "Try again"
            call screen lesson_two_fill


    label lessonOneFillThree:
        $ ans_fl2_was_dropped = False
        scene lof3
        e "You can use {b}image tag (<img>){/b} to add images to a web page"
        call screen lesson_three_fill

        label call_o3:
            $ ans_fl2_was_dropped = False
            call screen lesson_three_fill

        label if_wrong_l3:
            scene lof3
            "Try again"
            call screen lesson_three_fill



    label lessonOneFillFour:
        $ ans_btn_was_dropped = False
        $ ans_img_was_dropped = False
        $ ans_tp_was_dropped = False
        $ ans_tbl_was_dropped = False
        scene lof4
        e "You need HTML tags to add different elements to a page."
        call screen lesson_four_fill

        label call_o4:
            $ ans_btn_was_dropped = False
            $ ans_img_was_dropped = False
            $ ans_tp_was_dropped = False
            $ ans_tbl_was_dropped = False
            call screen lesson_four_fill

        label if_wrong_l4:
            scene lof4
            "Try again"
            call screen lesson_four_fill

    label lessonOneIntro:
        show lesson_one_intro
        "Take note..."
        jump lessonBeforeFillFive

    label lessonBeforeFillFive:
        scene lesson_before_f5
        "The structure of a web page is built in HTML"
        "You can then style the page with CSS"
        "JavaScript is used to make pages Interactive"

    label lessonOneFillFive:
        $ ans_html_was_dropped = False
        $ ans_js_was_dropped = False
        $ ans_css_was_dropped = False
        scene lof5
        call screen lesson_five_fill

        label call_o5:
            $ ans_html_was_dropped = False
            $ ans_js_was_dropped = False
            $ ans_css_was_dropped = False
            call screen lesson_five_fill

        label if_wrong_l5:
            scene lof5
            "Try again"
            call screen lesson_five_fill

    label lessonHtmlTakeaways:
        show lesson_html_takeaways
        "Before we move on to the next one, try to remember this lesson takeaways"
        jump introToHTML

    label introToHTML:
        scene lesson_0_1
        "You’ll start writing, running and testing real {b}HTML code{/b} in this lesson to build the structure of a web page."
        "But, first let's discuss the element tag"
        jump openingTag

    label openingTag:
        scene opening_tag
        "An opening tag is the first part of an HTML element and is enclosed in angle brackets ({b}<{/b} and {b}>{/b})."
        "It signifies the beginning of an HTML element."
        jump closingTag

    label closingTag:
        scene closing_tag
        "A {b}closing tag{/b} is the second part of an HTML element and is also enclosed in angle brackets ({b}<{/b} and {b}>{/b}), but it includes a forward slash {b}(/){/b} before the tag name."
        "It signifies the end of an HTML element."
        jump tagContent

    label tagContent:
        scene tag_content
        "The {b}content{/b} of an HTML element is the information between the {b}opening{/b} and {b}closing tags{/b}."
        "It represents the data or text that will be displayed on the web page."
        jump elementTag

    label elementTag:
        scene elelment_tag
        "An {b}HTML element{/b} consists of the {b}opening tag{/b}, {b}content{/b}, and {b}closing tag{/b}."
        "It represents a specific piece of content or structure on a {b}web page{/b}."
        "In later lesson we wil discussing and use different elements"
        "This element called heading tag it has 6 different kind"
        "moving on"
        jump tagAttribute

    label tagAttribute:
        scene tag_attribute
        "This example {b}<a> tag{/b} can be called {b}HyperText, Hyperlink, or link tag{/b}. Let`s use this to exaplain {b}attributes{/b}"
        "An {b}attribute{/b} provides additional information about an HTML element and is always included in the {b}opening tag{/b}."
        "It is made up of a {b}name{/b} and a {b}value{/b}."
        '"Example: In {b}<a href="https://www.example.com">{/b}, {b}href{/b} is the attribute {b}name{/b},"'
        'and "{b}https://www.example.com{/b}" is the attribute {b}value{/b}.'
        jump tagAttributeName

    label tagAttributeName:
        scene tag_attribute_name
        "The {b}name{/b} of an attribute specifies the type of information it is providing" 
        "It comes {b}before{/b} the equal sign {b}(=){/b} in the attribute."
        'Example: In <a href="https://www.example.com">, {b}href{/b} is an {b}attribute name{/b}.'
        jump tagAttributeValue

    label tagAttributeValue:
        scene tag_attribute_value
        "The {b}value{/b} of an attribute provides the specific information associated with that attribute."
        "It comes {b}after{/b} the equal sign {b}(=){/b} in the attribute, enclosed in quotes."
        'Example: In <a href="https://www.example.com">, {b}"https://www.example.com"{/b} is an {b}attribute values{/b}.'
        jump tagSummary

    label tagSummary:
        scene tag_summary
        "In summary, {b}HTML{/b} uses a combination of {b}opening{/b} and {b}closing tags{/b}, {b}content{/b}, and {b}attributes{/b} to structure and present {b}information{/b} on a web page."
        "{b}Elements{/b} represent different parts of the content, and attributes provide additional details about those elements."
        'Also, there are elements that don`t require a closing tag. These are called "void" or "empty" element tags. '
        'These elements consist only of an opening tag, and they don`t have content or a closing tag.'
        'Instead, they may include attributes in the opening tag to provide additional information.'
        jump basicTag

    label basicTag:
        scene lesson_0_2
        "Many HTML elements require both opening and closing tags."
        jump lessonOneFillSix

    label lessonOneFillSix:
        $ ans_btntg_was_dropped = False
        $ ans_like_was_dropped = False
        call screen lesson_six_fill

        label call_o6:
            $ ans_btntg_was_dropped = False
            $ ans_like_was_dropped = Falsee
            call screen lesson_six_fill

        label if_wrong_l6:
            show screen lesson_six_fill
            "Try again"
            call screen lesson_six_fill

            

    label lessonOneFillSeven:
        $ ans_tgbtn_was_dropped = False
        scene lof7
        e "Closing tags are very similar to the opening tags. "
        e "The only difference is that they contain a forward slash."
        call screen lesson_seven_fill

        label call_o7:
            $ ans_tgbtn_was_dropped = False
            call screen lesson_seven_fill

        label if_wrong_l7:
            scene lof7
            "Try again"
            call screen lesson_seven_fill




    label lessonOneFillEighth:
        $ ans_comment_was_dropped = False
        scene lof8
        e "You can customize the text for the button. The content of the button is placed between the tags"
        call screen lesson_eighth_fill

        label call_o8:
            $ ans_comment_was_dropped = False
            call screen lesson_eighth_fill

        label if_wrong_l8:
            scene lof8
            "Try again"
            call screen lesson_eighth_fill



    
    label lessonOneFillNine:
        $ ans_ptag_was_dropped = False
        $ ans_ptag2_was_dropped = False
        scene lof9
        e "Many elements require both opening and closing tags, also known as container tags. The paragraphtext is another example"
        call screen lesson_nine_fill

        label call_o9:
            $ ans_ptag_was_dropped = False
            $ ans_ptag2_was_dropped = False
            call screen lesson_nine_fill

        label if_wrong_l9:
            scene lof9
            "Try again"
            call screen lesson_nine_fill


        
    label lessonOneFillTen:
        $ ans_ft1_was_dropped = False
        $ ans_ft2_was_dropped = False
        $ ans_ft3_was_dropped = False
        scene lof10
        call screen lesson_ten_fill

        label call_o10:
            $ ans_ft1_was_dropped = False
            $ ans_ft2_was_dropped = False
            $ ans_ft3_was_dropped = False
            call screen lesson_ten_fill

        label if_wrong_l10:
            scene lof10
            "Try again"
            call screen lesson_ten_fill


    label lessonOneBeforeEleven:
        show screen lesson_before_eleven_fill
        "Ready to write, run and test real HTML code? The {b}Code Playground{/b} allows you to do that"
        "hit the 'Run' textbutton below to see what the web browser will display"
        call screen lesson_before_eleven_fill

        label lesson_one_11_run:
            show lesson_one_11_run 
            "The code you write in 'index.html' will be read by the browser and display it"
            "And you coded p tag and button tag now the content will be displayed like so"
            jump lessonOneFillEleven


    label lessonOneFillEleven:
        scene lesson_1_11 
        "You can combine multiple elements in your code."
        "If you were to run this, what would be the content of the web page?"

        menu:
            'An image and a button':
                jump if_wrong_l11
            'A paragraph text and a button':
                "you are correct"
                jump lessonOneFillTwelve
            

        
        label if_wrong_l11:
            "incorrect"
            jump lessonOneFillEleven 
    

    label lessonOneFillTwelve:
        $ ans_t1_was_dropped = False
        $ ans_t2_was_dropped = False
        scene lof12
        e "Tags use angle brackets <>"
        call screen lesson_twelve_fill

        label call_o12:
            $ ans_t1_was_dropped = False
            $ ans_t2_was_dropped = False
            call screen lesson_twelve_fill

        label if_wrong_l12:
            scene lof12
            "Try again"
            call screen lesson_twelve_fill


    label webBrowser:
        scene lesson_after_of12
        "Your {b}web browser{/b} (e.g. Chrome, Safari, etc.) can read HTML code and translate it into what you see when you surf the web."
        jump aWebBrowser

    label aWebBrowser:
        scene lesson_8_22 
        "A web browser…"
        "Is what?"

        menu:
            'requires the user to understand HTML code':
                jump if_wrong_l13
            'translates HTML code into web pages':
                "you are correct"
                jump lessonOneTakeaways
            

        
        label if_wrong_l13:
            "incorrect"
            jump aWebBrowser 
    
    
    label lessonOneTakeaways:
        show lesson_one_takeaways
        "In the next lesson, you’ll learn about a new HTML element: the heading.    "

    call screen lesson_ui

    label you_pass:
        "You did it"






















    return