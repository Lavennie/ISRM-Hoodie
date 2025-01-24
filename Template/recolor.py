import sys
  
def replaceColor(template, newFile, mainColor, lineColor):
    with open (template, 'r') as template:
        templateData = template.read()
    templateData = templateData.replace("#FF0000", mainColor.upper())
    templateData = templateData.replace("#000000", lineColor.upper())
    with open (newFile, 'w') as file:
        file.write(templateData)


variation = input("Enter \'1\' for FMF/FRI front side and \'2\' for variation with cars: ")
backFile = "template back.svg"
# pick front side variation
if variation == '1':
    frontFile = "template front.svg"
elif variation == '2':
    frontFile = "template front cars.svg"
else:
    input("\033[31mWrong variation selection.\033[0m")
    sys.exit(1)
    
# pick main color and check if it is in correct format
color = input("Enter custom hex color (e.g. #C8B9EB): ")
if color[0] != '#':
    input("\033[31mColor needs to start with \'#\'.\033[0m")
    sys.exit(1)
if len(color) not in [4, 7] :
    input("\033[31mColor string needs to be of lenght 4 or 7.\033[0m")
    sys.exit(1)
for c in color[1::]:
    if c not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']:
        input("\033[31mNon-first characters need to be one of the following: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F (upper or lower case).\033[0m")
        sys.exit(1)

# pick lines color - black or white
blackWhite = input("Enter \'1\' for black lines or \'2\' for white lines: ")
if blackWhite == '1':
    lineColor = "#000000"
    lineColorName = "black"
elif blackWhite == '2':
    lineColor = "#FFFFFF"
    lineColorName = "white"
else:
    input("\033[31mWrong line color selection.\033[0m")
    sys.exit(1)
    
fileID = input("Enter <name> used for generated files (e.g. \'<name> black front.svg\' will be generated): ")

# create new files with updated colors
if (variation == '1'):
    replaceColor(backFile, f"{fileID} {lineColorName} back.svg", color, lineColor)
    replaceColor(frontFile, f"{fileID} {lineColorName} front.svg", color, lineColor)
else:
    replaceColor(backFile, f"{fileID} {lineColorName} back cars.svg", color, lineColor)
    replaceColor(frontFile, f"{fileID} {lineColorName} front cars.svg", color, lineColor)
    