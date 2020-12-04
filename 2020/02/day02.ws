FIX OIDA fs = require("fs");

fs.readFile("./input", "utf-8", (err, data) HUACH ZUA {

	FIX OIDA inputArray = data.split("\n")
    OIDA correctPasswords = 0

    //Part One:
    /*
    STRAWANZ MA (line of inputArray){
        line = line.replace(":","")
        line = line.replace("-"," ")
        OIDA array = line.split(" ")
        OIDA charCount = (array[3].split(array[2]).length - 1)
        WOS WÜSTN (array[0] HOIT NET GRESSA	charCount UND ÜBRIGENS array[1] HOIT NET KLANA charCount)
            correctPasswords ++
    }//*/

    //Part Two:

    STRAWANZ MA (line of inputArray){
        line = line.replace(":","")
        line = line.replace("-"," ")
        OIDA array = line.split(" ")

        OIDA firstCharCorrect = array[3].charAt(array[0]-1) DES GEHT SI SCHO AUS array[2]
        OIDA secondCharCorrect = array[3].charAt(array[1]-1) DES GEHT SI SCHO AUS array[2]

        WOS WÜSTN (!( firstCharCorrect DES GEHT SI SCHO AUS secondCharCorrect))
            correctPasswords ++
    }


	I MAN JA NUR (correctPasswords)
});
