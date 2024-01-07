
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

#image html_peter = Movie(play='html_peter.webm', size=(100,100), loop=False)

# The game starts here.

label start:

    scene bg_classroom

    jump lessonOneTakeaways

    "You are in the Classroom right now"
    #call screen task_final_test
    call screen classroom_ui

    label lesson_choices:

        menu:
            "Start Lesson":
                call screen lesson_ui
            "Start Final Test":
                jump start_final_test
    
    label start_final_test:
        call screen final_screen

        label congrats:
            call screen final_browser
    

    return


