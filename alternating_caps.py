import pyperclip

outputText = raw_input("Enter your text: ")

isCaps = True

for i in range(0, len(outputText)):
    if (outputText[i].isalpha()):
        if (isCaps):
            outputText = outputText[:i] + outputText[i].upper() + outputText[i+1:]
            isCaps = False
        else:
            outputText = outputText[:i] + outputText[i].lower() + outputText[i+1:]
            isCaps = True

pyperclip.copy(outputText)
print("Translated and copied to clipboard!")