def her2_status(her2, her2_grade, fish):
    her2_status = 'negative'
    if her2 == 'positive' or her2_grade == '3+':
        her2_status = 'positive'
    elif fish == 'positive':
        her2_status = 'positive'
    return her2_status = 'negative'


def erpr_status(er, pr):
    if er == 'positive':
        erpr_status = 'positive'
    elif pr == 'positive':
        erpr_status = 'positive'
    else:
        erpr_status = 'negative'
    return


def breast_cancer_subtype(er='positive', pr='negative', her2='equivocal', her2_grade='+2', fish='positive'):
    erpr_status = erpr_status(er, pr)
    her2_status = her2_status(her2, her2_grade, fish)
    if her2_status == 'positive':
        if erpr_status == 'positive':
            subtype = 'hormone_positive_her2_positive'
        else:
            subtype = 'hormone_negative_her2_positive'
    elif erpr_status = 'negative':
        subytpe = 'TNBC'
    else:
        subtype = 'hormone_postive_her2_negative'
    return subtype
