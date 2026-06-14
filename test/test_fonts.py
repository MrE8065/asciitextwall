import pyfiglet

fonts = sorted(pyfiglet.FigletFont.getFonts())

with open("test/output.txt", "w", encoding="utf-8") as output:
    # Go to start of file
    output.seek(0)
    # Clean contents
    output.truncate()

    print("Writing results to test/output.txt...")
    for font in fonts:
        output.write(font+"\n")
        text = pyfiglet.figlet_format(text="FooBar", font=font, width=160)
        output.write(text+"\n")
    print("Completed")
