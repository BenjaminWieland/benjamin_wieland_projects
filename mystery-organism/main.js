// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G'];
  return dnaBases[Math.floor(Math.random() * 4)];
};

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = [];
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase());
  }
  return newStrand;
};

// Returns an object of the mysterious organism "P.aequor"
const pAequorFactory = (number, dnaArr) => {
  return {
    specimenNum : number,
    dna : dnaArr,
    //Picks out one specific DNA base and replaces it with a random new one
    mutate() {
      let randIndex1 = this.dna.indexOf(this.dna[Math.floor(Math.random() * 15)]);
      let randIndex2;
      do {
          randIndex2 = returnRandBase();
      } while (this.dna[randIndex1] === randIndex2);

      this.dna[randIndex1] = randIndex2;
      },
    //Creates a new object and compares the DNA of the new object with that of the original one
    compareDNA(otherObj) {
      const sameCount = this.dna.reduce((count, element, index) => {
        if (element === otherObj.dna[index]) {
          return count + 1;
        }
        return count;
      }, 0)
      const samePercentage = (sameCount / this.dna.length) * 100;
      const endPercentage = samePercentage.toFixed(2);
      return `Specimen #1 and specimen #2 have ${endPercentage}% DNA in common.`;
    },
    //Checks if either the percentage of 'C' or 'G' bases is above 60%
    willLikelySurvive() {
      let countC = 0;
      let countG = 0;
      for (i of this.dna) {
        if (i === 'C') {
          countC++;
        }
        else if (i === 'G') {
          countG++;
        }
      }
      const percentageC = (countC / this.dna.length) * 100;
      const percentageG = (countG / this.dna.length) * 100;
      if (percentageC >= 60 || percentageG >= 60) {
        return true;
      } else {
        return false;
      }
    },
    //Creates a complement strand of bases ('A'->'T'; 'C'->'G' and vice versa)
    complementStrand() {
      let newStrand = [];
      for (i of this.dna) {
        if (i === 'A') {
          newStrand.push('T');
        }
        else if (i === 'T') {
          newStrand.push('A');
        }
        else if (i === 'C') {
          newStrand.push('G');
        }
        else if (i === 'G') {
          newStrand.push('C');
        }
      }
      return newStrand;
    }
  }
}

//Creates an array of 30 specimens for which .willLikelySurvive() returns true
const survivingSpecimen = [];
let idCounter = 1;

while (survivingSpecimen.length < 30) {
  let newOrg = pAequorFactory(idCounter, mockUpStrand());
  if (newOrg.willLikelySurvive()) {
    survivingSpecimen.push(newOrg);
  }
  idCounter++;
}

console.log(survivingSpecimen);