

def main():

    def are_you_cough():
        if_cough = input("Are you coughing? (y or n)")
        if if_cough == 'y':
            short_of_breath()
        elif if_cough == 'n':
            have_headache(False)

    def short_of_breath():
        if_short_of_breath = input("Are you short of breath or \
wheezing or coughing up phlegm? (y or n)")
        if if_short_of_breath == 'y':
            print("Possibilities include pneumonia oor infection of airways.")
        elif if_short_of_breath == "n":
            have_headache(True)

    def have_headache(is_cough=True):

        if_headache = input("Do you have a headache? (y or n)")
        if not is_cough:
            if if_headache == 'y':
                experience_follow()
            elif if_headache == 'n':
                aching_bone()
        else:
            if if_headache == 'y':
                print("Possibilities include viral infection.")
            elif if_headache == 'n':
                aching_bone()

    def aching_bone():
        if_aching_bone = input("Do you have aching bones or \
aching joints? (y or n)")
        if if_aching_bone == 'y':
            print("Possibilities include viral infection.")
        elif if_aching_bone == 'n':
            have_rash()

    def have_rash():
        if_have_rash = input("Do you have a rash? (y or n)")
        if if_have_rash == 'y':
            print("Insufficient information to list possibilities.")
        elif if_have_rash == 'n':
            have_sore_throat()

    def have_sore_throat():
        if_sore_throat = input("Do you have a sore throat? (y or n)")
        if if_sore_throat == 'y':
            print("Possibilities include a throat infection.")
        elif if_sore_throat == 'n':
            have_back_pain()

    def have_back_pain():
        if_back_pain = input("Do you have back pain just above \
the waist with chills and fever? (y or n)")
        if if_back_pain == 'y':
            print("Possibilities include kidney infection.")
        elif if_back_pain == 'n':
            pain_urinating()

    def pain_urinating():
        if_pain_urinating = input("Do you have pain urinating or\
 are urinating more often? (y or n)")
        if if_pain_urinating == 'y':
            print("Possibilities include a urinary tract infection.")
        elif if_pain_urinating == 'n':
            spend_in_sun()

    def spend_in_sun():
        if_spend_sun = input("Have you spent the day in the \
sun or in hot conditions? (y or n)")
        if if_spend_sun == 'y':
            print("Possibilities sunstroke or heat exhaustion.")
        elif if_spend_sun == 'n':
            print("Insufficient information to list possibilities.")

    def experience_follow():
        if_expe_follow = input("Are are experiencing any of the following\
:pain when bending your head forward, nausea or vomiting, bright light hurting\
 your eyes,drowsiness or confusion? (y or n)")
        if if_expe_follow == 'y':
            print("Possibilities include menigitis.")
        elif if_expe_follow == 'n':
            vomit()

    def vomit():
        if_vomit = input("Are you vomiting or had diarrhea? (y or n)")
        if if_vomit == 'y':
            print("Possibilities include digestive tract infection.")
        elif if_vomit == 'n':
            aching_bone()

    are_you_cough()

main()
