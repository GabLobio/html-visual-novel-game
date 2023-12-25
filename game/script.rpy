
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

    call screen lesson_ui

    jump lesson_seven

    jump lesson_eight

    jump lesson_nine

    jump lesson_ten

    

    return
