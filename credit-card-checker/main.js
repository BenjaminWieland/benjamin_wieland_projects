//Functions for checking credit card numbers

//Arrays with credit card numbers:

// All valid credit card numbers
const valid1 = [4, 5, 3, 9, 6, 7, 7, 9, 0, 8, 0, 1, 6, 8, 0, 8]
const valid2 = [5, 5, 3, 5, 7, 6, 6, 7, 6, 8, 7, 5, 1, 4, 3, 9]
const valid3 = [3, 7, 1, 6, 1, 2, 0, 1, 9, 9, 8, 5, 2, 3, 6]
const valid4 = [6, 0, 1, 1, 1, 4, 4, 3, 4, 0, 6, 8, 2, 9, 0, 5]
const valid5 = [4, 5, 3, 9, 4, 0, 4, 9, 6, 7, 8, 6, 9, 6, 6, 6]

// // All invalid credit card numbers
const invalid1 = [4, 5, 3, 2, 7, 7, 8, 7, 7, 1, 0, 9, 1, 7, 9, 5]
const invalid2 = [5, 7, 9, 5, 5, 9, 3, 3, 9, 2, 1, 3, 4, 6, 4, 3]
const invalid3 = [3, 7, 5, 7, 9, 6, 0, 8, 4, 4, 5, 9, 9, 1, 4]
const invalid4 = [6, 0, 1, 1, 1, 2, 7, 9, 6, 1, 7, 7, 7, 9, 3, 5]
const invalid5 = [5, 3, 8, 2, 0, 1, 9, 7, 7, 2, 8, 8, 3, 8, 5, 4]

// // Can be either valid or invalid
const mystery1 = [3, 4, 4, 8, 0, 1, 9, 6, 8, 3, 0, 5, 4, 1, 4]
const mystery2 = [5, 4, 6, 6, 1, 0, 0, 8, 6, 1, 6, 2, 0, 2, 3, 9]
const mystery3 = [6, 0, 1, 1, 3, 7, 7, 0, 2, 0, 9, 6, 2, 6, 5, 6, 2, 0, 3]
const mystery4 = [4, 9, 2, 9, 8, 7, 7, 1, 6, 9, 2, 1, 7, 0, 9, 3]
const mystery5 = [4, 9, 1, 3, 5, 4, 0, 4, 6, 3, 0, 7, 2, 5, 2, 3]

// // An array of all the arrays above
const batch = [valid1, valid2, valid3, valid4, valid5, invalid1, invalid2, invalid3, invalid4, invalid5, mystery1, mystery2, mystery3, mystery4, mystery5]


// Check for validity

/* Function splits array in two separate arrays,
sums them both up and calculates the modulo
of their sum, thereby using the Luhn algorithm to test
the validity*/

const validateCred = array => {
    let newArr1 = [];
    for (let i = array.length-2; i >= 0; i -= 2) {
        let doubleIndex = array[i] * 2;
        if (doubleIndex > 9) {
            let endIndex = doubleIndex - 9;
            newArr1.push(endIndex);
        } else {
            newArr1.push(doubleIndex);
        }
    }
    let newArr2 = [];
    for (let j = array.length-1; j >=0; j-= 2) {
        newArr2.push(array[j]);
    }
    let sumArr1 = 0;
    for (let k = 0; k < newArr1.length; k++) {
        sumArr1 += newArr1[k];
    }
    let sumArr2 = 0;
    for (let l = 0; l < newArr2.length; l++) {
        sumArr2 += newArr2[l];
    }
    let moduloArr = (sumArr1 + sumArr2) % 10;

    if (moduloArr === 0) {
        return true;
    } else {
        return false;
    }
}

//Function creates new array of invalid card numbers

const findInvalidCards = batchArr => {
    let invalidCards = [];
    for (i of batchArr) {
        let status = validateCred(i);
        if (status === false) {
            invalidCards.push(i);
        }
    }
    return invalidCards;
}

/*Function identifies credit card companies by the first
number of the array and then returns an array with all credit card companies
that have issued invalid numbers - every company is only listed once*/

const invalidBatch = findInvalidCards(batch);

const idInvalidCardCompanies = invalidArr => {
    let companyList = [];
    for (i of invalidArr) {
        if (i[0] === 3) {
            companyList.push('Amex');
        }
        else if (i[0] === 4) {
            companyList.push('Visa');
        }
        else if (i[0] === 5) {
            companyList.push('Mastercard');
        }
        else if (i[0] === 6) {
            companyList.push('Discover');
        }
        else {
            return 'Company not found';
        }
    }
    let companyListFiltered = companyList.filter((item, index) => {
        return companyList.indexOf(item) === index;
    });
    return companyListFiltered;
}

console.log(idInvalidCardCompanies(invalidBatch));




