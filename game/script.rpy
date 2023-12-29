
define e = Character("Eileen")

default lesson_one_finish = False
default lesson_two_finish = False
default lesson_three_finish = False
default lesson_four_finish = False
default lesson_five_finish = False
default lesson_six_finish = False
default lesson_seven_finish = False
default lesson_eight_finish = False
default lesson_nine_finish = False
default lesson_ten_finish = False

# The game starts here.

label start:

    scene bg_classroom

    jump lessonAttributeIntro

    "You are in the Classroom right now"


    call screen classroom_ui

    label lesson_choices:

        menu:
            "Start Lesson":
                call screen lesson_ui
            "Start Final Test":
                jump start_final_test
    
    label start_final_test:
        call screen scrollable_screen
    

    return
