dictionary = {
    "baasto": "waa cunto somaliyeed",
    "computer": "alada casrigaa",
    "IT": "waa barshada computerka"
}
def raadi():
    eray = input("soo gali erayga aad radinayso") .lower()
    if eray in dictionary:
        print(f"{eray.capitalize()}: {dictionary[eray]}")
    else:
        print(f"{eray.capitalize()} lama helo kumana jiro dicrionary")
raadi()            