def blood_pressure(systolic, diastolic):
    categories = ["Low", "Normal", "Prehigh", "Stage 1 high", "Stage 2 high"]
    categorySys = ""
    categoryDia = ""
    category = ""
    if 70 <= systolic < 90:
        categorySys = "Low"
    elif 90 <= systolic < 120:
        categorySys = "Normal"
    elif 120 <= systolic < 140:
        categorySys = "Prehigh"
    elif 140 <= systolic < 160:
        categorySys = "Stage 1 high"
    elif 160 <= systolic <= 190:
        categorySys = "Stage 2 high"
    if 40 <= diastolic < 60:
        categoryDia = "Low"
    elif 60 <= diastolic < 80:
        categoryDia = "Normal"
    elif 80 <= diastolic < 90:
        categoryDia = "Prehigh"
    elif 90 <= diastolic < 100:
        categoryDia = "Stage 1 high"
    elif 100 <= diastolic <= 120:
        categoryDia = "Stage 2 high"
    if categorySys != categoryDia:
        sysI = categories.index(categorySys)
        diaI = categories.index(categoryDia)
        category = categorySys if sysI > diaI else categoryDia
    else:
        category = categorySys
    return category
