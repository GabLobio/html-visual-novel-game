



label lesson_five:
    scene bg_classroom
    if lesson_four_finish:
        jump lessonAttributeIntro
    else:
        "Please finish lesson 4"
        call screen lesson_ui

    #jump lessonFiveFillFourtyseven

    label lessonAttributeIntro:
        scene lesson_attributes_intro
        "Ready to start Attribute Topic?"
        jump lessonFiveFillOne


    label lessonFiveFillOne:
        $ ans_ffive_o1_was_dropped = False
        scene l5f1
        "{b}Attributes{/b} can be {b}optional{/b} or {b}required{/b}. You already know some required attributes."
        "The image tag requires an attribute to work correctly."
        call screen lesson_five_ls1_fill

        label call_fv1:
            $ ans_ffive_o1_was_dropped = False
            call screen lesson_five_ls1_fill
        
        label if_lfv1_wrong:
            scene l5f1
            "Try again"
            call screen lesson_five_ls1_fill

    
    label lessonFiveFilltwo:
        $ ans_ffv_two1_was_dropped = False
        scene l5f2
        "For container tags, the attributes always go in the opening tag. The anchor tag is another example of an HTML element that requires an attribute to work correctly."
        call screen lesson_five_ls2_fill

        label call_fv2:
            $ ans_ffv_two1_was_dropped = False
            call screen lesson_five_ls2_fill
        
        label if_lfv2_wrong:
            scene l5f2
            "Try again"
            call screen lesson_five_ls2_fill

    label lessonFiveFillthree:
        scene lesson_8_22 
        "href (in the anchor tag) and src (in the image tag) are examples of?   "

        menu:
            "attributes":
                "You are correct"
                jump lessonFiveFillFour
            "values":
                jump if_lfv3_wrong
            "properties":
                jump if_lfv3_wrong
 
        label if_lfv3_wrong:
            "incorrect"
            jump lessonFiveFillthree
    



    label lessonFiveFillFour:
        scene lesson_8_22 
        "In the container tags, attributes always go to what tag?"

        menu:
            "in the closing tag":
                jump if_lfv4_wrong
            "in the opening tag":
                "You are correct"
                jump lessonFiveFillFive
 
        label if_lfv4_wrong:
            "incorrect"
            jump lessonFiveFillFour

    
    label lessonFiveFillFive:
        $ ans_ffv_fv1_was_dropped = False
        scene l5f5
        "It's best practice to describe what images are showing. The {b}alt{/b} attribute (alternative text) is used to add image descriptions."
        call screen lesson_five_ls5_fill

        label call_fv5:
            $ ans_ffv_fv1_was_dropped = False
            call screen lesson_five_ls5_fill
        
        label if_lfv5_wrong:
            scene l5f5
            "Try again"
            call screen lesson_five_ls5_fill

    
    label lessonFiveFillSix:
        scene lesson_8_22 
        "The alt attribute can be: \n- read aloud by screen readers \n- shown when the image doesn`t load \n- read by search engines"
        "Is adding alternative text to images makes your page more accessible?"

        menu:
            "False":
                jump if_lfv6_wrong
            "True":
                "You are correct"
                jump lessonFiveFillSeven
 
        label if_lfv6_wrong:
            "incorrect"
            jump lessonFiveFillSix


    label lessonFiveFillSeven:
        $ ans_ffv_svn1_was_dropped = False
        $ ans_ffv_svn2_was_dropped = False
        scene l5f7
        call screen lesson_five_ls7_fill

        label call_fv7:
            $ ans_ffv_svn1_was_dropped = False
            $ ans_ffv_svn2_was_dropped = False
            call screen lesson_five_ls7_fill
        
        label if_lfv7_wrong:
            scene l5f7
            "Try again"
            call screen lesson_five_ls7_fill


    label lessonFiveFillEight:
        $ ans_ffv_egt1_was_dropped = False
        $ ans_ffv_egt2_was_dropped = False
        $ ans_ffv_egt3_was_dropped = False
        scene l5f8
        call screen lesson_five_ls8_fill

        label call_fv8:
            $ ans_ffv_egt1_was_dropped = False
            $ ans_ffv_egt2_was_dropped = False
            $ ans_ffv_egt3_was_dropped = False
            call screen lesson_five_ls8_fill
        
        label if_lfv8_wrong:
            scene l5f8
            "Try again"
            call screen lesson_five_ls8_fill


    label lessonFiveFillNine:
        scene l5f9
        "You can control the size of images in your web pages. {b}width{/b} is an optional attribute. Run the code to see what the web browser will display"
        call screen lesson_five_ls9_fill

        label when_run_five_nine:
            scene lesson_5_9_run
            "See the difference? The attribute width added a width length of 300 pixel"
            jump lessonFiveFillTen    


    label lessonFiveFillTen:
        $ ans_ffv_ten1_was_dropped = False
        $ ans_ffv_ten2_was_dropped = False
        scene l5f10
        call screen lesson_five_ls10_fill

        label call_fv10:
            $ ans_ffv_ten1_was_dropped = False
            $ ans_ffv_ten2_was_dropped = False
            call screen lesson_five_ls10_fill
        
        label if_lfv10_wrong:
            scene l5f10
            "Try again"
            call screen lesson_five_ls10_fill


    label lessonFiveFillEleven:
        scene l5f11
        "{b}height{/b} is an optional attribute for the image element. Run the code to see what the web browser will display"
        call screen lesson_five_ls11_fill

        label when_run_five_eleven:
            scene lesson_5_11_run
            "See the difference? The attribute height added a height length of 300 pixel"
            jump lessonFiveFillTwelve


    label lessonFiveFillTwelve:
        scene l5f12
        "You can provide both {b}width and height{/b}. Run the code to see what the web browser will display"
        call screen lesson_five_ls12_fill

        label when_run_five_twelve:
            scene lesson_5_12_run
            "See the difference? Also Changing the {b}aspect ratio{/b} between width and height will distort the image."
            jump lessonFiveFillThirteen


    label lessonFiveFillThirteen:
        scene lesson_8_22 
        "When only one of the 2 attributes is given, the web browser will calculate the other based on the {b}aspect ratio{/b} so the image is not stretched or squeezed"
        "True or False? The aspect ratio of an image determines its rectangular shape."

        menu:
            "False":
                jump if_lfv13_wrong
            "True":
                "You are correct"
                jump lessonFiveFillFourteen
 
        label if_lfv13_wrong:
            "incorrect"
            jump lessonFiveFillThirteen



    label lessonFiveFillFourteen:
        scene lesson_8_22 
        "Changing the {b}aspect ratio{/b} of an image causes distortion, which can look bad."
        "Changing the aspect ration will result in image of what?"

        menu:
            "Black and white":
                jump if_lfv14_wrong
            "Stretched or squeeze":
                "You are correct"
                jump lessonAttributeTakeaways
 
        label if_lfv14_wrong:
            "incorrect"
            jump lessonFiveFillFourteen


    label lessonAttributeTakeaways:
        scene lesson_attributes_takeaways
        "In the next topic, you`ll create menus for your website with navigation links."
        jump lessonMenuIntro
    

    label lessonMenuIntro:
        scene lesson_menus_navigation
        "In this topic, you`ll learn to help users to find what they`re looking for with navigation {b}links{/b}."
        jump lessonFiveFillFifteen

    
    label lessonFiveFillFifteen:
        $ ans_ffv_fft1_was_dropped = False
        $ ans_ffv_fft2_was_dropped = False
        $ ans_ffv_fft3_was_dropped = False
        scene l5f15
        call screen lesson_five_ls15_fill

        label call_fv15:
            $ ans_ffv_fft1_was_dropped = False
            $ ans_ffv_fft2_was_dropped = False
            $ ans_ffv_fft3_was_dropped = False
            call screen lesson_five_ls15_fill
        
        label if_lfv15_wrong:
            scene l5f15
            "Try again"
            call screen lesson_five_ls15_fill

        
    label lessonFiveFillSixteen:
        $ ans_ffv_sixt1_was_dropped = False
        $ ans_ffv_sixt2_was_dropped = False
        scene l5f16
        call screen lesson_five_ls16_fill

        label call_fv16:
            $ ans_ffv_sixt1_was_dropped = False
            $ ans_ffv_sixt2_was_dropped = False
            call screen lesson_five_ls16_fill
        
        label if_lfv16_wrong:
            scene l5f16
            "Try again"
            call screen lesson_five_ls16_fill

    
    label lessonFiveFillSeventeen:
        $ ans_ffv_sevt1_was_dropped = False
        scene l5f17
        "The {b}<nav>{/b} container tag defines a set of links that allows the user to navigate between pages of a website."
        call screen lesson_five_ls17_fill

        label call_fv17:
            $ ans_ffv_sevt1_was_dropped = False
            call screen lesson_five_ls17_fill
        
        label if_lfv17_wrong:
            scene l5f17
            "Try again"
            call screen lesson_five_ls17_fill

    
    label lessonFiveFillEighteen:
        $ ans_ffv_eght1_was_dropped = False
        $ ans_ffv_eght2_was_dropped = False
        $ ans_ffv_eght3_was_dropped = False
        $ ans_ffv_eght4_was_dropped = False
        scene l5f18
        "Links to the different pages are added with the anchor tag <a> and nested inside the <nav> container tag."
        call screen lesson_five_ls18_fill

        label call_fv18:
            $ ans_ffv_eght1_was_dropped = False
            $ ans_ffv_eght2_was_dropped = False
            $ ans_ffv_eght3_was_dropped = False
            $ ans_ffv_eght4_was_dropped = False
            call screen lesson_five_ls18_fill
        
        label if_lfv18_wrong:
            scene l5f18
            "Try again"
            call screen lesson_five_ls18_fill


    label lessonFiveFillNineteen:
        $ ans_ffv_nnt1_was_dropped = False
        scene l5f19
        "The HTML project for a multi-page website is made of different HTML documents (or files)."
        call screen lesson_five_ls19_fill

        label call_fv19:
            $ ans_ffv_nnt1_was_dropped = False
            call screen lesson_five_ls19_fill
        
        label if_lfv19_wrong:
            scene l5f19
            "Try again"
            call screen lesson_five_ls19_fill


    label lessonFiveFillTwenty:
        scene lesson_8_22 
        "HTML documents must be saved with the right {b}file extension{/b} (file type) for web browsers to recognize them."
        "What do you think is the file extension for an HTML document?"

        menu:
            ".pdf":
                jump if_lfv20_wrong
            ".html":
                "You are correct"
                jump lessonFiveFillTwentyOne
 
        label if_lfv20_wrong:
            "incorrect"
            jump lessonFiveFillTwenty


    label lessonFiveFillTwentyOne:
        scene l5f21
        "Run the code to see what the web browser will display"
        call screen lesson_five_ls21_fill

        label when_run_five_twentyone:
            scene lesson_5_21_run
            "Clicking the link will take you to the their respective pages, also you need to provide the content for the other two HTML documents."
            jump lessonFiveFillTwentyTwo


    label lessonFiveFillTwentyTwo:
        scene lesson_5_22
        "It`s best practice to name your homepage index.html so that the web browser can find and load it."
        jump lessonFiveFillTwentyThree

    
    label lessonFiveFillTwentyThree:
        scene lesson_8_22 
        "How many HTML documents(or files) will the project of a single-page website contain?"

        menu:
            "1":
                "You are correct"
                jump lessonFiveFillTwentyFour
            "As many files as the number of sections":
                jump if_lfv23_wrong
            "2":
                jump if_lfv23_wrong
 
        label if_lfv23_wrong:
            "incorrect"
            jump lessonFiveFillTwentyThree


    label lessonFiveFillTwentyFour:
        $ ans_ffv_twtf1_was_dropped = False
        scene l5f24
        "To jump to a specific part of a single-page website, first you need to mark the section with the {b}id (ID){/b} attribute."
        call screen lesson_five_ls24_fill

        label call_fv24:
            $ ans_ffv_twtf1_was_dropped = False
            call screen lesson_five_ls24_fill
        
        label if_lfv24_wrong:
            scene l5f24
            "Try again"
            call screen lesson_five_ls24_fill


    label lessonFiveFillTwentyFive:
        $ ans_ffv_twtfv1_was_dropped = False
        $ ans_ffv_twtfv2_was_dropped = False
        scene l5f25
        "The {b}id{/b} attribute is used to identify the element you want to target with the navigation link."
        call screen lesson_five_ls25_fill

        label call_fv25:
            $ ans_ffv_twtfv1_was_dropped = False
            $ ans_ffv_twtfv2_was_dropped = False
            call screen lesson_five_ls25_fill
        
        label if_lfv25_wrong:
            scene l5f25
            "Try again"
            call screen lesson_five_ls25_fill

        
    
    label lessonFiveFillTwentySeven:
        $ ans_ffv_twtsv1_was_dropped = False
        $ ans_ffv_twtsv2_was_dropped = False
        scene l5f27
        call screen lesson_five_ls27_fill

        label call_fv27:
            $ ans_ffv_twtsv1_was_dropped = False
            $ ans_ffv_twtsv2_was_dropped = False
            call screen lesson_five_ls27_fill
        
        label if_lfv27_wrong:
            scene l5f27
            "Try again"
            call screen lesson_five_ls27_fill


    label lessonFiveFillTwentyEight:
        scene lesson_5_28
        jump lessonMenuTakeaways

    
    label lessonMenuTakeaways:
        scene lesson_menus_takeaways
        jump lessonForm


    label lessonForm:
        scene lesson_forms
        "You can use forms to let your visitors: \n  - get in contact with you \n  - send orders, requests and other information \n  - create an account or register \n  - and much more"
        jump lessonFiveFillTwentyNine


    label lessonFiveFillTwentyNine:
        $ ans_ffv_twtn1_was_dropped = False
        scene l5f29
        "Forms are made of input elements like text fields, checkboxes, and submit buttons. These input elements are nested inside the <form> container tag."
        call screen lesson_five_ls29_fill

        label call_fv29:
            $ ans_ffv_twtn1_was_dropped = False
            call screen lesson_five_ls29_fill
        
        label if_lfv29_wrong:
            scene l5f29
            "Try again"
            call screen lesson_five_ls29_fill        


    label lessonFiveFillThirty:
        scene l5f30
        "Run the code to see what the web browser will display"
        call screen lesson_five_ls30_fill

        label when_run_five_thirty:
            scene lesson_5_30_run
            "The most common form element is <input>. There are many forms of <input> element, depending on the type attribute."
            "input could be text, radio, or checkbox"
            jump lessonFiveFillThirtyone


    label lessonFiveFillThirtyone:
        scene l5f31
        "Run the code to see what the web browser will display"
        call screen lesson_five_ls31_fill

        label when_run_five_thirtyone:
            scene lesson_5_31_run
            "Form elements will be displayed in the same line unless we use the {b}<br> (line break) tag{/b}."
            jump lessonFiveFillThirtytwo


    label lessonFiveFillThirtytwo:
        $ ans_ffv_thtt1_was_dropped = False
        $ ans_ffv_thtt2_was_dropped = False
        scene l5f32
        "Labels can be added for the different input elements with the {b}<label> tag{/b}."
        "Also remember that labels and inputs are inline elements, meaning they will not start on a new line"
        "You will have to use <br> so it doesnt end up on the same line"
        call screen lesson_five_ls32_fill

        label call_fv32:
            $ ans_ffv_thtt1_was_dropped = False
            $ ans_ffv_thtt2_was_dropped = False
            call screen lesson_five_ls32_fill
        
        label if_lfv32_wrong:
            scene l5f32
            "Try again"
            call screen lesson_five_ls32_fill    



    label lessonFiveFillThirtythree:
        scene l5f33
        "Run the code to see what the web browser will display"
        call screen lesson_five_ls33_fill

        label when_run_five_thirtythree:
            scene lesson_5_33_run
            "As you can see we use <br> tag to separate the labels and inputs that accords to its input form"
            "Next with paragraph tag"
            jump lessonFiveFillThirtyfour


    label lessonFiveFillThirtyfour:
        scene l5f34
        "Run the code to see what the web browser will display"
        call screen lesson_five_ls34_fill

        label when_run_five_thirtyfour:
            scene lesson_5_34_run
            "It's considered a very good practice to connect the label to the input elements with the use of {b}for{/b} and {b}id{/b} attributes."
            jump lessonFiveFillThirtyfive


    label lessonFiveFillThirtyfive:
        $ ans_ffv_thtfv1_was_dropped = False
        scene l5f35
        "The {b}id{/b} attribute is used to identify a unique input element. The {b}for{/b} attribute in a label targets (and matches!) an input`s id. "
        call screen lesson_five_ls35_fill

        label call_fv35:
            $ ans_ffv_thtfv1_was_dropped = False
            call screen lesson_five_ls35_fill
        
        label if_lfv35_wrong:
            scene l5f35
            "Try again"
            call screen lesson_five_ls35_fill 


    label lessonFiveFillThirtysix:
        $ ans_ffv_thtsx1_was_dropped = False
        $ ans_ffv_thtsx2_was_dropped = False
        scene l5f36
        "To connect labels and inputs, their {b}id{/b} and {b}for{/b} attribute values must match up exactly."
        call screen lesson_five_ls36_fill

        label call_fv36:
            $ ans_ffv_thtsx1_was_dropped = False
            $ ans_ffv_thtsx2_was_dropped = False
            call screen lesson_five_ls36_fill
        
        label if_lfv36_wrong:
            scene l5f36
            "Try again"
            call screen lesson_five_ls36_fill


    label lessonFiveFillThirtynine:
        scene lesson_8_22 
        "The {b}id{/b} attribute is used to identify unique elements in an HTML document."
        "True or False? You can give multiple elements to the same id in one HTML document"

        menu:
            "False":
                "You are correct"
                jump lessonFiveFillFourty
            "True":
                jump if_lfv39_wrong
 
        label if_lfv39_wrong:
            "incorrect"
            jump lessonFiveFillThirtynine


    label lessonFiveFillFourty:
        scene lesson_5_40 
        "There's something wrong with the form code. Can you identify it?"

        menu:
            "missing id attributes":
                "You are correct"
                jump lessonFiveFillFourtyone
            "labels should appear before the inputs":
                jump if_lfv40_wrong
            "<label> is an empty tag":
                jump if_lfv40_wrong
 
        label if_lfv40_wrong:
            "incorrect"
            jump lessonFiveFillFourty


    label lessonFiveFillFourtyone:
        $ ans_ffv_ftyo1_was_dropped = False
        $ ans_ffv_ftyo2_was_dropped = False
        $ ans_ffv_ftyo3_was_dropped = False
        $ ans_ffv_ftyo4_was_dropped = False
        scene l5f41
        call screen lesson_five_ls41_fill

        label call_fv41:
            $ ans_ffv_ftyo1_was_dropped = False
            $ ans_ffv_ftyo2_was_dropped = False
            $ ans_ffv_ftyo3_was_dropped = False
            $ ans_ffv_ftyo4_was_dropped = False
            call screen lesson_five_ls41_fill
        
        label if_lfv41_wrong:
            scene l5f41
            "Try again"
            call screen lesson_five_ls41_fill


    label lessonFiveFillFourtytwo:
        scene lesson_8_22 
        "When labels and form fields are correctly connected... The what?"

        menu:
            "label and form fields are displayed on the same line":
                jump if_lfv42_wrong
            "label and form fields are displayed in the same color":
                jump if_lfv42_wrong
            "hitting the label selects the form field":
                "You are correct"
                jump lessonFormtakeaways
 
        label if_lfv42_wrong:
            "incorrect"
            jump lessonFiveFillFourtytwo


    label lessonFormtakeaways:
        scene lesson_form_takeaways
        "In the next lesson, you'll take your web form skills to the next level."
    
    label lessonFormSubmit:
        scene lesson_form_submit
        "In this lesson, you`ll learn to submit form data."
        jump lessonFiveFillFourtythree
    

    label lessonFiveFillFourtythree:
        scene lesson_5_43 
        "What will the browser display?"

        menu:
            "A table":
                jump if_lfv43_wrong
            "A form with two input field":
                "You are correct"
                jump lessonFiveFillFourtyfour
 
        label if_lfv43_wrong:
            "incorrect"
            jump lessonFiveFillFourtythree


    label lessonFiveFillFourtyfour:
        $ ans_ffv_ftyfr1_was_dropped = False
        $ ans_ffv_ftyfr2_was_dropped = False
        scene l5f44
        "A {b}submit{/b} button is used to send the data in a form. The {b}submit{/b} type of input adds a button to the form."
        call screen lesson_five_ls44_fill

        label call_fv44:
            $ ans_ffv_ftyfr1_was_dropped = False
            $ ans_ffv_ftyfr2_was_dropped = False
            call screen lesson_five_ls44_fill
        
        label if_lfv44_wrong:
            scene l5f44
            "Try again"
            call screen lesson_five_ls44_fill


    label lessonFiveFillFourtyfive:
        scene lesson_8_22 
        "You can use the {b}submit{/b} input to send the data in the form to a database hosted in a server."
        "Do you remember what a server is?"

        menu:
            "A computer that is always connected to the internet and listening for request informations":
                "You are correct"
                jump lessonFiveFillFourtysix
            "The device that is being used to access the web":
                jump if_lfv45_wrong
 
        label if_lfv45_wrong:
            "incorrect"
            jump lessonFiveFillFourtyfive


    label lessonFiveFillFourtysix:
        $ ans_ffv_ftysix1_was_dropped = False
        $ ans_ffv_ftysix2_was_dropped = False
        scene l5f46
        "The {b}name{/b} attribute is used to reference the data after submitting the form "
        call screen lesson_five_ls46_fill

        label call_fv46:
            $ ans_ffv_ftysix1_was_dropped = False
            $ ans_ffv_ftysix2_was_dropped = False
            call screen lesson_five_ls46_fill
        
        label if_lfv46_wrong:
            scene l5f46
            "Try again"
            call screen lesson_five_ls46_fill



    label lessonFiveFillFourtyseven:
        scene lesson_5_47
        "Only form elements with a name attribute will have their values passed to the database when submitting a form."
        jump lessonFiveFillFourtyeight


    label lessonFiveFillFourtyeight:
        scene lesson_5_48 
        "Where will the text entered by the user in the second field go?"

        menu:
            'to the "email" field (column) in the database':
                jump if_lfv48_wrong
            'to the "city" field (column) in the database':
                "you are correct"
                jump lessonFiveFillFourtynine
 
        label if_lfv48_wrong:
            "incorrect"
            jump lessonFiveFillFourtyeight


    label lessonFiveFillFourtynine:
        scene lesson_5_49 
        "The form above will not send data to the database when submitted. Why?"

        menu:
            'submit button is missing':
                jump if_lfv49_wrong
            'input fields don’t have names':
                "you are correct"
                jump lessonFiveFillFifty
 
        label if_lfv49_wrong:
            "incorrect"
            jump lessonFiveFillFourtynine


    label lessonFiveFillFifty:
        scene lesson_5_50 
        "The name attribute is used to put the input from the user in the correct field (column) in the database."
        "Name attributes need to be added to what?"

        menu:
            'label':
                jump if_lfv50_wrong
            'input fields':
                "you are correct"
                jump lessonFiveFillFiftyone
 
        label if_lfv50_wrong:
            "incorrect"
            jump lessonFiveFillFifty

    label lessonFiveFillFiftyone:
        $ ans_ffv_ffyo1_was_dropped = False
        $ ans_ffv_ffyo2_was_dropped = False
        scene l5f51
        "Remember labels and input fields need to be correctly paired"
        call screen lesson_five_ls51_fill

        label call_fv51:
            $ ans_ffv_ffyo1_was_dropped = False
            $ ans_ffv_ffyo2_was_dropped = False
            call screen lesson_five_ls51_fill
        
        label if_lfv51_wrong:
            scene l5f51
            "Try again"
            call screen lesson_five_ls51_fill


    label lessonFiveFillFiftytwo:
        scene lesson_5_52 
        "How will the email field be referenced in the database?"

        menu:
            "co":
                jump if_lfv52_wrong
            "em":
                "You are correct"
                jump lessonFiveFillFiftythree
            "email":
                jump if_lfv52_wrong
 
        label if_lfv52_wrong:
            "incorrect"
            jump lessonFiveFillFiftytwo


    label lessonFiveFillFiftythree:
        $ ans_ffv_ffyth1_was_dropped = False
        $ ans_ffv_ffyth2_was_dropped = False
        scene l5f53
        "Names and values are needed to correctly store information in the database. The HTML code needs to include where and what to put in the database."
        call screen lesson_five_ls53_fill

        label call_fv53:
            $ ans_ffv_ffyth1_was_dropped = False
            $ ans_ffv_ffyth2_was_dropped = False
            call screen lesson_five_ls53_fill
        
        label if_lfv53_wrong:
            scene l5f53
            "Try again"
            call screen lesson_five_ls53_fill


    label lessonFiveFillFiftyfour:
        scene lesson_5_54 
        "What will this form send to the database when the second radio button is selected?"

        menu:
            'label':
                jump if_lfv54_wrong
            'cash':
                jump if_lfv54_wrong
            'card':
                "you are correct"
                jump lessonFiveFillFiftyfive
            
 
        label if_lfv54_wrong:
            "incorrect"
            jump lessonFiveFillFiftyfour


    label lessonFiveFillFiftyfive:
        scene lesson_5_55 
        "Where will the users’ choice of payment method be stored in the database?"

        menu:
            'field (column) named "cash"':
                "you are correct"
                jump lessonFiveFillFiftysix
            'field (column) named "radio"':
                jump if_lfv55_wrong
            'field (column) named "pay"':
                jump if_lfv55_wrong
            
 
        label if_lfv55_wrong:
            "incorrect"
            jump lessonFiveFillFiftyfive


    label lessonFiveFillFiftysix:
        scene l5f56
        "For the case of text inputs, you can use the value attribute to define a default value that will be submitted unless a different value is provided by the user."
        "Run the code to see what the web browser will display"
        call screen lesson_five_ls56_fill

        label when_run_five_fiftysix:
            scene lesson_5_56_run
            "Well done"
            jump lessonFiveFillFiftyseven


    label lessonFiveFillFiftyseven:
        scene lesson_5_57 
        "The {b}value{/b} in the text input above will be sent to the database?"

        menu:
            'only when the user doesn’t provide a different value':
                "you are correct"
                jump lessonFormSubmitTakeaways
            'always':
                jump if_lfv57_wrong
            
 
        label if_lfv57_wrong:
            "incorrect"
            jump lessonFiveFillFiftyseven


    label lessonFormSubmitTakeaways:
        scene lesson_submit_takeaways
        "Bravo! Your coding skills are reaching new heights. Keep exploring, and may your web development adventures continue to thrive!"






    return


