




######################################################################################################################


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
                    text "{b}Headings:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. “<h1>”- Heading 1{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use for the main heading or title of your content.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h1>Welcome to My Game</h1>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}2. “<h2>” - Heading 2{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Subheadings or sections within the main content.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h2>Chapter 1: The Beginning</h2>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}3. “<h3>” - Heading 3{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Further subdivisions of <h2> sections.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h3>Scene 1: Exploring the Forest</h3>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}4. “<h4>” - Heading 4{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use for subsections within <h3>.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h4>Discovering a Hidden Path</h4>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}5. “<h5>” - Heading 5{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Subsections of <h4> or smaller details within your content.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h5>Collecting Clues</h5>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}6. “<h6>” - Heading 6{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Rarely used. Smallest level of heading, often for minor details.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <h6>Note: Important Reminder</h6>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen img_hint():
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
                    text "{b}Images:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}“<img>” - Image Tag{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use the <img> tag to embed images in your webpage.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n    {b}Attributes{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • {b}src{/b}: Specifies the source (URL or file path) of the image.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • {b}alt{/b}: Provides alternative text for accessibility.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • {b}width{/b}: Sets the width of the image.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      • {b}height{/b}: Sets the height of the image.' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <img src="image.jpg" alt="A beautiful landscape" width="500" height="300">' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n    {b}Explanation:{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • The {b}src{/b} attribute specifies the image file.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • The {b}alt{/b} attribute describes the image for users with screen readers or if ' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '        the image fails to load.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      • {b}width{/b} and {b}height{/b} attributes control the size of the displayed image.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n'
                    text '\n'
                    text '\n'
                    text '\n'


######################################################################################################################


screen comment_hint():
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
                    text "{b}Comments:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}“ <!-- --> ” - Comment{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use <!-- --> to add comments in your HTML code. Comments are not displayed' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '         on the webpage but can provide helpful notes for developers.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n    {b}Example:{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n     <!-- This is a comment. It won`t appear on the webpage. -->' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen standards_best_practices_hint():
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
                    text "{b}Standards & Best Practices:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}Indentation in HTML{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '\n    • Maintain consistent indentation to enhance code readability. Use spaces or ' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '       tabs consistently throughout your HTML document.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n    • Choose either spaces or tabs and stick to the same indentation style.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n    • Use indentation to represent the hierarchy of HTML elements.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n    {b}Example:{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n     <html>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        <head>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <title>My Webpage</title>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </head>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n        <body>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <h1>Welcome to My Webpage</h1>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <p>This is a sample paragraph.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <!-- Additional elements go here -->' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n        </body>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n     <html>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '\n     Use an indentation size of 2 or 4 spaces for readability.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '     Also Consistent indentation helps you spot errors and maintain a clean code structure.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen text_formatting_hint():
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
                    text "{b}Text Formatting:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Bold Text - <strong> and <b>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use <strong> for strong importance and <b> for bold text. <strong> is semantically preferred.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <p>This is <strong>important</strong> information.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <p>This is <b>bold</b> text.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6




                    text '\n\n{b}2. Italic Text - <em> and <i>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      Use <em> for emphasized text and <i> for italic text. <em> is semantically preferred.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <p>This is <em>emphasized</em> text.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            <p>This is <i>italic</i> text.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}3. Underline Text - <u>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use <u> for underlined text. However, underlining is not always recommended for readability.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <p>This text is <u>underlined</u>.</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n\nThese tags help convey meaning and structure to your text.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\nAlways consider the semantics of your content when choosing between semantic and presentational tags.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen links_hint():
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
                    text "{b}Links:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Basic Link - <a>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Use the <a> (anchor) tag to create hyperlinks.' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n      {b}Attributes{/b}:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '      • {b}href{/b}: Specifies the URL of the linked page or resource.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <a href="https://www.example.com">Visit Example.com</a>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}2. Linking to Another Page in the Same Site{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • For links within the same website, use relative URLs.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <a href="/about">About Us</a>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n{b}3. Adding Link Text - <a>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    
                    text '      • Include descriptive text within the <a> tags to provide context.' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <p>Visit <a href="https://www.example.com">Example.com</a> for more informa</p>' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6


######################################################################################################################


screen list_hint():
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
                    text "{b}List:{/b}\n\n" color "#dfdfdf" xoffset 6 yoffset 6

                    
                    text '{b}1. Unordered List - <ul>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use <ul> to create a list without a specific order.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ul>>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Item 1</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Item 2</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Item 3</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            </ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n\n{b}2. Ordered List - <ol>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use <ol> to create a numbered list.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ol>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>First Step</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Second Step</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Third Step</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            </ol>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n\n{b}3. List Items - <li>{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • Use <li> inside <ul> or <ol> to represent each item in the list.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Red</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Green</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Blue</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n            </ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6



                    text '\n\n\n{b}4. Nested Lists{/b}' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    

                    text '\n      • You can put lists inside other lists to create a hierarchy.' size 24 color "#dfdfdf" xoffset 6 yoffset 6


                    
                    text '\n      Example:' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n            <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                <li>Fruits' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                        <li>Apple</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                        <li>Banana</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                </li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n                <li>Vegetables' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                        <li>Carrot</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                        <li>Spinach</li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                    <ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    text '\n                </li>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n            </ul>' size 24 color "#dfdfdf" xoffset 6 yoffset 6
                    
                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6

                    text '\n' size 24 color "#dfdfdf" xoffset 6 yoffset 6
