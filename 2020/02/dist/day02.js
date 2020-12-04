const fs = require("fs");

fs.readFile("./input", "utf-8", (err, data) => {
  const inputArray = data.split("\n");
  let correctPasswords = 0;

  //Part One:
  /*
    for (line of inputArray){
        line = line.replace(":","")
        line = line.replace("-"," ")
        let array = line.split(" ")
        let charCount = (array[3].split(array[2]).length - 1)
        if (array[0] <=	charCount && array[1] >= charCount)
            correctPasswords ++
    }//*/

  //Part Two:

  for (line of inputArray) {
    line = line.replace(":", "");
    line = line.replace("-", " ");
    let array = line.split(" ");

    let firstCharCorrect = array[3].charAt(array[0] - 1) == array[2];
    let secondCharCorrect = array[3].charAt(array[1] - 1) == array[2];
    console.log(firstCharCorrect + " " + secondCharCorrect);
    if (!(firstCharCorrect == secondCharCorrect)) correctPasswords++;
  }

  console.log(correctPasswords);
});
